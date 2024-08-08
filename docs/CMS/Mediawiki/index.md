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
sudo wget https://releases.wikimedia.org/mediawiki/1.39/mediawiki-1.39.8.zip
sudo unzip mediawiki-1.39.8.zip
sudo mv mediawiki-1.39.8 mediawiki
sudo chown -R www-data:www-data /var/www/mediawiki
sudo chmod -R 755 /var/www/mediawiki
sudo rm mediawiki-1.39.8.zip
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


