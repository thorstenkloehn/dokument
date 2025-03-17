## Ollama
Ollama ist ein Open-Source-Tool, das es ermöglicht, große Sprachmodelle (LLMs) lokal auf einem Computer auszuführen. Es ist eine Alternative zu Cloud-basierten LLMs wie GPT-3, die von Unternehmen wie OpenAI angeboten werden. Ollama ermöglicht es, LLMs auf einem Computer auszuführen, ohne dass eine Internetverbindung erforderlich ist. Dies bedeutet, dass Benutzer die volle Kontrolle über ihre Daten haben und keine Bedenken hinsichtlich Datenschutz und Sicherheit haben müssen.
### Installation
Geben Sie den folgenden Befehl in die Konsole ein, um Ollama zu installieren:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```
Geben Sie den folgenden Befehl ein, um Ollama zu starten Laden Sie das Modell herunter:
```bash
ollama pull llama3.2:latest
```
### open-webui 
open-webui ist ein Tool, das es ermöglicht, die Benutzeroberfläche von Ollama im Webbrowser zu öffnen. 
Geben Sie den folgenden Befehl in die Konsole ein,
```bash
mkdir /testseite
cd /testseite
python3 -m venv .venv
source .venv/bin/activate
pip install open-webui
```
Geben Sie den folgenden Befehl ein, um die Benutzeroberfläche von Ollama im Webbrowser zu öffnen:
```bash
/testseite/.venv/bin/open-webui serve
str + c Programm beenden
```
### systemctl Datei erstellen
Erstellen Sie eine Datei mit dem Namen ollama.service in /etc/systemd/system/ mit dem folgenden Inhalt:
```bash

sudo nano /etc/systemd/system/open-webui.service
```
Fügen Sie den folgenden Inhalt in die Datei ein:
```bash
[Unit]
Description=Open WebUI
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/testseite
ExecStart=/testseite/.venv/bin/open-webui serve
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
Geben Sie den folgenden Befehl ein, um den Dienst zu starten:
```bash
systemctl start open-webui
```
Geben Sie den folgenden Befehl ein, um den Dienst zu aktivieren:
```bash
systemctl enable open-webui
```
Geben Sie den folgenden Befehl ein, um den Status des Dienstes zu überprüfen:
```bash
systemctl status open-webui
```
### Certbot
Geben Sie den folgenden Befehl in die Konsole ein, um Certbot zu installieren:
```bash
sudo systemctl stop nginx
sudo certbot certonly --standalone -d ai.ahrensburg.city
```
### nginx Konfiguration
Erstellen Sie eine Konfigurationsdatei mit dem Namen ollama in /etc/nginx/sites-available/ mit dem folgenden Inhalt:
```bash
sudo nano /etc/nginx/conf.d/ollama.conf
```
Fügen Sie den folgenden Inhalt in die Datei ein:
```bash
server {
   listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name ai.ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/ai.ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ai.ahrensburg.city/privkey.pem;
    location / {
        proxy_pass http://localhost:8080;
        proxy_set_header Connection $http_connection;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}
```
Geben Sie den folgenden Befehl ein, um den nginx-Dienst neu zu starten:
```bash
sudo systemctl restart nginx
```



