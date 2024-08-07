# Ubuntu 20.04
Diese Seite beschreibt, wie man alle notwendige Software installiert, einrichtet und konfiguriert, um einen eigenen Kachelserver zu betreiben. Diese Schritt-für-Schritt-Anleitung wurde für Ubuntu Linux 20.04 LTS (Focal Fossa) geschrieben und im Mai 2020 getestet.
## Software installation
Der OSM-Kachelserver-Stack ist eine Sammlung von Programmen und Bibliotheken, die zusammenarbeiten, um einen Kachelserver zu erstellen. Wie so oft bei OpenStreetMap gibt es viele Wege, dieses Ziel zu erreichen, und fast alle Komponenten haben Alternativen, die verschiedene spezifische Vor- und Nachteile haben. Dieses Tutorial beschreibt die gängigste Version, die der auf den Haupt-Kachelservern von OpenStreetMap.org ähnlich ist.

Er besteht aus 5 Hauptkomponenten: mod_tile, renderd, mapnik, osm2pgsql und einer PostgreSQL/PostGIS-Datenbank. Mod_tile ist ein Apache-Modul, das zwischengespeicherte Kacheln bereitstellt und entscheidet, welche Kacheln neu gerendert werden müssen - entweder weil sie noch nicht zwischengespeichert sind oder weil sie veraltet sind. Renderd bietet ein Prioritätswarteschlangensystem für verschiedene Arten von Anfragen, um die Last von Renderanfragen zu verwalten und auszugleichen. Mapnik ist die Softwarebibliothek, die das eigentliche Rendern durchführt und von renderd verwendet wird.

Beachten Sie, dass diese Anweisungen gegen einen neu installierten Ubuntu 20.04 Server geschrieben und getestet wurden. Wenn Sie bereits andere Versionen einiger Software installiert haben (vielleicht haben Sie von einer früheren Ubuntu-Version aktualisiert, oder Sie haben einige PPAs zum Laden eingerichtet), dann müssen Sie möglicherweise einige Anpassungen vornehmen.

Dieser Leitfaden geht davon aus, dass Sie alles von einem Nicht-Root-Benutzer über "sudo" ausführen. Der standardmäßig verwendete Nicht-Root-Benutzername ist unten "renderaccount" - Sie können diesen lokal erstellen, wenn Sie möchten, oder Skripte bearbeiten, um auf einen anderen Benutzernamen zu verweisen, wenn Sie möchten. Wenn Sie den Benutzer "renderaccount" erstellen, müssen Sie ihn zur Gruppe der Benutzer hinzufügen, die zu Root sudo können. Von Ihrem normalen Nicht-Root-Benutzerkonto aus:

