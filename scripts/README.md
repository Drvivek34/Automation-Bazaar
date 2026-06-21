# Automation Scripts Automations — Automation-Bazaar

5 automations in **Automation Scripts**. [← Back to master directory](../README.md)

| ID | Title | Author | Rating | Notes / Use Cases |
|---|---|---|---|---|
| #020 | [Nightly restic/rsync backup](nightly-restic-rsync-backup.md) | Community (restic docs) | ★★★★★ 4.7 | Encrypted incremental backups of key paths to local + remote, with pruning and a status notification. |
| #021 | [Let's Encrypt cert auto-renew + reload](let-s-encrypt-cert-auto-renew-reload.md) | Community (certbot) | ★★★★★ 4.6 | Renews TLS certificates and reloads the web server only when a cert actually changes. |
| #022 | [Docker prune + unhealthy-container restart](docker-prune-unhealthy-container-restart.md) | Community | ★★★★☆ 4.4 | Frees disk by pruning dangling images/volumes and restarts containers failing healthchecks. |
| #023 | [Log rotation + compress + ship](log-rotation-compress-ship.md) | Community (logrotate) | ★★★★☆ 4.3 | Rotates and compresses app logs and ships archives to object storage. |
| #036 | [PostgreSQL Backup to AWS S3](postgresql-backup-to-aws-s3.md) | DevOps Cron Scripts | ★★★★☆ 4.5 | A robust shell script designed to be scheduled via cron that performs a pg_dump, compresses the database archive, and uploads it safely to an AWS S3 bucket. |