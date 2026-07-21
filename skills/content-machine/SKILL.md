---
name: content-machine
description: Orchestrator for the full content pipeline - Oracle scan, spike selection, optional research, interview panel, voice-locked drafting with Writers Council gate, lessons loop, and repurposing. Run this for an end-to-end session, or invoke the stage skills individually. Trigger phrases include "run the content machine", "content machine", "/content-machine".
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebFetch, WebSearch, ToolSearch, AskUserQuestion]
---

# Content Machine — the full run

Chains the stage skills in order. Each stage's own SKILL.md is the authority for that stage; this file only sequences and hands off.

```
/oracle ──▶ pick spike ──▶ /interview (± research brief) ──▶ /draft (+ council)
                                                                  │
              /repurpose ◀── user approves/edits final ◀──────────┘
                                        │
                                    /lessons
```

## Preconditions

The personal folder must exist (run `/content-setup` first if not — check `~/.content-machine/` or its redirect). If `voice-guide.md` or `sources.md` is missing or still contains template placeholders, stop and route to setup. Drafting without a codified voice is how slop happens.

## Sequence

1. **Oracle** — run `skills/oracle`. Present the ranked list.
2. **Selection** — user picks a spike (or says "you pick": choose the highest-scoring spike with a lived story and say why in one line).
3. **Interview** — run `skills/interview`, offering the research brief when the spike involves external claims.
4. **Draft + Council** — run `skills/draft`. Do not show the user any draft that hasn't been through the council.
5. **Finalize** — user edits/approves. Capture all verbal feedback for the next stage.
6. **Lessons** — run `skills/lessons`. Never skip this; the loop is the machine's compounding asset.
7. **Repurpose** — offer `skills/repurpose`. Optional per session.

## Session rules

- **One spike per run.** Parallel pieces in one session blur transcripts and voices.
- **Stages are resumable.** If the user leaves mid-pipeline, the artifacts (spike list, transcript, draft) are all files in the personal folder — a later session picks up from the last file.
- **Never reorder the gate stages.** Interview before draft, council before human, lessons before done. The order is the anti-slop mechanism; shortcuts reintroduce the failure mode this machine was built to kill.

## Cadence

Designed as a daily driver: `/oracle` every morning (2 minutes to read the list), full pipeline 2–3× a week, `/repurpose` on the days between. The Spike Vault means no run is wasted — unused ideas are inventory for dry weeks.
