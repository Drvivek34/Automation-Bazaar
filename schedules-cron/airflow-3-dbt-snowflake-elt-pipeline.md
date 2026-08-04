# Airflow 3 + dbt + Snowflake ELT pipeline

**ID** #037 · **Platform/Category** Schedules & Cron · **Author** Stefen-Taime · **Rating** ⭐ 4.5/5

🔗 **Source:** [https://github.com/Stefen-Taime/snow-airflow-dbt](https://github.com/Stefen-Taime/snow-airflow-dbt)  ·  **License:** See source repository

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
A production-style multi-stage ELT pipeline using Airflow 3, dbt, Snowflake, GitHub Actions, and observability dashboards, with separate ingestion and transformation DAGs.

## 🎯 Use when
> To study or adapt a current Airflow + dbt orchestration pattern with freshness checks, transformations, tests, and operational visibility.

## ⚡ Trigger
Scheduled Airflow DAGs

## 🏁 Steps
1. Ingest the source data into the raw Snowflake layer.
2. Trigger the dbt transformation DAG from the orchestration layer.
3. Build staging, intermediate, core, and mart models with dbt.
4. Run freshness and data-quality checks, then publish dashboards and alerts.

## ⚠️ Note
Configure Airflow variables to resolve database passwords securely.

## 🏷️ Keywords
airflow 3, dbt, snowflake, elt, data quality, github actions

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.