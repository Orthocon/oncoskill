"""Offline package/install integrity tests. These do not grade model responses."""
import io
import json
from pathlib import Path, PurePosixPath
import re
import shutil
import tempfile
import unittest
from urllib.parse import unquote, urlsplit
import zipfile

from scripts import build_packages as build


class PackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sources = build.read_sources()
        cls.artifacts = build.package_bytes(cls.sources)

    def fixture(self):
        temp = tempfile.TemporaryDirectory(prefix="oncoskill-package-", dir="/private/tmp" if Path("/private/tmp").is_dir() else None)
        self.addCleanup(temp.cleanup)
        base = Path(temp.name).resolve()
        skill = base / "oncoskill"
        shutil.copytree(build.SKILL, skill)
        manifest = base / "files.txt"
        shutil.copy(build.MANIFEST, manifest)
        return skill, manifest

    def test_archive_extracts_exact_skill_without_repository(self):
        with tempfile.TemporaryDirectory() as tmp, zipfile.ZipFile(io.BytesIO(self.artifacts["oncoskill.zip"])) as archive:
            self.assertIsNone(archive.testzip())
            self.assertEqual(set(archive.namelist()), {"oncoskill/" + p for p in self.sources})
            for entry in archive.infolist():
                self.assertFalse(PurePosixPath(entry.filename).is_absolute())
                self.assertNotIn("..", PurePosixPath(entry.filename).parts)
                self.assertEqual((entry.external_attr >> 16) & 0o111, 0)
            archive.extractall(tmp)
            for path, data in self.sources.items():
                self.assertEqual((Path(tmp) / "oncoskill" / path).read_bytes(), data)
            self.assertFalse((Path(tmp) / "research").exists())

    def test_router_dependencies_exist_after_install(self):
        router = self.sources["SKILL.md"].decode()
        paths = re.findall(r"`([a-zA-Z0-9_./-]+\.(?:md|json))`", router)
        self.assertGreater(len(paths), 15)
        for path in paths:
            with self.subTest(path=path):
                self.assertIn(path, self.sources)

    def test_chat_has_all_operational_sections_and_resolving_links(self):
        chat = self.artifacts["oncoskill-chat.md"].decode()
        for name in self.sources.keys() - {"CHANGELOG.md"}:
            self.assertIn(f"## Source file: {name}\n", chat)
        self.assertNotIn("## Source file: CHANGELOG.md", chat)
        anchors = re.findall(r'<a id="([^"]+)">', chat)
        self.assertEqual(len(anchors), len(set(anchors)))
        for target in re.findall(r"\]\(#(file-[^)]+)\)", chat):
            self.assertIn(target, anchors)
        # Critical leaf files must contain their full text, not only an index entry.
        for name in ["references/modes/nutrition.md", "references/core/privacy.md", "assets/state-templates/current-state-simple.md"]:
            self.assertIn(self.sources[name].decode().strip(), chat)

    def test_existing_downloads_match_sources(self):
        for name, data in self.artifacts.items():
            self.assertEqual((build.ROOT / "downloads" / name).read_bytes(), data, f"Rebuild {name}")

    def test_build_is_reproducible_and_changes_with_source(self):
        self.assertEqual(build.package_bytes(self.sources), self.artifacts)
        changed = dict(self.sources)
        changed["references/core/tone.md"] += b"\nSynthetic test change.\n"
        revised = build.package_bytes(changed)
        self.assertNotEqual(revised["oncoskill.zip"], self.artifacts["oncoskill.zip"])
        self.assertNotEqual(revised["oncoskill-chat.md"], self.artifacts["oncoskill-chat.md"])

    def test_rejects_unlisted_file(self):
        skill, manifest = self.fixture()
        (skill / "accidental-note.txt").write_text("Synthetic test only")
        with self.assertRaisesRegex(ValueError, "Unlisted files"):
            build.read_sources(skill, manifest)

    def test_rejects_symlink(self):
        skill, manifest = self.fixture()
        target = skill / "SKILL.md"
        target.unlink()
        target.symlink_to(build.SKILL / "SKILL.md")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            build.read_sources(skill, manifest)

    def test_rejects_path_traversal(self):
        skill, manifest = self.fixture()
        manifest.write_text("../outside.md\n")
        with self.assertRaisesRegex(ValueError, "Unsafe package path"):
            build.read_sources(skill, manifest)

    def test_rejects_missing_file(self):
        skill, manifest = self.fixture()
        (skill / "POLICY.md").unlink()
        with self.assertRaisesRegex(ValueError, "Missing package source"):
            build.read_sources(skill, manifest)

    def test_rejects_duplicate_entry(self):
        skill, manifest = self.fixture()
        manifest.write_text(manifest.read_text() + "SKILL.md\n")
        with self.assertRaisesRegex(ValueError, "Duplicate"):
            build.read_sources(skill, manifest)

    def test_policy_copies_match_and_schemas_parse(self):
        for name in ["POLICY.md", "INTENDED_USE.md", "DISCLAIMER.md"]:
            canonical = (build.ROOT / name).read_text().replace("skills/oncoskill/schemas/", "schemas/")
            self.assertEqual(canonical, self.sources[name].decode(), name)
        for name, data in self.sources.items():
            if name.endswith(".schema.json"):
                schema = json.loads(data)
                self.assertEqual(schema["type"], "object")
                self.assertTrue(set(schema.get("required", [])) <= schema["properties"].keys())
        self.assertIn('version: "' + self.sources["VERSION"].decode().strip() + '"', self.sources["SKILL.md"].decode())

    def test_relative_markdown_links_resolve(self):
        files = list(build.SKILL.rglob("*.md")) + [build.ROOT / p for p in ["README.md", "INSTALL.md", "docs/run-as-your-own-agent.md"]]
        for file in files:
            for raw in re.findall(r"\[[^\]\n]+\]\(([^\s)]+)\)", file.read_text()):
                url = urlsplit(raw)
                if url.scheme or url.netloc or not url.path:
                    continue
                with self.subTest(file=file.name, link=raw):
                    self.assertTrue((file.parent / unquote(url.path)).exists())


if __name__ == "__main__":
    unittest.main()
