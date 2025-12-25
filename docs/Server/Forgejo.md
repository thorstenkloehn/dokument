/**
 * Forgejo ist eine Open-Source-Plattform zur Verwaltung von Quellcode-Repositories, die auf Gitea basiert.
 * Sie bietet Funktionen wie Versionskontrolle mit Git, Issue-Tracking, Code-Reviews, Pull Requests und eine Web-Oberfläche zur Zusammenarbeit an Softwareprojekten.
 * Forgejo kann selbst gehostet werden und eignet sich für Teams und Einzelpersonen, die eine unabhängige, datenschutzfreundliche Alternative zu kommerziellen Git-Diensten suchen.
 */

## Installation

Um Forgejo herunterzuladen und ausführbar zu machen, führen Sie folgende Befehle aus:

```bash
wget https://codeberg.org/forgejo/forgejo/releases/download/v13.0.3/forgejo-13.0.3-linux-amd64
chmod +x forgejo-13.0.3-linux-amd64
sudo cp forgejo-13.0.3-linux-amd64 /usr/local/bin/forgejo
sudo chmod 755 /usr/local/bin/forgejo
sudo apt install git git-lfs
```

Erstellen Sie einen Benutzer `git` auf dem System. Forgejo wird unter diesem Benutzer ausgeführt, und beim Zugriff auf Git über SSH (was standardmäßig der Fall ist), ist dieser Benutzer Teil der URL (zum Beispiel in `git clone git@git.example.com:YourOrg/YourRepo.git` steht das `git` vor dem @ für den Benutzer, den Sie jetzt anlegen). Unter Debian, Ubuntu und deren Derivaten geschieht dies mit:

```bash
sudo adduser --system --shell /bin/bash --gecos 'Git Version Control' \
  --group --disabled-password --home /home/git git
```

## Verzeichnisse anlegen

Erstellen Sie nun die Verzeichnisse, die Forgejo verwenden wird, und setzen Sie die Zugriffsrechte entsprechend:

```bash
sudo mkdir /var/lib/forgejo
sudo chown git:git /var/lib/forgejo && sudo chmod 750 /var/lib/forgejo
```
In diesem Verzeichnis speichert Forgejo seine Daten, einschließlich Ihrer Git-Repositories.

```bash
sudo mkdir /etc/forgejo
sudo chown root:git /etc/forgejo && sudo chmod 770 /etc/forgejo
```
In diesem Verzeichnis wird die Forgejo-Konfigurationsdatei `app.ini` abgelegt. Zu Beginn muss Forgejo Schreibrechte auf dieses Verzeichnis haben. Nach der Installation können Sie die Rechte so anpassen, dass Forgejo nur noch Lesezugriff hat, da die Konfiguration dann nicht mehr verändert werden sollte.
## Optional: Datenbank einrichten

Wenn Sie SQLite als Datenbank für Forgejo verwenden, ist an dieser Stelle keine weitere Einrichtung erforderlich.

Falls Sie eine leistungsfähigere Datenbank benötigen, können Sie MySQL/MariaDB oder PostgreSQL verwenden (SQLite reicht laut Forgejo-Dokumentation für mindestens 10 Nutzer, möglicherweise sogar für mehr).

Weitere Informationen zur Einrichtung finden Sie im [Forgejo Database Preparation Guide](https://forgejo.org/docs/latest/admin/database-preparation/).

## Forgejo als systemd-Dienst einrichten

Forgejo stellt ein systemd-Service-Skript bereit. Laden Sie dieses an den richtigen Ort herunter:

```bash
sudo wget -O /etc/systemd/system/forgejo.service https://codeberg.org/forgejo/forgejo/raw/branch/forgejo/contrib/systemd/forgejo.service
```

Wenn Sie nicht SQLite, sondern MySQL, MariaDB oder PostgreSQL verwenden, müssen Sie die Datei `/etc/systemd/system/forgejo.service` bearbeiten und die entsprechenden `Wants=`- und `After=`-Zeilen auskommentieren. Ansonsten sollte der Dienst wie bereitgestellt funktionieren.

Nach dem Hinzufügen oder Ändern einer systemd-Service-Datei müssen Sie systemd neu laden:

```bash
sudo systemctl daemon-reload
```

Aktivieren und starten Sie nun den Forgejo-Dienst, um mit der Installation fortzufahren:

```bash
sudo systemctl enable forgejo.service
sudo systemctl start forgejo.service
```
## Weitere Konfiguration in der app.ini

Bevor Sie weitere Änderungen an der Konfiguration vornehmen, stoppen Sie zunächst den Forgejo-Dienst:

```bash
sudo systemctl stop forgejo.service
```

Nachdem die Einrichtung abgeschlossen ist, empfiehlt es sich, das Verzeichnis `/etc/forgejo` und die Datei `app.ini` für den Benutzer `git` schreibgeschützt zu machen. Forgejo benötigt nach der Erstkonfiguration keine Schreibrechte mehr auf diese Dateien:

```bash
sudo chmod 750 /etc/forgejo
sudo chmod 640 /etc/forgejo/app.ini
```

Bearbeiten Sie nun als root die Datei `/etc/forgejo/app.ini`, um weitere Einstellungen vorzunehmen:

```bash
sudo nano /etc/forgejo/app.ini
```
## Port ändern


Standardmäßig lauscht Forgejo auf Port 3000. Um den Port zu ändern, bearbeiten Sie die Konfigurationsdatei `app.ini`, die sich im Verzeichnis `/etc/forgejo` befindet:

```bash
sudo nano /etc/forgejo/app.ini
```

Suchen Sie den Abschnitt `[server]` und passen Sie die Zeile `HTTP_PORT` an, zum Beispiel:

```
[server]
HTTP_PORT = 8080
```

Speichern Sie die Datei und starten Sie den Forgejo-Dienst neu, damit die Änderung wirksam wird:

```bash
sudo systemctl restart forgejo.service
```

## Template ändern
Wechseln Sie in das Verzeichnis `/var/lib/forgejo/custom/templates/custom`.
```
cd var/lib/forgejo/custom/templates/custom
```

### Weitere nützliche Templates

Neben `extra_links.tmpl` und `extra_tabs.tmpl` gibt es weitere hilfreiche Templates, die Sie im Verzeichnis `$FORGEJO_CUSTOM/templates/custom/` ablegen können:

- **header.tmpl**: Wird direkt vor dem Ende des `<head>`-Tags eingefügt. Hier können Sie z. B. eigene CSS-Dateien einbinden.
- **body_outer_pre.tmpl**: Wird unmittelbar nach dem Start des `<body>`-Tags eingefügt.
- **body_inner_pre.tmpl**: Wird vor der oberen Navigationsleiste, aber bereits innerhalb des Hauptcontainers `<div class="full height">` eingefügt.
- **body_inner_post.tmpl**: Wird vor dem Ende des Hauptcontainers eingefügt.
- **body_outer_post.tmpl**: Wird vor dem unteren `<footer>`-Element eingefügt.
- **footer.tmpl**: Wird direkt vor dem Ende des `<body>`-Tags eingefügt und eignet sich gut für zusätzliches JavaScript.

Mit diesen Templates können Sie das Aussehen und Verhalten der Forgejo-Oberfläche gezielt anpassen.


