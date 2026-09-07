# Research synthesis (design rationale)

A human-readable digest of the research and verification behind Oncoskill's v0 design, so the
reasoning doesn't dissolve into chat history. Every factual claim here is backed by a source in
[../research/source-ledger.yaml](../research/source-ledger.yaml). All passes ran 2026-06-19.

---

## 1. The gap Oncoskill fills

Many tools (BelongAI Dave, Galen, Ankr, Outcomes4Me, OncoTeam, RoupenMD, PancrePal, …) help
patients **understand** cancer information. Almost none **run the operational process** of
treatment. The unmet need — and Oncoskill's focus — is:

> *"What do we do now, who do we ask, what do we send, what do we check, and what must we not
> forget?"* — plus a caregiver mode for the 3-a.m. anxiety, deadlines, and knowing when to stop.

Existing tools mostly answer *"what does this mean?"*. Oncoskill answers *"what do we do about
it?"* while staying strictly out of diagnosis and prescribing.

## 2. What we reuse from open source (and what we don't)

- **RoupenMD (Apache-2.0)** — the best safety/scaffolding template: explicit no-diagnose /
  no-prescribe / no-treatment-change rules, a citation/evidence-ledger requirement, a
  reading-level target, and a 3-tier specificity gate with an "abstain" fallback. Verified
  Apache-2.0 with original prompt files (no nested third-party license). **We adapt the design
  with attribution** (no NOTICE file upstream; we retain the license + state modifications).
- **OncoTeam (MIT)** — learn-from reference for decomposing care-ops into discrete tasks. We do
  not lift its app infrastructure.
- **patiently-ai** — the closest document-explainer skill, good **structure** to study. But the
  host repo has only an MIT *badge* and **no actual LICENSE file**, and the skill is third-party
  branded (PharmaTools.AI). **Learn structure only; write original text.**
- **CANQURE** (CRUD app + unvalidated ML) and **PancrePal** (stale stub) — low/again learn-only.

## 3. Two corrections to earlier source material

- **"Galen Cancer Navigator" is mis-scoped.** No such consumer patient app was confirmed; the
  real galenhealth.org is a **B2B clinician** tumor-board tool. Don't model a patient product on
  it.
- **BelongAI "validated at ASCO 2024" is overstated.** The ASCO 2024 abstract is real, but it's
  a vendor-co-authored **perception survey of 8 oncologists**, not an RCT or outcomes study.
  Treat "validated" with skepticism.

## 4. Anthropic Agent Skills — verified spec (drives the architecture)

Verified against the official docs (overview + skills-guide):

- A skill is a directory; `SKILL.md` = YAML frontmatter + Markdown body, optional `scripts/`,
  `references/`, `assets/`.
- **Required frontmatter:** `name` (≤64, lowercase `a-z 0-9 -`, no `anthropic`/`claude`, no XML)
  and `description` (≤1024, says *what + when*). Optional: `license`, `compatibility`,
  `metadata` (version goes here), `allowed-tools` (experimental). No standalone `version` field.
- **Progressive disclosure:** metadata ~100 tokens (always) → SKILL.md body **<5k tokens**
  (on activation) → bundled resources (on demand, effectively unlimited).
- **Custom skills do NOT sync across surfaces** → the installable package must be
  **self-contained** (license, schemas, references all live inside `skills/oncoskill/`).
- **Network access by surface:** Claude API = **none** (code-execution container has no
  internet); claude.ai = depends on settings; Claude Code = full. → **dual-mode keyed on the
  tools actually available**, never on the surface name; no unconditional "fetch the live page."
- **Not eligible for ZDR** → tell users before they upload.
- Official **security warning**: use skills only from trusted sources; external-URL fetches are
  risky → trust model in README; v0 ships no scripts and no outbound network.
- Limits: up to **8 skills/request** (Messages API); each skill bundle **<30 MB**. (A claimed
  "20 per session" limit was not verified by us; moot for a single skill — don't design around
  the number.)

## 5. Evidence standard and source hierarchy

Current clinical guidelines / specialty-society consensus (NCCN, ESMO, ESGO, ESTRO, FIGO; ESPEN
for nutrition; IPOS/APOS/NCCN-Distress/Macmillan/CancerCare for psycho-oncology) > systematic
reviews > major-center patient guidance > peer-reviewed studies. Forums/blogs/social are not
evidence. Phrase strength honestly: *"guideline/consensus-recommended"* ≠ *"RCT-proven."* Every
bundled clinical fact carries claim-metadata and a `review_due` date.

## 6. The v0 golden-test vehicle: skull-base chordoma → particle therapy

We needed a **neutral** clinical scenario that mirrors the project's founding care-ops arc:

