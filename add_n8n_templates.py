#!/usr/bin/env python3
import json
import os
import re

DB_PATH = "/root/bazaars/Automation-Bazaar/automations_data.json"

NEW_TEMPLATES = [
    {
        "title": "Telegram AI Bot with NeurochainAI",
        "author": "enescingoz (awesome-n8n-templates)",
        "source": "https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Telegram%20AI%20Bot_%20NeurochainAI%20Text%20&%20Image%20-%20NeurochainAI%20Basic%20API%20Integration.json",
        "category_slug": "n8n",
        "category_label": "n8n",
        "description": "Integrates the NeurochainAI API inside Telegram to offer text and image generation directly in your chat threads.",
        "useWhen": "When you want an affordable, custom-branded Telegram bot that handles both text chat and image creation.",
        "trigger": "New message in Telegram chat",
        "steps": [
            "Listen for a new message in Telegram.",
            "Route the prompt to NeurochainAI text/image generation nodes.",
            "Parse the API response.",
            "Reply to the user in Telegram with text or image attachment."
        ],
        "keywords": ["telegram", "bot", "neurochainai", "image-generation", "text-generation"],
        "note": "Requires setting up your Telegram bot token and NeurochainAI API key."
    },
    {
        "title": "Detect toxic language in Telegram messages",
        "author": "enescingoz (awesome-n8n-templates)",
        "source": "https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Detect%20toxic%20language%20in%20Telegram%20messages.json",
        "category_slug": "n8n",
        "category_label": "n8n",
        "description": "Monitors active Telegram chats, analyzes message text for toxicity using moderation AI, and flags/reports violations.",
        "useWhen": "For community managers looking to automatically moderate chat channels and keep interactions constructive.",
        "trigger": "New message in moderated Telegram group",
        "steps": [
            "Monitor Telegram group updates.",
            "Send message content to OpenAI/moderation API.",
            "Evaluate score against toxic language threshold.",
            "If toxic, notify administrators or take delete/warn actions."
        ],
        "keywords": ["moderation", "telegram", "security", "toxic language", "openai"],
        "note": "Customize the toxicity thresholds to balance safe communities with false positives."
    },
    {
        "title": "Translate Telegram audio messages with AI (55 languages)",
        "author": "enescingoz (awesome-n8n-templates)",
        "source": "https://github.com/enescingoz/awesome-n8n-templates/blob/main/Telegram/Translate%20Telegram%20audio%20messages%20with%20AI%20(55%20supported%20languages).json",
        "category_slug": "n8n",
        "category_label": "n8n",
        "description": "Receives audio/voice messages in Telegram, transcribes them using speech-to-text (Whisper), translates them into 55 support languages, and replies back.",
        "useWhen": "When conducting multi-lingual communications or support over voice notes.",
        "trigger": "New voice/audio message in Telegram",
        "steps": [
            "Receive Telegram voice message file.",
            "Download and transcribe with OpenAI Whisper.",
            "Translate transcribed text to target language via LLM.",
            "Send translation reply back to Telegram chat."
        ],
        "keywords": ["whisper", "speech-to-text", "translation", "telegram", "audio"],
        "note": "Large voice messages might hit model size limits, optimize chunk size if necessary."
    },
    {
        "title": "Hacker News Throwback Machine",
        "author": "enescingoz (awesome-n8n-templates)",
        "source": "https://github.com/enescingoz/awesome-n8n-templates/blob/main/Other_Integrations_and_Use_Cases/Hacker%20News%20Throwback%20Machine%20-%20See%20What%20Was%20Hot%20on%20This%20Day,%20Every%20Year!.json",
        "category_slug": "n8n",
        "category_label": "n8n",
        "description": "Cuts through the noise to fetch the top-voted Hacker News posts from exactly 1, 2, 5, or 10 years ago today.",
        "useWhen": "For retro-tech enthusiasts or anyone compiling curated newsletters on historical tech discussions.",
        "trigger": "Scheduled Cron (Daily)",
        "steps": [
            "Calculate matching retro dates (1, 2, 5, 10 years ago).",
            "Query Algolia HN API for high-score items on those dates.",
            "Format the results into a daily throwback brief.",
            "Publish to Slack, email, or Notion."
        ],
        "keywords": ["hacker news", "retro", "cron", "slack", "newsletter"],
        "note": "Maintains an engaging tech history logger automatically."
    },
    {
        "title": "Siri AI Agent with Apple Shortcuts",
        "author": "enescingoz (awesome-n8n-templates)",
        "source": "https://github.com/enescingoz/awesome-n8n-templates/blob/main/Other_Integrations_and_Use_Cases/Siri%20AI%20Agent_%20Apple%20Shortcuts%20powered%20voice%20template.json",
        "category_slug": "n8n",
        "category_label": "n8n",
        "description": "Bridges iOS Siri voice shortcuts to a powerful agentic backend in n8n, enabling deep custom commands via voice.",
        "useWhen": "For voice-activated smart home commands or hands-free task triggers on iPhones.",
        "trigger": "iOS Apple Shortcut webhook call",
        "steps": [
            "Receive Siri shortcut webhook payload.",
            "Parse voice input transcripts.",
            "Call LLM Agent with tool calling to process request.",
            "Return custom speech response text to Siri for voice synthesis."
        ],
        "keywords": ["siri", "shortcuts", "webhook", "voice-agent", "ios"],
        "note": "Requires setting up an Apple Shortcut to capture audio and trigger the webhook."
    }
]

def kebab_case(name):
    s = name.lower()
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

def main():
    if not os.path.exists(DB_PATH):
        print(f"Error: {DB_PATH} not found!")
        return

    with open(DB_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    existing_slugs = {item["slug"] for item in data["loops"]}
    next_num = max(int(item["number"]) for item in data["loops"]) + 1

    added = 0
    for t in NEW_TEMPLATES:
        slug = kebab_case(t["title"])
        if slug in existing_slugs:
            print(f"Skipping {t['title']} (duplicate)")
            continue

        item_obj = {
            "number": f"{next_num:03d}",
            "category": {
                "slug": t["category_slug"],
                "label": t["category_label"]
            },
            "platform": t["category_slug"],
            "title": t["title"],
            "slug": slug,
            "author": t["author"],
            "source": t["source"],
            "license": "See source",
            "averageRating": 4.5,
            "reviews": [],
            "description": t["description"],
            "useWhen": t["useWhen"],
            "trigger": t["trigger"],
            "steps": t["steps"],
            "keywords": t["keywords"],
            "implementationNote": t["note"],
            "published": "2026-06-20",
            "modified": "2026-06-20"
        }
        data["loops"].append(item_obj)
        existing_slugs.add(slug)
        next_num += 1
        added += 1
        print(f"Added {t['title']}")

    if added > 0:
        data["loopCount"] = len(data["loops"])
        with open(DB_PATH, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print(f"Successfully added {added} new templates to database.")
    else:
        print("No templates added.")

if __name__ == "__main__":
    main()
