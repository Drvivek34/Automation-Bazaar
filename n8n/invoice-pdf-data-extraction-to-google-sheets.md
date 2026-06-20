# Invoice/PDF data extraction to Google Sheets

**ID** #005 · **Platform/Category** n8n · **Author** Intuz (templates roundup) · **Rating** ⭐ 4.6/5

🔗 **Source:** [https://www.intuz.com/blog/best-n8n-workflow-templates](https://www.intuz.com/blog/best-n8n-workflow-templates)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
Parses invoice PDFs, extracts line items with an LLM/OCR, and appends structured rows to Google Sheets.

## 🎯 Use when
> When you process many invoices/receipts manually.

## ⚡ Trigger
New file in Drive/email attachment

## 🏁 Steps
1. Detect new PDF
2. OCR / LLM-extract fields
3. Validate totals
4. Append row to Google Sheets

## ⚠️ Note
Add a confidence threshold and route low-confidence docs for review.

## 🏷️ Keywords
ocr, invoices, google sheets, data extraction

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.