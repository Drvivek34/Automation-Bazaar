# ⚙️ Automation-Bazaar: The Curated Automation Workflows Directory

Welcome to **Automation-Bazaar** — a categorized, community-rated directory of **33** ready-to-use automations across **n8n, Make.com, Zapier, scripts, cron/schedules, and more**. Every entry links to its original source and keeps its author — no workflow files are copied here.

*Last updated: 2026-06-20 · Goal: 5,000+ high-quality automations · Part of the [Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)*

## 🤝 How to Add a New Automation (GitHub-first)
We welcome additions — **always credit the original author/source**.

### Option A — Submit an issue (no coding)
1. Open a [new submission](https://github.com/Drvivek34/Automation-Bazaar/issues/new/choose) and pick **Submit an Automation**.
2. Fill in title, platform/category, source URL, author, trigger, steps, and a note.
3. A maintainer or the daily automation adds it and recompiles this directory.

### Option B — Pull request
1. Fork, then add your entry object to [`automations_data.json`](automations_data.json).
2. Run `python3 compile_markdown.py` to regenerate the tables.
3. Open a PR. Keep the entry attributed and self-contained.

## 🔌 Platforms Covered
- 🟧 **n8n** — open-source workflow automation
- 🟪 **Make.com** — visual scenario automation
- 🟠 **Zapier** — app-to-app zaps
- 📜 **Automation Scripts** — backups, certs, ops glue
- ⏰ **Schedules & Cron** — the timers that drive workflows
- 🧩 **Other Platforms** — GitHub Actions, Airflow, and more

## 📚 Master Directory (all automations)
Sorted by rating. Click a title for full setup details.

| ID | Category | Title | Author | Rating | Notes / Use Cases |
|---|---|---|---|---|---|
| #002 | n8n | [RAG chatbot over a company knowledge base](n8n/rag-chatbot-over-a-company-knowledge-base.md) | n8n Team (templates) | ★★★★★ 4.9 | Retrieval-augmented chatbot that embeds your docs into a vector store (Pinecone/Qdrant/Supabase) and answers from them. |
| #001 | n8n | [AI email auto-responder (Gmail + GPT-4/Claude)](n8n/ai-email-auto-responder-gmail-gpt-4-claude.md) | enescingoz (awesome-n8n-templates) | ★★★★★ 4.8 | Reads incoming Gmail, classifies by topic/urgency with an LLM, and drafts a context-aware reply for review. |
| #003 | n8n | [Blog post → LinkedIn/X/newsletter repurposer](n8n/blog-post-linkedin-x-newsletter-repurposer.md) | enescingoz (awesome-n8n-templates) | ★★★★★ 4.7 | Turns one blog post into platform-tailored LinkedIn posts, tweets, and an email newsletter draft. |
| #015 | Zapier | [New lead → HubSpot + Slack notify](zapier/new-lead-hubspot-slack-notify.md) | Databox (21 zaps) | ★★★★★ 4.7 | Adds new leads to HubSpot and pings sales in Slack. |
| #020 | Automation Scripts | [Nightly restic/rsync backup](scripts/nightly-restic-rsync-backup.md) | Community (restic docs) | ★★★★★ 4.7 | Encrypted incremental backups of key paths to local + remote, with pruning and a status notification. |
| #024 | Schedules & Cron | [Daily database backup cron](schedules-cron/daily-database-backup-cron.md) | Community | ★★★★★ 4.7 | Scheduled pg_dump/mysqldump with rotation and off-box copy. |
| #004 | n8n | [Telegram AI assistant bot](n8n/telegram-ai-assistant-bot.md) | n8n community | ★★★★★ 4.6 | A Telegram bot backed by an LLM with memory, for Q&A and task commands. |
| #005 | n8n | [Invoice/PDF data extraction to Google Sheets](n8n/invoice-pdf-data-extraction-to-google-sheets.md) | Intuz (templates roundup) | ★★★★★ 4.6 | Parses invoice PDFs, extracts line items with an LLM/OCR, and appends structured rows to Google Sheets. |
| #007 | n8n | [Lead enrichment + CRM sync](n8n/lead-enrichment-crm-sync.md) | Goodspeed Studio (agency templates) | ★★★★★ 4.6 | Enriches new leads (company, role, socials) and upserts them into the CRM with a Slack alert. |
| #009 | Make.com | [Form submission → CRM contact → Slack notify](make-com/form-submission-crm-contact-slack-notify.md) | Make Templates | ★★★★★ 4.6 | Watches a form, creates/updates a CRM contact, and posts a notification to Slack. |
| #014 | Zapier | [Brand mention on X → Slack alert](zapier/brand-mention-on-x-slack-alert.md) | Databox (21 zaps) | ★★★★★ 4.6 | Notifies a Slack channel whenever your brand is mentioned on X/Twitter. |
| #021 | Automation Scripts | [Let's Encrypt cert auto-renew + reload](scripts/let-s-encrypt-cert-auto-renew-reload.md) | Community (certbot) | ★★★★★ 4.6 | Renews TLS certificates and reloads the web server only when a cert actually changes. |
| #026 | Schedules & Cron | [Weekly dependency update + PR](schedules-cron/weekly-dependency-update-pr.md) | Renovate/Dependabot pattern | ★★★★★ 4.6 | Scheduled dependency upgrades that open a PR and run CI before merge. |
| #027 | Other Platforms | [GitHub Actions scheduled CI sweep](other-platforms/github-actions-scheduled-ci-sweep.md) | GitHub Docs | ★★★★★ 4.6 | A scheduled workflow that runs tests/lint/security sweeps and reports results. |
| #006 | n8n | [Daily AI news digest to email/Slack](n8n/daily-ai-news-digest-to-email-slack.md) | ai-rockstars (templates roundup) | ★★★★☆ 4.5 | Aggregates RSS/news sources, summarizes with an LLM, and sends a daily digest. |
| #010 | Make.com | [RSS → AI summary → Notion](make-com/rss-ai-summary-notion.md) | Make Templates | ★★★★☆ 4.5 | Pulls new RSS items, summarizes with an AI module, and stores them in a Notion database. |
| #012 | Make.com | [Webhook payment → tag CRM contact](make-com/webhook-payment-tag-crm-contact.md) | Make Templates | ★★★★☆ 4.5 | Receives a payment webhook, finds the customer, and tags/segments them in the CRM. |
| #016 | Zapier | [Incoming email → task/to-do](zapier/incoming-email-task-to-do.md) | Zapier (examples) | ★★★★☆ 4.5 | Turns starred/labeled emails into tasks in your project tool. |
| #018 | Zapier | [Calendly booking → CRM + reminder](zapier/calendly-booking-crm-reminder.md) | Ringover (zap examples) | ★★★★☆ 4.5 | On a new Calendly booking, creates/updates a CRM record and schedules reminders. |
| #028 | Other Platforms | [Airflow daily ETL DAG](other-platforms/airflow-daily-etl-dag.md) | Apache Airflow Docs | ★★★★☆ 4.5 | An orchestrated daily extract-transform-load pipeline with retries and alerting. |
| #029 | n8n | [Telegram AI Bot with NeurochainAI](n8n/telegram-ai-bot-with-neurochainai.md) | enescingoz (awesome-n8n-templates) | ★★★★☆ 4.5 | Integrates the NeurochainAI API inside Telegram to offer text and image generation directly in your chat threads. |
| #030 | n8n | [Detect toxic language in Telegram messages](n8n/detect-toxic-language-in-telegram-messages.md) | enescingoz (awesome-n8n-templates) | ★★★★☆ 4.5 | Monitors active Telegram chats, analyzes message text for toxicity using moderation AI, and flags/reports violations. |
| #031 | n8n | [Translate Telegram audio messages with AI (55 languages)](n8n/translate-telegram-audio-messages-with-ai-55-languages.md) | enescingoz (awesome-n8n-templates) | ★★★★☆ 4.5 | Receives audio/voice messages in Telegram, transcribes them using speech-to-text (Whisper), translates them into 55 support languages, and replies back. |
| #032 | n8n | [Hacker News Throwback Machine](n8n/hacker-news-throwback-machine.md) | enescingoz (awesome-n8n-templates) | ★★★★☆ 4.5 | Cuts through the noise to fetch the top-voted Hacker News posts from exactly 1, 2, 5, or 10 years ago today. |
| #033 | n8n | [Siri AI Agent with Apple Shortcuts](n8n/siri-ai-agent-with-apple-shortcuts.md) | enescingoz (awesome-n8n-templates) | ★★★★☆ 4.5 | Bridges iOS Siri voice shortcuts to a powerful agentic backend in n8n, enabling deep custom commands via voice. |
| #008 | n8n | [WhatsApp inbound automation](n8n/whatsapp-inbound-automation.md) | n8n community | ★★★★☆ 4.4 | Handles inbound WhatsApp messages, routes by intent, and replies or creates a ticket. |
| #011 | Make.com | [Email parser → Airtable](make-com/email-parser-airtable.md) | Make Templates | ★★★★☆ 4.4 | Parses structured emails (orders, alerts) and writes records into Airtable. |
| #013 | Make.com | [Multi-channel social scheduler](make-com/multi-channel-social-scheduler.md) | Make Templates | ★★★★☆ 4.4 | Takes a content row and publishes/schedules it across several social platforms. |
| #017 | Zapier | [Form submission → Google Sheets row](zapier/form-submission-google-sheets-row.md) | Zapier (examples) | ★★★★☆ 4.4 | Appends every new form response as a row in Google Sheets. |
| #022 | Automation Scripts | [Docker prune + unhealthy-container restart](scripts/docker-prune-unhealthy-container-restart.md) | Community | ★★★★☆ 4.4 | Frees disk by pruning dangling images/volumes and restarts containers failing healthchecks. |
| #019 | Zapier | [Sync unsubscribes across email systems](zapier/sync-unsubscribes-across-email-systems.md) | Getmagical (best zaps) | ★★★★☆ 4.3 | Propagates an unsubscribe in one tool to all other email systems for compliance. |
| #023 | Automation Scripts | [Log rotation + compress + ship](scripts/log-rotation-compress-ship.md) | Community (logrotate) | ★★★★☆ 4.3 | Rotates and compresses app logs and ships archives to object storage. |
| #025 | Schedules & Cron | [Hourly inbox/RSS poll](schedules-cron/hourly-inbox-rss-poll.md) | Community | ★★★★☆ 4.2 | A cron schedule that polls inboxes/feeds to drive downstream automations. |

## 🗂️ Categories
- [n8n](n8n/README.md) (13)
- [Make.com](make-com/README.md) (5)
- [Zapier](zapier/README.md) (6)
- [Automation Scripts](scripts/README.md) (4)
- [Schedules & Cron](schedules-cron/README.md) (3)
- [Other Platforms](other-platforms/README.md) (2)

---
Part of the **[Mega AI Bazaar](https://drvivek34.github.io/Mega-AI-Bazaar/)**. Licensed MIT for structure/text; each automation keeps its original author's license.