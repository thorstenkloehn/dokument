## Postgres Datenbank erstellen
```bash
sudo -u postgres -i
createdb -E UTF8 -O thorsten mediawiki
exit
```
## PHP installieren
```bash
sudo apt install php-fpm php-pgsql php-xml php-curl php-gd php-mbstring php-xmlrpc php-xmlrpc php-zip php-int -y
```

## Composer installieren
```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === 'dac665fdc30fdd8ec78b38b9800061b4150413ff2e3b6f88543c636f7cd84f6db9189d43a81e5503cda447da73c7e5b6') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"

sudo mv composer.phar /usr/local/bin/composer
```


## Mediawiki installieren
```bash
git clone https://gerrit.wikimedia.org/r/mediawiki/core.git mediawiki
cd mediawiki
git tag -l | sort -V
git checkout 1.39.8
git submodule update --init --recursive
sudo chown -R www-data:www-data /home/thorsten/mediawiki
sudo chmod -R 755 /home/thorsten/mediawiki

```
## Nginx Konfiguration

```
sudo nano /etc/nginx/conf.d/mediawiki.conf
```

```

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ahrensburg.city/privkey.pem;
    root /home/thorsten/mediawiki;
    index index.php index.html index.htm;
    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
    }

    location ~ /\.ht {

           deny all;
    }
}
server {
    listen 80;
    listen [::]:80;
    server_name ahrensburg.city;
    return 301 https://$host$request_uri;
}
```

## Lesbare URLs konfiguriern in mediawiki
```bash
sudo nano /var/www/mediawiki/LocalSettings.php
```

```php
$wgScriptPath = "";
$wgArticlePath = "/$1";
$wgUsePathInfo = true;

```
## mediawiki extensions installieren
```bash
sudo nano /var/www/mediawiki/LocalSettings.php
```
```php
wfLoadExtension( 'CookieWarning' );
wfLoadExtension( 'SemanticMediaWiki' );
enableSemantics( 'ahrensburg.city' );
wfLoadExtension( 'WikiMarkdown' );
wfLoadExtension( 'SimpleBlogPage' );
wfLoadExtension( 'Gadgets' );
$wgCookieWarningEnabled=true;
$wgCookieWarningMoreUrl='';
$wgCookieWarningGeoIPServiceURL='';
$wgCookieWarningGeoIPLookup='none';
$wgCookieWarningForCountryCodes="EU";
$wgGroupPermissions['user']['move'] = false;
wfLoadExtension( 'Maps' );
$egMapsDefaultService = 'leaflet';
```


## composer.local.json
```json 
{
    "require": {
        "mediawiki/semantic-media-wiki": "~4.0"
    },
    "extra": {
        "merge-plugin": {
            "include": [
                "extensions/*/composer.json",
                "skins/*/composer.json",
                "extensions/WikiMarkdown/composer.json"
            ]
        }
    }
}
```


## Weblinks
* [Git clone](https://www.mediawiki.org/wiki/Download_from_Git)