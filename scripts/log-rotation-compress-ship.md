# Log rotation + compress + ship

**ID** #023 · **Platform/Category** Automation Scripts · **Author** Community (logrotate) · **Rating** ⭐ 4.3/5

🔗 **Source:** [https://linux.die.net/man/8/logrotate](https://linux.die.net/man/8/logrotate)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
Rotates and compresses app logs and ships archives to object storage.

## 🎯 Use when
> When app logs grow unbounded.

## ⚡ Trigger
Cron (daily)

## 🏁 Steps
1. Rotate + compress logs
2. Upload archives to storage
3. Apply retention
4. Verify free space

## ⚠️ Note
Coordinate with the app's own log handling to avoid gaps.

## 🏷️ Keywords
logs, logrotate, retention, ops

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.