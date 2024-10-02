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

