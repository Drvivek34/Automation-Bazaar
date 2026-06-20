# Docker prune + unhealthy-container restart

**ID** #022 · **Platform/Category** Automation Scripts · **Author** Community · **Rating** ⭐ 4.4/5

🔗 **Source:** [https://docs.docker.com/](https://docs.docker.com/)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
Frees disk by pruning dangling images/volumes and restarts containers failing healthchecks.

## 🎯 Use when
> When long-running Docker hosts drift or bloat.

## ⚡ Trigger
Cron (hourly/daily)

## 🏁 Steps
1. Prune dangling images/volumes
2. List unhealthy containers
3. Restart them
4. Report reclaimed space

## ⚠️ Note
Exclude volumes you must keep from pruning.

## 🏷️ Keywords
docker, prune, healthcheck, ops

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.