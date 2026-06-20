# Nightly restic/rsync backup

**ID** #020 · **Platform/Category** Automation Scripts · **Author** Community (restic docs) · **Rating** ⭐ 4.7/5

🔗 **Source:** [https://restic.readthedocs.io/](https://restic.readthedocs.io/)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
Encrypted incremental backups of key paths to local + remote, with pruning and a status notification.

## 🎯 Use when
> When you need reliable, versioned backups.

## ⚡ Trigger
Cron (nightly)

## 🏁 Steps
1. Snapshot configured paths
2. Push to repo (local + S3/B2)
3. Prune by retention policy
4. Notify on success/failure

## ⚠️ Note
Test restores regularly — an untested backup is a hope, not a backup.

## 🏷️ Keywords
backup, restic, rsync, cron

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.