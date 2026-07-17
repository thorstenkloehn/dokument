# Tomcat 10 auf Ubuntu installieren

Diese Anleitung beschreibt die Installation von Apache Tomcat 10 auf einem Ubuntu-System.

## 1. System aktualisieren
Zuerst sollten die Paketlisten und das System aktualisiert werden:
```bash
sudo apt update && sudo apt upgrade -y
```

## 2. Java installieren
Tomcat 10 erfordert Java 11 oder höher. Wir installieren OpenJDK 17:
```bash
sudo apt install openjdk-17-jdk -y
java -version
```

## 3. Tomcat 10 installieren
Installieren Sie Tomcat 10 sowie die Native-Bibliothek (für bessere Performance und OpenSSL-Support) über die Paketverwaltung. Das Administrationspaket (`tomcat10-admin`) ist optional:
```bash
sudo apt update
sudo apt install tomcat10 libtcnative-1 -y
# Optional für Web-Manager: sudo apt install tomcat10-admin
```

## 4. Status überprüfen
Nach der Installation sollte der Tomcat-Dienst automatisch gestartet sein. Dies kann wie folgt überprüft werden:
```bash
sudo systemctl status tomcat10
```

## 5. Deployment (Manuell via SSH)
Wenn Sie kein Web-Interface nutzen möchten (aus Sicherheitsgründen oft bevorzugt), können Sie Ihre `.war`-Dateien direkt per SCP oder SFTP in das Webapps-Verzeichnis kopieren:

```bash
# Beispiel für den Upload via SCP
scp meine_app.war root@dein-server-ip:/var/lib/tomcat10/webapps/
```

Tomcat erkennt neue Dateien im `webapps`-Ordner normalerweise automatisch und entpackt sie.

## 6. Unix Domain Sockets (Optional)
Wenn Sie Tomcat hinter einem Reverse Proxy wie Nginx betreiben, kann die Kommunikation über Unix Domain Sockets effizienter sein als über TCP.

### Konfiguration in der `server.xml`
Fügen Sie einen speziellen `<Connector>` in der Datei `/etc/tomcat10/server.xml` hinzu. Anstatt eines `port`-Attributs verwenden Sie `unixDomainSocketPath`:

```xml
<Connector 
    protocol="org.apache.coyote.http11.Http11NioProtocol" 
    unixDomainSocketPath="/var/run/tomcat10/tomcat.sock"
    unixDomainSocketPathPermissions="rw-rw----"
    maxThreads="200"
    connectionTimeout="20000" />
```

### Berechtigungen und Systemd-Konfiguration
Standardmäßig schränkt die Systemd-Unit von Tomcat unter Ubuntu die Schreibrechte ein (`ReadOnlyPaths`). Damit Tomcat den Socket in `/var/run/tomcat10/` anlegen darf, müssen wir einen Override erstellen.

Führen Sie folgenden Befehl aus:
```bash
sudo systemctl edit tomcat10
```

Fügen Sie im Editor folgende Zeilen ein:
```ini
[Service]
RuntimeDirectory=tomcat10
RuntimeDirectoryMode=0770
ReadWritePaths=/var/run/tomcat10
```
*Hinweis: Dies erstellt das Verzeichnis `/run/tomcat10` (was ein Symlink auf `/var/run/tomcat10` ist) automatisch beim Start des Dienstes mit den korrekten Rechten für den Tomcat-Benutzer.*

### Berechtigungen für Nginx (Reverse Proxy)
Damit Nginx auf den Unix-Socket zugreifen darf, muss der Nginx-Benutzer (`www-data`) zur Gruppe `tomcat` hinzugefügt werden:

```bash
sudo usermod -aG tomcat www-data
```

Stellen Sie nach der Änderung sicher, dass der Dienst neu gestartet wird:
```bash
sudo systemctl restart tomcat10
```
*(Eventuell muss auch Nginx neu gestartet werden, damit die Gruppenänderung wirksam wird: `sudo systemctl restart nginx`)*

