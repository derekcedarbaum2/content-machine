---
name: draft
description: Turn an interview transcript into an anchor piece in the user's codified voice, then gate it through the six-persona Writers Council at a hard 9.0 threshold. Offers multiple hooks and closings. The transcript's words are the only allowed source material. Trigger phrases include "draft it", "write the piece", "/draft".
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion]
---

# Draft — shape the clay, never invent it

Read first, all four: the interview transcript (from `/interview`), and the personal folder's `profile.md`, `voice-guide.md`, `content-lessons.md`. Then `reference/council-personas.md`. Personal folder resolution: `~/.content-machine/redirect.md` first line if present, else `~/.content-machine/`.

## The transcript-words rule (the machine's core gate)

**Every substantive sentence in the draft must be traceable to the interview transcript.** You may reorder, trim, splice, and fix grammar. You may not add claims, examples, framings, or vocabulary the user didn't produce. Exceptions: the hook and the closing line, plus connective tissue (transitions ≤ ~6 words). The writer's job is shaping clay — the user already made the clay.

❌ Violation: transcript says "he rebuilt it in a week"; draft says "he rebuilt it in a week — proof that the era of the mega-consultancy is ending." (second clause invented)
✅ Compliant: transcript says "McKinsey said six months. He did it in a week with Claude Code. Nobody at the bank has looked at consultants the same way since." → draft uses exactly these sentences, tightened.

## Steps

### 1. Confirm format
Ask which anchor format (from `profile.md`'s anchor list): long LinkedIn, newsletter section, essay, thread script. One format per run.

### 2. Draft
- Structure and rhythm come from `voice-guide.md` (their hook formulas, their structures, their #1 rule).
- Check every item in `content-lessons.md` — these are past mistakes; repeating a logged lesson is the one unforgivable error.
- Body: transcript words only, per the rule above.

### 3. Hooks and closings
Offer **3 hook options and 2 closing options** (the one place invention is allowed), each in a distinct register from the voice guide's hook formulas. Label which formula each uses.

### 4. Self-check the transcript-words rule
Before the council: list any sentence not traceable to the transcript (excluding hook/closing/transitions). If any exist, rewrite or delete them. State "transcript check: clean" or the violations found.

### 5. Writers Council
Run per `reference/council-personas.md`: six independent scores 1–10 with one-line justifications and one fix each. **Aggregate mean ≥ 9.0 to pass.** On failure: fix only the two lowest dimensions, re-run all six. Max 3 loops, then present best-with-scores. If the personal `sources.md` names a local slop-gate script, run it during the Allergist's turn; a failing exit caps the Allergist at 4.

### 6. Present
Show: final draft, the hook/closing options, the council scorecard, and the loop count. Save to `drafts/YYYY-MM-DD-<spike-slug>.md` in the personal folder with the transcript path in frontmatter.

## What happens next

User edits/approves → `/lessons` captures what the machine got wrong → `/repurpose` fans out derivatives.
