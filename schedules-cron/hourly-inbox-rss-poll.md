# Hourly inbox/RSS poll

**ID** #025 · **Platform/Category** Schedules & Cron · **Author** Community · **Rating** ⭐ 4.2/5

🔗 **Source:** [https://crontab.guru/](https://crontab.guru/)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
A cron schedule that polls inboxes/feeds to drive downstream automations.

## 🎯 Use when
> When a workflow needs periodic fetches.

## ⚡ Trigger
Cron (hourly)

## 🏁 Steps
1. Fetch new items
2. Hand off to the workflow
3. Record last-seen cursor
4. Backoff on errors

## ⚠️ Note
Keep a cursor to avoid reprocessing.

## 🏷️ Keywords
cron, polling, rss, schedule

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.