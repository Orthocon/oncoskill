# Oncoskill

Oncoskill is a free, open-source toolkit that helps patients with any serious or complex
illness (it started with cancer) and their caregivers run the operational side of treatment: understanding documents, preparing for consultations,
deciding the next concrete step, organizing second opinions, and managing the emotional
load. It does not replace doctors — it runs the operating system around the doctors, and
helps people be prepared, not confrontational. Non-commercial; anyone may use, fork, and
improve it.

> **Two AGENTS.md files, two purposes.** *This* file (repo root) is for people **building or
> contributing to** Oncoskill. To **install Oncoskill into your own agent** (Claude or another
> runtime — Codex, Hermes, OpenClaw, a custom bot), see
> [docs/run-as-your-own-agent.md](docs/run-as-your-own-agent.md) and the skill's portable entry point
> [skills/oncoskill/AGENTS.md](skills/oncoskill/AGENTS.md).

## Current direction (a working hypothesis, open to revision)
Where we lean today, not a locked decision. If you see a stronger path, propose it with
trade-offs.
- MVP is likely a SKILL (or small set of skills) in the Anthropic Agent Skills format,
  runnable inside a Claude Project / Cowork. A full autonomous agent is deferred to v2.
- The skill does two jobs: (1) explain any medical document in plain language + generate
  questions for the doctor; (2) answer "what do I do now / who to ask / what to send /
  what to check / what not to forget", with ready-to-send letter templates.
- Human always in the loop: it explains, prepares, drafts — it never sends or decides alone.
- Generic core first, for any condition. Cross-border / second-opinion access (including EU S2)
  is a core competency, not a disease pack. Condition-specific material lives in packs under
  `skills/oncoskill/references/packs/`; the first is `oncology/`. Skull-base chordoma is used only
  as a synthetic test vehicle, not a pack.

## Principles
- Simplicity for a non-technical person under stress beats technical elegance. If a change
  makes the tool harder to use, it is not an improvement.
- Evidence-aware, not catastrophic: calm, honest, not sugar-coated, not frightening.
- Source hierarchy: current clinical guidelines of the relevant specialty society (e.g. ESC, EAN,
  EULAR, KDIGO; for oncology NCCN, ESMO, ESGO, ESTRO, FIGO; ESPEN for nutrition;
  IPOS/APOS/Macmillan/CancerCare for psycho-oncology) > systematic reviews >
  major-center patient guidance > peer-reviewed studies. Forums/blogs/social are not evidence.
- Verify before asserting: doctor names, doses, figures need a source. Never invent.

## Guardrails
- Not an AI doctor: no diagnoses, prescribing, overriding clinicians, or emergency care.
  On red-flag symptoms, direct the person to their care team / emergency services.
- Draft-only: never auto-send or change anything external without explicit human approval.
- Don't build an autonomous agent at this stage (deferred to v2).
- Privacy: keep ALL personal/medical data of real patients OUT of this repo. Ship templates
  and logic only.

## How to work on this project
- Research → propose 2–3 options with trade-offs → wait for explicit approval before building
  or finalizing. Silence is not approval.
- Map interdependencies before implementing; don't refactor unrelated things.
- Don't report something as done without saying how it was verified.
- Keep it usable by non-technical contributors: plain-English README, clear structure.

Maintainer's personal working preferences are in CLAUDE.local.md (git-ignored, not published).
