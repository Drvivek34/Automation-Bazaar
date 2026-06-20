# RAG chatbot over a company knowledge base

**ID** #002 · **Platform/Category** n8n · **Author** n8n Team (templates) · **Rating** ⭐ 4.9/5

🔗 **Source:** [https://n8n.io/workflows/](https://n8n.io/workflows/)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
Retrieval-augmented chatbot that embeds your docs into a vector store (Pinecone/Qdrant/Supabase) and answers from them.

## 🎯 Use when
> When you need a grounded assistant that answers from your own content.

## ⚡ Trigger
Chat message / webhook

## 🏁 Steps
1. Ingest + chunk documents
2. Embed and upsert to a vector DB
3. On query, retrieve top-k context
4. Answer with the LLM citing sources

## ⚠️ Note
Re-index on document changes to avoid stale answers.

## 🏷️ Keywords
rag, vector store, chatbot, pinecone, qdrant

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.