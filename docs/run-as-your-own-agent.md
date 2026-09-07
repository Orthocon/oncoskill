# Use Oncoskill in your assistant

Start by giving your assistant [the repository link](https://github.com/VladShifter/oncoskill) and
asking it to help install and use Oncoskill. It should follow [INSTALL.md](../INSTALL.md), check what
your app actually supports, and help with your first question. You don't need to learn the folder layout.

## If your app supports custom Skills

Download [oncoskill.zip](../downloads/oncoskill.zip?raw=1) and give it to the app's custom-Skill installer.
The archive contains one `oncoskill/` folder with `SKILL.md`, references, templates, and policies.
It does not contain the development repository or evaluation cases.

For Claude, use its custom-Skill upload feature when available in your account. A Project attachment
and an installed Skill are different: attaching a file does not prove automatic skill activation.
See [Anthropic's current instructions](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview).
For a CLI or another agent, let the assistant check that runtime's current installation method and
load the whole `skills/oncoskill/` directory. Do not replace an existing configuration without checking it.

## If you use an ordinary chat

Download [oncoskill-chat.md](../downloads/oncoskill-chat.md?raw=1), attach it, and say:

> Use the attached Oncoskill instructions to help me. First read its SKILL.md and POLICY.md sections,
> then the sections needed for my question. Tell me if you cannot read something. My question is: …

The document contains the operational references and templates in one place. It needs an assistant
that can read/search the attachment; reading a preview or only its beginning is insufficient.
This uses Oncoskill in the conversation, not a permanent native installation. If attachment limits
prevent access, the assistant should say so and request just the relevant source file from the repo.

## Start with one useful task

For example: “I have an oncology appointment tomorrow. Help me prepare three questions from this
report.” Or: “I am helping someone with treatment and feel lost. Help me choose one thing to do today.”
No document is required to start. Before uploading one, consider removing unnecessary identifiers;
storage and access depend on your app and settings, not on the skill.

When helpful, keep one short [Current State](../skills/oncoskill/assets/state-templates/current-state-simple.md)
note outside any public repository. The assistant must say whether it can save changes. If it cannot,
it gives you an update to copy; provide the latest note in a new chat when needed.

## What the assistant should confirm

Briefly, in your language: which version it loaded, whether it can read the relevant files and your
documents, whether live research is available, and whether updates can actually be saved. It should
then help with your question. It should not call a README preview an installation or claim every
medical reference was reviewed recently.

All paths preserve the same boundaries: explain, check evidence, prepare questions and drafts;
support second opinions and patient choice; never prescribe or send anything on your behalf.
See the [policy](../skills/oncoskill/POLICY.md).

The packages are checked locally for structure and content. Compatibility and behaviour in each host
still need an actual run; we do not claim that every listed platform has been tested. The format is
documented in the [Agent Skills specification](https://agentskills.io/specification).
