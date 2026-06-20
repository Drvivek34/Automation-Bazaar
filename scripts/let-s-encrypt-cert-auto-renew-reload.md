# Let's Encrypt cert auto-renew + reload

**ID** #021 · **Platform/Category** Automation Scripts · **Author** Community (certbot) · **Rating** ⭐ 4.6/5

🔗 **Source:** [https://eff-certbot.readthedocs.io/](https://eff-certbot.readthedocs.io/)  ·  **License:** See source

[← Category index](README.md) · [← Master directory](../README.md)

---

## 📝 What it does
Renews TLS certificates and reloads the web server only when a cert actually changes.

## 🎯 Use when
> When you manage your own TLS certs.

## ⚡ Trigger
Cron / systemd timer

## 🏁 Steps
1. Run certbot renew
2. Detect changed certs
3. Reload nginx/apache
4. Alert on failure

## ⚠️ Note
Use --deploy-hook so reloads happen only on renewal.

## 🏷️ Keywords
tls, certbot, lets encrypt, nginx

## 💬 Reviews
- *No community reviews yet — be the first.*

> ℹ️ Ratings are editorial/curated until community reviews accumulate.