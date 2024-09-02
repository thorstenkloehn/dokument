## Wordpress Installieren
### Voraussetzungen
```bash
sudo apt install software-properties-common
sudo add-apt-repository ppa:ondrej/php
sudo apt update
sudo apt install mysql-server nginx -y

sudo apt-get install php8.3 php8.3-fpm php8.3-mysql php8.3-xml php8.3-curl php8.3-gd php8.3-mbstring php8.3-xmlrpc php8.3-zip php8.3-intl -y
```
### Datenbank erstellen
```bash
sudo mysql -u root -p
CREATE DATABASE wordpress;
CREATE USER 'wordpress'@'localhost' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wordpress'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
### Wordpress installieren
```bash
cd /home/thorsten
sudo wget https://de.wordpress.org/latest.zip
sudo unzip latest.zip
sudo rm latest.zip

### Berechtigungen setzen
```bash
sudo chown -R www-data:www-data /home/thorsten/wordpress
sudo chmod -R 755 /home/thorsten/wordpress
```
### Nginx Konfiguration auf subdomain
```bash
sudo nano /etc/nginx/conf.d//wordpress
```
```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name blog.ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/blog.ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/blog.ahrensburg.city/privkey.pem;
    root /home/thorsten/wordpress;
    index index.php index.html index.htm;
    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
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



