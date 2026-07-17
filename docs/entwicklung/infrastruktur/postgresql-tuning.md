# Praxis-Guide: PostgreSQL Performance Tuning & Monitoring

Schritt-für-Schritt-Anleitung zur Leistungsoptimierung von PostgreSQL für produktive Webanwendungen und speicherintensive Abfragen.

---

## ⚡ 1. Speicher- & Hardware-Tuning (`postgresql.conf`)

Werte für einen Server mit **16 GB RAM** und **4 CPU-Kernen**:

```ini
# Arbeitsspeicher für Caching (ca. 25% des RAMs)
shared_buffers = 4GB

# Arbeitsspeicher pro Sortier-/Join-Operation
work_mem = 64MB

# Arbeitsspeicher für Wartungsarbeiten (VACUUM, INDEX)
maintenance_work_mem = 512MB

# Schätzung des Betriebssystem-Caches (ca. 50-75% des RAMs)
effective_cache_size = 12GB

# Parallele Abfrageausführung
max_worker_processes = 4
max_parallel_workers_per_gather = 2
max_parallel_workers = 4

# Checkpoint-Tuning
checkpoint_completion_target = 0.9
wal_buffers = 16MB
```

```bash
sudo systemctl restart postgresql
```

---

## 🔍 2. Langsame Abfragen identifizieren mit `pg_stat_statements`

In `postgresql.conf` aktivieren:

```ini
shared_preload_libraries = 'pg_stat_statements'
pg_stat_statements.track = all
```

In SQL ausführen:

```sql
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Top 5 zeitintensivste Abfragen finden
SELECT 
    calls,
    total_exec_time / 1000 AS total_sec,
    mean_exec_time AS avg_ms,
    query
FROM pg_stat_statements
ORDER BY total_exec_time DESC
LIMIT 5;
```

---

## 🔗 Verwandte Themen
* [PostgreSQL Installation](postgresql.md) – Grundkonfiguration
* [PostgreSQL Backup & Recovery](postgresql-backup-restore.md) – Backups
* [PostgreSQL + pgvector](../../wissen/daten/datenbanken/pgvector-anleitung.md) – Vektoreinbettungen
