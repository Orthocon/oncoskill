# Feedback synthesis (review → design rationale)

A de-identified, product-level digest of the multi-chat review that drove this build wave, so the
reasoning behind each addition doesn't dissolve into chat history. This is a **working doc**: it
records *what gaps the review surfaced and what feature-level change answered each one* — nothing
case-specific. It is the companion to [research-synthesis.md](research-synthesis.md) (which covers
the v0 design rationale) and to the source additions in
[../research/source-ledger.yaml](../research/source-ledger.yaml).

A standing rule shaped every change below, so it's stated once here rather than repeated per item:
**Oncoskill is built from one private case, so every lived specific is generalized.** A drug, dose,
food rule, legal basis, contact, technique name, or protocol number that appeared in the review is
carried into the skill only as a *flagged example* of a general principle — never as a universal
rule — with the standard "adapt to your region and follow your own team" caveat at the top of any
lived, medical, financial, or legal module. Worked examples are synthetic composites. Nothing here
contains a real name, clinic, case, or personal detail.

---

## 1. Corrections — things stated too strongly the first time

The review caught a handful of places where the skill (or its eval set) implied more certainty than
the evidence carried. The fix in each case is the same posture: **say what the source actually
supports, mark the rest as a question.**

- **A lab value flagged as "slightly low" with no reference range present.** The skill's own rule is
  that a value only gets interpreted as in- or out-of-range when the range is actually in the
  document. The golden eval violated its own rule. Corrected to state the value as *mentioned in the
  report — worth confirming the reference range and whether it needs attention*, not as a soft
  diagnosis.
- **Evidence-strength language.** Reinforced throughout: *"guideline-/consensus-recommended"* is not
  *"RCT-proven,"* and the difference is stated rather than blurred. Conference abstracts are kept
  separate from peer-reviewed evidence wherever the skill weighs sources.
- **Diagnosis/stage restated vs inferred.** Made an explicit, repeated boundary: the agent may
  *faithfully restate* a stage a signed report documents, but never independently infers one from raw
  data or images. This was promoted from an implicit norm to a stated rule with its own eval.

## 2. The founding gap — a care-plan gap-check engine

The single largest theme in the review: the most valuable thing the tool can do is help a frightened
person notice when a **guideline-supported option may be missing from the local plan** — and do it
*without* turning into "your doctor is wrong." This became the founding gap-check capability:

- Define the exact clinical question; work from documented facts only; check whether
  staging/pathology/biomarkers are even complete enough to reason about; line up the applicable
  guideline decision-nodes; compare expected-vs-local-plan-vs-what's-missing.
- **Classify the difference** instead of assuming error: clinical reason / patient preference /
  resource or capability gap / outdated practice / insufficient data / legitimate disagreement. Most
  "gaps" have an innocent explanation; the tool's job is to surface a *question*, not a verdict.
- Output a short **Care Plan Gap Brief** artifact (question, documented facts, missing facts,
  guideline-expected step, local plan, possible explanations, evidence for/against, urgency,
  diplomatic questions, what-would-change-the-plan). Recorded as a **section of Current State**, not a
  new tracker.
- An **advanced-technique quality gate** phrased generically: don't ask a centre "do you do
  [procedure]?" — ask whether they perform the *exact technique/configuration* for *this situation*,
  including the critical component if indicated, and accept a patient after a prior phase elsewhere
  within a stated window. Cancer-agnostic by construction.

This is the clearest expression of the advocacy stance the maintainer asked to keep prominent:
**trust your team, and verify** — calm, weighted, evidence-backed questions, not a fight with the
doctors, with the ultimate responsibility for the care received resting with the patient/caregiver.

## 3. The active-treatment layer — the part most tools skip

Review showed a whole missing surface: the day-to-day *internal loop* of being on active treatment,
where a caregiver most needs a steady second brain. Added as new modes:

- **On-treatment loop** — locate the person in their cycle, then separate *expected cumulative
  side-effects* from *red flags*, and explicitly **do not normalize** the danger signs (new severe
  weakness/near-faint, new back pain, reduced urination, confusion, fever during/after chemo,
  uncontrolled vomiting/diarrhoea, chest pain, breathlessness, new neuro symptoms, bleeding) → calm
  escalation plus a concise message for the team. Reading lab *trends* over single points.
