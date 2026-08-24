# Schedules & Cron Automations — Automation-Bazaar

6 automations in **Schedules & Cron**. [← Back to master directory](../README.md)

| ID | Title | Author | Rating | Notes / Use Cases |
|---|---|---|---|---|
| #024 | [Daily database backup cron](daily-database-backup-cron.md) | Community | ★★★★★ 4.7 | Scheduled pg_dump/mysqldump with rotation and off-box copy. |
| #025 | [Hourly inbox/RSS poll](hourly-inbox-rss-poll.md) | Community | ★★★★☆ 4.2 | A cron schedule that polls inboxes/feeds to drive downstream automations. |
| #026 | [Weekly dependency update + PR](weekly-dependency-update-pr.md) | Renovate/Dependabot pattern | ★★★★★ 4.6 | Scheduled dependency upgrades that open a PR and run CI before merge. |
| #037 | [Airflow 3 + dbt + Snowflake ELT pipeline](airflow-3-dbt-snowflake-elt-pipeline.md) | Stefen-Taime | ★★★★☆ 4.5 | A production-style multi-stage ELT pipeline using Airflow 3, dbt, Snowflake, GitHub Actions, and observability dashboards, with separate ingestion and transformation DAGs. |
| #042 | [Daily AI news briefing via Tavily/Serper with quota guard](daily-web-briefing-with-quota-guard.md) | @bazaar_ops | ★★★★☆ 4.5 | A cron-driven daily briefing: pulls overnight AI/web-search news through Tavily (or Serper for Google-exact results), dedupes against yesterday's links, and delivers a digest — but only after a quota preflight confirms the provider has free-tier headroom. |
| #043 | [Weekly search-API quota & spend report](weekly-search-quota-usage-report.md) | @bazaar_ops | ★★★★☆ 4.5 | A weekly cron that reads every web-search provider's usage log and posts a quota report: used vs allowance, projected exhaustion date, and which providers to rotate into rotation next week — covering Tavily, Exa, Firecrawl, Brave, and Serper free tiers. |