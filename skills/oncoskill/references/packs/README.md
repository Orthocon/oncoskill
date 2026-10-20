# Condition packs

The core of Oncoskill (`../core`, `../modes`, `../support`, `../../assets`) is condition-agnostic:
explaining documents, next steps, consultations, second opinions, cross-border/S2 care, money,
caregiver support. A **pack** adds what is specific to one group of conditions. Load a pack only when
the person's documented condition matches it.

## Packs available

- `oncology/` — cancer: active chemo/RT days, fertility preservation before gonadotoxic treatment,
  survivorship, pathology & biomarker logistics, psycho-oncology. See `oncology/README.md`.

## No pack for the condition?

Run the generic core. Take condition specifics from the person's own documents and care team, and,
when a live search tool is actually present, from the relevant specialty society or national
guideline (see `../core/source-hierarchy.md`). Do not carry one pack's rules into another condition
(for example, neutropenic food rules or chemo-day logic do not apply to heart failure).

## Adding a pack

A pack lives in its own folder and contains: trusted sources (guideline bodies, patient
organisations), typical documents and how they are staged or graded, the usual care pathway, key
questions for the team, condition-specific red flags, nutrition and lifestyle considerations, and
life after the acute phase. Each clinical claim carries `../../schemas/claim.schema.json` metadata
(source, version, `verified_at`, `review_due`, strength, applicability). The skull-base chordoma
material in `evals/public/` is a **test vehicle**, not a pack.
