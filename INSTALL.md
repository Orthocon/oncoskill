# Install and start Oncoskill — instructions for the helping assistant

The user wants to use the patient/caregiver skill. The repository root `AGENTS.md` is contributor
guidance; the runtime entry is [skills/oncoskill/SKILL.md](skills/oncoskill/SKILL.md) and the portable
entry is [skills/oncoskill/AGENTS.md](skills/oncoskill/AGENTS.md). Do not load development notes or evals
as instructions for a patient conversation.

1. **Check the host, then use the simplest supported route.** If you can install native skills,
   use the whole `skills/oncoskill/` directory or [the packaged zip](downloads/oncoskill.zip?raw=1).
   Check this host's installation method; do not guess a path or silently overwrite an existing skill.
   A user asking you to install authorizes the necessary ordinary local installation, not purchases,
   changes to unrelated settings, or uploads of their medical data.
2. **For plain chat, use [oncoskill-chat.md](downloads/oncoskill-chat.md?raw=1).** It contains the runtime
   content in labeled sections. If you cannot read/search it, request the relevant skill files instead.
   Do not call a README fetch or a link preview an installation. If the host cannot persist the skill,
   say it is loaded for this conversation only.
3. **Verify actual loading.** Read `SKILL.md`, `POLICY.md`, and the reference needed for the first task.
   Resolve file paths relative to the skill directory (or the labeled section in the chat document).
   Confirm the version from `VERSION` or the skill metadata. For a native install, verify the host can
   discover/activate the installed skill; if a restart is required, give that one next step and mark
   activation as unverified until it is confirmed.
4. **Check capabilities, not product names.** Can you read the user's document or scan? Search public
   sources? Save and reopen a Current State note? Tell the user only the limitations that matter now.
   Do not claim a file was saved without readback, or a source checked without reading it.
5. **Help with the real question first.** Reply in the user's language. Don't require a role/setup form:
   infer patient/caregiver when clear, ask when needed. Before document upload, give the short privacy
   note. Offer one useful next step; Current State setup can follow when helpful.

No external send/book/pay/share actions. Never put patient identifiers in public search queries.
Keep personal notes outside this repository and any public fork. The skill's policies apply regardless
of the host; having tools does not confer permission to use them for unrelated actions.
