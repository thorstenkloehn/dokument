# Wiki.js nativ unter Linux installieren

Diese Anleitung zeigt, wie **Wiki.js 2.x** ohne Container aus dem offiziellen Release-Archiv eingerichtet und anschließend als `systemd`-Dienst betrieben wird. Sie setzt eine bereits vorbereitete Datenbank und eine unterstützte Node.js-Version voraus.

!!! note "Hinweis zur Quelle"
    Die Arbeitsschritte orientieren sich an der offiziellen [Linux-Anleitung von Wiki.js](https://docs.requarks.io/install/linux). Der Text wurde eigenständig formuliert, neu gegliedert und um praktische Hinweise ergänzt; er ist keine wörtliche Übersetzung.

---

## Voraussetzungen

Vor dem Start sollten folgende Komponenten bereitstehen:

- eine aktuelle Linux-Distribution mit `systemd`,
- eine von Wiki.js unterstützte Node.js-Version,
- mindestens 1 GB Arbeitsspeicher und ausreichend Speicherplatz,
- eine leere Datenbank mit eigenem Benutzerkonto,
- eine eigene Domain oder Subdomain für das Wiki.

Für produktive Installationen empfiehlt das Wiki.js-Projekt **PostgreSQL**. Welche Versionen aktuell unterstützt werden, steht in den offiziellen [Systemanforderungen](https://docs.requarks.io/install/requirements).

!!! warning "Achtung"
    Die unterstützten Versionen von Node.js und den Datenbanken können sich ändern. Prüfe deshalb vor einer Neuinstallation immer die aktuellen Systemanforderungen.

---

## 1. Systembenutzer und Zielordner anlegen

Ein eigener Benutzer begrenzt die Rechte des Wiki-Prozesses. Das folgende Beispiel verwendet `/var/wiki` als Installationsverzeichnis:

```bash
sudo useradd --system --home-dir /var/wiki --shell /usr/sbin/nologin wikijs
sudo mkdir -p /var/wiki
sudo chown wikijs:wikijs /var/wiki
```

---

## 2. Wiki.js herunterladen und entpacken

Lade das aktuelle Release zunächst in ein temporäres Verzeichnis. Danach wird das Archiv direkt in den endgültigen Zielordner entpackt:

```bash
cd /tmp
wget https://github.com/Requarks/wiki/releases/latest/download/wiki-js.tar.gz
sudo tar xzf wiki-js.tar.gz -C /var/wiki
sudo chown -R wikijs:wikijs /var/wiki
```

!!! tip "Tipp"
    In sicherheitskritischen Umgebungen sollte das Archiv vor dem Entpacken anhand der vom Projekt bereitgestellten Prüfsummen oder Release-Informationen kontrolliert werden.

---

## 3. Konfiguration vorbereiten

Wiki.js liefert eine Beispielkonfiguration mit. Kopiere sie als `config.yml` und bearbeite anschließend insbesondere Port und Datenbankzugang:

```bash
sudo -u wikijs cp /var/wiki/config.sample.yml /var/wiki/config.yml
sudo nano /var/wiki/config.yml
```

Eine PostgreSQL-Konfiguration kann beispielsweise so aussehen:

```yaml
port: 3000

db:
  type: postgres
  host: localhost
  port: 5432
  user: wikijs
  pass: EIN_LANGES_ZUFAELLIGES_PASSWORT
  db: wikijs
```

Die Datenbank und das angegebene Datenbankkonto müssen bereits existieren. Weitere Optionen erklärt die offizielle [Konfigurationsreferenz](https://docs.requarks.io/install/config).

!!! warning "Achtung: Zugangsdaten schützen"
    Die Datei `config.yml` enthält üblicherweise das Datenbankpasswort. Beschränke deshalb den Zugriff auf den Dienstbenutzer:

    ```bash
    sudo chmod 600 /var/wiki/config.yml
    sudo chown wikijs:wikijs /var/wiki/config.yml
    ```

Nur wenn **SQLite** verwendet wird, müssen zusätzlich dessen native Bindings im Installationsordner neu gebaut werden:

```bash
cd /var/wiki
sudo -u wikijs npm rebuild sqlite3
```

Für den produktiven Betrieb ist PostgreSQL die bessere Wahl.

---

## 4. Ersten Start testen

Starte Wiki.js zunächst im Vordergrund. So werden Konfigurations- oder Datenbankfehler direkt im Terminal sichtbar:

```bash
cd /var/wiki
sudo -u wikijs env NODE_ENV=production /usr/bin/node server
```

Sobald der Start erfolgreich war, öffne im Browser `http://SERVER-IP:3000` beziehungsweise die konfigurierte Domain und führe den Einrichtungsassistenten aus. Beende den Testlauf danach mit ++ctrl+c++, bevor der dauerhafte Dienst gestartet wird.

---

## 5. `systemd`-Dienst einrichten

Lege die Datei `/etc/systemd/system/wikijs.service` mit folgendem Inhalt an:

```ini
[Unit]
Description=Wiki.js
After=network-online.target
Wants=network-online.target

[Service]
Type=simple
User=wikijs
Group=wikijs
WorkingDirectory=/var/wiki
Environment=NODE_ENV=production
ExecStart=/usr/bin/node server
Restart=on-failure
RestartSec=5

[Install]
WantedBy=multi-user.target
```

Danach liest `systemd` die neue Definition ein. Der zweite Befehl aktiviert den automatischen Start und startet Wiki.js sofort:

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now wikijs
```

Status und Protokollausgaben lassen sich so kontrollieren:

```bash
sudo systemctl status wikijs
sudo journalctl -u wikijs -f
```

!!! note "Hinweis zum Node.js-Pfad"
    `/usr/bin/node` ist ein häufig verwendeter Pfad, aber nicht auf jedem System korrekt. Zeigt `command -v node` einen anderen Speicherort, muss `ExecStart` entsprechend angepasst werden.

---

## 6. Netzwerk und Reverse Proxy

Wiki.js kann selbst Anfragen annehmen. Für eine öffentliche Installation ist dennoch meist ein Reverse Proxy wie Nginx, Caddy oder Apache sinnvoll, insbesondere für HTTPS und eine saubere Domain-Konfiguration.

Wiki.js wird auf einer eigenen Domain oder Subdomain betrieben, zum Beispiel `wiki.example.org`. Ein Betrieb in einem Unterpfad wie `example.org/wiki` wird nicht unterstützt.

---

## Kurzprüfung

```bash
systemctl is-enabled wikijs
systemctl is-active wikijs
curl -I http://127.0.0.1:3000
```

Wenn der Dienst aktiviert und aktiv ist und der HTTP-Aufruf eine Antwort liefert, läuft die Anwendung. Danach sollten noch HTTPS, Firewall, Backups und regelmäßige Updates eingerichtet werden.

---

## Quellen und weiterführende Informationen

- [Wiki.js: Installation unter Linux](https://docs.requarks.io/install/linux) – technische Ausgangsbasis dieser eigenständig formulierten Anleitung
- [Wiki.js: Systemanforderungen](https://docs.requarks.io/install/requirements)
- [Wiki.js: Konfigurationsreferenz](https://docs.requarks.io/install/config)
- [Wiki.js-Agenten-Pipeline](wikijs-ki-agent.md) – automatisierte Inhaltspflege über die GraphQL-API
- [Dokumentationsübersicht](index.md)
