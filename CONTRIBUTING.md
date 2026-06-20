# Contributing to Automation-Bazaar

Add an automation via the [submission form](https://github.com/Drvivek34/Automation-Bazaar/issues/new/choose) or a PR.

## Source of truth
All entries live in [`automations_data.json`](automations_data.json). The markdown
(master table + per-category folders + detail pages) is **generated** from it by
`compile_markdown.py` — don't hand-edit the generated `.md` files.

## Add via PR
1. Add an object to the `loops` array in `automations_data.json` with: `title`, `author`,
   `source` (URL), `category` (`{label, slug}`), `description`, `useWhen`, `trigger`,
   `steps[]`, `keywords[]`, optional `implementationNote`.
2. Run `python3 compile_markdown.py`.
3. Commit both the JSON and regenerated markdown; open a PR.

## Rules
- **Attribution mandatory** — every entry keeps its original author + source URL.
- **No copied workflow files / secrets** — link to the source template instead.
- Categories: `n8n`, `make-com`, `zapier`, `scripts`, `schedules-cron`, `other-platforms`.
- Keep ratings honest (editorial until real reviews exist).

Part of the [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/).
