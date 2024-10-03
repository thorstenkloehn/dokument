## ginx einstellung
```
sudo nano /etc/nginx/conf.d/start.conf
```
```nginx
  GNU nano 7.2                                                                           start.conf                                                                                     
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ahrensburg.city/privkey.pem;
     root /var/www/mediawiki;
    index index.php index.html index.htm;
   location /Bilder {
        proxy_pass http://localhost:8081/Bilder;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

location /karte {
    alias /var/www/karte;
    autoindex on;
}
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