1. an **outcome-determining** part of treatment;
2. whose **advanced version is the guideline-recommended standard** for that situation;
3. that is **not available in the patient's own country**;
4. so the patient must **organize a cross-border transfer themselves (S2 / Directive 2011/24)**;
5. with **local clinician under-offering** plausible.

Four independent research agents converged on **skull-base chordoma → high-dose particle
(proton/carbon-ion) radiotherapy**:

- Local control = survival; the **radiotherapy modality is the outcome lever** (radioresistant
  tumour adjacent to brainstem/optics).
- ESMO bone-sarcoma CPG: particle therapy *"should ... be considered the treatment of choice
  [IV, B]"* — the strongest neutral-site guideline language. **Consensus/observational, not an
  RCT** — so the skill must say "guideline-recommended," not "proven."
- Carbon-ion exists in the EU only in Austria (MedAustron), Germany (HIT, MIT), Italy (CNAO);
  Ireland/Finland have no proton centre. Cross-border S2 is **documented**: the Irish HSE
  leaflet literally walks through "E112(IE), also known as the S2 form"; the Chordoma Foundation
  EU has a dedicated S2/Directive page; the NHS ran a Proton Overseas Programme.
- **Fully synthetic:** selected to test a clear modality/access question and an EU funding route.
  The fictional details are not a coded description of any real patient's case.

**Scope discipline:** the test stays strictly on the **radiotherapy-modality + S2** decision,
**not** the surgical part. Alternatives considered: **NET → PRRT (Lutathera)** — strongest
guideline grade (ESMO [I,A], RCT) and more relatable, kept as a **later public demo**, but its
cross-border arc is weaker (EU-wide approval, gap is centre-level not country-level);
**limb-sarcoma → ILP** — rejected.

## 7. Locked v0 decisions

- **One self-contained installable skill** `skills/oncoskill/`; thin `SKILL.md`, depth in
  `references/`.
- **Generic core**; cross-border/S2 is a **core competency**, not a disease pack. **No disease
  pack in v0**; first disease pack later under a **common** cancer (for reach + relatability).
- **Dual mode** (Evidence default / Live research when tools allow).
- **Synthetic, labeled** example cases only; real cases stay in git-ignored `evals-private/`.
- **License:** Apache-2.0 (code/schemas/tests) + CC BY 4.0 (content); name/logo via trademark,
  not a non-commercial restriction.
- **`next-action`** carries the lived-experience plays: **Institution Channel Map**,
  **escalation/de-escalation playbook**, power-of-attorney as a tool, and
  owner/follow-up/escalation-condition tracking.
- **Build order:** ① skeleton + licensing + source-ledger + schemas + this synthesis + one
  golden test → ② the two workflows (explain-document, next-action) → caregiver module next.

## 8. Honesty / open caveats

- Chordoma "standard of care" is **consensus/observational**, not RCT — phrased accordingly.
- The "local clinician under-offers" leg is plausible but not quantified in a study; the
  synthetic case presents it as realistic, not as a cited fact.
- A few sources were bot-blocked to automated fetch (NCCN, EUR-Lex, the Portuguese Diretiva
  portal) — these are flagged `medium`/`low` confidence in the ledger; verify in a browser
  before citing to a user.

## 9. Roadmap (post-core / deferred — do not build in v0)

Captured so it isn't lost; built only after the core slice passes its tests
(infrastructure freeze until then).

- **Cross-framework portability.** Today the installable artifact is a Claude Agent Skill
  (`SKILL.md`). The Agent Skills format is an open standard adopted by several non-Claude agents
  (Cursor, Gemini CLI, Copilot, Codex, Goose, OpenCode), so it is already portable to a number of
  runtimes. For runtimes that don't read it natively (e.g. a from-scratch Hermes/OpenClaw agent),
  ship a **portable plain-instructions version + a short "install in your agent" guide** per
  convention. This serves the "maximum reach" mission and is a strong v1+ deliverable.
- **Cross-border jurisdiction modules** beyond EU/S2 (UK, US, national treatment-abroad schemes).
- **First disease pack** under a *common* cancer (chosen later, public-guideline-only) — a
  maintainer decision; flagship candidates weighed for reach and public-guideline coverage.
- **Later modes**: caregiver (next, right after core), nutrition claim-check, evidence/care-plan
  gap-check; then survivorship, hypothesis lifecycle.
- **Family-communication rules** (a dedicated module): how to talk with family — sharing news,
  involving relatives, managing conflicting opinions, protecting the patient's wishes, talking with
  children. *To be scoped later; needs its own source search (psycho-oncology / IPOS / Macmillan /
  CancerCare family-support materials).*
- **Second relatable public demo** case (NET → PRRT) for outreach/the public post.
