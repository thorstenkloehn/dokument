## Wordpress Installieren

Wordpress ist ein Content Management System (CMS) und Blogging-Tool, das auf PHP und MySQL basiert. Es ist kostenlos und Open Source und bietet eine Vielzahl von Funktionen, einschließlich eines Plug-in-Architektur und eines Themas, die es den Benutzern ermöglichen, Websites zu erstellen und zu verwalten.

### Installieren von Wordpress auf einem Ubuntu 20.04-Server

#### System aktualisieren

Bevor Sie beginnen, müssen Sie sicherstellen, dass Ihr System auf dem neuesten Stand ist. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
sudo apt update -y
sudo apt upgrade -y
```
#### nginx installieren

Als nächstes müssen Sie Nginx installieren, um Ihre Wordpress-Website zu hosten. Sie können Nginx installieren, indem Sie das folgende Kommando ausführen:

```bash 
sudo apt install nginx -y
``` 
### Mysql installieren
```
sudo apt install mysql-server -y
sudo mysql_secure_installation
```
#### Datenbank und Benutzer erstellen

Nach der Installation von MySQL müssen Sie eine Datenbank und einen Benutzer für Wordpress erstellen. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
sudo mysql -u root -p
CREATE DATABASE wordpress;
CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
### PHP installieren

Als nächstes müssen Sie PHP und einige PHP-Erweiterungen installieren, die von Wordpress benötigt werden. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
sudo apt install php-fpm php-mysql php-xml php-curl php-gd php-mbstring php-xmlrpc php-xmlrpc php-zip -y
```
### Wordpress herunterladen

Als nächstes müssen Sie Wordpress herunterladen und in Ihrem Webroot-Verzeichnis extrahieren. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
cd /var/www/html
sudo wget https://de.wordpress.org/latest-de_DE.tar.gz
sudo tar -xvzf latest-de_DE.tar.gz
sudo mv wordpress/* .
sudo rm -rf wordpress latest-de_DE.tar.gz
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
```
### Nginx-Konfiguration

Als nächstes müssen Sie eine Nginx-Konfigurationsdatei für Ihre Wordpress-Website erstellen. Sie können dies tun, indem Sie das folgende Kommando ausführen:
sudo nano /etc/nginx/conf.d/blog.conf
```bash


```
Fügen Sie den folgenden Inhalt hinzu:

```nginx

server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name blog.ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/blog.ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/blog.ahrensburg.city/privkey.pem;
    root /var/www/html;

    index index.php index.html index.htm;

    location / {
        try_files $uri $uri/ /index.php?$args;
    }

    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php7.4-fpm.sock;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        include fastcgi_params;
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
## Local Wordpress Installieren

Wordpress ist ein Content Management System (CMS) und Blogging-Tool, das auf PHP und MySQL basiert. Es ist kostenlos und Open Source und bietet eine Vielzahl von Funktionen, einschließlich eines Plug-in-Architektur und eines Themas, die es den Benutzern ermöglichen, Websites zu erstellen und zu verwalten.


### System aktualisieren

Bevor Sie beginnen, müssen Sie sicherstellen, dass Ihr System auf dem neuesten Stand ist. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
sudo apt update -y
sudo apt upgrade -y
```

### Mysql installieren
```
sudo apt install mysql-server -y
sudo mysql_secure_installation
```
#### Datenbank und Benutzer erstellen

Nach der Installation von MySQL müssen Sie eine Datenbank und einen Benutzer für Wordpress erstellen. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
sudo mysql -u root -p
CREATE DATABASE wordpress;
CREATE USER 'wpuser'@'localhost' IDENTIFIED BY 'secure_password';
GRANT ALL PRIVILEGES ON wordpress.* TO 'wpuser'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```
### PHP installieren

Als nächstes müssen Sie PHP und einige PHP-Erweiterungen installieren, die von Wordpress benötigt werden. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
sudo apt install php-fpm php-mysql php-xml php-curl php-gd php-mbstring php-xmlrpc php-xmlrpc php-zip -y
```
### Wordpress herunterladen
```
cd /var/www/html
sudo wget https://de.wordpress.org/latest-de_DE.tar.gz
sudo tar -xvzf latest-de_DE.tar.gz
sudo mv wordpress/* .
sudo rm -rf wordpress latest-de_DE.tar.gz
sudo chown -R www-data:www-data /var/www/html
sudo chmod -R 755 /var/www/html
sudo rm /etc/nginx/sites-enabled/default
```
## Wordpress Nginx Lokale Rechner
sudo nano /etc/nginx/conf.d/blog.conf
```
server {
    listen 80;
    server_name example.com;  # Ersetzen Sie 'example.com' durch Ihre Domain
    root /var/www/html;       # Pfad zu Ihrer WordPress-Installation

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

    # Zusätzliche Konfiguration für Multisite
    location /files/ {
        access_log off;
        log_not_found off;
        expires max;
    }

    location ^~ /blogs.dir/ {
        internal;
        alias /var/www/html/wp-content/blogs.dir/;
        access_log off;
        log_not_found off;
        expires max;
    }
}
```