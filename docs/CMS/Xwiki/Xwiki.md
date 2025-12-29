# XWiki Installation auf Ubuntu mit apt-get und PostgreSQL

## Voraussetzungen

- Ubuntu Server (empfohlen: 20.04 oder neuer)
- Root- oder Sudo-Rechte

## 1. System aktualisieren

```bash
sudo apt update
sudo apt upgrade
```

## 2. PostgreSQL installieren

```bash
sudo apt install postgresql postgresql-contrib
```

### PostgreSQL-Datenbank und Benutzer anlegen
```
sudo -u postgres -i
createdb -E UTF8 -O thorsten xwiki
exit
```



## 3. XWiki Repository hinzufügen

Zuerst muss der Paketmanager so konfiguriert werden, dass das XWiki-Repository verwendet wird. Dies geschieht einfach mit folgendem Befehl:

```bash
sudo wget https://maven.xwiki.org/xwiki-keyring.gpg -O /usr/share/keyrings/xwiki-keyring.gpg
sudo wget "https://maven.xwiki.org/stable/xwiki-stable.list" -O /etc/apt/sources.list.d/xwiki-stable.list
```

Jetzt kann die Paketdatenbank aktualisiert werden, um die Daten aus diesem Repository zu laden:

```bash
sudo apt-get update
```

## 3.1. Verfügbare XWiki-Pakete anzeigen

Um zu sehen, welche XWiki-Pakete im Repository verfügbar sind, kannst du folgenden Befehl verwenden:

```bash
apt-cache search xwiki
```

Dies listet alle XWiki-bezogenen Pakete auf, z.B. verschiedene Versionen für Tomcat und Datenbanken oder zusätzliche Erweiterungen.

## 4. XWiki und benötigte Pakete installieren

```bash
sudo apt install xwiki-tomcat10-pgsql
```

## 5. XWiki starten

Der Dienst startet automatisch. Prüfen mit:

```bash
sudo systemctl status tomcat10
```

## 6. XWiki im Browser aufrufen

Gehe zu: `http://<deine-server-ip>:8080/xwiki`

Folge dem Einrichtungsassistenten.

---

**Weitere Infos:**  
[XWiki Installationsanleitung](https://www.xwiki.org/xwiki/bin/view/Documentation/AdminGuide/Installation/InstallationViaAPT/)


## Backup erstellen

Um ein Backup der XWiki-Datenbank zu erstellen, verwende folgenden Befehl:

```bash
sudo -u postgres pg_dump xwiki > /home/thorsten/xwiki_backup.sql
```

Optional kannst du auch das Verzeichnis mit den Anhängen sichern (Standardpfad):

```bash
sudo tar czvf /home/thorsten/xwiki_files_backup.tar.gz /var/lib/xwiki/data
```

**Hinweis:**  
Stelle sicher, dass XWiki während des Backups keine Schreibzugriffe auf die Datenbank oder Dateien durchführt, um Konsistenz zu gewährleisten.

## Backup wiederherstellen

Um ein Backup der XWiki-Datenbank wiederherzustellen, führe folgende Schritte aus:

1. **Datenbank zurückspielen:**

```bash
sudo -u postgres dropdb xwiki
sudo -u postgres createdb -E UTF8 -O thorsten xwiki
sudo -u postgres psql xwiki < /home/thorsten/xwiki_backup.sql
```

2. **Dateianhänge zurückkopieren:**

```bash
sudo systemctl stop tomcat10
sudo tar xzvf /home/thorsten/xwiki_files_backup.tar.gz -C /
sudo systemctl start tomcat10
```

**Hinweis:**  
Stelle sicher, dass XWiki während der Wiederherstellung gestoppt ist, um Dateninkonsistenzen zu vermeiden.