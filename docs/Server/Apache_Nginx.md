## Apache auf Port 8080 betreiben (statt 80)

Diese Anleitung beschreibt, wie der Apache-Webserver auf Port 8080 statt dem Standard-Port 80 betrieben wird. Dies ist z.B. sinnvoll, wenn ein anderer Dienst (wie Nginx oder ein Reverse Proxy) Port 80 belegt oder Sie Apache absichern möchten.
### Schritt 1: Apache-Port ändern

Öffne die Datei `/etc/apache2/ports.conf`:

```bash
sudo nano /etc/apache2/ports.conf
```
Füge (oder ändere) folgende Zeile:

```
Listen 8080
```

#### Für Ubuntu 20.04: VHost anpassen
Öffne die Datei `/etc/apache2/sites-available/000-default.conf` und passe den VirtualHost an:

```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```
Ändere die Zeile zu:

```
<VirtualHost *:8080>
```

#### Für Ubuntu 22.04/24.04 und neuer
Meist reicht es, nur die `ports.conf` zu ändern. Prüfe aber, ob in den VHost-Dateien noch explizit auf Port 80 verwiesen wird.
### Schritt 2: Apache neu starten

```bash
sudo systemctl restart apache2
```

### Schritt 3: Firewall anpassen (falls aktiv)
Erlaube Port 8080:

```bash
sudo ufw allow 8080/tcp
```

### Hinweise
- Nach der Umstellung ist Apache unter http://<server-ip>:8080 erreichbar.
- Prüfe, ob andere Dienste Port 80 nutzen (z.B. Nginx, Certbot, etc.).

---

## Nginx als Reverse Proxy vor Apache (optional)
Wenn du möchtest, dass Anfragen an Port 80 (und ggf. 443) von Nginx entgegengenommen und an Apache auf Port 8080 weitergeleitet werden, kannst du Nginx als Reverse Proxy konfigurieren:

### Beispiel-Konfiguration für `/etc/nginx/sites-available/default`:

```nginx
server {
	listen 80;
	server_name _;

	location / {
		proxy_pass http://127.0.0.1:8080;
		proxy_set_header Host $host;
		proxy_set_header X-Real-IP $remote_addr;
		proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
		proxy_set_header X-Forwarded-Proto $scheme;
	}
}
```
Danach Nginx neu starten:

```bash
sudo systemctl restart nginx
```

---

## SSL mit Let's Encrypt (Certbot)
Wenn du HTTPS nutzen möchtest, kannst du Certbot verwenden. Beispiel für Nginx:

```bash
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo certbot --nginx
```
Folge den Anweisungen, um ein Zertifikat zu erhalten.

---

## Fehlerbehebung
- Prüfe mit `sudo netstat -tulpen | grep 80`, ob Port 80 noch von einem anderen Dienst belegt ist.
- Apache-Logs findest du unter `/var/log/apache2/`.
- Nginx-Logs unter `/var/log/nginx/`.
## Kachelserver mit Apache-Server Port 80 auf 8080 umleiten
### Mit Ubuntu 20.04 LTS
Geben Sie den folgenden Befehl ein, um den Apache-Server zu installieren:
```bash
sudo nano /etc/apache2/ports.conf
```
Fügen Sie die folgende Zeile hinzu, um den Port 80 auf den Port 8080 umzuleiten:
```bash
Listen 8080
```
Speichern Sie die Datei.

Geben Sie den folgenden Befehl ein, um den Apache-Server zu installieren:
```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```
Fügen Sie die folgende Zeile hinzu, um den Port 80 auf den Port 8080 umzuleiten:
```bash
<VirtualHost *:8080>
```
Speichern Sie die Datei.

Geben Sie den folgenden Befehl ein, um den Apache-Server zu installieren:
```bash
sudo systemctl restart apache2
```
Der Apache-Server leitet jetzt den Port 80 auf den Port 8080 um.

### Mit Ubuntu 22.04 LTS oder höher

Brauchen Sie nicht /etc/apache2/sites-available/000-default.conf ändern, nur /etc/apache2/ports.conf ändern.
Geben Sie den folgenden Befehl ein, um den Apache-Server zu installieren:



```bash
sudo nano /etc/apache2/ports.conf
```


Fügen Sie die folgende Zeile hinzu, um den Port 80 auf den Port 8080 umzuleiten:

```bash
Listen 8080
```


Speichern Sie die Datei.

Geben Sie den folgenden Befehl ein, um den Apache-Server zu installieren:

```bash
sudo systemctl restart apache2
```

