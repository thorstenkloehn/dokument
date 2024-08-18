## MediaWiki auf einem Ubuntu 20.04 Nginx-Server installieren

```
sudo apt update -y
sudo apt upgrade -y
sudo apt install nginx -y
sudo apt install mysql-server -y
sudo mysql_secure_installation
sudo mysql -u root -p
CREATE DATABASE mediawiki;
CREATE USER 'mwuser'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON mediawiki.* TO 'mwuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;

sudo apt install php-fpm php-mysql php-xml php-curl php-gd php-mbstring php-xmlrpc php-xmlrpc php-zip -y
cd /var/www
git clone https://gerrit.wikimedia.org/r/mediawiki/core.git mediawiki
cd mediawiki
git tag -l | sort -V
git checkout REL1_35
cd mediawiki
git submodule update --init --recursive

```
## Nginx Konfiguration

```
sudo nano /etc/nginx/conf.d/mediawiki.conf
```

```

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name wiki.ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/blog.ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/blog.ahrensburg.city/privkey.pem;
    root /var/www/mediawiki;

    index index.php;

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
    server_name blog.ahrensburg.city;
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
fLoadExtension( 'CookieWarning' );
wfLoadExtension( 'SemanticMediaWiki' );
enableSemantics( 'wiki.ahrensburg.city' );
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
## Composer installieren
```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === 'dac665fdc30fdd8ec78b38b9800061b4150413ff2e3b6f88543c636f7cd84f6db9189d43a81e5503cda447da73c7e5b6') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"

sudo mv composer.phar /usr/local/bin/composer
```

## composer.local.json

## Weblinks
* [Git clone](https://www.mediawiki.org/wiki/Download_from_Git)