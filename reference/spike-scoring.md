# Spike Scoring — the Oracle's rubric

A **content spike** is a moment from your week that can carry a piece of content: a story, a strong opinion, a surprising number, a public disagreement worth weighing in on. The Oracle scans your sources, finds candidate spikes, scores them, and returns a ranked list. This file is the scoring contract.

## Scoring dimensions

Score each candidate on five dimensions, 0–2 each. **Max 10.**

| Dimension | 0 | 1 | 2 |
|---|---|---|---|
| **Story/anecdote** | No narrative — an abstract observation | A situation is referenced but not lived ("clients often struggle with X") | A specific lived moment with people and stakes ("on Tuesday's call, the CFO said...") |
| **Strong POV** | Neutral summary, no position | A lean, hedged ("I tend to think...") | A falsifiable claim someone could disagree with |
| **Specific examples** | None | One vague example | Named tools, numbers, dates, quotes |
| **Novelty** | Restates common wisdom | Familiar take, fresh angle | A take you haven't seen said, or a contrarian read of a live debate |
| **Timeliness** | Evergreen only | Loosely connected to something current | Rides a conversation happening this week |

## Hard gates

- **Score ≥ 6 to make the daily list.** Below 6 goes to the Spike Vault only.
- **Return 10–15 spikes per run.** If fewer than 10 clear the gate, return what cleared — never pad with sub-6 spikes.
- **Balance sources:** target roughly half internal (your systems), half internet reader (accounts and sites you follow). If one side is dry, say so instead of forcing balance.
- **Internet-reader spikes must name the response mode:** quote-post, reply, or standalone take referencing the source.
- **Every spike — used or not — is appended to the Spike Vault.** Ideas are inventory.

## Scored examples

❌ **Score 2 — rejected:**
> "AI is changing how companies think about content marketing."

No story (0), no POV (0), no examples (0), zero novelty (0), vaguely timely (2... generously 1). This is the statistical mean of the internet. The Vault doesn't even want it.

❌ **Score 5 — vault only:**
> "A client mentioned their McKinsey engagement was slow. Could write about consultants vs. AI speed."

Situation referenced but not lived (1), implied POV not stated (1), one vague example (1), familiar take (1), loosely current (1). Close, but it needs the actual moment.

✅ **Score 9 — top of list:**
> "A banker told me McKinsey quoted 6 months for an internal tool. He rebuilt it himself in a week with Claude Code. Spike: the consulting pyramid is repricing in real time — and most consultancies are pretending it isn't."

Lived moment with a named actor (2), falsifiable claim (2), concrete numbers (2), fresh angle on a live debate (2), rides this week's conversation (1).

✅ **Score 8 — internet reader:**
> "Aaron Levie says forward-deployed engineers are the key to enterprise AI. Ethan Mollick says they'll disappoint because the bottleneck is org structure, not code. Response mode: standalone take. Spike: they're both right, and that's the problem — here's what both miss from the deployment trenches."

Live public disagreement (2 novelty, 2 timeliness), position staked (2), named principals (2), no personal story yet (0) — the interview step supplies it.

## Output format per spike

```
[score] SOURCE — one-line spike statement
        why it scores: <one line>
        (internet spikes only) response mode: quote-post | reply | standalone
```

Rank descending. No prose between entries.
