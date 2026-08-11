# Moodle installieren: Git, PostgreSQL und Nginx

Diese Anleitung richtet **Moodle** produktiv auf einem eigenen Server ein — per **Git-Checkout** (offizieller Installationsweg für Moodle, kein apt-Paket), mit **PostgreSQL** als Datenbank und **Nginx** als Reverse Proxy über PHP-FPM. Sie folgt demselben Muster wie die [Drupal-](../drupal/installieren.md) und [XWiki-Installation](../xwiki/installieren.md) in diesem Wiki.

!!! warning "Achtung"
    Die unterstützten PHP- und PostgreSQL-Versionen sowie der aktuell empfohlene Stable-/LTS-Zweig ändern sich mit jedem Moodle-Release. Vor einer Neuinstallation immer die aktuellen [Moodle-Releases](https://moodledev.io/general/releases) prüfen. Diese Anleitung geht von **PHP 8.3** und **PostgreSQL 14+** aus.

---

## Voraussetzungen

- Ubuntu-Server mit `sudo`-Rechten
- eine eigene Domain/Subdomain, z. B. `moodle.wissen-ahrensburg.de`
- Nginx bereits mit SSL-Zertifikat eingerichtet (siehe [Nginx & SSL](../../../entwicklung/infrastruktur/nginx-ssl.md))

---

## 1. PHP, Erweiterungen und PostgreSQL installieren

```bash
sudo apt update
sudo apt install -y php8.3-fpm php8.3-cli php8.3-pgsql php8.3-gd \
  php8.3-xml php8.3-mbstring php8.3-curl php8.3-zip php8.3-intl \
  php8.3-soap php8.3-bcmath php8.3-opcache git postgresql
```

`php8.3-intl` und `php8.3-soap` werden von Moodle zusätzlich zu den bei Drupal üblichen Erweiterungen vorausgesetzt, `php8.3-bcmath` wird für präzise Bewertungsberechnungen im Gradebook empfohlen. `php8.3-pgsql` stellt den PDO-Treiber bereit, ohne den Moodle keine Verbindung zu PostgreSQL aufbauen kann.

---

## 2. Moodle per Git installieren

Für Moodle gibt es kein offizielles apt-Paket — empfohlen ist ein Git-Checkout des jeweiligen Stable-Zweigs, da sich spätere Updates dann als einfaches `git pull` erledigen lassen, statt Dateien manuell zu ersetzen:

```bash
cd /var/www
sudo git clone https://github.com/moodle/moodle.git moodle
cd moodle
git branch -a --list "origin/MOODLE_*_STABLE" | sort -V | tail -5
sudo git checkout -t origin/MOODLE_500_STABLE
sudo chown -R www-data:www-data /var/www/moodle
```

Der `git branch`-Aufruf listet die verfügbaren Stable-Zweige sortiert nach Version — daraus den aktuell unterstützten Zweig auswählen (siehe Warnhinweis oben) und statt `MOODLE_500_STABLE` einsetzen.

---

## 3. Datenverzeichnis anlegen

Moodle benötigt außerhalb des Webroots ein separates Verzeichnis für hochgeladene Dateien, Caches und Sitzungsdaten (`$CFG->dataroot`) — es darf nicht von Nginx ausgeliefert werden:

```bash
sudo mkdir -p /var/moodledata
sudo chown -R www-data:www-data /var/moodledata
sudo chmod -R 0770 /var/moodledata
```

`0770` beschränkt den Zugriff auf den Besitzer und die Gruppe (`www-data`) — für andere Nutzer ist das Verzeichnis komplett gesperrt.

---

## 4. PostgreSQL-Datenbank anlegen

```bash
sudo -u postgres psql -c "CREATE ROLE moodle WITH LOGIN PASSWORD 'EIN_LANGES_ZUFAELLIGES_PASSWORT';"
sudo -u postgres psql -c "CREATE DATABASE moodle OWNER moodle ENCODING 'UTF8' LC_COLLATE 'C' LC_CTYPE 'C' TEMPLATE template0;"
```

!!! note "Hinweis"
    Moodle erwartet für PostgreSQL-Datenbanken explizit die Locale `C` statt der Systemlocale — deshalb `LC_COLLATE`/`LC_CTYPE` hier abweichend von einer sonst üblichen `de_DE.UTF-8`-Datenbank setzen. PostgreSQL lauscht per Default-Konfiguration ohnehin nur lokal (`listen_addresses = 'localhost'`); da Moodle über PHP-FPM auf demselben Host läuft, ist keine Netzwerkfreigabe für Port 5432 nötig.

---

## 5. Site-Installation headless per CLI

Anders als bei Drupal/Drush installiert sich Moodle über ein eigenes CLI-Skript direkt aus dem Core heraus:

```bash
cd /var/www/moodle
sudo -u www-data php admin/cli/install.php \
  --wwwroot="https://moodle.wissen-ahrensburg.de" \
  --dataroot=/var/moodledata \
  --dbtype=pgsql \
  --dbhost=localhost \
  --dbname=moodle \
  --dbuser=moodle \
  --dbpass=EIN_LANGES_ZUFAELLIGES_PASSWORT \
  --fullname="Wissen Ahrensburg" \
  --shortname="WA-Moodle" \
  --adminuser=admin \
  --adminpass=EIN_WEITERES_LANGES_PASSWORT \
  --agree-license \
  --non-interactive
```

!!! tip "Tipp: Browser-Assistent als Alternative"
    Falls die nichtinteraktive Installation nicht ausreicht (z. B. für die Auswahl zusätzlicher Sprachpakete), lässt sich der grafische Installationsassistent wie bei den anderen Wiki-/CMS-Systemen in diesem Repository per [SSH-Tunnel](../../../entwicklung/infrastruktur/ssh-tunnel.md) absichern, statt ihn öffentlich zu exponieren:
    ```bash
    cd /var/www/moodle
    sudo -u www-data php -S 127.0.0.1:8888
    ```
    ```bash
    ssh -L 8888:127.0.0.1:8888 admin@SERVER-IP
    ```
    Der Assistent ist dann unter `http://127.0.0.1:8888` erreichbar, verschlüsselt über die SSH-Verbindung.

---

## 6. Cron-Job einrichten

Moodle muss `admin/cli/cron.php` mindestens jede Minute ausführen — dort laufen Benachrichtigungen, Kursaufgaben und geplante Tasks. Statt eines klassischen `crontab`-Eintrags empfiehlt die Moodle-Doku einen systemd-Timer, da dieser verhindert, dass ein neuer Lauf startet, während der vorige (z. B. bei einer aufwendigen Aufgabe) noch nicht beendet ist:

```ini title="/etc/systemd/system/moodle-cron.service"
[Unit]
Description=Moodle Cron

[Service]
Type=oneshot
User=www-data
ExecStart=/usr/bin/php /var/www/moodle/admin/cli/cron.php
```

```ini title="/etc/systemd/system/moodle-cron.timer"
[Unit]
Description=Moodle Cron, jede Minute

[Timer]
OnBootSec=1min
OnUnitActiveSec=1min
AccuracySec=1sec

[Install]
WantedBy=timers.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now moodle-cron.timer
systemctl list-timers moodle-cron.timer
```

`Type=oneshot` sorgt zusammen mit dem Timer dafür, dass systemd den nächsten Lauf erst nach Abschluss des vorherigen einplant — ein manuelles Overlap-Locking wie bei klassischem Cron ist damit nicht nötig.

---

## 7. PHP-FPM-Pool

Wie bei der Drupal-Installation empfiehlt sich ein eigener Pool, damit Moodle ressourcenseitig von anderen PHP-Diensten auf demselben Host isoliert ist, z. B. `/etc/php/8.3/fpm/pool.d/moodle.conf` mit `listen = /run/php/php8.3-fpm-moodle.sock`.

```bash
sudo systemctl restart php8.3-fpm
```

---

## 8. Nginx-Konfiguration

Erstellen oder bearbeiten Sie `/etc/nginx/conf.d/moodle.conf`:

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name moodle.wissen-ahrensburg.de;
    root /var/www/moodle;
    client_max_body_size 100M;
    ssl_certificate /etc/letsencrypt/live/wissen-ahrensburg.de/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/wissen-ahrensburg.de/privkey.pem;

    location ~ /\.git { deny all; }
    location ~ ^/(CHANGELOG|README|UPGRADING|COPYING)\.(md|txt)$ { deny all; }

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ [^/]\.php(/|$) {
        fastcgi_split_path_info ^(.+?\.php)(/.*)$;
        try_files $fastcgi_script_name =404;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
        fastcgi_read_timeout 300;
        fastcgi_pass unix:/run/php/php8.3-fpm-moodle.sock;
    }

    location ~* "\.(js|css|gif|jpg|jpeg|png|svg|woff|woff2)$" {
        expires max;
        log_not_found off;
    }
}

