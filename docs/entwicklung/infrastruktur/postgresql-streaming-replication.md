# Praxis-Guide: PostgreSQL Streaming Replication & Read Replicas

Einrichtung von asynchroner **Streaming-Replikation** in PostgreSQL zur Erhöhung der Ausfallsicherheit (High Availability) und zur Leseskalierung (Read Replicas).

---

```mermaid
graph LR
    ClientWrite["✍️ Schreibzugriffe"] --> Primary["🐘 Primary Database (10.0.0.1)"]
    Primary -->|Streaming WAL Logs (Port 5432)| Replica1["📖 Read Replica 1 (10.0.0.2)"]
    Primary -->|Streaming WAL Logs (Port 5432)| Replica2["📖 Read Replica 2 (10.0.0.3)"]
    ClientRead["🔍 Lesezugriffe"] --> Replica1
    ClientRead --> Replica2
```

---

## ⚙️ 1. Primary Node Konfiguration (`10.0.0.1`)

In `/etc/postgresql/16/main/postgresql.conf`:

```ini
listen_addresses = '*'
wal_level = replica
max_wal_senders = 10
max_replication_slots = 10
hot_standby = on
```

In `/etc/postgresql/16/main/pg_hba.conf` Replikations-User erlauben:

```text
host    replication     replicator      10.0.0.0/24             md5
```

```sql
-- Replikations-Benutzer anlegen
CREATE ROLE replicator WITH REPLICATION LOGIN PASSWORD 'geheim_repl_123';
```

```bash
sudo systemctl restart postgresql
```

---

## ⚙️ 2. Standby / Read Replica Node Konfiguration (`10.0.0.2`)

```bash
# 1. Dienst stoppen & altes Datenverzeichnis leeren
sudo systemctl stop postgresql
sudo rm -rf /var/lib/postgresql/16/main/*

# 2. Base Backup vom Primary laden
sudo -u postgres pg_basebackup -h 10.0.0.1 -D /var/lib/postgresql/16/main -U replicator -v -P -R

# 3. Replica starten
sudo systemctl start postgresql
```

---

## 🔍 3. Replikations-Status prüfen

Auf dem **Primary Server**:

```sql
SELECT client_addr, state, sync_state, replay_lag FROM pg_stat_replication;
```

---

## 🔗 Verwandte Themen
* [PostgreSQL Performance Tuning](postgresql-tuning.md) – Performance-Tuning
* [PostgreSQL PgBouncer Connection Pooling](postgresql-pgbouncer.md) – Connection Pooling
* [PostgreSQL Backup & Recovery](postgresql-backup-restore.md) – Backup-Strategien
