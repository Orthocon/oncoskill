# Contributing to Oncoskill

Thank you for helping. Oncoskill is a free, public-good tool for cancer patients and caregivers, and
it is meant to be improved by many people — including non-technical contributors. This page is the
"rules of the house" so quality and safety stay high. Please read it before you propose a change.

If anything here is unclear, open an issue and ask — that's a contribution too.

## The non-negotiables

1. **Never commit real patient data.** No real names, dates of birth, record numbers, contacts,
   addresses, or anyone's actual medical details — not even relabeled as "example". Use synthetic,
   clearly-labeled illustrative cases. A pre-commit scan (`scripts/phi_scan.py`) helps catch slips,
   but it's only a backstop — the rule is on you.
2. **Verify before you assert.** Every clinical claim needs a real, current source; never invent a
   name, dose, figure, version, or contact. If you can't verify something, mark it unverified and say
   so. (See the source hierarchy below.)
3. **Keep the safety boundary.** Oncoskill explains, prepares, and drafts — it does not diagnose,
   stage, prescribe, change treatment, or act on its own, and it routes red-flag symptoms to the care
   team / emergency services. Don't add anything that crosses that line. (Full rules:
   [POLICY.md](POLICY.md), [INTENDED_USE.md](INTENDED_USE.md), [DISCLAIMER.md](DISCLAIMER.md).)
4. **Simplicity for a stressed, non-technical person beats cleverness.** If a change makes the tool
   harder to use, it isn't an improvement.
5. **Keep the voice human.** Warm, plain, honest — not a report, not sugar-coated, not frightening
   (see `skills/oncoskill/references/core/tone.md`).

## Source hierarchy (for any evidence you add)

Current clinical guidelines / specialty-society consensus (NCCN, ESMO, ESGO, ESTRO, FIGO; ESPEN for
nutrition; IPOS/NCCN-Distress/Macmillan/CancerCare for psycho-oncology) > systematic reviews >
major-center patient guidance > peer-reviewed studies. Forums, blogs, and social media are **not**
evidence. State strength honestly — "guideline/consensus-recommended" is not "proven by a randomized
trial". Record the source in [research/source-ledger.yaml](research/source-ledger.yaml) and put the
checked passage, dates, strength, and applicability in the installed
[checked source notes](skills/oncoskill/references/support/verified-sources.md). A homepage, link check,
or agreement between models is not verification of a medical claim.

## How the project is laid out

- `skills/oncoskill/` — the installable skill (self-contained). `SKILL.md` is the thin router; depth
  lives in `references/` (core voice/rules, modes, support), with `schemas/` and `assets/`.
- `docs/`, `research/` — the design rationale and the research register.
- `evals/` — synthetic test scenarios (with `Expected` / `Forbidden` contracts). `evals-private/` is
  git-ignored and never published.

> **Duplicated-on-purpose files — keep them in sync.** So the binding rules travel inside the
> uploaded bundle, `POLICY.md`, `DISCLAIMER.md`, and `INTENDED_USE.md` exist **twice**: the repo-root
> copy is the source of truth, and a copy lives inside `skills/oncoskill/`. **If you edit the root
> copy, re-copy it into `skills/oncoskill/` in the same change** (the only intended difference is that
> in-skill links are relative — e.g. `schemas/…` instead of `skills/oncoskill/schemas/…`). A stale
> in-skill copy means installed users get the wrong policy — treat a drift between them as a bug.
> The research register `research/source-ledger.yaml` is deliberately **not** bundled; in-skill files must
> refer to it as "the project repo source ledger (not bundled)," never link it as if installed users
> can open it.

## Build and check the downloads

The user-facing zip and single chat document are committed under `downloads/`, so users can fetch them
from the repository without running a build. Edit `skills/oncoskill/`, not generated downloads.
The explicit `scripts/package-files.txt` lists what may ship; inspect any new file before adding it.
The builder rejects missing/unlisted files and symlinks, and never reads the development worktrees.

Run `python3 scripts/build_packages.py`, then `python3 -m unittest discover -s tests -v` and
`python3 scripts/build_packages.py --check`. These offline tests cover extraction, dependencies,
content parity, unsafe paths, and duplicate policies. They do **not** test a model or prove native
activation. For behaviour changes, run the affected synthetic cases in `evals/public/`, record the
actual model/host/tools and response, and distinguish a fresh run from an editing-session walkthrough.

For the PHI scan, pass the public source files being proposed for publication; do not recursively scan
private worktrees or medical notes. Review every candidate: public source dates/contacts and labeled
synthetic data can trigger the scanner. Do not mark a warning scan clean without inspecting it.
Generated downloads are covered by the exact-source-parity check and the same source review.

## Good ways to contribute

- **Improve wording** so it's clearer and more human for a frightened reader.
- **Add or correct a source** in the ledger (with a real link + date).
- **Add a support resource** (a real, reputable org / helpline) with attribution.
- **Propose a new disease pack** — built from public guidelines only, each claim carrying the
  metadata in `schemas/claim.schema.json` (source, version, `verified_at`, `review_due`, strength).
- **Add a synthetic eval** (input + `Expected` + `Forbidden` + rubric) for a behaviour we should
  guarantee.
- **Translate** templates or content (keep meaning and the safety wording intact).

## How to propose a change

1. Fork the repo and make your change on a branch.
2. Build/check the downloads above and run `python3 scripts/phi_scan.py` with the public source paths
   being changed. Inspect candidates and make sure no real patient data is present.
3. Open a pull request describing **what** changed and **how you verified** it (which source, which
   eval). If it touches clinical content, cite the source.
4. Be ready for review focused on safety, accuracy, simplicity, and tone.

## What not to do

- Don't turn Oncoskill into an "AI doctor", add autonomous send/act features, or have the skill fetch
  hidden external URLs.
- Don't paste third-party text you don't have the right to relicense (learn the structure, write your
  own — see [NOTICE](NOTICE) and the source ledger).
- Don't add real patient data. (Yes, it's worth saying twice.)

## License

By contributing, you agree your contributions are licensed under the project's terms: code/schemas/
tests under Apache-2.0 ([LICENSE](LICENSE)), written content under CC BY 4.0
([LICENSE-CONTENT.md](LICENSE-CONTENT.md)).
