## Drupal Installieren

#### Postgres Datenbank erstellen
```
sudo -u postgres -i
createdb -E UTF8 -O thorsten drupal
psql
\c drupal
CREATE EXTENSION pg_trgm;
\q
exit
```

### PHP installieren
```
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
sudo apt install php8.3 php8.3-fpm php8.3-pgsql php8.3-xml php8.3-curl php8.3-gd php8.3-mbstring php8.3-xmlrpc php8.3-xmlrpc php8.3-zip php8.3-intl -y
```
## Drupal herunderladen
```
cd $HOME
composer create-project drupal/recommended-project:11.0.1 drupal
sudo chown -R www-data:www-data /home/thorsten/drupal/web
sudo chmod -R 755 /home/thorsten/drupal/web

```

## Nginx Konfiguration

```
sudo systemctl stop nginx
sudo certbot certonly --standalone -d drupal.ahrensburg.city
sudo nano /etc/nginx/conf.d/drupal.conf
```

```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name drupal.ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/drupal.ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/drupal.ahrensburg.city/privkey.pem;
    root /home/thorsten/drupal/web;
    index index.php index.html index.htm;
    location / {
        try_files $uri $uri/ /index.php?$args;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
    }
}
server {
    listen 80;
    listen [::]:80;
    server_name drupal.ahrensburg.city;
    return 301 https://$host$request_uri;
}
```

```

```