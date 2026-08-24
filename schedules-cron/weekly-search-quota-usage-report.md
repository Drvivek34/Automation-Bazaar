# Weekly search-API quota & spend report

**ID** #043 · **Platform/Category** Schedules & Cron · **Author** @bazaar_ops · **Rating** ⭐ 4.5/5

🔗 **Source:** [https://github.com/Drvivek34/Automation-Bazaar](https://github.com/Drvivek34/Automation-Bazaar)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
A weekly cron that reads every web-search provider's usage log and posts a quota report: used vs allowance, projected exhaustion date, and which providers to rotate into rotation next week — covering Tavily, Exa, Firecrawl, Brave, and Serper free tiers.

## 🎯 Use when
> When multiple search keys are in rotation and silent exhaustion keeps surprising you.

## ⚡ Trigger
Mondays at 09:00 IST (cron: 30 3 * * 1 UTC)

## 🏁 Steps
1. Read per-provider monthly logs and current usage counters.
2. Compare against verified allowances (Tavily 1,000cr; Exa $10; Firecrawl 1,000cr; Brave $5; Serper 2,500 one-time).
3. Project exhaustion dates from 7-day burn rates.
4. Compose markdown report; alert on any provider above 80%.
5. Deliver via webhook/Pushover and archive the report.

## ⚠️ Note
Remember Brave requires a card since Aug 2025 — include its metered spend, not just credits.

## 🏷️ Keywords
quota, report, exa, firecrawl, brave

## 💬 Reviews
- **@cron_keeper** (★★★★★ 5/5): *Quota check before the digest runs means zero dead mornings.*
- **@serp_watcher** (★★★★☆ 4/5): *Serper credits lasted the whole month with the dedupe rule.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.