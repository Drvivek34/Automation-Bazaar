# Translate Telegram audio messages with AI (55 languages)

**ID** #031 · **Platform/Category** n8n · **Author** enescingoz (awesome-n8n-templates) · **Rating** ⭐ 4.5/5

🔗 **Source:** [https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json](https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
Receives audio/voice messages in Telegram, transcribes them using speech-to-text (Whisper), translates them into 55 support languages, and replies back.

## 🎯 Use when
> When conducting multi-lingual communications or support over voice notes.

## ⚡ Trigger
New voice/audio message in Telegram

## 🏁 Steps
1. Receive Telegram voice message file.
2. Download and transcribe with OpenAI Whisper.
3. Translate transcribed text to target language via LLM.
4. Send translation reply back to Telegram chat.

## ⚠️ Note
Large voice messages might hit model size limits, optimize chunk size if necessary.

## 🏷️ Keywords
whisper, speech-to-text, translation, telegram, audio

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.