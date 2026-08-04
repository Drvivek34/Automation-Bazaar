# Hourly CI fixer and recompile sweep

**ID** #040 · **Platform/Category** Other Platforms · **Author** GitHub gh-aw contributors · **Rating** ⭐ 4.5/5

🔗 **Source:** [https://github.com/github/gh-aw/blob/main/.github/workflows/avenger.md](https://github.com/github/gh-aw/blob/main/.github/workflows/avenger.md)  ·  **License:** See source repository

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
A scheduled GitHub Actions maintenance pattern that checks CI, merges the current base branch, recompiles generated workflows only when needed, runs formatting and tests, and opens a PR for fixable issues.

## 🎯 Use when
> To keep a repository's generated workflows and mechanical CI fixes current without creating noisy PRs when CI is already green.

## ⚡ Trigger
Hourly schedule or manual dispatch

## 🏁 Steps
1. Check the latest completed CI status on the default branch.
2. Stop without changes when CI is passing.
3. If CI is failing, update from the default branch and recompile only when source workflow files changed.
4. Run formatting and tests, then open a reviewable PR with the bounded diff.

## ⚠️ Note
Keep the workflow read-only until a reviewed PR is created; pin third-party actions and cap generated diffs.

## 🏷️ Keywords
github actions, scheduled CI, workflow recompile, automated maintenance, pull request

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.