- **Anemia as an operational blocker** — surfaced repeatedly as a fork that gets dropped: separating
  "oxygen-carrying capacity now" from "iron stores," the question of a target before
  chemoradiation/anaesthesia, and the fact that correction sometimes can be arranged faster. Framed
  as questions to the team, never self-treatment.
- **Medications** under the stricter public-tool boundary (see §5 of this list): explain a
  prescribed medicine and its leaflet, verify the active ingredient/dose *from the package* (brands
  differ by country — given only as a flagged example), flag interactions to the **pharmacist/team**,
  and **never compute a personal dose or green-light combining drugs.** The pharmacist is surfaced as
  the fast, free, underused first-line.
- **Perioperative** support (surgery day + first 72h), **oncofertility** under a closing window
  (options laid out, never chosen; the law-vs-medicine distinction flagged), **survivorship**, and
  the **patient's own mental health** (distinct from the caregiver's).

All of these route between each other rather than duplicating, and each opens with the
adapt-to-your-region caveat because each touches lived/medical specifics.

## 4. One place of memory — ledgers folded into Current State

The review exposed a real risk of **entity sprawl**: every new capability wanting its own tracker.
The decision, made explicit across the build, is that there is **one living source of truth, Current
State**, and the new things the review surfaced are *sections inside it*, not separate files:
medications, allergies, labs week-to-week, decisions, recommendations (doctor-given and self-found),
windows/deadlines, documents, team-given red flags, care-team contacts. Modules say "offer to update
the relevant section of Current State" and never invent a new ledger.

Only two artifacts stay genuinely separate, because they differ in *shape and audience*: the
**Outreach Ledger** (a clinic / second-opinion CRM) and the **Doctor Share Pack** (a clean outward
dossier, explicitly *not* the internal Current State). The schema was enriched additively to hold the
new sections; blank copy-paste templates were added in the human spirit for a stressed user to fill.

## 5. Access-engineering and finance — the operational spine

A dense cluster of review feedback was about the *logistics of getting care*, where small mistakes
are expensive and irreversible. Added or sharpened:

- **Multi-centre coordination** on the assumption that **centres do not talk to each other**: map
  every centre, one owner per *handoff* (the risk lives in the seams), make every forward explicit
  and confirmed.
- **"Burned bridge" play** for a channel that has gone cold or tense: recognise the signals, one ask
  per letter, let it cool, switch the "voice" to the patient, and **hold formal complaints and
  regulators until active treatment is over** (a public complaint mid-treatment can poison the
  relationship care depends on; small communities de-anonymize fast). Likewise **don't go to the
  media during active treatment** — document now, escalate later.
- **Sequencing before an irreversible or costly step**: confirm preconditions *in writing*, **never
  release a fallback before the primary is truly secured**, and run a one-screen sync-check before
  money moves.
- **Informed-decision delay**: overall treatment time often matters more than the exact start date,
  so a short weighted delay to confirm something is frequently safe — raised as a precise *question
  to the team*, not a reassurance the tool gives on its own.
- **Finance / payer map** broadened beyond the EU: the funding routes (pre-authorisation, direct
  billing, public cross-border, self-pay-then-reimburse, letter of guarantee, exceptional
  reimbursement) and which document each needs; **separating medical alignment from financial
  authorisation**; a cost-estimate / slot-hold checklist; and the recurring lesson that **verbal
  answers from payers are not decisions — get it in writing.**
