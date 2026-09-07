# Evals

These are the behavioural tests Oncoskill must pass before a slice is considered done.

## Two folders

- **`evals/public/`** (this repo): **fully synthetic** scenarios. No real patient. Each case is
  an illustrative composite, clearly labeled, with its clinical arc grounded on real published
  sources (cited in [../research/source-ledger.yaml](../research/source-ledger.yaml)) — the
  *patient* is fictional, the *clinical pattern* is real.
- **`evals-private/`** (git-ignored, local only): any real retrospective material a maintainer
  uses to sanity-check the design. **Never committed.** See `.gitignore`.

## What a golden test contains

- **Input** — what the user provides (a synthetic document/notes + an ask).
- **Expected** — what the skill *must do* (explain, separate facts/interpretation/unknowns,
  missing-check, diplomatic doctor questions, next actions, dated evidence line).
- **Forbidden** — what the skill *must not say or do* (diagnose, prescribe, categorical
  treatment determination, claim to replace the team).
- **Rubric** — how to score pass/fail.

## How to run (v0)

v0 is prompt/reference content with no executable harness. To run a golden test by hand: load
`skills/oncoskill/` as the skill, paste the test **Input**, and check the response against
**Expected** and **Forbidden** using the **Rubric**. An automated harness may come later.

## Current cases

**Core / golden:**
- `public/colorectal-explain-nextstep.md` — **primary** (common scenario): explain a document +
  decide next steps + catch a missing standard step, raised as a question.
- `public/chordoma-crossborder-core.md` — edge case: advanced guideline-standard modality unavailable
  locally → cross-border S2; raise the question, don't decide.
- `public/prompt-injection.md` — red-team: a malicious instruction hidden inside an uploaded document.

**Lived-experience behaviours (synthetic):**
- `public/symptom-trend.md` — new severe symptoms mid-treatment must NOT be normalized → escalate.
- `public/medication-adverse-effect.md` — med boundary: no personal dose, no green-lighting a combo, pharmacist-first.
- `public/documented-stage-restate.md` — restate a documented stage; never infer one.
- `public/prognosis.md` — safe prognosis (no death-clock).
- `public/oncofertility-decision.md` — closing window; options without a verdict; "preserve an option, not a guarantee".
- `public/post-op-aftercare.md` — discharge note; routine vs urgent; no prescribing.
- `public/caregiver-breakdown.md` — caregiver overload; steady + route, no platitudes.
- `public/food-safety.md` — food safety without panic or over-restriction.
- `public/plan-gap.md` — local plan may omit a guideline option → raise as a question.
- `public/technical-capability-audit.md` — don't infer capability from a marketing page; gate questions.
- `public/private-fallback.md` — private fallback for a public delay; will the team accept the result?
- `public/consultation-tracker.md` — keep questions trackable; post-consult checklist.
- `public/redaction-consent.md` — what to strip before sharing a doctor pack; consent/authority.
- `public/conflicting-guidelines.md` — present both honestly; question for the team.
- `public/unsupported-centre-claim.md` — no vague "best centre"; criteria-based comparison.
- `public/live-interpreter.md` — faithful real-time translation; preserve doses/dates; no advice.

**0.1.1 regressions:** `public/release-regressions.md` covers setup from a link, fever outside an assumed
window, iron route, review of agreed plans, complaints during treatment, honest persistence,
model consensus, and embedded document commands. Food-safety and redaction expectations were corrected.
Do not use the old result file as evidence that the new version passes these cases.

## Offline checks versus behaviour

`python3 -m unittest discover -s tests -v` verifies package integrity and installation files without
calling a model. The editing-session examples in `results/2026-09-07-walkthrough.md` show intended
responses and their limitations; they are not fresh model runs. No 0.1.1 cross-host behavioural PASS
is claimed until actual responses are recorded with provenance.

## Recording a run

When you run an eval, record the **provenance** of the run alongside the result: model + version,
date/time, surface (Claude Code / claude.ai / API), and which tools were available (Evidence mode vs
Live research). The **prompt-injection** case in particular must be *actually run*, not just present —
record its pass/fail with the model used. See `evals/results/` for the format.
