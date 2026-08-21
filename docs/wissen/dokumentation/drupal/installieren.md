# Drupal installieren: Composer, PostgreSQL und Nginx

Diese Anleitung richtet **Drupal** (aktuell 10.x/11.x) produktiv auf einem eigenen Server ein — per **Composer** (offizieller Installationsweg, kein apt-Paket), mit **PostgreSQL** als Datenbank und **Nginx** als Reverse Proxy über PHP-FPM. Sie folgt demselben Muster wie die [XWiki-](../xwiki/installieren.md) und [Wiki.js-Installation](../wikijs-linux-installation.md) in diesem Wiki.

!!! warning "Achtung"
    Die unterstützten PHP- und PostgreSQL-Versionen ändern sich mit jedem Drupal-Minor-Release. Vor einer Neuinstallation immer die aktuellen [Systemanforderungen](https://www.drupal.org/docs/system-requirements) prüfen. Diese Anleitung geht von **PHP 8.3** und **PostgreSQL 14+** aus.

---

## Voraussetzungen

- Ubuntu-Server mit `sudo`-Rechten
- eine eigene Domain/Subdomain, z. B. `drupal.wissen-ahrensburg.de`
- Nginx bereits mit SSL-Zertifikat eingerichtet (siehe [Nginx & SSL](../../../entwicklung/infrastruktur/nginx-ssl.md))

---

## 1. PHP und PostgreSQL-Treiber installieren

```bash
sudo apt update
sudo apt install -y php8.3-fpm php8.3-cli php8.3-pgsql php8.3-gd \
  php8.3-xml php8.3-mbstring php8.3-curl php8.3-zip php8.3-opcache \
  postgresql
```

`php8.3-pgsql` stellt den PDO-Treiber bereit, ohne den Drupal keine Verbindung zu PostgreSQL aufbauen kann. Composer wird bewusst **nicht** aus den apt-Quellen installiert (siehe nächster Schritt).

---

## 2. Composer installieren

Das Ubuntu-Paket `composer` hinkt neuen Composer-Releases oft deutlich hinterher und wird von der Drupal-Doku nicht empfohlen — stattdessen den offiziellen Installer direkt von getcomposer.org holen und vor der Ausführung per Prüfsumme verifizieren:

```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
EXPECTED_HASH="$(curl -sS https://composer.github.io/installer.sig)"
php -r "if (hash_file('sha384', 'composer-setup.php') === '$EXPECTED_HASH') { echo 'Installer verifiziert' . PHP_EOL; } else { echo 'Installer beschaedigt' . PHP_EOL; unlink('composer-setup.php'); exit(1); }"
sudo php composer-setup.php --install-dir=/usr/local/bin --filename=composer
php -r "unlink('composer-setup.php');"
```

Die erwartete SHA-384-Prüfsumme wird dabei live von `composer.github.io/installer.sig` bezogen statt fest in dieser Anleitung hinterlegt — Composer-Releases (und damit die Prüfsumme des Installer-Skripts) ändern sich regelmäßig, ein hartkodierter Hash wäre schon nach dem nächsten Release veraltet. `--install-dir`/`--filename` legen `composer.phar` direkt ausführbar als `/usr/local/bin/composer` ab, ein zusätzliches `sudo mv composer.phar /usr/local/bin/composer` entfällt damit.

```bash
composer --version
```

---

## 3. PostgreSQL-Datenbank anlegen

```bash
sudo -u postgres psql -c "CREATE ROLE drupal WITH LOGIN PASSWORD 'EIN_LANGES_ZUFAELLIGES_PASSWORT';"
sudo -u postgres psql -c "CREATE DATABASE drupal OWNER drupal ENCODING 'UTF8' TEMPLATE template0;"
```

!!! note "Hinweis"
    PostgreSQL lauscht per Default-Konfiguration (`postgresql.conf`, `listen_addresses = 'localhost'`) ohnehin nur lokal. Da Drupal über PHP-FPM auf demselben Host läuft, ist keine Netzwerkfreigabe für Port 5432 nötig — Zugriff läuft komplett über `localhost`.

---

## 4. Drupal per Composer installieren

```bash
cd /var/www
sudo composer create-project drupal/recommended-project drupal-projekt
cd drupal-projekt
sudo composer require drush/drush
sudo chown -R www-data:www-data /var/www/drupal-projekt
```

`drupal/recommended-project` ist das offizielle, von der Drupal Association gepflegte Composer-Template — es bringt Drupal Core samt sinnvoller Standard-Abhängigkeiten mit. `drush` ist die Kommandozeilen-Shell für Drupal und wird im nächsten Schritt für die headless-Installation gebraucht.

---

## 5. Site-Installation headless per Drush

Anders als bei XWiki oder Wiki.js braucht Drupal für die Ersteinrichtung **keinen SSH-Tunnel zu einem temporären Setup-Assistenten** — `drush site:install` erledigt die komplette Einrichtung nichtinteraktiv direkt auf der Kommandozeile:

```bash
cd /var/www/drupal-projekt
sudo -u www-data vendor/bin/drush site:install standard \
  --db-url=pgsql://drupal:EIN_LANGES_ZUFAELLIGES_PASSWORT@localhost/drupal \
  --site-name="Wissen Ahrensburg" \
  --account-name=admin \
  --account-pass=EIN_WEITERES_LANGES_PASSWORT \
  --yes
```

!!! tip "Tipp: Browser-Assistent als Alternative"
    Falls `drush` nicht zur Verfügung steht, lässt sich der grafische Installationsassistent genauso wie bei den anderen Wiki-Systemen in diesem Repository per [SSH-Tunnel](../../../entwicklung/infrastruktur/ssh-tunnel.md) absichern, statt ihn öffentlich zu exponieren:
    ```bash
    cd /var/www/drupal-projekt/web
    sudo -u www-data php -S 127.0.0.1:8888
    ```
    ```bash
    ssh -L 8888:127.0.0.1:8888 admin@SERVER-IP
    ```
    Der Assistent ist dann unter `http://127.0.0.1:8888` erreichbar, verschlüsselt über die SSH-Verbindung.

---

## 6. PHP-FPM-Pool

Der Standard-Pool von `php8.3-fpm` reicht für den Anfang aus und lauscht bereits über einen Unix-Socket:

```bash
grep "^listen" /etc/php/8.3/fpm/pool.d/www.conf
```

Erwartete Ausgabe: `listen = /run/php/php8.3-fpm.sock`. Für mehrere PHP-Anwendungen auf demselben Host empfiehlt sich stattdessen ein eigener Pool (z. B. `/etc/php/8.3/fpm/pool.d/drupal.conf` mit `listen = /run/php/php8.3-fpm-drupal.sock`), damit Drupal ressourcenseitig von anderen PHP-Diensten isoliert ist.

```bash
sudo systemctl restart php8.3-fpm
```

---

## 7. Nginx-Konfiguration

Erstellen oder bearbeiten Sie `/etc/nginx/conf.d/drupal.conf`:

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name drupal.wissen-ahrensburg.de;
    root /var/www/drupal-projekt/web;
    ssl_certificate /etc/letsencrypt/live/wissen-ahrensburg.de/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/wissen-ahrensburg.de/privkey.pem;

    location = /favicon.ico { log_not_found off; access_log off; }
    location = /robots.txt  { allow all; log_not_found off; access_log off; }

    location ~ ^/sites/.*/private/ { return 403; }
    location ~ ^/sites/[^/]+/files/.*\.php$ { deny all; }

    location / {
        try_files $uri /index.php?$query_string;
    }

    location @rewrite {
        rewrite ^ /index.php;
    }

    location ~ "\.php$|^/update\.php" {
        fastcgi_split_path_info ^(.+?\.php)(|/.*)$;
        try_files $fastcgi_script_name =404;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param QUERY_STRING $query_string;
        fastcgi_intercept_errors on;
        fastcgi_pass unix:/run/php/php8.3-fpm-drupal.sock;
    }

    location ~* "\.(js|css|gif|jpg|jpeg|png|svg|woff|woff2)$" {
        try_files $uri @rewrite;
        expires max;
        log_not_found off;
    }
}

