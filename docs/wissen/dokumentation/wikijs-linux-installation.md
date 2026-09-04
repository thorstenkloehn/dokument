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

## 4. Ersteinrichtung auf einem Headless-Server

Wiki.js 2.x stellt nach aktuellem Stand **keinen offiziell dokumentierten CLI-Befehl** bereit, der den ersten Administrator vollständig im Terminal anlegt. Der gelegentlich genannte Aufruf ist deshalb nicht Bestandteil dieser Anleitung:

```bash
# Nicht verwenden: gehört nicht zur offiziellen Wiki.js-2.x-Installation
node server/cli setup
```

Auf einer Maschine ohne grafische Oberfläche wird der Einrichtungsassistent stattdessen sicher über einen **SSH-Tunnel** aufgerufen. Setze den Host in `config.yml` zunächst auf die lokale Schnittstelle:

```yaml
bindIP: 127.0.0.1
port: 3000
```

Starte Wiki.js anschließend auf dem Server:

```bash
cd /var/wiki
sudo -u wikijs env NODE_ENV=production /usr/bin/node server
```

Öffne auf deinem eigenen Rechner ein zweites Terminal und leite den lokalen Port `3000` verschlüsselt zum Server weiter:

```bash
ssh -L 3000:127.0.0.1:3000 admin@SERVER-IP
```

Solange die SSH-Verbindung besteht, erreichst du den Assistenten im lokalen Browser unter `http://127.0.0.1:3000`. Dort legst du das erste Administratorkonto an. Der Setup-Port muss dafür weder öffentlich freigegeben noch vor Abschluss der Ersteinrichtung einem Reverse Proxy ausgesetzt werden. Mehr zu Local Forwarding und weiteren Tunnel-Varianten: [SSH-Tunnel: Portweiterleitung über SSH](../../entwicklung/infrastruktur/ssh-tunnel.md).

!!! warning "Achtung: Keine inoffiziellen Setup-Befehle automatisieren"
    Ein nicht vorhandener CLI-Aufruf bricht mit einem Modulfehler ab und richtet kein Administratorkonto ein. Auch direkte Änderungen an den Wiki.js-Datenbanktabellen sind keine stabile Automatisierungsschnittstelle. Verwende für reproduzierbare Installationen die offizielle Bereitstellungsanleitung und schließe die einmalige Kontoanlage über den geschützten Web-Assistenten ab.

---

## 5. Ersten Start testen

Starte Wiki.js zunächst im Vordergrund. So werden Konfigurations- oder Datenbankfehler direkt im Terminal sichtbar:

```bash
cd /var/wiki
sudo -u wikijs env NODE_ENV=production /usr/bin/node server
```

Sobald der Start erfolgreich war, öffne im Browser `http://SERVER-IP:3000` beziehungsweise die konfigurierte Domain und führe den Einrichtungsassistenten aus. Auf einem Headless-Server verwendest du dafür den zuvor beschriebenen SSH-Tunnel. Beende den Testlauf danach mit ++ctrl+c++, bevor der dauerhafte Dienst gestartet wird.

---

## 6. `systemd`-Dienst einrichten

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

## 7. Netzwerk und Reverse Proxy

Wiki.js kann selbst Anfragen annehmen. Für eine öffentliche Installation ist dennoch meist ein Reverse Proxy wie Nginx, Caddy oder Apache sinnvoll, insbesondere für HTTPS und eine saubere Domain-Konfiguration.

Wiki.js wird auf einer eigenen Domain oder Subdomain betrieben, zum Beispiel `wiki.wissen-ahrensburg.de`. Ein Betrieb in einem Unterpfad wie `example.org/wiki` wird nicht unterstützt.

Beispielkonfiguration für `/etc/nginx/conf.d/wikijs.conf` mit Let's-Encrypt-Zertifikat (siehe [Nginx & SSL](../../entwicklung/infrastruktur/nginx-ssl.md) zur Zertifikatsbeschaffung mit Certbot):

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name wiki.wissen-ahrensburg.de;
    ssl_certificate /etc/letsencrypt/live/wissen-ahrensburg.de/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/wissen-ahrensburg.de/privkey.pem;

    location / {
        proxy_pass http://127.0.0.1:3000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 80;
    listen [::]:80;
    server_name wiki.wissen-ahrensburg.de;
    return 301 https://$host$request_uri;
}
```

```bash
sudo nginx -t
sudo systemctl reload nginx
```

!!! tip "Tipp"
    Statt der TCP-Verbindung über `127.0.0.1:3000` lässt sich Nginx auch über einen Unix-Socket an Wiki.js anbinden — siehe [Nginx über Unix-Socket anbinden](wikijs-nginx-unix-socket.md).

### Wiki.js dauerhaft vor direktem Internetzugriff schützen

Das `bindIP: 127.0.0.1` aus Schritt 4 sollte nicht nur für die Ersteinrichtung gelten, sondern **dauerhaft** so bleiben:

```yaml
bindIP: 127.0.0.1
port: 3000
```

Damit lauscht Wiki.js ausschließlich auf localhost — von außen ist Port 3000 grundsätzlich unerreichbar, unabhängig von jeder Firewall-Regel. Nginx läuft auf demselben Host und erreicht Wiki.js weiterhin problemlos über `127.0.0.1:3000` (oder über den in [Nginx über Unix-Socket anbinden](wikijs-nginx-unix-socket.md) beschriebenen Unix-Socket).

Nach einer Änderung an `config.yml` den Dienst neu starten:

```bash
sudo systemctl restart wikijs
```

Zusätzlich als zweite, unabhängige Absicherungsebene (falls `bindIP` versehentlich wieder auf `0.0.0.0` gestellt wird): Port 3000 nie in der Firewall freigeben, sondern ausschließlich HTTP/HTTPS für Nginx erlauben.

```bash
sudo ufw allow "Nginx Full"
sudo ufw deny 3000/tcp
sudo ufw status verbose
```

Die explizite `deny`-Regel ist bei UFWs Standardrichtlinie (`default deny incoming`) zwar redundant, macht die Absicht aber in `ufw status` sichtbar und dokumentiert sie selbsterklärend. Details zu UFW: [UFW-Firewall installieren und steuern](../../entwicklung/infrastruktur/ufw-firewall.md).

Für spätere administrative Zugriffe direkt auf Port 3000 (z. B. Fehlersuche ohne Nginx) eignet sich statt einer Portfreigabe weiterhin ein [SSH-Tunnel](../../entwicklung/infrastruktur/ssh-tunnel.md).

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
- [Evolution und Architekturen von Wiki.js](wikijs-evolution-digitaler.md) – Architektur- und Versionsgeschichte dieser Installation
- [Wiki.js-Agenten-Pipeline](wikijs-ki-agent.md) – automatisierte Inhaltspflege über die GraphQL-API
- [UFW-Firewall installieren und steuern](../../entwicklung/infrastruktur/ufw-firewall.md)
- [SSH-Tunnel: Portweiterleitung über SSH](../../entwicklung/infrastruktur/ssh-tunnel.md)
- [Dokumentationsübersicht](index.md)
