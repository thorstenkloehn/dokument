# Praxis-Guide: PostgreSQL PgBouncer Connection Pooling

**PgBouncer** ist ein extrem leichtgewichtiger Connection-Pooler für PostgreSQL, der den Ressourcenverbrauch von Datenbankverbindungen drastisch reduziert und tausende parallele Client-Verbindungen ermöglicht.

---

```mermaid
graph LR
    Apps["📱 Tausende App-Verbindungen"] --> PgBouncer["⚡ PgBouncer (Port 6432)"]
    PgBouncer -->|Wiederverwendeter Connection-Pool| Postgres["🐘 PostgreSQL (Port 5432)"]
```

---

## 🛠️ 1. Installation

```bash
sudo apt update && sudo apt install -y pgbouncer
```

---

## ⚙️ 2. Konfiguration (`/etc/pgbouncer/pgbouncer.ini`)

```ini
[databases]
meine_db = host=127.0.0.1 port=5432 dbname=meine_db

[pgbouncer]
listen_addr = 0.0.0.0
listen_port = 6432
auth_type = md5
auth_file = /etc/pgbouncer/userlist.txt

# Transaction-Pooling (Optimal für Web-Anwendungen)
pool_mode = transaction

# Verbindungslimits
max_client_conn = 5000
default_pool_size = 20
min_pool_size = 10
```

### User-Authentifizierung (`/etc/pgbouncer/userlist.txt`)
```text
"postgres" "md5_passwort_hash"
"app_user" "md5_passwort_hash"
```

```bash
sudo systemctl restart pgbouncer
```

---

## 🔗 Verwandte Themen
* [PostgreSQL Performance Tuning](postgresql-tuning.md) – Performance-Optimierung
* [PostgreSQL Backup & Recovery](postgresql-backup-restore.md) – Sicherung