```bash
sudo -i
sudo adduser renderaccount
usermod -aG sudo renderaccount
exit
exit
ssh renderaccount@yourserver
sudo apt-get update 
sudo apt-get upgrade
sudo apt-get install curl
```
## Nodejs Installation
* [Anleitung](https://github.com/nodesource/distributions)

Um diese Komponenten zu erstellen, müssen zunächst eine Vielzahl von Abhängigkeiten installiert werden:
```bash
sudo apt install libboost-all-dev git tar unzip wget bzip2 build-essential autoconf libtool libxml2-dev libgeos-dev libgeos++-dev libpq-dev libbz2-dev libproj-dev munin-node munin protobuf-c-compiler libfreetype6-dev libtiff5-dev libicu-dev libgdal-dev libcairo2-dev libcairomm-1.0-dev apache2 apache2-dev libagg-dev liblua5.2-dev ttf-unifont lua5.1 liblua5.1-0-dev
```
Stimmen Sie der Installation zu. Dies wird eine Weile dauern, also gehen Sie und trinken Sie eine Tasse Tee. Diese Liste enthält verschiedene Dienstprogramme und Bibliotheken, den Apache-Webserver und "carto", das zur Umwandlung von Carto-CSS-Stylesheets in ein Format verwendet wird, das der Kartenrenderer "mapnik" verstehen kann. Wenn das abgeschlossen ist, installieren Sie die zweite Reihe von Voraussetzungen:

## Installation von PostgreSQL / PostGIS

Auf Ubuntu gibt es vorgepackte Versionen von sowohl PostGIS als auch PostgreSQL, diese können einfach über den Ubuntu-Paketmanager installiert werden.
```bash

sudo apt install postgresql postgresql-contrib postgis postgresql-12-postgis-3 postgresql-12-postgis-3-scripts osmosis

```
Hier ist "postgresql" die Datenbank, in der wir Kartendaten speichern, und "postgis" fügt ihr zusätzliche grafische Unterstützung hinzu. Stimmen Sie erneut zu, um die Installation durchzuführen.

Jetzt müssen Sie eine PostGIS-Datenbank erstellen. Die Standardwerte verschiedener Programme gehen davon aus, dass die Datenbank "gis" heißt und wir werden in diesem Tutorial die gleiche Konvention verwenden, obwohl dies nicht notwendig ist. Ersetzen Sie Ihren Benutzernamen durch "renderaccount", wo er unten verwendet wird. Dies sollte der Benutzername sein, der Karten mit Mapnik rendert.

```bash
sudo -u postgres -i
createuser renderaccount # answer yes for superuser (although this isn't strictly necessary)
createdb -E UTF8 -O renderaccount gis
psql
\c gis
CREATE EXTENSION postgis;
CREATE EXTENSION hstore;
ALTER TABLE geometry_columns OWNER TO renderaccount;
ALTER TABLE spatial_ref_sys OWNER TO renderaccount;
\q
exit
```
## Installation von osm2pgsql und osmosis
```bash
sudo apt-get install osm2pgsql osmosis
```
## Installation von Mapnik
```bash
sudo apt install autoconf apache2-dev libtool libxml2-dev libbz2-dev libgeos-dev libgeos++-dev libproj-dev gdal-bin libmapnik-dev mapnik-utils python3-mapnik python3-psycopg2 python3-yaml

```
## Installation von mod_tile und renderd
Als nächstes installieren wir mod_tile und renderd. "mod_tile" ist ein Apache-Modul, das Anfragen nach Kacheln bearbeitet; "renderd" ist ein Daemon, der tatsächlich Kacheln rendert, wenn "mod_tile" sie anfordert. Wir verwenden den "switch2osm"-Zweig von https://github.com/SomeoneElseOSM/mod_tile, der selbst von https://github.com/openstreetmap/mod_tile abgezweigt ist, aber so modifiziert wurde, dass er Ubuntu 20.04 unterstützt, und mit ein paar anderen Änderungen, um auf einem Standard-Ubuntu-Server zu arbeiten, anstatt auf einem der OSM-Rendering-Server.
## Kompilieren Sie den mod_tile-Quellcode:
```bash
mkdir ~/src
cd ~/src
git clone -b switch2osm https://github.com/SomeoneElseOSM/mod_tile.git
cd mod_tile
./autogen.sh
```
(Das sollte mit "autoreconf: Verlassen des Verzeichnisses '.'" enden.)
```bash
./configure
```
(Das sollte mit "config.status: erstelle Makefile" enden.)
```bash
make
```
Beachten Sie, dass hier einige "beunruhigende" Nachrichten über den Bildschirm scrollen werden. Es sollte jedoch mit "make[1]: Verlassen des Verzeichnisses '/home/renderaccount/src/mod_tile'" enden.
```bash
sudo make install
```
(Das sollte mit "make[1]: Verlassen des Verzeichnisses '/home/renderaccount/src/mod_tile'" enden.)
```bash
sudo make install-mod_tile
```
(Das sollte mit "chmod 644 /usr/lib/apache2/modules/mod_tile.so" enden.)
```bash
sudo ldconfig
```
(das sollte nichts zurückgeben)
## Konfiguration des Stylesheets
Jetzt, da alle notwendige Software installiert ist, müssen Sie ein Stylesheet herunterladen und konfigurieren.

Der Stil, den wir hier verwenden, ist derjenige, der von der "Standard"-Karte auf der openstreetmap.org-Website verwendet wird. Er wird gewählt, weil er gut dokumentiert ist und überall auf der Welt funktionieren sollte (einschließlich an Orten mit nicht-lateinischen Ortsnamen). Es gibt jedoch ein paar Nachteile - es ist sehr viel ein Kompromiss, der global funktionieren soll, und es ist ziemlich kompliziert zu verstehen und zu modifizieren, falls Sie das tun müssen.

Die Heimat von "OpenStreetMap Carto" im Web ist https://github.com/gravitystorm/openstreetmap-carto/ und es hat seine eigenen Installationsanweisungen unter https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md, obwohl wir hier alles abdecken, was getan werden muss.

Hier gehen wir davon aus, dass wir die Details des Stylesheets in einem Verzeichnis unter "src" im Home-Verzeichnis des Benutzers "renderaccount" (oder welchen anderen Sie verwenden) speichern.

```bash
cd ~/src
git clone https://github.com/gravitystorm/openstreetmap-carto
cd openstreetmap-carto
```
Als nächstes installieren wir eine geeignete Version des "carto"-Compilers.
```bash
sudo npm install -g carto
carto -v
```
Das sollte eine Versionsnummer zurückgeben, die größer als 1.2.0 ist. Wenn das nicht der Fall ist, müssen Sie möglicherweise eine neuere Version von "carto" installieren. Wenn Sie das tun müssen, können Sie dies mit dem folgenden Befehl tun:
Dann konvertieren wir das Carto-Projekt in etwas, das Mapnik verstehen kann
```bash
carto project.mml > mapnik.xml
```
## Daten laden
```bash
mkdir ~/data
cd ~/data
wget https://download.geofabrik.de/europe/germany/schleswig-holstein-latest.osm.pbf
osmosis --read-pbf file=schleswig-holstein-latest.osm.pbf --bounding-box left=10.1141 right=10.3716 top=53.7136 bottom=53.6249 --write-pbf file=ahrensburg.pbf
osm2pgsql -d gis --create --slim  -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/ahrensburg.pbf
```
## Erstellen von Indizes
Seit Version v5.3.0 müssen einige zusätzliche Indizes nun manuell angewendet werden.
```bash
cd ~/src/openstreetmap-carto/
psql -d gis -f indexes.sql
```
Es sollte 14 Mal mit "CREATE INDEX" antworten.
## Shapefile-Download
Obwohl die meisten Daten zur Erstellung der Karte direkt aus der oben heruntergeladenen OpenStreetMap-Datendatei stammen, werden immer noch einige Shapefiles für Dinge wie Ländergrenzen bei geringer Zoomstufe benötigt. Um diese herunterzuladen und zu indizieren:
```bash
cd ~/src/openstreetmap-carto/
scripts/get-external-data.py
```
Dieser Prozess beinhaltet einen erheblichen Download und kann einige Zeit in Anspruch nehmen - während er läuft, wird nicht viel auf dem Bildschirm angezeigt. Tatsächlich wird ein "data"-Verzeichnis unter "openstreetmap-carto" gefüllt.

## Schriftarten
In der Version v5.6.0 und höher von Carto müssen Schriftarten manuell installiert werden:
```bash
cd ~/src/openstreetmap-carto/
scripts/get-fonts.sh
```
## Einrichten Ihres Webservers
### Konfigurieren von renderd
Die Konfigurationsdatei für "renderd" ist "/usr/local/etc/renderd.conf". Bearbeiten Sie diese mit einem Texteditor wie nano:
```bash
sudo nano /usr/local/etc/renderd.conf
```
## Apache konfigurieren
```bash
sudo mkdir /var/lib/mod_tile
sudo chown renderaccount /var/lib/mod_tile

sudo mkdir /var/run/renderd
sudo chown renderaccount /var/run/renderd
```
Jetzt müssen wir Apache über "mod_tile" informieren, also mit nano (oder einem anderen Editor):
```bash
sudo nano /etc/apache2/conf-available/mod_tile.conf
```
Fügen Sie die folgende Zeile in diese Datei ein:
```bash
LoadModule tile_module /usr/lib/apache2/modules/mod_tile.so
```
und speichern Sie es, und führen Sie dann aus:
```bash
sudo a2enconf mod_tile
```
Das wird Ihnen sagen, dass Sie "service apache2 reload" ausführen müssen, um die neue Konfiguration zu aktivieren; das werden wir noch nicht gleich tun.

Wir müssen jetzt Apache über "renderd" informieren. Mit nano (oder einem anderen Editor):
```bash
sudo nano /etc/apache2/sites-available/000-default.conf
```
Fügen Sie das Folgende zwischen den Zeilen "ServerAdmin" und "DocumentRoot" ein:

```bash
LoadTileConfigFile /usr/local/etc/renderd.conf
ModTileRenderdSocketName /var/run/renderd/renderd.sock
# Timeout before giving up for a tile to be rendered
ModTileRequestTimeout 0
# Timeout before giving up for a tile to be rendered that is otherwise missing
ModTileMissingRequestTimeout 30

```
und laden Sie Apache zweimal neu:

```bash
sudo service apache2 reload
sudo service apache2 reload
```
(Ich vermute, dass es zweimal gemacht werden muss, weil Apache "verwirrt" wird, wenn es beim Laufen neu konfiguriert wird)

Wenn Sie einen Webbrowser auf: http://ihreserveripadresse/index.html richten, sollten Sie die "Es funktioniert!" Seite von Ubuntu / Apache bekommen.

(Wenn Sie nicht wissen, welche IP-Adresse zugewiesen wurde, können Sie wahrscheinlich "ifconfig" verwenden, um es herauszufinden - wenn die Netzwerkkonfiguration nicht zu kompliziert ist, wird es wahrscheinlich die "inet addr" sein, die nicht "127.0.0.1" ist). Wenn Sie einen Server bei einem Hosting-Anbieter verwenden, dann ist es wahrscheinlich, dass die interne Adresse Ihres Servers anders sein wird als die externe Adresse, die Ihnen zugewiesen wurde, aber diese externe IP-Adresse wird Ihnen bereits zugesandt worden sein und es wird wahrscheinlich diejenige sein, auf der Sie den Server derzeit zugreifen.

Beachten Sie, dass dies nur die "http" (Port 80) Seite ist - Sie müssen ein wenig mehr Apache-Konfiguration machen, wenn Sie https aktivieren wollen, aber das ist außerhalb des Rahmens dieser Anweisungen. Wenn Sie jedoch "Let's Encrypt" verwenden, um Zertifikate auszustellen, dann kann der Prozess der Einrichtung davon auch die Apache HTTPS-Seite konfigurieren.

## Erstmaliges Ausführen von renderd
Als nächstes führen wir renderd aus, um einige Kacheln zu rendern. Zunächst führen wir es im Vordergrund aus, damit wir Fehler sofort sehen können:
```bash
renderd -f -c /usr/local/etc/renderd.conf
```
Hier können einige Warnungen auftreten - machen Sie sich darüber vorerst keine Sorgen. Sie sollten keine Fehler erhalten. Wenn doch, speichern Sie die vollständige Ausgabe in einem Pastebin und stellen Sie eine Frage zu dem Problem irgendwo wie help.openstreetmap.org (verlinken Sie auf das Pastebin - fügen Sie nicht den gesamten Text in die Frage ein).

Richten Sie einen Webbrowser auf: http://ihreserveripadresse/hot/0/0/0.png

Sie sollten eine Weltkarte in Ihrem Browser sehen und einige weitere Debug-Informationen auf der Kommandozeile, einschließlich "DEBUG: START TILE" und "DEBUG: DONE TILE". Ignorieren Sie jede "DEBUG: Failed to read cmd on fd" Nachricht - es ist kein Fehler. Wenn Sie kein Kachel erhalten und andere Fehler auftreten, speichern Sie erneut die vollständige Ausgabe in einem Pastebin und stellen Sie eine Frage zu dem Problem irgendwo wie help.openstreetmap.org.

Wenn das alles funktioniert, drücken Sie Strg-C, um den Rendering-Prozess im Vordergrund zu stoppen.
## Renderd im Hintergrund ausführen
Als nächstes richten wir "renderd" ein, um im Hintergrund zu laufen. Zuerst bearbeiten Sie die Datei "~/src/mod_tile/debian/renderd.init", so dass "RUNASUSER" auf das Nicht-Root-Konto eingestellt ist, das Sie zuvor verwendet haben, wie zum Beispiel "renderaccount", und kopieren Sie es dann in das Systemverzeichnis:
```bash
nano ~/src/mod_tile/debian/renderd.init
sudo cp ~/src/mod_tile/debian/renderd.init /etc/init.d/renderd
sudo chmod u+x /etc/init.d/renderd
sudo cp ~/src/mod_tile/debian/renderd.service /lib/systemd/system/
```
Die Datei "renderd.service" ist eine "systemd"-Service-Datei. Die hier verwendete Version ruft lediglich alte init-Befehle auf. Um zu testen, ob der Startbefehl funktioniert:
```bash
sudo /etc/init.d/renderd start
```
(Das sollte mit "[ ok ] Starten von renderd (über systemctl): renderd.service" antworten.)

Um es jedes Mal automatisch zu starten:
```bash
sudo systemctl enable renderd
```
## Apache port ändern
Wenn Sie Apache auf einem anderen Port als 80 laufen lassen möchten, können Sie dies tun, indem Sie die Datei "/etc/apache2/ports.conf" bearbeiten. Zum Beispiel, um es auf Port 8080 zu ändern:
```bash
sudo nano /etc/apache2/ports.conf
```
Ändern Sie die Zeile "Listen 80" in "Listen 8080" und speichern Sie die Datei. Starten Sie dann Apache neu:
```bash
sudo /etc/init.d/apache2 restart
```
## ahrensburg.city installieren
```bash
sudo apt install snapd
sudo apt-get install nginx
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl stop nginx
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo systemctl stop nginx
sudo certbot certonly --standalone -d ahrensburg.city -d www.ahrensburg.city
sudo certbot certonly --standalone -d karte.ahrensburg.city
sudo certbot certonly --standalone -d blog.ahrensburg.city
sudo certbot certonly --standalone -d wiki.ahrensburg.city
```
## Neuen Nutzer erstellen
```bash
sudo adduser thorsten
sudo usermod -aG sudo thorsten
exit
```
## ssh thorsten
```bash
ssh thorsten@
cd $HOME
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql
\c thorsten
CREATE EXTENSION postgis;
CREATE EXTENSION hstore;
ALTER TABLE geometry_columns OWNER TO thorsten;
ALTER TABLE spatial_ref_sys OWNER TO thorsten;
## Passwort für den Benutzer postgres setzen
\password thorsten
\q
exit
```
## Herunterladen der Daten
```bash
cd $HOME
wget https://download.geofabrik.de/europe/germany/schleswig-holstein-latest.osm.pbf
osmosis --read-pbf file=schleswig-holstein-latest.osm.pbf --bounding-box left=10.1141 right=10.3716 top=53.7136 bottom=53.6249 --write-pbf file=ahrensburg.pbf

osm2pgsql  -d thorsten --create  -G --hstore  ahrensburg.pbf
```
## Build von Ahrensburg.city
```bash
cd $HOME
git clone https://github.com/thorstenkloehn/ahrensburg.city.git
cd ahrensburg.city
npm install
npm run build
```
## Systemctl Einrichten
```bash

sudo cp ahrensburg-city.service /etc/systemd/system/ahrensburg-city.service
sudo systemctl enable ahrensburg-city
sudo systemctl start ahrensburg-city

```
## config daten kopieren
```bash
cp env.local.example .env.local
nano .env.local
```

## Restart
```bash
sudo cp ahrensburg-city.conf /etc/nginx/conf.d/ahrensburg-city.conf
sudo systemctl restart ahrensburg-city
sudo systemctl restart nginx
```