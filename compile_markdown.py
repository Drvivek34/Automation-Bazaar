#!/usr/bin/env python3
"""Compiles automations_data.json into the front README master table + per-category
folders with index tables and per-item detail pages. No workflow code is copied —
each entry links to its original source."""
import json, os

REPO_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(REPO_DIR, "automations_data.json")
REPO_URL = "https://github.com/Drvivek34/Automation-Bazaar"
WEBSITE = "https://drvivek34.github.io/Mega-AI-Bazaar/"

def stars(rating):
    return "★" * int(round(rating)) + "☆" * (5 - int(round(rating)))

def compile_markdown():
    with open(DB_PATH, encoding="utf-8") as f:
        data = json.load(f)
    loops = data["loops"]
    categories = data["categories"]
    total = data.get("loopCount", len(loops))
    updated = data.get("updated", "2026-06-20")

    r = []
    r.append("# ⚙️ Automation-Bazaar: The Curated Automation Workflows Directory")
    r.append("\n[![Mega AI Bazaar](https://img.shields.io/badge/🌐_Mega_AI_Bazaar-browse_all-6C5CE7)](https://drvivek34.github.io/Mega-AI-Bazaar/)")
    r.append(f"\nWelcome to **Automation-Bazaar** — a categorized, community-rated directory of **{total}** "
             "ready-to-use automations across **n8n, Make.com, Zapier, scripts, cron/schedules, and more**. "
             "Every entry links to its original source and keeps its author — no workflow files are copied here.")
    r.append(f"\n*Last updated: {updated} · Goal: 5,000+ high-quality automations · Part of the "
             f"[Mega AI Bazaar]({WEBSITE})*")

    # How to add — FIRST, as requested
    r.append("\n## 🤝 How to Add a New Automation (GitHub-first)")
    r.append("We welcome additions — **always credit the original author/source**.")
    r.append("\n### Option A — Submit an issue (no coding)")
    r.append(f"1. Open a [new submission]({REPO_URL}/issues/new/choose) and pick **Submit an Automation**.")
    r.append("2. Fill in title, platform/category, source URL, author, trigger, steps, and a note.")
    r.append("3. A maintainer or the daily automation adds it and recompiles this directory.")
    r.append("\n### Option B — Pull request")
    r.append("1. Fork, then add your entry object to [`automations_data.json`](automations_data.json).")
    r.append("2. Run `python3 compile_markdown.py` to regenerate the tables.")
    r.append("3. Open a PR. Keep the entry attributed and self-contained.")

    r.append("\n## 🔌 Platforms Covered")
    r.append("- 🟧 **n8n** — open-source workflow automation")
    r.append("- 🟪 **Make.com** — visual scenario automation")
    r.append("- 🟠 **Zapier** — app-to-app zaps")
    r.append("- 📜 **Automation Scripts** — backups, certs, ops glue")
    r.append("- ⏰ **Schedules & Cron** — the timers that drive workflows")
    r.append("- 🧩 **Other Platforms** — GitHub Actions, Airflow, and more")

    # Master table
    r.append("\n## 📚 Master Directory (all automations)")
    r.append("Sorted by rating. Click a title for full setup details.")
    r.append("\n| ID | Category | Title | Author | Rating | Notes / Use Cases |")
    r.append("|---|---|---|---|---|---|")

    by_cat = {c["slug"]: [] for c in categories}
    for lp in sorted(loops, key=lambda l: (l.get("averageRating", 0), len(l.get("reviews", []))), reverse=True):
        cs, cl = lp["category"]["slug"], lp["category"]["label"]
        link = f"{cs}/{lp['slug']}.md"
        r.append(f"| #{lp['number']} | {cl} | [{lp['title']}]({link}) | {lp['author']} | "
                 f"{stars(lp['averageRating'])} {lp['averageRating']} | {lp['description']} |")
        by_cat[cs].append(lp)

    r.append("\n## 🗂️ Categories")
    for c in categories:
        r.append(f"- [{c['label']}]({c['slug']}/README.md) ({len(by_cat[c['slug']])})")

    r.append(f"\n---\nPart of the **[Mega AI Bazaar]({WEBSITE})**. Licensed MIT for structure/text; "
             "each automation keeps its original author's license.")

    with open(os.path.join(REPO_DIR, "README.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(r))
    print("README.md compiled.")

    # Per-category folders + detail pages
    for c in categories:
        cs, cl = c["slug"], c["label"]
        d = os.path.join(REPO_DIR, cs)
        os.makedirs(d, exist_ok=True)
        items = sorted(by_cat[cs], key=lambda l: l["number"])
        cr = [f"# {cl} Automations — Automation-Bazaar",
              f"\n{len(items)} automations in **{cl}**. [← Back to master directory](../README.md)",
              "\n| ID | Title | Author | Rating | Notes / Use Cases |", "|---|---|---|---|---|"]
        for lp in items:
            cr.append(f"| #{lp['number']} | [{lp['title']}]({lp['slug']}.md) | {lp['author']} | "
                      f"{stars(lp['averageRating'])} {lp['averageRating']} | {lp['description']} |")
        with open(os.path.join(d, "README.md"), "w", encoding="utf-8") as f:
            f.write("\n".join(cr))
        for lp in items:
            write_detail(lp, d)
        # keep empty cats tracked by git
        open(os.path.join(d, ".gitkeep"), "a").close()
        print(f"{cs}/ compiled ({len(items)}).")

def write_detail(lp, d):
    m = [f"# {lp['title']}",
         f"\n**ID** #{lp['number']} · **Platform/Category** {lp['category']['label']} · "
         f"**Author** {lp['author']} · **Rating** ⭐ {lp['averageRating']}/5",
         f"\n🔗 **Source:** [{lp['source']}]({lp['source']})  ·  **License:** {lp.get('license','See source')}",
         "\n[← Category index](README.md) · [← Master directory](../README.md)\n\n---",
         f"\n## 📝 What it does\n{lp['description']}",
         f"\n## 🎯 Use when\n> {lp['useWhen']}",
         f"\n## ⚡ Trigger\n{lp['trigger']}",
         "\n## 🏁 Steps"]
    m += [f"{i+1}. {s}" for i, s in enumerate(lp["steps"])]
    if lp.get("implementationNote"):
        m.append(f"\n## ⚠️ Note\n{lp['implementationNote']}")
    m.append("\n## 🏷️ Keywords\n" + ", ".join(lp.get("keywords", [])))
    m.append("\n## 💬 Reviews")
    if lp.get("reviews"):
        for rv in lp["reviews"]:
            m.append(f"- **{rv['author']}** ({stars(rv['rating'])} {rv['rating']}/5): *{rv['comment']}*")
    else:
        m.append("- *No community reviews yet — be the first.*")
    m.append(f"\n> ℹ️ Ratings are editorial/curated until community reviews accumulate.")
    with open(os.path.join(d, f"{lp['slug']}.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(m))

if __name__ == "__main__":
    compile_markdown()