- **Cross-border** specifics gained the **self-pay → private-insurance reimbursement** route as a
  third model, with the written-acceptance-before-wiring rule, the reimbursement evidence chain
  (estimate + final invoice in the patient's name + proof of payment, reconciled), the
  payment-source-vs-reimbursement-destination account trap, and a point-of-payment verification
  ritual. All flagged as mechanics that vary by insurer and country.

## 6. Support modules — match the help to the state

The review pushed back on generic "seek support" advice. The support layer now tries to match the
*kind* of help to the situation, each opening with the region caveat and each external resource
flagged "verify before relying; not endorsement; add to the ledger":

- **Authorised representative / records access** — when a clinic will only speak to the patient, the
  move is a legal-authorisation pack, not conflict; the instrument varies by jurisdiction (flagged
  example, not legal advice); a non-response is itself an event to log.
- **Pathology & biomarkers** — the bottleneck is usually the *specimen*, not the test; track the
  block, slides, scoring/assay, chain of custody; preserve material for future profiling.
- **Trials & compassionate use** — a navigation process and a routing path, always "worth asking,"
  never "you qualify"; compassionate use is a national route.
- **Second-opinion & molecular-profiling platforms** — listed as flagged, region/eligibility-
  dependent examples, never a ranking.
- **Psycho-oncology methods** — screen intensity first (self-harm → local crisis line *first*), then
  a chooser among approaches rather than a single referral; and the standing reminder that **the
  caregiver needs their own support, separate from the patient's.**
- **First country pack** — built as an explicitly-labelled *regional example* of what a country pack
  looks like, with all contacts marked "verify the current number before release." Other countries
  differ; the pack is a template, not a universal.

## 7. Research discipline — knowing when to stop

A theme that recurred: research can become its own anxiety loop. Added discipline:

- **Stop-rule / diminishing returns** — stop when new sources stop changing the decision, the
  question list, the uncertainty, or the next step.
- **Negative-search log** — record what was searched, where, and what was *not* found; absence of
  evidence is not evidence of absence.
- **Criteria-based centre comparison** — replace "the best centre" with transparent criteria
  (documented capability, disease-specific MDT, accreditation, published experience, accepts
  international, timeline, confirmed contact, funding route, unknowns). The tool refuses vague
  prestige ranking.
- **Privacy before multi-model research** — de-identified case summary by default; don't upload raw
  records to every model; log what was sent where; source PDFs carry metadata.
- **Doctor-facing evidence brief** — no "AI" in the title, but AI-assistance disclosed in the
  methodology; evidence levels marked; raw URLs; local clinical language. And the rule that **recalled
  clinical numbers never go into a message to a clinician** — only values the user supplies from their
  own documents.
- **Technical-capability audit** — distinguish a real clinical service from research-only, trial-only,
  or a marketing claim, and route each question to the right department.

## 8. Letters and scripts — the artifacts to act on

The review wanted more ready-to-adapt outputs, and a clean split between two classes of artifact:

- **Letters** — expanded from a small starter set to a fuller library of skeletons (slot hold,
  follow-up on silence, escalation, de-escalation, authorised-representative cover, cross-border
  support and home-system request, letter of guarantee, invoice-format and cost-estimate
  clarification, self-pay-plus-reimbursement clarification, imaging and pathology-block requests,
  medical-summary request, "for-the-record" summary after a verbal answer, technique-statement
  request, second-opinion medical-necessity questions, trial pre-screening, compassionate-use
  inquiry, and more). Each carries a one-liner of when/who/attach/ask and keeps the
  concise-respectful-specific rules.
- **Scripts** — a distinct, lighter class: 2–3 line interpersonal scripts for a reception desk, a
  phone call, or a first message to a named contact, with simple "if they say X, respond Y" branches,
  and local-language lines flagged as examples. Different shape from a formal letter, so kept
  separate.
- A **Doctor Share Pack** was added as a clean outward dossier with its own build workflow and a
  strict separation from the internal Current State and the private vault — including an explicit
  "what *not* to include" (internal/emotional notes, unverified AI hypotheses, stray personal data).

## 9. Evals — coverage for every new behaviour

The review's gaps became test cases. New synthetic, illustrative-composite evals were added so each
load-bearing behaviour is checked in the human voice (covering the topic, not printing analytical
headings): live medical-interpreter fidelity, food-safety without panic, the oncofertility decision,
post-op aftercare, caregiver breakdown, plan-gap-as-a-question, technical-capability audit, the
private-fallback test, the consultation-question tracker, redaction/consent before sharing,
conflicting guidelines, refusing an unsupported "best centre" ranking, the symptom-trend
non-normalization, a medication adverse-effect routed to the pharmacist, restating a documented stage
(not inferring), and the prognosis conversation (no death-clock). The eval README now lists the full
current set, and notes that runs should record provenance (model/version/tools/date) and that the
prompt-injection case must actually be run, not merely present.

## 10. Roadmap — surfaced but deliberately deferred

A few review threads are real but out of scope for this wave; captured here so they aren't lost:

- **Disease packs** beyond the first regional example, built only on public guideline content, chosen
  later for reach and relatability.
- **Cross-border modules** beyond the current set (further national treatment-abroad schemes).
- **Family-communication module** (sharing news, involving relatives, talking with children) — needs
  its own psycho-oncology source search before it's built.
- **Portable plain-instructions version** of the skill for non-Claude agents, per the cross-framework
  portability goal.
- A **fresh verification pass** on the review-surfaced sources, which currently sit at medium/low
  confidence with a "verify before public release" caveat precisely because they came via review, not
  a dedicated check.
