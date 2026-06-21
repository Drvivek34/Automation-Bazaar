# Airflow Multi-Stage dbt Pipeline Trigger

**ID** #037 · **Platform/Category** Schedules & Cron · **Author** Data Engineering Patterns · **Rating** ⭐ 4.5/5

🔗 **Source:** [https://github.com/airflow-templates/dbt-pipeline-dag](https://github.com/airflow-templates/dbt-pipeline-dag)  ·  **License:** MIT

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
An Apache Airflow DAG that schedules and orchestrates multi-stage dbt (data build tool) transformations, generating database schemas and verifying testing runs.

## 🎯 Use when
> To orchestrate scheduled data warehouse loads and quality assertions.

## ⚡ Trigger
Cron Schedule (Every weekday at 06:00 AM)

## 🏁 Steps
1. Start Airflow DAG run.
2. Execute dbt source freshness tests.
3. Trigger dbt run command across models.
4. Assert database quality constraints via dbt test.
5. Trigger Slack alert on failure nodes.

## ⚠️ Note
Configure Airflow variables to resolve database passwords securely.

## 🏷️ Keywords
airflow, dbt, dag, data-engineering, cron

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.