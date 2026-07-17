APT-Konfiguration  
Zuerst müssen Sie Ihren Paketmanager so konfigurieren, dass er das XWiki-Repository verwendet. Dies können Sie einfach mit den folgenden Befehlen tun:

```bash
sudo wget https://maven.xwiki.org/xwiki-keyring.gpg -O /usr/share/keyrings/xwiki-keyring.gpg
sudo wget "https://maven.xwiki.org/stable/xwiki-stable.list" -O /etc/apt/sources.list.d/xwiki-stable.list
```

**Information**  
Beachten Sie, dass es mehrere Repositories gibt, aus denen Sie wählen können (als Alternative zum oben genannten Stable-Repository):

- `https://maven.xwiki.org/releases/xwiki-releases.list`: Alle veröffentlichten Versionen, einschließlich Meilensteine und Release Candidates (instabil).
- `https://maven.xwiki.org/stable/xwiki-stable.list`: Alle veröffentlichten Versionen, ohne Meilensteine und Release Candidates (stabil).
- `https://maven.xwiki.org/lts/xwiki-lts.list`: Alle veröffentlichten Cycle-LTS-Versionen.
- `https://maven.xwiki.org/lts/xwiki-lts-latest.list`: Neueste LTS-Versionen (kann Cycle-LTS oder Intermediate-LTS sein, wenn diese höher sind).

Weitere Informationen zu den verschiedenen unterstützten Zweigen finden Sie auf der Support-Seite.

## Aktualisierung
```bash
sudo apt-get update
```

## Suchen nach XWiki-Versionen
```bash
apt-cache search xwiki
```
## XWiki mit Tomcat 10 installieren
```bash
sudo apt-get install xwiki-tomcat10-pgsql
sudo systemctl stop tomcat10
```

## Tomcat-10-Port auf 9000 ändern

```
sudo nano /etc/tomcat10/server.xml
```
Suchen Sie in der Datei `server.xml` nach dem folgenden Abschnitt:

```xml
<Connector port="8080" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443" />
```

Ändern Sie den Wert des `port`-Attributs von `8080` auf `9000`:

```xml
<Connector port="9000" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443" />
```

Speichern Sie die Datei und schließen Sie den Editor.

## Nginx Konfigration
  
Um Nginx als Reverse Proxy für XWiki zu konfigurieren, erstellen oder bearbeiten Sie eine Konfigurationsdatei, z.B. `/etc/nginx/conf.d/xwiki.conf`:

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name www.ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ahrensburg.city/privkey.pem;

    location / {
        proxy_pass http://localhost:9000/;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```

Aktivieren Sie die Konfiguration und starten Sie Nginx neu:

```bash

sudo nginx -t
sudo systemctl reload nginx
```

Passen Sie `server_name` an Ihre Domain an.




