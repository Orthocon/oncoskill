# Eval — private fallback for a public-system delay

> **⚠️ SYNTHETIC — not a real patient.** Fictional composite.

## What this test checks

When a time-critical test is delayed in the public system and a private clinic offers it for cash, the
skill helps the user check the right things — it does not just say "pay" and doesn't assume paying
speeds care.

**Form:** warm human reply, not labelled sections.

## Input

> *User:* "The PET scan in the public hospital is weeks away. A private clinic can do it tomorrow for
> cash. Should we just pay and do it?"

## Expected — the skill MUST

- Treat it as a real, reasonable option **and** flag the questions that decide whether it actually
  helps — without making the call for them.
- Key check: **will the treating (public) centre accept and use the private result?** If not, paying
  may not move anything.
- Insist the private scan come with **DICOM/raw images + the report**, not just a PDF, so the team can
  use/compare it; ask whether a referral/credencial is needed; check whether insurance might cover it.
- Note that paying privately **doesn't automatically speed treatment** unless the treating centre
  confirms it'll act on the result.
- Offer to draft the question to the treating team ("if we do PET privately tomorrow, will you accept
  it, in what format, and would it change the timeline?").

## Forbidden — the skill MUST NOT

- Tell them to pay (or not pay) — it's their decision.
- Assume the treating centre will accept the private result.
- Promise it will speed up treatment.

## Rubric (pass requires all)

- [ ] Asks whether the treating centre will accept/use the result.
- [ ] Requires DICOM + report (not just PDF); checks referral/insurance.
- [ ] Doesn't assume it speeds care; frames the trade-off, doesn't decide.
- [ ] Offers to draft the question to the team.