server {
    listen 80;
    listen [::]:80;
    server_name moodle.wissen-ahrensburg.de;
    return 301 https://$host$request_uri;
}
```

```bash
sudo nginx -t
sudo systemctl reload nginx
```

`client_max_body_size 100M` erlaubt größere Datei-Uploads (z. B. Videos in Kursen) — bei Bedarf an den tatsächlichen Nutzungsfall anpassen. `fastcgi_read_timeout 300` verhindert Zeitüberschreitungen bei länger laufenden Admin-Vorgängen (z. B. Kurs-Backups). `fastcgi_pass` verweist auf den in Schritt 7 eingerichteten dedizierten Pool-Socket — bei Nutzung des Standard-Pools stattdessen `unix:/run/php/php8.3-fpm.sock` verwenden. Das eigentliche Datenverzeichnis `/var/moodledata` liegt bereits außerhalb von `root` und ist damit für Nginx grundsätzlich unerreichbar; die zusätzlichen `deny`-Regeln sichern nur Repository-Metadaten innerhalb des Webroots ab.

---

## 9. Firewall (UFW)

```bash
sudo ufw allow "Nginx Full"
sudo ufw deny 5432/tcp
sudo ufw status verbose
```

PostgreSQL bindet zwar schon per Konfiguration nur an `localhost` (Schritt 4), die explizite `deny`-Regel dokumentiert diese Absicht aber zusätzlich sichtbar in `ufw status` — als zweite, unabhängige Absicherungsebene, falls `postgresql.conf` später versehentlich geändert wird. Details zu UFW: [UFW-Firewall installieren und steuern](../../../entwicklung/infrastruktur/ufw-firewall.md).

---

## Kurzprüfung

```bash
sudo systemctl is-active php8.3-fpm nginx postgresql
systemctl is-active moodle-cron.timer
curl -I https://moodle.wissen-ahrensburg.de
```

Meldet der `curl`-Aufruf `HTTP/2 200`, ist die Installation erreichbar. Danach im Backend (`/login/index.php`) anmelden und unter **Website-Administration → Server → Umgebung** die Umgebungsprüfung (`admin/environment.php`) laufen lassen — sie meldet fehlende PHP-Erweiterungen oder Berechtigungsprobleme.

---

## Quellen und weiterführende Informationen

- [Moodle: Installing Moodle](https://docs.moodle.org/en/Installing_Moodle)
- [Moodle: Releases](https://moodledev.io/general/releases)
- [Moodle: NGINX](https://docs.moodle.org/en/NGINX)
- [Moodle: Cron](https://docs.moodle.org/en/Cron)
- [Drupal installieren: Composer, PostgreSQL und Nginx](../drupal/installieren.md)
- [XWiki installieren](../xwiki/installieren.md)
- [UFW-Firewall installieren und steuern](../../../entwicklung/infrastruktur/ufw-firewall.md)
- [SSH-Tunnel: Portweiterleitung über SSH](../../../entwicklung/infrastruktur/ssh-tunnel.md)
- [Dokumentationsübersicht](../index.md)
