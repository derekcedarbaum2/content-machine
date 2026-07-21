# Content Machine

A content pipeline you run inside Claude Code. An Oracle mines your week for ideas. An interview panel pulls your actual thinking out of your head. A drafting step is locked to your own words. A writers council gates quality at 9/10. A lessons loop makes the whole thing sharper every time you use it.

Rebuilt from the system Alex Lieberman (Morning Brew co-founder, now Tenex) demoed on [Lenny's "How I AI"](https://www.lennysnewsletter.com/p/how-i-ai-how-the-founder-of-morning) in July 2026. He didn't publish his repo; this is a from-scratch reconstruction of the architecture he described, with the rubrics and gates made explicit. All credit for the design goes to him. Read [STRATEGY.md](STRATEGY.md) for the full thesis and the parts of his system that aren't software.

## Why this doesn't produce slop

The machine never writes for you. It interviews you, then rearranges what you said. The core rule: **the draft may only use words from your interview transcript** (hook and closing excepted). If the output is thin, the input was thin. Alex's framing: slop is an indictment of the interview answers, not the AI.

Three files make it yours: a profile, a voice guide built from studying your ten best posts, and a lessons file that accumulates every correction you make. The machine gets more like you with every piece.

## The pipeline

```
/oracle ──▶ pick a spike ──▶ /interview ──▶ /draft (+ writers council) ──▶ you edit
                                                                              │
                          /repurpose ◀── /lessons (the machine learns) ◀──────┘
```

| Stage | Skill | What it does |
|---|---|---|
| 0 | `/content-setup` | One-time: scaffolds your personal folder, codifies your voice from real posts |
| 1 | `/oracle` | Scans 7 days of your systems + accounts you follow; returns 10–15 scored "content spikes" |
| 2 | `/interview` | Six interviewer personas (Ferriss, Rogan, Barbaro, Walters, Stern, King) extract your take |
| 3 | `/draft` | Writes in your voice from transcript words only; six-persona council gates at ≥ 9.0 |
| 4 | `/lessons` | Diffs your final edit against the draft; approved lessons feed every future piece |
| 5 | `/repurpose` | Cuts the anchor into format-native derivatives (content pyramid) |
| — | `/content-machine` | Orchestrates the full run |

## Install

**As a Claude Code plugin:**

```
/plugin install derekcedarbaum2/content-machine
```

**Or clone and use directly:**

```bash
git clone https://github.com/derekcedarbaum2/content-machine.git
cd content-machine
claude   # skills are picked up from skills/
```

Then run `/content-setup`. It builds your personal folder (default `~/.content-machine/`, relocatable), interviews you for your profile, and studies your top posts to write your voice guide. Nothing personal lives in this repo — the machine is shared, your voice is not.

## What's where

```
skills/          the seven pipeline skills
reference/       the contracts: spike scoring, interviewer personas, council personas,
                 slop tells, content pyramid
templates/       blank personal-folder files /content-setup scaffolds from
example/         the whole system filled in for a fictional founder (Maya Torres) —
                 read this to see what "done" looks like, including a real transcript
                 and a council-scored draft
STRATEGY.md      the full strategy: distribution as moat, the machine, and the
                 human layer (employee advocacy, the Creator Cup)
```

## Connecting your systems

The Oracle reads whatever your Claude Code environment can reach — MCP servers for Slack, Gmail, Notion, Linear, calendars, plus web fetch for the internet reader. You declare what it may scan (and what's off-limits — your employer's Slack, say) in your personal `sources.md`. The Oracle touches nothing outside that file.

## License

MIT. The architecture is Alex Lieberman's, described publicly on the podcast; this implementation and the rubrics are original work.
