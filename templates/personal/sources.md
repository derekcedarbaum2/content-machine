# Sources — Oracle feed configuration

<!-- Read by /oracle before every scan. The Oracle may ONLY touch what this file lists.
     Filled by /content-setup. -->

## Internal systems (last 7 days)

<!-- List each system the Oracle may scan, with access notes.
     Examples: notes vault paths, Slack workspaces, Gmail, meeting notes,
     task trackers (Todoist/Linear/Jira), calendar. -->
- <system 1 — e.g. "Obsidian vault: ~/vault/Journal/ and ~/vault/Meetings/">
- <system 2 — e.g. "Slack workspace <name>, channels: #wins, #client-calls">
- <system 3>

## Off-limits (hard boundary)

<!-- Systems and content classes the Oracle must never surface spikes from,
     even if credentials are available. Common case: your employer's workspace.
     A useful screening rule: *referencing* an experience is fine; content whose
     origin is an internal document, deck, or meeting record is not. Spell yours out. -->
- <e.g. "Employer Slack workspace <name>: entirely off-limits">
- <e.g. "Client-confidential material: anonymize company + individuals before a spike is listed">

## Internet reader (last 7 days)

<!-- Accounts and sites the Oracle scans for quote-post / reply / response spikes. -->

### X accounts
- <@account>
- <@account>

### LinkedIn accounts
- <name / url>

### Sites & newsletters
- <url>

## Local slop gate (optional)

<!-- If you have a deterministic script that scans a draft for AI tells
     (banned-phrase lists, punctuation-rate checks against your human baseline),
     name it here. The Writers Council's Slop Allergist runs it; a failing exit
     caps the Allergist score at 4. -->
- script: <absolute path, or "none">
- catalog: <path to your personal AI-tells catalog, or "reference/slop-tells.md">
