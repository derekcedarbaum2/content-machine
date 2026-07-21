---
name: lessons
description: The reinforcement loop. After the user finalizes a piece, diff the machine's draft against the published version, abstract generalizable lessons from what the user changed, get explicit approval, and append to content-lessons.md so the machine never repeats the mistake. Trigger phrases include "run the lessons loop", "log lessons", "/lessons".
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, AskUserQuestion]
---

# Lessons — the loop that makes the machine yours

This is why the machine improves with use where generic AI writing doesn't: every edit the user makes is a training signal, captured as prose rules the drafting step must obey forever after. Personal folder resolution: `~/.content-machine/redirect.md` first line if present, else `~/.content-machine/`.

## Inputs

- The machine's draft (from `drafts/`)
- The final version the user actually published or approved (pasted, or edited in place)
- Any verbal feedback the user gave along the way ("this line is AI-cringey")

## Steps

### 1. Diff
Compare draft vs. final, sentence by sentence. Collect: deletions, rewrites, reorderings, additions.

### 2. Abstract
Turn each meaningful change into a **generalizable rule**, categorized:
- **Tone** — register errors ("too breathless", "false modesty")
- **Structure & flow** — ordering, pacing, where the piece sagged
- **Language** — specific words/constructions the user removes on sight
- **Format** — platform-specific habits (fold behavior, line breaks, emoji)

The abstraction test: would this rule have prevented the edit AND apply to future pieces? One-off factual fixes are not lessons.

❌ Not a lesson: "Changed 'six months' to '6 months'." (one-off)
❌ Too vague: "Make it sound more natural." (unenforceable)
✅ A lesson: "TONE — Never use the setup-punchline construction 'They're both right — and that's exactly the problem.' User flags this cadence as AI-cringe. State the tension directly instead."

### 3. Approve — never auto-append
Present the proposed lessons as a numbered list. The user approves, rejects, or edits each. **Only approved lessons are written.** A lessons file polluted with wrong rules degrades every future draft.

### 4. Append
Add approved lessons to `content-lessons.md` under their category, dated. Check for contradictions with existing lessons — if a new lesson contradicts an old one, surface the conflict and ask which wins; never hold both.

### 5. Confirm
Report what was appended and the new lesson count per category.

## Gate

The loop is complete only when: diff performed, lessons proposed with categories, user explicitly approved, file appended, contradictions resolved. If the user gave feedback mid-draft ("that hook is cheesy") that didn't make it into a lesson, ask about it here — spoken feedback that evaporates is the loop's failure mode.
