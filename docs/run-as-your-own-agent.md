# Run Oncoskill as your own agent

Oncoskill is packaged as an [Anthropic Agent Skill](https://agentskills.io) (`skills/oncoskill/`), but
you don't have to use it only inside Claude. This guide is for someone who wants to put Oncoskill into
**their own agent** — on Claude or another runtime.

> The repo's *root* `AGENTS.md` is a different thing: it's for people building and contributing to
> Oncoskill. The file that orients an *agent* installing the skill is `skills/oncoskill/AGENTS.md`.

Whatever path you take, Oncoskill stays what it is: a **human-in-the-loop, draft-only, not-an-AI-doctor**
support tool. Don't deploy it anywhere that can't honour those boundaries (see "What every install must
carry", below).

## Path A — Claude (native, easiest, most tested)

- **claude.ai** (Pro/Max/Team/Enterprise, code execution on): zip `skills/oncoskill/` and upload it as a
  custom Skill in Settings.
- **Claude Code**: drop `skills/oncoskill/` into `~/.claude/skills/` (personal) or `.claude/skills/`
  (project).
- **Claude API / Developer Platform**: upload it via the skills endpoints and reference it with the code
  execution tool (beta headers required).

Note: custom skills **don't sync across surfaces** — install per surface. Privacy: Agent Skills are not
covered by Zero Data Retention; tell users before they upload documents.

## Path B — agents that read the open Agent Skills standard

The Agent Skills format is an **open standard** (agentskills.io), and per our research it has been
adopted by a number of non-Claude agents — **Cursor, Gemini CLI, OpenAI Codex, GitHub Copilot / VS Code,
Goose, OpenCode**, and others. Support evolves, so check your runtime's current docs. For these, point
the agent at `skills/oncoskill/` (or `SKILL.md`) and it reads the skill the same way Claude does.

Several of these (notably Codex) also read an `AGENTS.md` from a directory — `skills/oncoskill/AGENTS.md`
is there for exactly that, as a portable entry that points to `SKILL.md` and carries the safety rules.

## Path C — a generic / from-scratch agent (Hermes, OpenClaw, a custom bot, a plain system-prompt assistant)

If your runtime doesn't natively read the skill format, wire it up by hand:

1. Use **`skills/oncoskill/AGENTS.md`** as the entry point and **`SKILL.md`** as the system prompt.
2. Give the agent the files under **`references/`** as a knowledge base it can read on demand (core/,
   modes/, support/). If it *can't* read files on demand, **inline** `SKILL.md` + `references/core/*`
   into the system prompt and attach the rest (`references/modes/`, `references/support/`, `schemas/`,
   `assets/`) as documents/knowledge.
3. Keep **one Current State document** as the agent's memory
   (`skills/oncoskill/assets/state-templates/current-state.md`).
4. **You** are responsible for the human-in-the-loop wiring: this agent must not send, book, pay, or act
   externally on its own. If you can't guarantee that, don't deploy it.

A quick flattened single file you can paste into a plain assistant: the review bundle the maintainer
generates (`dist/oncoskill-review-bundle.md`) concatenates the skill into one document — usable as a
rough "everything in one place" system prompt, though it includes review/governance material you can
trim. A dedicated clean "system-prompt build" can be generated on request.

## What every install MUST carry (any runtime)

- **Not an AI doctor**: no diagnosis/prescribing/dosing for an individual; restate a documented stage,
  never infer one; red flags → care team / emergency.
- **Human in the loop, draft-only, no autonomous actions** — drafts only; a person sends.
- **Dual mode**: bundled dated facts by default; live lookups only with a real search tool; never assume
  internet.
- **Privacy**: sensitive health data, not ZDR-covered on most surfaces; warn before upload; no real data
  in any repo; share only on explicit approval.
- **The advocacy stance** (trust-and-verify, the system isn't always invested, the responsibility is the
  user's) and the **genericization** rule (everything specific is an example; adapt to the person's
  region/system/language; follow their team).

(These are the same boundaries enforced in `POLICY.md`, `skills/oncoskill/references/core/`, and
`SKILL.md`.)

## Honest status

Cross-runtime support for the skill format is real but **still evolving**, and a from-scratch agent
needs you to wire the human-in-the-loop yourself. This is an **early, optional** path — the native
Claude install (Path A) is the most tested. Treat non-Claude installs as something to verify carefully
before letting a real patient or caregiver rely on them.
