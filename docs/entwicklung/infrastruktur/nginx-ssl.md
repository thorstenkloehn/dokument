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
  -d *.ahrensburg.city -d ahrensburg.city
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
    - **Name/Host:** Geben Sie den von Certbot angezeigten Wert ein (z.B. `_acme-challenge` oder `_acme-challenge.ahrensburg.city`).
    - **Typ:** Wählen Sie `TXT`.
    - **Wert:** Kopieren Sie den von Certbot bereitgestellten Schlüssel (eine zufällige Zeichenkette).

4. **Speichern Sie den neuen TXT-Record.**
    Die Änderung kann einige Minuten bis zu mehreren Stunden dauern, bis sie weltweit wirksam ist.

5. **Fahren Sie mit Certbot fort, sobald der Record aktiv ist.**
    Sie können die Ausbreitung des TXT-Records mit Tools wie [dig](https://toolbox.googleapps.com/apps/dig/) oder [whatsmydns.net](https://www.whatsmydns.net/) überprüfen.

**Beispiel für einen TXT-Record:**
| Name/Host                       | Typ | Wert                        |
|----------------------------------|-----|-----------------------------|
| _acme-challenge.ahrensburg.city  | TXT | `xxxxxxxxxxxxxxxxxxxxxxxx`   |

**Hinweis:** Jeder Zertifikatsantrag erzeugt einen neuen Wert für den TXT-Record. Wiederholen Sie die Schritte bei jeder neuen Verifizierung.

### Vorteile eines Wildcard-SSL-Zertifikats

- **Schutz aller Subdomains:** Ein Wildcard-Zertifikat sichert die Hauptdomain sowie beliebig viele Subdomains (z.B. `mail.ahrensburg.city`, `blog.ahrensburg.city`) mit nur einem Zertifikat ab.
- **Einfachere Verwaltung:** Es muss nur ein Zertifikat ausgestellt, installiert und erneuert werden, unabhängig von der Anzahl der Subdomains.
- **Kosteneffizienz:** Im Vergleich zu Einzelzertifikaten für jede Subdomain ist ein Wildcard-Zertifikat meist günstiger und reduziert den administrativen Aufwand.
- **Zukunftssicherheit:** Neue Subdomains können jederzeit hinzugefügt und automatisch durch das bestehende Zertifikat geschützt werden, ohne ein neues Zertifikat beantragen zu müssen.

