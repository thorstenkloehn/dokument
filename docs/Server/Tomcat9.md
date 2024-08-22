## Tomcat 9
Tomcat ist ein Open-Source-Webserver und Servlet-Container, der von der Apache Software Foundation entwickelt wird. Tomcat implementiert die Java Servlet- und JavaServer Pages-Spezifikationen und bietet eine "reine Java"-HTTP-Webserver-Umgebung für Java-Code, der ausgeführt wird. Tomcat ist ein leistungsfähiger Webserver, der auch als Web-Container bezeichnet wird. Ein Web-Container (auch als Servlet-Container bezeichnet) ist ein Anwendungs-Server, der Servlets und JSPs ausführt. Es gibt viele andere Web-Container, die Sie verwenden können, z.B. JBoss, Glassfish, etc.

### Installation auf Ubuntu 24.04
Tomcat 9 ist in den Standard-Repositorys von Ubuntu 24.04 enthalten. Sie können es einfach installieren, indem Sie den folgenden Befehl ausführen:
### Tomcat 9 herunterladen
```bash
sudo apt update
sudo apt upgrade
cd $HOME
wget https://dlcdn.apache.org/tomcat/tomcat-9/v9.0.93/bin/apache-tomcat-9.0.93.tar.gz
```
### Tomcat 9 entpacken
```bash
sudo tar -xvzf apache-tomcat-9.0.93.tar.gz -C /opt/
sudo mv /opt/apache-tomcat-9.0.93 /opt/tomcat
```
### Benutzer und Gruppe erstellen:
```bash
sudo useradd -m -s /bin/false tomcat
sudo groupadd tomcat
sudo usermod -a -G tomcat tomcat
```
### Besitzrechte ändern:
```bash
sudo chown -R tomcat:tomcat /opt/tomcat
```
### Tomcat 9 als Service einrichten
```bash
sudo nano /etc/systemd/system/tomcat.service
```
### Tomcat 9 Service Datei
```bash
[Unit]
Description=Apache Tomcat Web Server
After=network.target

[Service]
Type=forking
User=tomcat
Group=tomcat
WorkingDirectory=/opt/tomcat/bin
ExecStart=/opt/tomcat/bin/startup.sh
ExecStop=/opt/tomcat/bin/shutdown.sh

[Install]
WantedBy=multi-user.target   
```

### Tomcat 9 starten
```bash
sudo systemctl daemon-reload 
sudo systemctl start tomcat 
sudo systemctl enable tomcat
```

## Webanwendung bereitstellen
### Webanwendung in den Webapps-Ordner
```bash
/opt/tomcat/webapps
```

