---
name: oracle
description: Daily idea engine. Scans the last 7 days of your connected systems and your internet-reader sources, scores candidate "content spikes" against the shared rubric, appends everything to your Spike Vault, and returns a ranked list of 10-15. Trigger phrases include "run the oracle", "find content spikes", "/oracle".
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebFetch, WebSearch, ToolSearch]
---

# Oracle — mine the week for content spikes

Read first: `reference/spike-scoring.md` (the scoring contract) and the personal folder's `sources.md` (what you may scan). Personal folder resolution: `~/.content-machine/redirect.md` first line if present, else `~/.content-machine/`.

## Hard rules

1. **Scan only sources listed in `sources.md`.** Systems it marks off-limits are off-limits even if credentials are available. If `sources.md` names a screening rule for a source (e.g., an employer-confidentiality boundary), apply it to every spike from that source before listing it.
2. **Window: last 7 days.** Older material only if `sources.md` says otherwise.
3. **Score every candidate with the rubric. ≥ 6 makes the list; everything scored goes to the Spike Vault** (`spike-vault.md` in the personal folder) with date, score, source, and one-line statement — used or not. Ideas are inventory.
4. **Target 10–15 list entries, roughly half internal / half internet reader.** Fewer is fine; padding with sub-6 spikes is not.
5. **Also surface repurpose candidates:** scan the personal `drafts/` folder for published pieces whose spike is alive again (a debate reignited, a number updated). Mark these `REPURPOSE`.

## Scan procedure

**Internal (per sources.md):** notes/vault folders, meeting notes, journals, email, chat workspaces, task/issue trackers, calendar. You're hunting moments: a story told in a thread, a strong claim made on a call, a number that surprised someone, a customer sentence worth quoting.

**Internet reader (per sources.md):** the listed accounts and sites, last 7 days. You're hunting live debates and posts worth responding to. Every internet spike names its response mode: quote-post, reply, or standalone.

Use whatever connected tools the environment provides (MCP servers, web fetch/search). If a listed source has no available tool, say so in the output — don't silently skip it.

## Output

The ranked list in the exact format from `reference/spike-scoring.md`, internal and internet sections labeled, repurpose candidates at the end. Then one closing line: which spike you'd pick and why — one sentence, no hedging.

❌ **Bad output entry:** "You had some interesting discussions about AI this week that could make good content."
✅ **Good output entry:** `[9] SLACK #client-calls — Banker rebuilt McKinsey's 6-month proposal in one week with Claude Code; consulting is repricing in real time. why it scores: lived story + numbers + live debate.`

## After the run

Confirm the Spike Vault append happened (count entries before/after). The user picks a spike and continues with `/interview`.
