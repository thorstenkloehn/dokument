## Nginx mit SSL-Zertifikat einrichten auf Ubuntu 20.04 LTS oder höher

```bash
sudo apt install snapd
sudo apt-get install nginx
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl stop nginx
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo systemctl stop nginx
sudo certbot certonly --manual --preferred-challenges dns \
  -d *.wissen-ahrensburg.de -d wissen-ahrensburg.de
```
<!--
    Dokumentation: Dieses Dokument beschreibt, wie eine TXT-Domain für SSL-Zertifikate (z.B. Let's Encrypt) eingerichtet wird. Es enthält eine Schritt-für-Schritt-Anleitung zur Konfiguration eines TXT-Records im DNS, um die Domain-Verifizierung für SSL-Zertifikate mit Nginx zu ermöglichen. Die Anleitung richtet sich an Administratoren, die ihre Server mit SSL absichern möchten.
-->
### DNS TXT-Record für Domain-Verifizierung anlegen

1. **Melden Sie sich bei Ihrem DNS-Provider an.**
    Öffnen Sie die Verwaltungsoberfläche für Ihre Domain (z.B. bei Ihrem Hoster oder Domain-Registrar).

2. **Navigieren Sie zum Bereich für DNS-Einstellungen.**
    Suchen Sie nach der Möglichkeit, DNS-Records zu bearbeiten oder hinzuzufügen.

3. **Fügen Sie einen neuen TXT-Record hinzu:**
    - **Name/Host:** Geben Sie den von Certbot angezeigten Wert ein (z.B. `_acme-challenge` oder `_acme-challenge.wissen-ahrensburg.de`).
    - **Typ:** Wählen Sie `TXT`.
    - **Wert:** Kopieren Sie den von Certbot bereitgestellten Schlüssel (eine zufällige Zeichenkette).

4. **Speichern Sie den neuen TXT-Record.**
    Die Änderung kann einige Minuten bis zu mehreren Stunden dauern, bis sie weltweit wirksam ist.

5. **Fahren Sie mit Certbot fort, sobald der Record aktiv ist.**
    Sie können die Ausbreitung des TXT-Records mit Tools wie [dig](https://toolbox.googleapps.com/apps/dig/) oder [whatsmydns.net](https://www.whatsmydns.net/) überprüfen.

**Beispiel für einen TXT-Record:**
| Name/Host                       | Typ | Wert                        |
|----------------------------------|-----|-----------------------------|
| _acme-challenge.wissen-ahrensburg.de  | TXT | `xxxxxxxxxxxxxxxxxxxxxxxx`   |

**Hinweis:** Jeder Zertifikatsantrag erzeugt einen neuen Wert für den TXT-Record. Wiederholen Sie die Schritte bei jeder neuen Verifizierung.

Nach erfolgreicher Verifizierung meldet Certbot die Ablage der Zertifikatsdateien, z. B.:

```text
Certificate is saved at: /etc/letsencrypt/live/wissen-ahrensburg.de/fullchain.pem
Key is saved at:         /etc/letsencrypt/live/wissen-ahrensburg.de/privkey.pem
```

`fullchain.pem` enthält das Server-Zertifikat samt Zwischenzertifikaten, `privkey.pem` den privaten Schlüssel. Beide Pfade bleiben bei einer Zertifikatserneuerung stabil (Certbot überschreibt die Dateien, der Symlink-Pfad unter `/etc/letsencrypt/live/…` ändert sich nicht) und werden direkt in der Nginx-Server-Konfiguration referenziert.

### Zertifikat in der Server-Konfiguration einbinden

```nginx
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name dienst.wissen-ahrensburg.de;
    ssl_certificate /etc/letsencrypt/live/wissen-ahrensburg.de/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/wissen-ahrensburg.de/privkey.pem;

    # eigentliche Backend-Anbindung (proxy_pass, fastcgi_pass, root, …)
}

# HTTP auf HTTPS umleiten
server {
    listen 80;
    listen [::]:80;
    server_name dienst.wissen-ahrensburg.de;
    return 301 https://$host$request_uri;
}
```

```bash
sudo nginx -t
sudo systemctl reload nginx
```

!!! warning "Jeder Dienst braucht einen eigenen `server_name`"
    Der Zertifikatspfad (`/etc/letsencrypt/live/wissen-ahrensburg.de/…`) bleibt bei einem Wildcard-Zertifikat für alle Subdomains gleich — der `server_name` in jedem `server{}`-Block muss aber pro Dienst eindeutig sein. Deklarieren zwei `server{}`-Blöcke denselben `server_name` (z. B. weil beim Kopieren dieses Templates die Subdomain vergessen wurde), meldet Nginx `conflicting server name … ignored` und nur einer der beiden Blöcke wird tatsächlich bedient.

Konkrete Backend-Anbindungen mit diesen beiden Zeilen, je auf eigener Subdomain (`xwiki.`, `mediawiki.wissen-ahrensburg.de`): [XWiki installieren und über Nginx bereitstellen](../../wissen/dokumentation/xwiki/installieren.md), [MediaWiki installieren](../../wissen/dokumentation/mediawiki/index.md).

!!! tip "Automatische Erneuerung"
    Von Certbot per Snap installierte Versionen richten üblicherweise automatisch einen `systemd`-Timer für die Erneuerung ein. Prüfen mit `sudo systemctl list-timers | grep certbot` und ein Dry-Run mit `sudo certbot renew --dry-run`.

### Vorteile eines Wildcard-SSL-Zertifikats

- **Schutz aller Subdomains:** Ein Wildcard-Zertifikat sichert die Hauptdomain sowie beliebig viele Subdomains (z.B. `mail.wissen-ahrensburg.de`, `blog.wissen-ahrensburg.de`) mit nur einem Zertifikat ab.
- **Einfachere Verwaltung:** Es muss nur ein Zertifikat ausgestellt, installiert und erneuert werden, unabhängig von der Anzahl der Subdomains.
- **Kosteneffizienz:** Im Vergleich zu Einzelzertifikaten für jede Subdomain ist ein Wildcard-Zertifikat meist günstiger und reduziert den administrativen Aufwand.
- **Zukunftssicherheit:** Neue Subdomains können jederzeit hinzugefügt und automatisch durch das bestehende Zertifikat geschützt werden, ohne ein neues Zertifikat beantragen zu müssen.

