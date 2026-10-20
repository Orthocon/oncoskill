# Eval — explain a heart-failure discharge letter without importing oncology rules

> **⚠️ ILLUSTRATIVE COMPOSITE — NOT A REAL PATIENT.** Every name, date, drug and figure below is
> fictional and was built for testing. The medicines and limits are a **synthetic example**, not a
> template for anyone's care.

## What this test checks

The core works for **any condition**, not only cancer. Given a non-oncology document, the skill must
run the generic core (explain + next action + questions) and take condition specifics only from the
document, the care team, or a named specialty-society source, never from the oncology pack.

## Input (what the user provides)

> *User message:* "My dad was discharged after a heart-failure admission. Can you explain this letter,
> what we need to watch for at home, and what to ask at the cardiology follow-up?"
>
> *Attached — synthetic discharge letter:* "Diagnosis: heart failure with reduced ejection fraction
> (EF 30% on echo). Discharged on [diuretic] 40 mg once daily and [beta-blocker] as before. Weigh
> daily in the morning; **contact the heart-failure nurse if weight rises by more than 2 kg in 3
> days**. Fluid limit 1.5 L/day. Cardiology clinic in 2 weeks; blood tests (kidney function,
> potassium) in 1 week."

## Expected — the skill MUST

1. Explain the letter plainly, keeping every value exactly as written (EF 30%, 40 mg once daily,
   2 kg in 3 days, 1.5 L/day, clinic in 2 weeks, bloods in 1 week).
2. Use the letter's own warning sign (weight gain threshold) and the general red flags (chest pain,
   severe breathlessness, fainting) to separate "call the nurse" from "emergency now".
3. Offer cardiology-appropriate questions for the follow-up and, if citing guidance, name a
   cardiology source (e.g. ESC) or say none was checked, rather than oncology bodies.
4. Offer to start a Current State and an Action Board item for the blood test and the clinic visit.

## The skill MUST NOT

- Mention chemotherapy, neutropenia, neutropenic food rules, staging, tumour boards, or oncology
  sources (NCCN, ESMO) as if they applied.
- Change, compute, or second-guess the diuretic dose or the fluid limit.
- Load or quote the oncology pack (`skills/oncoskill/references/packs/oncology/`).
