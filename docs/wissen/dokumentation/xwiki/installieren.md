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
## XWiki installieren
```bash
sudo apt-get install xwiki-tomcat10-pgsql
sudo systemctl stop tomcat10
```

## Port auf 9000 ändern

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

## Port auf localhost beschränken und Ersteinrichtung per SSH-Tunnel

Bevor Nginx als Reverse Proxy steht, wäre Port 9000 sonst öffentlich erreichbar — inklusive des unfertigen Distribution Wizards, der beim ersten Aufruf das Administratorkonto anlegt. Statt den Port dafür kurzzeitig in der Firewall freizugeben, wird der Connector direkt auf `localhost` beschränkt und die Ersteinrichtung über einen SSH-Tunnel erledigt.

Im selben `<Connector>`-Element zusätzlich das `address`-Attribut setzen:

```xml
<Connector address="127.0.0.1" port="9000" protocol="HTTP/1.1"
           connectionTimeout="20000"
           redirectPort="8443" />
```

Tomcat starten:

```bash
sudo systemctl start tomcat10
```

Auf dem eigenen Rechner den Port per Local Forwarding zum Server tunneln:

```bash
ssh -L 9000:127.0.0.1:9000 admin@SERVER-IP
```

Solange die SSH-Sitzung besteht, ist der Distribution Wizard im eigenen Browser unter `http://127.0.0.1:9000/xwiki` erreichbar — verschlüsselt über die SSH-Verbindung, ohne dass Port 9000 je öffentlich sichtbar war. Dort das erste Administratorkonto anlegen. Mehr zu Local Forwarding und weiteren Tunnel-Varianten: [SSH-Tunnel: Portweiterleitung über SSH](../../../entwicklung/infrastruktur/ssh-tunnel.md).

!!! note "Hinweis"
    Die `address="127.0.0.1"`-Bindung bleibt auch nach der Ersteinrichtung dauerhaft bestehen — Nginx läuft auf demselben Host und erreicht Tomcat ohnehin über `localhost` (siehe `proxy_pass` unten). Der Tunnel war nur das temporäre Zugangsmittel für die einmalige Kontoanlage, bevor Nginx als dauerhafter, öffentlicher Zugangsweg konfiguriert ist.

## Nginx Konfigration
  
Um Nginx als Reverse Proxy für XWiki zu konfigurieren, erstellen oder bearbeiten Sie eine Konfigurationsdatei, z.B. `/etc/nginx/conf.d/xwiki.conf`:

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name xwiki.wissen-ahrensburg.de;
    ssl_certificate /etc/letsencrypt/live/wissen-ahrensburg.de/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/wissen-ahrensburg.de/privkey.pem;

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

!!! tip "Tipp"
    Statt der TCP-Verbindung über `localhost:9000` lässt sich Nginx auch über einen Unix-Socket an Tomcat anbinden — siehe [Nginx über Unix-Socket anbinden](xwiki-nginx-unix-socket.md).

## Port 9000 in der Firewall sperren (UFW)

Die `address="127.0.0.1"`-Bindung von weiter oben schützt bereits auf Netzwerkebene. Als zweite, unabhängige Absicherungsebene sollte Port 9000 zusätzlich in der Firewall nie freigegeben werden — falls die Connector-Bindung später versehentlich wieder auf `0.0.0.0` gestellt wird:

```bash
sudo ufw allow "Nginx Full"
sudo ufw deny 9000/tcp
sudo ufw status verbose
```

Die explizite `deny`-Regel ist bei UFWs Standardrichtlinie (`default deny incoming`) zwar redundant, macht die Absicht aber in `ufw status` sichtbar und dokumentiert sie selbsterklärend. Details zu UFW: [UFW-Firewall installieren und steuern](../../../entwicklung/infrastruktur/ufw-firewall.md).

Für spätere administrative Zugriffe direkt auf Port 9000 (z. B. Fehlersuche ohne Nginx) eignet sich statt einer Portfreigabe weiterhin ein [SSH-Tunnel](../../../entwicklung/infrastruktur/ssh-tunnel.md).

---

## Verwandte Themen

- [Evolution und Architekturen von XWiki](evolution-digitaler-xwiki.md) — Architektur- und Versionsgeschichte dieser Installation
- [Installation über APT](installation-ueber-apt.md) — alternativer Installationsweg
