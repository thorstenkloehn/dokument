# MediaWiki auf dem Entwicklungsrechner: localhost mit Nginx und PostgreSQL

Diese Anleitung richtet **MediaWiki** rein lokal auf einem Entwicklungsrechner ein — erreichbar nur über `localhost`, ohne eigene Domain und ohne SSL-Zertifikat. Als Datenbank kommt **PostgreSQL** zum Einsatz, als Webserver **Nginx** über PHP-FPM. Sie folgt demselben Muster wie die [Moodle-Installation](../moodle/installieren.md) in diesem Wiki, ist aber bewusst auf einen lokalen Entwicklungsrechner statt einen produktiven Server zugeschnitten.

!!! warning "Achtung"
    Die unterstützten PHP- und PostgreSQL-Versionen ändern sich mit jedem MediaWiki-Release. Vor einer Installation immer die aktuelle [Kompatibilitätsmatrix](https://www.mediawiki.org/wiki/Compatibility) prüfen. Diese Anleitung geht von **PHP 8.3** und **PostgreSQL 14+** aus.

---

## Voraussetzungen

- Ubuntu-Entwicklungsrechner mit `sudo`-Rechten
- Kein DNS-Eintrag und kein SSL-Zertifikat nötig — die Installation ist ausschließlich über `http://localhost` erreichbar
- `git` zum Auschecken des MediaWiki-Cores

---

## 1. PHP, Erweiterungen, PostgreSQL und Nginx installieren

```bash
sudo apt update
sudo apt install -y php8.3-fpm php8.3-cli php8.3-pgsql php8.3-xml \
  php8.3-mbstring php8.3-curl php8.3-gd php8.3-intl php8.3-apcu \
  php8.3-opcache git nginx postgresql
```

`php8.3-pgsql` stellt den PDO-Treiber bereit, ohne den MediaWiki keine Verbindung zu PostgreSQL aufbauen kann. `php8.3-intl` wird für korrekte Sprach- und Sortierregeln benötigt, `php8.3-apcu` als lokaler Objekt-Cache empfohlen (spart auf dem Entwicklungsrechner einen zusätzlichen Memcached/Redis-Dienst).

---

## 2. PostgreSQL-Datenbank anlegen

```bash
sudo -u postgres psql -c "CREATE ROLE mediawiki WITH LOGIN PASSWORD 'EIN_LANGES_ZUFAELLIGES_PASSWORT';"
sudo -u postgres psql -c "CREATE DATABASE mediawiki OWNER mediawiki ENCODING 'UTF8' TEMPLATE template0;"
```

!!! note "Hinweis"
    PostgreSQL lauscht per Default-Konfiguration (`postgresql.conf`, `listen_addresses = 'localhost'`) ohnehin nur lokal. Da MediaWiki über PHP-FPM auf demselben Rechner läuft, ist keine Netzwerkfreigabe für Port 5432 nötig — auf einem reinen Entwicklungsrechner kann diese Vorgabe unverändert bleiben.

---

## 3. MediaWiki-Core per Git klonen

Für MediaWiki gibt es kein apt-Paket — der offizielle Weg ist ein Git-Checkout des Core-Repositorys samt Submodulen (Skins, Standard-Erweiterungen):

```bash
cd /var/www
sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git mediawiki
cd mediawiki
git tag -l | sort -V | tail -5
sudo git checkout tags/1.43.0 -b lokal-1.43
sudo git submodule update --init --recursive
sudo chown -R www-data:www-data /var/www/mediawiki
```

Der `git tag`-Aufruf listet die verfügbaren Releases sortiert nach Version — daraus das aktuell unterstützte Release wählen (siehe Warnhinweis oben) und statt `1.43.0` einsetzen.

---

## 4. PHP-FPM-Pool

Auf einem Entwicklungsrechner reicht der Standard-Pool aus:

```bash
grep "^listen" /etc/php/8.3/fpm/pool.d/www.conf
```

Erwartete Ausgabe: `listen = /run/php/php8.3-fpm.sock`. Für Fehlersuche während der Entwicklung empfiehlt sich zusätzlich, Fehleranzeige und Logging im Pool zu aktivieren statt sie nur in `LocalSettings.php` zu setzen:

```ini title="/etc/php/8.3/fpm/pool.d/www.conf (Auszug)"
php_admin_value[display_errors] = On
php_admin_value[error_reporting] = E_ALL
```

```bash
sudo systemctl restart php8.3-fpm
```

---

## 5. Nginx-Konfiguration für localhost

MediaWiki routet Seitenaufrufe intern über den Parameter `title` statt über echte Dateipfade — die Rewrite-Regel unterscheidet sich deshalb von einem einfachen `try_files … /index.php?$args` wie bei Drupal oder Moodle:

```bash
sudo nano /etc/nginx/sites-available/mediawiki-localhost
```

```nginx title="/etc/nginx/sites-available/mediawiki-localhost"
server {
    listen 80;
    listen [::]:80;
    server_name localhost;
    root /var/www/mediawiki;
    index index.php;

    location / {
        try_files $uri $uri/ @rewrite;
    }

    location @rewrite {
        rewrite ^/(.*)$ /index.php?title=$1&$args;
    }

    location ~ \.php$ {
        fastcgi_split_path_info ^(.+\.php)(/.*)$;
        fastcgi_pass unix:/run/php/php8.3-fpm.sock;
        fastcgi_index index.php;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param PATH_INFO $fastcgi_path_info;
    }

    location ~ /\.ht {
        deny all;
    }

    location ~* \.(js|css|gif|jpg|jpeg|png|svg|woff|woff2)$ {
        expires max;
        log_not_found off;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/mediawiki-localhost /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl reload nginx
```

Kein zweiter `server`-Block für Port 443/SSL — auf dem Entwicklungsrechner wird ausschließlich über `http://localhost` zugegriffen, ein Redirect auf HTTPS entfällt.

---

## 6. Installationsassistent im Browser aufrufen

Weil Nginx bereits lokal auf `localhost` lauscht, ist kein SSH-Tunnel wie bei einem entfernten Server nötig (vergleiche [SSH-Tunnel](../../../entwicklung/infrastruktur/ssh-tunnel.md)) — der Assistent ist direkt erreichbar:

```
http://localhost/mw-config/index.php
```

Im Assistenten:

- **Datenbanktyp**: PostgreSQL
- **Datenbankserver**: `localhost`
- **Datenbankname**: `mediawiki`
- **Benutzer/Passwort**: `mediawiki` / das in Schritt 2 vergebene Passwort
- **Wiki-Name**, Admin-Konto und gewünschte Erweiterungen nach Bedarf auswählen

Am Ende der Installation die generierte `LocalSettings.php` herunterladen und ins Webroot legen:

```bash
sudo mv ~/Downloads/LocalSettings.php /var/www/mediawiki/LocalSettings.php
sudo chown www-data:www-data /var/www/mediawiki/LocalSettings.php
sudo chmod 640 /var/www/mediawiki/LocalSettings.php
```

---

## 7. Lesbare URLs und Entwicklungseinstellungen

```bash
sudo nano /var/www/mediawiki/LocalSettings.php
```

```php title="LocalSettings.php (Ergänzungen)"
$wgServer = "http://localhost";
$wgScriptPath = "";
$wgArticlePath = "/$1";
$wgUsePathInfo = true;

# Nur auf dem Entwicklungsrechner aktivieren, niemals auf einem produktiven Server:
$wgShowExceptionDetails = true;
$wgDevelopmentWarnings = true;
$wgShowDBErrorBacktrace = true;
```

!!! warning "Achtung"
    `$wgShowExceptionDetails`, `$wgDevelopmentWarnings` und `$wgShowDBErrorBacktrace` legen interne Fehlerdetails (Stacktraces, Datenbank-Queries) offen — praktisch beim Debuggen auf dem Entwicklungsrechner, aber ein Sicherheitsrisiko auf einem öffentlich erreichbaren Server. Beim späteren Übertragen auf einen produktiven Server (z. B. per `rsync`) diese drei Zeilen entfernen oder auf `false` setzen.

Nach jeder Änderung an `LocalSettings.php` oder installierten Erweiterungen die Wartungsskripte laufen lassen:

```bash
cd /var/www/mediawiki
sudo -u www-data php maintenance/run.php update
sudo -u www-data php maintenance/run.php rebuildLocalisationCache
```

---

## Kurzprüfung

```bash
sudo systemctl is-active php8.3-fpm nginx postgresql
curl -I http://localhost
```

Meldet der `curl`-Aufruf `HTTP/1.1 200 OK`, ist die lokale Installation erreichbar. Danach im Browser unter `http://localhost/wiki/Spezial:Version` prüfen, ob PHP-Version, installierte Erweiterungen und die PostgreSQL-Verbindung korrekt erkannt werden.

---

## Quellen und weiterführende Informationen

- [MediaWiki: Kompatibilitätsmatrix](https://www.mediawiki.org/wiki/Compatibility)
- [MediaWiki: Installation Guide](https://www.mediawiki.org/wiki/Manual:Installation_guide)
- [MediaWiki: Nginx-Konfiguration](https://www.mediawiki.org/wiki/Manual:Running_MediaWiki_on_Nginx)
- [MediaWiki: PostgreSQL](https://www.mediawiki.org/wiki/Manual:PostgreSQL)
- [Moodle installieren: Git, PostgreSQL und Nginx](../moodle/installieren.md)
- [SSH-Tunnel: Portweiterleitung über SSH](../../../entwicklung/infrastruktur/ssh-tunnel.md)
- [Dokumentationsübersicht](../index.md)
