#!/usr/bin/env python3
"""Build public downloads from an explicit file list. No network or runtime dependencies."""
from __future__ import annotations

import argparse
import hashlib
import io
from pathlib import Path, PurePosixPath
import posixpath
import re
from urllib.parse import unquote, urlsplit
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/oncoskill"
MANIFEST = ROOT / "scripts/package-files.txt"


def read_sources(skill: Path = SKILL, manifest: Path = MANIFEST) -> dict[str, bytes]:
    names = [s for s in manifest.read_text().splitlines() if s and not s.startswith("#")]
    if len(names) != len(set(names)):
        raise ValueError("Duplicate package manifest entry")
    result = {}
    for name in names:
        rel = PurePosixPath(name)
        if rel.is_absolute() or ".." in rel.parts or "\\" in name:
            raise ValueError(f"Unsafe package path: {name}")
        path = skill / name
        if any(part.is_symlink() for part in [path, *path.parents] if part != skill.parent):
            raise ValueError(f"Symlink in package path: {name}")
        if not path.is_file():
            raise ValueError(f"Missing package source: {name}")
        result[name] = path.read_bytes()
    actual = {p.relative_to(skill).as_posix() for p in skill.rglob("*") if p.is_file() or p.is_symlink()}
    if actual != set(names):
        raise ValueError(f"Unlisted files in skill directory; inspect before packaging: {sorted(actual - set(names))}")
    return result


def anchor(name: str) -> str:
    return "file-" + re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")


def chat_document(sources: dict[str, bytes]) -> bytes:
    # Historical release notes are not instructions for patient conversations.
    included = ["SKILL.md", "POLICY.md"] + sorted(set(sources) - {"SKILL.md", "POLICY.md", "CHANGELOG.md"})
    version = sources["VERSION"].decode().strip()
    parts = [f"""# Oncoskill {version} — use in a chat

Attach this file and ask your assistant to use Oncoskill for your question. Start with one task;
you do not need to fill out forms or upload medical records to begin.

For the assistant: read the SKILL.md and POLICY.md sections first, then locate the sections needed
for the question. This file includes all operational references and templates, with their original
paths as section labels; relative paths in a section refer to that original location. No browsing
of folders is needed. If your host cannot read/search a needed section, say so and request that
specific source file. Do not call a preview a successful load or promise persistent memory.
This is conversation guidance, not proof of a native installation. Historical changelog is omitted.

Source: https://github.com/VladShifter/oncoskill . Code/schemas: Apache-2.0; written content: CC BY 4.0.
Generated from the same sources as the zip; edit the source skill, not this document.

<details><summary>Reference index</summary>

"""]
    parts.extend(f"- [{name}](#{anchor(name)})\n" for name in included)
    parts.append("\n</details>\n")
    for name in included:
        text = sources[name].decode("utf-8")
        if name == "SKILL.md":
            text = text.split("---", 2)[2].lstrip()
        if name.endswith(".md"):
            def rewrite(match):
                label, target = match.group(1), match.group(2)
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    return match.group(0)
                resolved = posixpath.normpath(posixpath.join(posixpath.dirname(name), unquote(parsed.path)))
                if resolved in included:
                    return f"[{label}](#{anchor(resolved)})"
                raise ValueError(f"Unresolved chat link in {name}: {target}")
            text = re.sub(r"\[([^\]\n]+)\]\(([^\s)]+)\)", rewrite, text)
        else:
            language = "json" if name.endswith(".json") else "text"
            text = f"````{language}\n{text.rstrip()}\n````\n"
        parts.append(f'\n---\n\n<a id="{anchor(name)}"></a>\n\n## Source file: {name}\n\n{text.rstrip()}\n')
    return "".join(parts).encode("utf-8")


def package_bytes(sources: dict[str, bytes]) -> dict[str, bytes]:
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for name in sorted(sources):
            info = zipfile.ZipInfo("oncoskill/" + name, date_time=(2020, 1, 1, 0, 0, 0))
            info.create_system = 3
            info.external_attr = 0o100644 << 16
            info.compress_type = zipfile.ZIP_DEFLATED
            z.writestr(info, sources[name], compresslevel=9)
    result = {"oncoskill.zip": buf.getvalue(), "oncoskill-chat.md": chat_document(sources)}
    result["SHA256SUMS"] = "".join(
        f"{hashlib.sha256(data).hexdigest()}  {name}\n" for name, data in sorted(result.items())
    ).encode()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if committed downloads differ from sources")
    args = parser.parse_args()
    artifacts = package_bytes(read_sources())
    target = ROOT / "downloads"
    if args.check:
        stale = [name for name, data in artifacts.items() if not (target / name).is_file() or (target / name).read_bytes() != data]
        if stale:
            raise SystemExit("Stale downloads; run python3 scripts/build_packages.py: " + ", ".join(stale))
        print("Package source parity: PASS")
    else:
        target.mkdir(exist_ok=True)
        for name, data in artifacts.items():
            (target / name).write_bytes(data)
            print(f"Built downloads/{name}: {len(data):,} bytes")


if __name__ == "__main__":
    main()
