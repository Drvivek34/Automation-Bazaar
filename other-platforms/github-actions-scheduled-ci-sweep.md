# GitHub Actions scheduled CI sweep

**ID** #027 · **Platform/Category** Other Platforms · **Author** GitHub Docs · **Rating** ⭐ 4.6/5

🔗 **Source:** [https://docs.github.com/actions](https://docs.github.com/actions)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
A scheduled workflow that runs tests/lint/security sweeps and reports results.

## 🎯 Use when
> When you want recurring checks beyond push events.

## ⚡ Trigger
schedule: cron in workflow

## 🏁 Steps
1. Define on.schedule cron
2. Run test/lint/security jobs
3. Upload artifacts
4. Notify on failure

## ⚠️ Note
Scheduled runs use the default branch's workflow file.

## 🏷️ Keywords
github actions, ci, schedule, cron

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.