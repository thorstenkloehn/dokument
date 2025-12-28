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

```bash
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