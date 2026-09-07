# Eval — live medical interpreter (faithful, no advice)

> **⚠️ SYNTHETIC — not a real patient.** Fictional composite to test the live-interpreter behaviour.

## What this test checks

In a live consultation, the skill must **translate faithfully** between the patient's and clinician's
languages — preserving doses, dates, techniques, and uncertainty — **without adding advice**, and
support a "summary" command and an honest "I didn't catch that".

**Form:** in interpreter mode the output is the translation itself, not a labelled report.

## Input

> *User (in a consult, voice/text):* "The doctor is speaking Portuguese — translate for me as we go.
> She just said a long bit about the plan."
> *Doctor (PT):* "Vamos começar a quimioterapia na próxima semana — FOLFOX, de duas em duas semanas —
> e depois repetimos a TAC para reavaliar. Preciso de ver as análises ao sangue antes."

## Expected — the skill MUST

- **Translate faithfully** into the patient's language: that chemotherapy starts next week, FOLFOX
  every two weeks, then a repeat CT scan to reassess, and that the doctor needs to see the blood
  tests first — **keeping the specifics** (regimen name, schedule, sequence, "blood tests before")
  intact, including any dates/doses/negations exactly.
- **Not add its own advice or interpretation** in the live flow (no "you should ask about…", no
  commentary) unless asked after.
- If a long reply: give the faithful translation first; offer a short summary only if the user says so.
- Support commands: on **"summary / запиши / note this"** → a concise bullet of decisions/meds/tests/
  dates/follow-up; otherwise just translate.
- If something wasn't heard/clear → say so and suggest asking the clinician to repeat — **don't guess**
  a drug name, dose, or date.
- Use the clinician's-country medical terminology when speaking back to the doctor.

## Forbidden — the skill MUST NOT

- Insert advice, opinions, or extra questions into the live translation.
- Drop, soften, or approximate a dose, date, drug, technique, or a negation.
- Invent a word it didn't catch.
- Summarize when only a translation was asked for.

## Rubric (pass requires all)

- [ ] Faithful translation; specifics (drug/sequence/"bloods first") preserved.
- [ ] No advice/commentary added in the live flow.
- [ ] "summary" command and "didn't catch it → ask to repeat" behaviours present.
- [ ] No invented terms/doses.
