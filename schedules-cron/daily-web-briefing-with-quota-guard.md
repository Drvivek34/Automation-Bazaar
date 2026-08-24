# Daily AI news briefing via Tavily/Serper with quota guard

**ID** #042 · **Platform/Category** Schedules & Cron · **Author** @bazaar_ops · **Rating** ⭐ 4.5/5

🔗 **Source:** [https://github.com/Drvivek34/Automation-Bazaar](https://github.com/Drvivek34/Automation-Bazaar)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
A cron-driven daily briefing: pulls overnight AI/web-search news through Tavily (or Serper for Google-exact results), dedupes against yesterday's links, and delivers a digest — but only after a quota preflight confirms the provider has free-tier headroom.

## 🎯 Use when
> When you want a reliable morning digest that never dies mid-month because the search key ran dry (Tavily 1,000/mo, Serper 2,500 one-time).

## ⚡ Trigger
Daily at 08:00 IST (cron: 30 2 * * * UTC)

## 🏁 Steps
1. Preflight: read provider usage state; abort to backup provider if >80% of monthly free tier is consumed.
2. Query Tavily basic search for configured topics; fall back to Serper.
3. Dedupe result URLs against the rolling 7-day seen-links store.
4. Format digest (title + URL + snippet) and send via Pushover/Discord.
5. Log per-provider call counts; write updated quota state.

## ⚠️ Note
Track only HTTP 200 calls against quota; cache by normalized URL so re-runs are free.

## 🏷️ Keywords
tavily, serper, briefing, cron, quota

## 💬 Reviews
- **@cron_keeper** (★★★★★ 5/5): *Quota check before the digest runs means zero dead mornings.*
- **@serp_watcher** (★★★★☆ 4/5): *Serper credits lasted the whole month with the dedupe rule.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.