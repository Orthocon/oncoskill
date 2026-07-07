# Oncoskill

**A free, open-source toolkit for cancer patients, for their caregivers, and for anyone organizing
a loved one's treatment and helping them get through it.** It helps run the operational side:
understanding documents, preparing for consultations, deciding the next concrete step, organizing
second opinions and cross-border care, and holding the emotional load.

> Oncoskill does **not** replace doctors. It runs the operating system *around* the doctors —
> and helps people be **prepared, not confrontational**.

It is non-commercial in spirit; anyone may use, fork, and improve it.

> ⚠️ **Status: work in progress (v0).** This repository is being built in the open. Structure
> and content may change. Nothing here is medical advice.

## Your role: trust your team, and verify

The most important idea in Oncoskill is this: **you are the advocate.** Said plainly and without
cynicism — the health system gives you what it has, but it doesn't always go looking for the *best*
option for you, and no one is obligated to invest maximally in any single patient. A clinician can
genuinely care and still be limited by time, resources, or a reluctance to question their own
institution. So the stance Oncoskill takes is simple: **trust your team, and verify.** Ask, confirm
against current guidance, and get a second opinion when the stakes are high.

This isn't a fight with your doctors, and it isn't paranoia. It's calm, weighted, informed
decisions — and refusing to assume that the default path is automatically the best one for you. The
ultimate responsibility for the care you (or the person you care for) receive rests with you, and
Oncoskill exists to help you carry it: to understand what's happening, ask the right questions, and
keep the operational side from falling through the cracks. The patient stays the decision-maker
throughout — their consent and their wishes come first, always.

---

## What it does

Two core jobs:

1. **Explain any medical document in plain language** — a lab result, an MRI/PET/CT report, a
   pathology report, a discharge summary, a doctor's letter — and generate clear, diplomatic
   **questions for your doctor**.
2. **Answer "what do I do now?"** — *what to do, who to ask, what to send, what to check, and
   what not to forget* — with ready-to-send **letter templates** and a way to keep track of
   clinics, deadlines, and open questions.

Those two jobs sit at the centre, but the same calm, prepared approach extends to the rest of the
journey: support **during active treatment** (side-effects vs red flags, lab trends, readiness for
the next milestone), **cross-border care and the money side** (funding routes, insurance, getting
answers in writing), and **structured decision-support** for hard choices under uncertainty — always
as questions for your team, never a decision made for you. You don't pick a "mode" — you just talk,
and Oncoskill routes to the right help quietly in the background.

A human is **always in the loop**: Oncoskill explains, prepares, and drafts. It never sends,
decides, diagnoses, or acts on its own.

## What it is NOT

- **Not an AI doctor.** No diagnoses, no prescribing, no dose calculations for you, no telling you
  to start, stop, or change treatment, no overriding your clinicians, no emergency care. On
  red-flag symptoms it points you to your care team or emergency services. It can faithfully
  restate what a signed report already documents (e.g. a stage written in the report), but it won't
  independently infer a diagnosis or stage from raw data or images.
- **Not a medication adviser.** For prescribed medicines it explains the leaflet, helps you verify
  the active ingredient and dose **from the package** (brands differ by country), and flags possible
  interactions — but it does **not** compute a personal dose or green-light combining drugs. Those
  go to your **pharmacist** (fast, free, underused) and your team.