server {
    listen 80;
    listen [::]:80;
    server_name drupal.wissen-ahrensburg.de;
    return 301 https://$host$request_uri;
}
```

```bash
sudo nginx -t
sudo systemctl reload nginx
```

`fastcgi_pass` verweist auf den in Schritt 6 eingerichteten dedizierten Pool-Socket — bei Nutzung des Standard-Pools stattdessen `unix:/run/php/php8.3-fpm.sock` verwenden.

---

## 8. Firewall (UFW)

```bash
sudo ufw allow "Nginx Full"
sudo ufw deny 5432/tcp
sudo ufw status verbose
```

PostgreSQL bindet zwar schon per Konfiguration nur an `localhost` (Schritt 3), die explizite `deny`-Regel dokumentiert diese Absicht aber zusätzlich sichtbar in `ufw status` — als zweite, unabhängige Absicherungsebene, falls `postgresql.conf` später versehentlich geändert wird. Details zu UFW: [UFW-Firewall installieren und steuern](../../../entwicklung/infrastruktur/ufw-firewall.md).

---

## Kurzprüfung

```bash
sudo systemctl is-active php8.3-fpm nginx postgresql
curl -I https://drupal.wissen-ahrensburg.de
```

Meldet der `curl`-Aufruf `HTTP/2 200`, ist die Installation erreichbar. Danach im Backend (`/user/login`) anmelden und unter **Berichte → Status des Systems** letzte Konfigurationshinweise prüfen (z. B. Cron-Einrichtung, Datei-Berechtigungen).

---

## Quellen und weiterführende Informationen

- [Drupal: Systemanforderungen](https://www.drupal.org/docs/system-requirements)
- [Drupal: Installation per Composer](https://www.drupal.org/docs/develop/using-composer/starting-a-site-using-composer)
- [Drush-Dokumentation](https://www.drush.org/)
- [Migration von MediaWiki, XWiki und Wiki.js nach Drupal](migration-wikisysteme.md)
- [UFW-Firewall installieren und steuern](../../../entwicklung/infrastruktur/ufw-firewall.md)
- [SSH-Tunnel: Portweiterleitung über SSH](../../../entwicklung/infrastruktur/ssh-tunnel.md)
- [Dokumentationsübersicht](../index.md)
