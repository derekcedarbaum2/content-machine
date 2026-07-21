---
name: content-setup
description: One-time setup for the content machine. Scaffolds your personal folder (profile, voice guide, content lessons, sources config), studies your top-performing posts to codify your voice, and wires your Oracle feeds. Run this before any other content-machine skill. Trigger phrases include "set up the content machine", "/content-setup".
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash, WebFetch, AskUserQuestion]
---

# Content Setup — scaffold the personal layer

The machine is shared; your voice is not. This skill builds the personal folder every other skill reads from. Nothing in it goes back to the shared repo.

## Personal folder resolution (convention used by every skill)

1. If `~/.content-machine/redirect.md` exists, its first line is the absolute path to the personal folder.
2. Otherwise the personal folder is `~/.content-machine/`.

## Steps

### 1. Choose the location
Ask where the personal folder should live (default `~/.content-machine/`; people with a notes vault often want it inside the vault). If non-default, create the folder there and write `~/.content-machine/redirect.md` containing the path.

### 2. Scaffold from templates
Copy every file in `templates/personal/` into the personal folder, plus create empty `transcripts/`, `drafts/`, and `spike-vault.md`.

### 3. Build `profile.md` (interview, don't guess)
Use AskUserQuestion / conversation to fill: who you are, role, company, what you're promoting (owned assets), anchor content formats, platforms, and the accounts/sites for the internet reader. Write answers into the template's sections.

### 4. Generate `voice-guide.md` (study, don't invent)
Ask for the user's top-performing posts — pasted text, exported files, or profile URLs to fetch. **Minimum 10 posts; refuse to generate a voice guide from fewer** — a voice guide built on 3 posts is fan fiction. From the corpus, extract:
- Executive summary of voice and tone
- Top 10 posts, quoted, each with one line on *why* it worked
- Hook formulas actually used (not generic hook advice)
- Content structures (how their pieces move)
- Language patterns: recurring phrases, profanity policy, emoji policy, sentence-length habits
- Core DNA and a #1 rule (Alex's: "write like you're texting a friend" — find *theirs*, don't copy his)

❌ "Your voice is authentic, direct, and engaging" — describes nobody.
✅ "You open 7 of your top 10 posts with a number. You never use exclamation points. Your average sentence is 11 words but you drop a 3-word fragment roughly every paragraph."

### 5. Wire `sources.md`
Fill the Oracle feed config: which internal systems the machine may scan (and which are off-limits — e.g., employer workspaces), the internet-reader account list from step 3, and an optional local slop-gate script path for the Allergist.

### 6. Verify
- All personal files exist and contain no unfilled `<placeholders>`.
- `voice-guide.md` quotes ≥ 10 real posts.
- `sources.md` names at least one internal source and one internet-reader source, and states any off-limits systems explicitly.

Setup is done when the verify checklist passes — then point the user at `/oracle` for their first run.
