# Praxis-Guide: MediaWiki Backup & Automated Restore Scripts

Vollständiges Backup- und Wiederherstellungs-Setup für MediaWiki-Instanzen, bestehend aus der MySQL/MariaDB-Datenbank, hochgeladenen Bildern (`images/`) und Konfigurationsdateien (`LocalSettings.php`).

---

## 🤖 1. Automatisiertes Backup-Skript (`backup_mediawiki.sh`)

```bash
#!/bin/bash
set -e

WIKI_DIR="/var/www/html/mediawiki"
BACKUP_DIR="/backups/mediawiki"
DATE=$(date +%Y%m%d_%H%M%S)

DB_NAME="wikidb"
DB_USER="wikiuser"
DB_PASS="geheim123"

mkdir -p "$BACKUP_DIR/$DATE"

echo "1. Sichere Datenbank..."
mysqldump -u "$DB_USER" -p"$DB_PASS" "$DB_NAME" | gzip > "$BACKUP_DIR/$DATE/wikidb_$DATE.sql.gz"

echo "2. Sichere LocalSettings.php & Uploads..."
tar -czf "$BACKUP_DIR/$DATE/images_$DATE.tar.gz" -C "$WIKI_DIR" images LocalSettings.php

echo "✅ Backup erfolgreich abgeschlossen unter: $BACKUP_DIR/$DATE"
```

---

## 🔄 2. Wiederherstellung (Restore)

```bash
# 1. Datenbank wiederherstellen
gunzip < wikidb_20260101.sql.gz | mysql -u wikiuser -p wikidb

# 2. Upload-Bilder & LocalSettings entpacken
tar -xzf images_20260101.tar.gz -C /var/www/html/mediawiki/
```

---

## 🔗 Verwandte Themen
* [MediaWiki Backup](backup.md) – Backup Übersicht
* [MediaWiki Wiederherstellen](wiederherstellen.md) – Restore Anleitung
* [MediaWiki Python Bot](mediawiki-python-bot.md) – API Bot
