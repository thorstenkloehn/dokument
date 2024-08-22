## Ubuntu Server 20.04
Tomcat 9 ist in den Standard-Repositorys von Ubuntu 20.04 enthalten. Sie können es einfach installieren, indem Sie den folgenden Befehl ausführen:
```bash
sudo apt update
sudo apt upgrade
sudo apt install tomcat9
```
## nginx als Reverse Proxy für Tomcat 9 einrichten
```bash
sudo apt install nginx
```
```bash
sudo systemctl stop nginx
sudo certbot certonly --standalone -d geoserver.ahrensburg.city
```
```bash
sudo nano /etc/nginx/conf.d/tomcat.conf
```
```bash
 server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name geoserver.ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/geoserver.ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/geoserver.ahrensburg.city/privkey.pem;

    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

server {
    listen 80;
    listen [::]:80;
    server_name geoserver.ahrensburg.city;
    return 301 https://$host$request_uri;
}


```
`