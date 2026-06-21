# PostgreSQL Backup to AWS S3

**ID** #036 · **Platform/Category** Scripts · **Author** DevOps Cron Scripts · **Rating** ⭐ 4.5/5

🔗 **Source:** [https://github.com/awesome-scripts/postgres-s3-backup](https://github.com/awesome-scripts/postgres-s3-backup)  ·  **License:** MIT

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
A robust shell script designed to be scheduled via cron that performs a pg_dump, compresses the database archive, and uploads it safely to an AWS S3 bucket.

## 🎯 Use when
> To secure off-site backups of production PostgreSQL databases automatically.

## ⚡ Trigger
Scheduled System Cron (Daily at 02:00 AM)

## 🏁 Steps
1. Dump PostgreSQL database schemas and records.
2. Compress dump file using gzip format.
3. Upload file to target AWS S3 bucket via AWS CLI.
4. Clean up local file archives to prevent disk filling.

## ⚠️ Note
Requires aws-cli config credentials and pg_dump tools installed locally.

## 🏷️ Keywords
postgres, backup, s3, aws, cron, bash

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.