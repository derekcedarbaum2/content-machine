---
name: repurpose
description: Fan an approved anchor piece out into derivative content (short tweets, threads, long LinkedIn, quote-posts) per the content-pyramid map, matching the user's historical style in each target format. Every derivative passes the Writers Council. Trigger phrases include "repurpose this", "make derivatives", "cut this into posts", "/repurpose".
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion]
---

# Repurpose — one anchor, many shards

Read first: `reference/content-pyramid.md`, the anchor piece, its interview transcript, and the personal `voice-guide.md` + `content-lessons.md`. Personal folder resolution: `~/.content-machine/redirect.md` first line if present, else `~/.content-machine/`.

## Steps

### 1. Ask what to produce
Never generate the full pyramid unprompted. Ask which derivatives and how many ("three short tweets and one long LinkedIn?"). Default suggestion: 2 short tweets + 1 long LinkedIn per anchor.

### 2. Study the format
For each target format, check the voice guide's format-specific sections (and, if thin, ask for 3–5 examples of the user's past posts in that format). A tweet is not a shrunk LinkedIn post; match how *they* write tweets.

### 3. Cut shards
Apply the pyramid rules: **one shard per derivative** — a single claim, story beat, or number from the anchor. Words still come from the anchor/transcript corpus; rearrange, don't invent (hook-level rephrasing allowed, same as `/draft`).

❌ One derivative summarizing the whole anchor ("5 takeaways from...")
✅ One derivative carrying the anchor's best number, another carrying its sharpest claim

### 4. Council every derivative
Each derivative passes the Writers Council (`reference/council-personas.md`) at the same **≥ 9.0** gate. Short formats concentrate slop tells — expect the Allergist to bite harder here, not softer.

### 5. Present and file
Show derivatives grouped by format with council scores. Append them to the anchor's file in `drafts/` under a `## Derivatives` section, dated.

## Scheduling note

Repurposing is also an Oracle feed: `/oracle` flags published anchors whose topic reignited as `REPURPOSE` candidates. An anchor from a month ago plus a fresh news hook is often the cheapest high-scoring spike available.
