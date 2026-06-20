# Daily database backup cron

**ID** #024 · **Platform/Category** Schedules & Cron · **Author** Community · **Rating** ⭐ 4.7/5

🔗 **Source:** [https://www.postgresql.org/docs/current/backup-dump.html](https://www.postgresql.org/docs/current/backup-dump.html)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
Scheduled pg_dump/mysqldump with rotation and off-box copy.

## 🎯 Use when
> Essential alongside any data-changing workflow.

## ⚡ Trigger
Cron (daily, off-peak)

## 🏁 Steps
1. Dump database
2. Compress + timestamp
3. Copy off-box
4. Rotate old dumps

## ⚠️ Note
Store at least one copy off the host.

## 🏷️ Keywords
cron, backup, postgres, mysql

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.