# Telegram calendar AI agent with RAG

**ID** #041 · **Platform/Category** n8n · **Author** Fanny-n8n-templates contributors · **Rating** ⭐ 4.5/5

🔗 **Source:** [https://github.com/Fgrodriguezs/Fanny-n8n-templates](https://github.com/Fgrodriguezs/Fanny-n8n-templates)  ·  **License:** See source repository

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
A current n8n automation pattern for conversational scheduling through Telegram with retrieval-augmented context and calendar actions.

## 🎯 Use when
> To prototype appointment scheduling that needs a chat interface, calendar availability, and contextual retrieval.

## ⚡ Trigger
Telegram message

## 🏁 Steps
1. Receive and normalize the Telegram request.
2. Retrieve approved context and available calendar slots.
3. Ask the agent to propose or confirm a time without guessing availability.
4. Create or update the calendar event only after explicit confirmation and log the result.

## ⚠️ Note
Use scoped credentials and confirmation gates for calendar writes; adapt the workflow to the source repository current JSON files.

## 🏷️ Keywords
n8n, Telegram, calendar, RAG, AI agent, scheduling

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.