- **Not a place for your private data.** See [Privacy & trust](#privacy--trust) and
  [DISCLAIMER](DISCLAIMER.md).

Oncoskill is **not intended, validated, certified, or marketed as medical-device software**; its
regulatory status may depend on deployment, jurisdiction, and actual use. It's also general,
example-level guidance built from real experience — cancers, drugs, doses, food rules, laws, and
health systems differ by person and country, so adapt anything here to your own situation and follow
your care team's instructions over it. See [INTENDED_USE.md](INTENDED_USE.md) for the precise,
honest scope.

## How to use it (no coding required)

Oncoskill is an [Anthropic Agent Skill](https://agentskills.io). The simplest way to use it:

1. Open a **Claude Project** (or Claude with custom Skills enabled).
2. Upload the `skills/oncoskill/` folder as a custom Skill (or drop its contents into your
   Project's instructions/files).
3. Paste or upload a document and ask, e.g., *"Explain this and prepare questions for my
   doctor,"* or *"What should we do next?"*

> Oncoskill works best when it can read your documents, but it never needs the internet to be
> useful — see **Evidence mode vs Live research mode** below.

**Want it to act like a dedicated agent — a patient's assistant or a caregiver's right hand — rather
than a tool you invoke each time?** Oncoskill ships with two ready personas and a portable entry
point, so it can run the same way on Claude, Codex, or a from-scratch bot:

- **[skills/oncoskill/AGENTS.md](skills/oncoskill/AGENTS.md)** — the install entry point: pick a role,
  load the skill, keep the non-negotiables.
- **[roles/patient.md](skills/oncoskill/roles/patient.md)** and
  **[roles/caregiver.md](skills/oncoskill/roles/caregiver.md)** — the two personas (who you are, how
  you talk, how proactive to be).
- **[docs/run-as-your-own-agent.md](docs/run-as-your-own-agent.md)** — the plain-language how-to for
  setting this up across different runtimes.

## Privacy & trust

Cancer documents are highly sensitive. Please read this before uploading anything.

- **Only install Oncoskill from the official repository, and audit it before use.** Anthropic
  warns that skills from untrusted sources can misuse tools or leak data. Oncoskill is fully
  auditable, ships **no executable scripts and makes no outbound network calls** in v0, and
  never fetches hidden external URLs.
- **Agent Skills are not covered by Zero Data Retention (ZDR).** Anything you upload is handled
  under the standard data-retention policy of whichever Claude surface you use. Oncoskill shows
  a short privacy reminder before you share documents.
- **No real patient data lives in this repository** — only templates, logic, and synthetic
  illustrative examples. Keep your own and others' medical data out of any fork.

## Evidence mode vs Live research mode

Depending on where Oncoskill runs, it may or may not have internet access (the Claude API has
none; claude.ai depends on your settings; Claude Code has full access). So Oncoskill works in
two modes and tells you which one it's in:

- **Evidence mode (always available):** reasons only from what you provided plus its own
  *bundled, dated* reference facts. It will say *"reviewed through: <date> — confirm the current
  version with your team."*
- **Live research mode (only when a web/search tool is actually available):** can look up
  current guidance and cite it.

It never claims something is current without either a live check or a dated bundled source.

## Repository layout

```
skills/oncoskill/      The installable, self-contained skill (everything below ships in the bundle):
    SKILL.md             thin router
    AGENTS.md            install-as-an-agent entry point
    roles/               patient.md, caregiver.md — the two agent personas
    references/          the modes + core rules + support packs
    assets/, schemas/    templates, letters, scripts, and the state schemas
    POLICY.md, …         the binding policy + licenses that travel with the skill
docs/                  Human-readable design docs, incl. run-as-your-own-agent.md
research/              source-ledger.yaml — the audited source list (repo-only, NOT bundled)
evals/                 Public, synthetic test scenarios (golden tests + red-team)
scripts/               Dev tools (e.g., a pre-commit scan for accidental personal data)
```

## Sources & evidence standard

Oncoskill follows a strict source hierarchy (current clinical guidelines > systematic reviews >
major-center patient guidance > peer-reviewed studies; forums/blogs/social are not evidence)
and phrases recommendations as *"guideline/consensus-recommended,"* never *"proven by RCT"*
unless that is literally true. Doctor names, doses, and figures always need a source. See
[research/source-ledger.yaml](research/source-ledger.yaml).

## Optional: an early agent network

Entirely optional and non-core. Cancer centers, clinicians, and patients *can* connect agents on an
early open network (Tobira) so they can find and route to each other — honest, early-stage, and
**never** a place for medical data. **Transparency:** Oncoskill's author is also Tobira's founder, so
this is a related project, disclosed plainly and offered as an option, not pushed. See
[skills/oncoskill/references/support/agent-network.md](skills/oncoskill/references/support/agent-network.md).

## Contributing

This is a public-good project meant to be forkable and improvable by non-technical contributors
too — see [CONTRIBUTING.md](CONTRIBUTING.md). Core rules: keep it simple for a stressed non-technical
user, verify before asserting, and never commit real patient data.

## License

- **Code, schemas, and tests:** Apache License 2.0 — see [LICENSE](LICENSE).
- **Written content, templates, and reference text:** Creative Commons Attribution 4.0
  (CC BY 4.0) — see [LICENSE-CONTENT.md](LICENSE-CONTENT.md).
- Third-party attributions: [NOTICE](NOTICE).
- The name and logo "Oncoskill" are not licensed for use that implies endorsement; please don't
  use them to suggest a fork is the official project.
