# Oncoskill

**A free, open-source toolkit for cancer patients, for their caregivers, and for anyone organizing
a loved one's treatment and helping them get through it.** It helps run the operational side:
understanding documents, preparing for consultations, deciding the next concrete step, organizing
second opinions and cross-border care, and holding the emotional load.

> Oncoskill does **not** replace doctors. It runs the operating system *around* the doctors —
> and helps people be **prepared, not confrontational**.

It is non-commercial in spirit; anyone may use, fork, and improve it.

> ⚠️ **Status: early release (v0.1.1).** This repository is being built in the open. Structure
> and content may change. Nothing here is medical advice.

## Start here

Give your assistant this message — it can handle the setup:

> Help me install and use Oncoskill: https://github.com/VladShifter/oncoskill . Read INSTALL.md,
> choose the simplest method this app supports, and verify the skill actually loaded. Then help
> with my first question. Reply in my language; tell me if you cannot read files or save updates.

По-русски:

> Помоги установить и использовать Oncoskill: https://github.com/VladShifter/oncoskill . Прочитай
> INSTALL.md, выбери подходящий способ для этого приложения и проверь, что скилл загрузился.
> Затем помоги с моим первым вопросом. Скажи, если не можешь читать файлы или сохранять изменения.

Or download [the Skill archive](downloads/oncoskill.zip?raw=1) / [the single chat document](downloads/oncoskill-chat.md?raw=1).
You can start without medical documents: “Help me prepare for tomorrow's oncology appointment.”
[More help with setup](docs/run-as-your-own-agent.md).

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
  the ingredient/strength **from the package** and regimen **from the prescription** (brands differ by country), and flags possible
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

Use the message or downloads in [Start here](#start-here). The installable package follows the
[open Agent Skills format](https://agentskills.io/specification). An assistant with native skill
support can install the folder; an ordinary chat can use the attached single document if it can
read/search it. Neither route guarantees persistent memory or internet access.

The agent's [installation instructions](INSTALL.md) and the [short user guide](docs/run-as-your-own-agent.md)
cover both routes. Help with the first real question comes before setting up notes or folders.

## Privacy & trust

Cancer documents are highly sensitive. Please read this before uploading anything.

- **Use a source you trust.** The installable skill contains no executable code. Your assistant may
  use its existing tools to read documents and research public sources for your request; it must not
  include patient identifiers in searches or upload private files to another service without consent.
  External sending, booking, payments, and sharing stay with the human.
- **The skill adds no special storage protection.** Retention, training use, and access depend on
  the app and settings, including whether it runs locally. Share only what is needed; removing
  identifiers first is allowed. The assistant gives a short reminder before document upload.
- **No real patient data lives in this repository** — only templates, logic, and synthetic
  illustrative examples. Keep your own and others' medical data out of any fork.

## Evidence mode vs Live research mode

Oncoskill checks the tools actually available in the current session:

- **Evidence mode:** explains supplied documents and uses the limited, dated
  [checked source notes](skills/oncoskill/references/support/verified-sources.md). Other clinical
  specifics are leads to verify, not a claim that the whole bundle has been medically reviewed.
- **Live research mode:** with an available web tool, reads original sources and checks the supporting
  passage and its applicability. A working URL or agreement between models is not verification.

It distinguishes when a source was published from when it was checked, and says when something
cannot be confirmed. If it cannot save your Current State, it provides an update to copy instead.

## Repository layout

```
skills/oncoskill/      The installable, self-contained skill (everything below ships in the bundle):
    SKILL.md             thin router
    AGENTS.md            install-as-an-agent entry point
    roles/               patient.md, caregiver.md — the two agent personas
    references/          the modes + core rules + support packs
    assets/, schemas/    templates, letters, scripts, and the state schemas
    POLICY.md, …         the binding policy + licenses that travel with the skill
downloads/             Ready-to-use zip and single chat document
INSTALL.md             Instructions for the assistant helping you set up
docs/                  Human-readable docs, incl. run-as-your-own-agent.md
research/              source-ledger.yaml — research register (repo-only, NOT bundled)
evals/                 Public, synthetic test scenarios (golden tests + red-team)
scripts/               Dev tools (e.g., a pre-commit scan for accidental personal data)
```

## Sources & evidence standard

Oncoskill follows a strict source hierarchy (current clinical guidelines > systematic reviews >
major-center patient guidance > peer-reviewed studies; forums/blogs/social are not evidence)
and phrases recommendations as *"guideline/consensus-recommended,"* never *"proven by RCT"*
unless that is literally true. Doctor names, doses, and figures always need a source. Start with the
[checked source notes](skills/oncoskill/references/support/verified-sources.md); the
[research register](research/source-ledger.yaml) also contains older leads requiring rechecking.

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
