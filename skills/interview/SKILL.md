---
name: interview
description: Extract your actual thinking on a chosen content spike. Optionally runs a research brief first, then a panel of six interviewer personas questions you one at a time until there's enough specific material to draft from. Produces the interview transcript that becomes the ONLY source corpus for drafting. Trigger phrases include "interview me", "run the panel", "/interview".
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, WebFetch, WebSearch, AskUserQuestion]
---

# Interview — the panel extracts, the transcript becomes law

Read first: `reference/interviewer-personas.md`. Personal folder resolution: `~/.content-machine/redirect.md` first line if present, else `~/.content-machine/`.

Why this step exists: the machine's anti-slop guarantee is that **drafts may only use words you said here** (hook and closing excepted). Thin interview → thin piece. As Alex Lieberman put it: when the machine produces slop, that's an indictment of the interview answers, not the AI.

## Step 1 — Confirm the spike

Take the spike the user picked (from `/oracle` or stated directly). Restate it in one line.

## Step 2 — Research brief (optional, offer it)

If the spike involves external claims or a public debate the user hasn't fully tracked, offer a research brief before questioning:
- What the principals actually said (quotes, links)
- The strongest version of each side
- Potential contrarian or novel angles nobody has taken
- Open questions the user could be the one to answer

Skip for pure lived-experience spikes — the user already has the material.

## Step 3 — The panel

Run per the shared rules in `reference/interviewer-personas.md`. Ask one question at a time. Rotate personas, and label each question with its persona. Ask ~5 questions total. Build every follow-up on the previous answer. Always chase specificity. Encourage voice-to-text answers — speed produces unguarded phrasing, and unguarded phrasing is voice.

**Stop condition:** you have (a) at least one lived story with specifics, (b) a falsifiable position, (c) at least two concrete details (names/numbers/quotes). If 5 questions haven't produced these, say which is missing and ask up to 3 more — don't draft from a corpus that fails this bar.

❌ Panel malpractice: "It sounds like you're saying deployment expertise matters more than model quality — is that right?" (feeds the subject its own phrasing; contaminates the corpus)
✅ "Larry King: In one or two sentences — what are Levie and Mollick both missing?"

## Step 4 — Write the transcript

Save verbatim Q&A to `transcripts/YYYY-MM-DD-<spike-slug>.md` in the personal folder, with the spike statement and research-brief pointer at top. Do not clean up the user's phrasing — the "mess" is the voice.

## Gate before handing to /draft

- Transcript file exists and contains the user's words verbatim.
- Stop-condition checklist (story / position / 2+ specifics) passes — state the three items explicitly.
