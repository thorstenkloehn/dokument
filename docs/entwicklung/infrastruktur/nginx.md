```
sudo nano /etc/nginx/conf.d/start.conf
```

```
                                                                                                                    
                                                                                                                     server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name doc.ahrensburg.city ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ahrensburg.city/privkey.pem;

   location /hot {
        proxy_pass http://localhost:9999/hot;
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
        # Hier verbinden wir Nginx mit dem Unix Socket
        proxy_pass         http://unix:/var/www/meincms.sock;
        proxy_http_version 1.1;
        proxy_set_header   Upgrade $http_upgrade;
        proxy_set_header   Connection keep-alive;
        proxy_set_header   Host $host;
        proxy_cache_bypass $http_upgrade;
        proxy_set_header   X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header   X-Forwarded-Proto $scheme;
    }

location /start {
    proxy_pass http://unix:/var/run/tomcat10/tomcat.sock;
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
}

}

server {
    listen 80;
    listen [::]:80;
    server_name ahrensburg.city;
    return 301 https://$host$request_uri;
}
```