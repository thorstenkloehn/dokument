# Praxis-Guide: PostgreSQL Backup, WAL-Archivierung & Recovery

Ein robuster Leitfaden für die Sicherung und Wiederherstellung von PostgreSQL-Datenbanken mittels `pg_dump`, `pg_restore` und Write-Ahead Log (WAL) Archivierung für Point-in-Time Recovery (PITR).

---

## 💾 1. Logische Backups (`pg_dump` & `pg_dumpall`)

### Einzeldatenbank sichern (komprimiertes Custom-Format)
```bash
pg_dump -U postgres -h localhost -F c -b -v -f "/backups/db_$(date +%Y%m%m_%H%M%S).dump" meine_datenbank
```

### Einzeldatenbank wiederherstellen (`pg_restore`)
```bash
# Datenbank vorab anlegen, falls nicht vorhanden
createdb -U postgres -h localhost meine_datenbank

# Wiederherstellung mit parallelen Jobs (-j 4)
pg_restore -U postgres -h localhost -d meine_datenbank -v -j 4 "/backups/db_backup.dump"
```

### Alle Datenbanken samt Rollen und Rechten sichern
```bash
pg_dumpall -U postgres -h localhost | gzip > "/backups/all_dbs_$(date +%Y%m%d).sql.gz"
```

---

## ⏱️ 2. Point-in-Time Recovery (PITR) & WAL-Archivierung

In `/etc/postgresql/16/main/postgresql.conf`:

```ini
wal_level = replica
archive_mode = on
archive_command = 'test ! -f /var/lib/postgresql/wal_archive/%f && cp %p /var/lib/postgresql/wal_archive/%f'
```

```bash
mkdir -p /var/lib/postgresql/wal_archive
chown -R postgres:postgres /var/lib/postgresql/wal_archive
sudo systemctl restart postgresql
```

---

## 🤖 3. Automatisiertes Backup-Skript (`auto_backup.sh`)

```bash
#!/bin/bash
set -e

BACKUP_DIR="/var/backups/postgresql"
RETENTION_DAYS=14
TIMESTAMP=$(date +%Y%m%d_%H%M%S)

mkdir -p "$BACKUP_DIR"

echo "Starte PostgreSQL Backup..."
pg_dumpall -U postgres | gzip > "$BACKUP_DIR/pg_all_$TIMESTAMP.sql.gz"

echo "Räume Backups älter als $RETENTION_DAYS Tage auf..."
find "$BACKUP_DIR" -type f -name "*.sql.gz" -mtime +$RETENTION_DAYS -delete

echo "✅ Backup erfolgreich abgeschlossen!"
```

---

## 🔗 Verwandte Themen
* [PostgreSQL Installation](postgresql.md) – Grundkonfiguration
* [PostgreSQL + pgvector](../../wissen/daten/datenbanken/pgvector-anleitung.md) – Vektordatenbanken
* [Docker KI-Stack](docker-ki-stack.md) – PostgreSQL im Container
