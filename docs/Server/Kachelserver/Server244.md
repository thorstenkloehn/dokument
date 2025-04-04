## Ubuntu 24.04 LTS Installation

Diese Seite beschreibt, wie man alle notwendige Software installiert, einrichtet und konfiguriert, um einen eigenen Kachelserver zu betreiben. Diese Schritt-für-Schritt-Anleitung wurde für Ubuntu Linux 24.04 (Noble Numbat) geschrieben und im April 2024 getestet.
## Softwareinstallation
Der OSM-Kachelserver-Stack ist eine Sammlung von Programmen und Bibliotheken, die zusammenarbeiten, um einen Kachelserver zu erstellen. Wie so oft bei OpenStreetMap gibt es viele Wege, dieses Ziel zu erreichen, und fast alle Komponenten haben Alternativen, die verschiedene spezifische Vor- und Nachteile haben. Dieses Tutorial beschreibt die gängigste Version, die der auf den Haupt-Kachelserven von OpenStreetMap.org ähnlich ist.

Er besteht aus 5 Hauptkomponenten: mod_tile, renderd, mapnik, osm2pgsql und einer PostgreSQL/PostGIS-Datenbank. Mod_tile ist ein Apache-Modul, das zwischengespeicherte Kacheln bereitstellt und entscheidet, welche Kacheln neu gerendert werden müssen - entweder weil sie noch nicht zwischengespeichert sind oder weil sie veraltet sind. Renderd bietet ein Prioritätswarteschlangensystem für verschiedene Arten von Anfragen, um die Last von Renderanfragen zu verwalten und zu glätten. Mapnik ist die Softwarebibliothek, die das eigentliche Rendern durchführt und von renderd verwendet wird.

Dank der Arbeit der Debian- und Ubuntu-Maintainer, die neuesten Versionen dieser Pakete in Ubuntu 24.04 zu integrieren, sind diese Anweisungen etwas kürzer als einige frühere Versionen.

Diese Anweisungen wurden geschrieben und gegen einen neu installierten Ubuntu 24.04 Server getestet. Wenn Sie bereits andere Versionen einiger Software installiert haben (vielleicht haben Sie von einer früheren Version aktualisiert, oder Sie haben einige PPAs zum Laden eingerichtet), dann müssen Sie möglicherweise einige Anpassungen vornehmen.

Um diese Komponenten zu erstellen, müssen zunächst eine Vielzahl von Abhängigkeiten installiert werden.

Dieser Leitfaden geht davon aus, dass Sie alles von einem Nicht-Root-Benutzer über "sudo" ausführen. Versuchen Sie nicht, alles unten als Root zu tun; es wird nicht funktionieren.

Aktualisieren Sie zunächst Ihre Paketliste und installieren Sie die erforderlichen Pakete:
## Nutzer erstellen bei Ubuntu 24.04 LTS

Um einen neuen Nutzer in Ubuntu 24.04 LTS zu erstellen, können Sie die folgenden Schritte ausführen:

1. Öffnen Sie ein Terminalfenster.


2. Führen Sie den folgenden Befehl aus, um einen neuen Nutzer zu erstellen:
```bash
sudo adduser --force-badname _renderd
sudo usermod -aG sudo _renderd
exit
```
### Login als neuer Nutzer

Der gegebene Codeblock zeigt, wie man sich als ein bestimmter Nutzer in einem Linux-System einloggt. Der Befehl `ssh` wird verwendet, um eine sichere Shell-Sitzung zu starten.

```bash
ssh _renderd@localhost
```
### System aktualisieren und upgraden

Um Ihr Ubuntu-System zu aktualisieren und zu upgraden, können Sie die folgenden Befehle verwenden:

1. **System aktualisieren**

   Der Befehl `sudo apt update` wird verwendet, um die Paketlisten für Upgrades für Pakete zu aktualisieren, die installiert werden müssen, und neue Pakete, die installiert werden können.

```bash
  sudo apt update
  sudo apt upgrade
```
## Nodjs Installation
Anleitung zur Installation von Node.js auf Ubuntu 24.04 LTS
```
sudo apt-get install curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 22
```

## Installation weitere Pakete
```bash
sudo apt install screen locate libapache2-mod-tile renderd git tar unzip wget bzip2 apache2 lua5.1 mapnik-utils python3-mapnik python3-psycopg2 python3-yaml gdal-bin postgresql postgresql-contrib postgis postgresql-16-postgis-3 postgresql-16-postgis-3-scripts osm2pgsql net-tools curl osmosis snapd
```
An diesem Punkt wurden einige neue Konten hinzugefügt. Sie können sie mit "tail /etc/passwd" sehen. "postgres" wird zur Verwaltung der Datenbanken verwendet, die wir zur Speicherung von Daten für das Rendering verwenden. "_renderd" wird für den Renderd-Daemon verwendet, und wir müssen sicherstellen, dass viele der unten aufgeführten Befehle als dieser Benutzer ausgeführt werden.

Jetzt müssen Sie eine PostGIS-Datenbank erstellen. Die Standardwerte verschiedener Programme gehen davon aus, dass die Datenbank "gis" heißt und wir werden in diesem Tutorial die gleiche Konvention verwenden, obwohl dies nicht notwendig ist. Beachten Sie, dass "_renderd" unten dem Benutzer entspricht, unter dem der Renderd-Daemon ausgeführt wird.

```bash
sudo -u postgres -i
createuser _renderd
createdb -E UTF8 -O _renderd gis
psql -d gis -c "CREATE EXTENSION postgis;" # Erweiterung hinzufügen
psql -d gis -c "CREATE EXTENSION hstore;" # Erweiterung hinzufügen
psql -d gis -c "ALTER TABLE geometry_columns OWNER TO _renderd;" # Rechte setzen
psql -d gis -c "ALTER TABLE spatial_ref_sys OWNER TO _renderd;" # Rechte setzen
exit
```
(Das wird Sie aus dem Benutzer "postgres" herausbringen)
## Mapnik
Mapnik wurde oben installiert. Wir werden überprüfen, ob es korrekt installiert wurde, indem wir Folgendes tun:
```bash
python3
>>> import mapnik
>>>
```
Wenn Sie keine Fehlermeldung erhalten, ist Mapnik korrekt installiert. Drücken Sie "Ctrl-D", um Python zu verlassen.

## Konfiguration des Stylesheets
Jetzt, da alle notwendige Software installiert ist, müssen Sie ein Stylesheet herunterladen und konfigurieren.

Der Stil, den wir hier verwenden, ist der, der von der "Standard"-Karte auf der Website openstreetmap.org verwendet wird. Er wurde gewählt, weil er gut dokumentiert ist und überall auf der Welt funktionieren sollte (einschließlich an Orten mit nicht-lateinischen Ortsnamen). Es gibt jedoch ein paar Nachteile - es ist sehr viel ein Kompromiss, der global funktionieren soll, und es ist ziemlich kompliziert zu verstehen und zu modifizieren, falls Sie das tun müssen.

Die Heimat von "OpenStreetMap Carto" im Web ist https://github.com/gravitystorm/openstreetmap-carto/ und es hat seine eigenen Installationsanweisungen unter https://github.com/gravitystorm/openstreetmap-carto/blob/master/INSTALL.md , obwohl wir hier alles abdecken, was getan werden muss.

Hier gehen wir davon aus, dass wir die Details des Stylesheets in einem Verzeichnis unter "src" im Home-Verzeichnis des jeweiligen Nicht-Root-Benutzerkontos speichern, das Sie verwenden; wir werden den Zugriff so ändern, dass der Benutzer "_renderd" darauf zugreifen kann.

```bash
mkdir ~/src
cd ~/src
git clone https://github.com/gravitystorm/openstreetmap-carto
cd openstreetmap-carto
git pull --all
git switch --detach v5.9.0
```
Als nächstes installieren wir eine geeignete Version des "carto"-Compilers.
    
```bash 
sudo npm install -g carto
carto -v
```
Das sollte mit einer Zahl antworten, die mindestens so hoch ist wie:
    
```bash
    1.2.0
```
Dann konvertieren wir das Carto-Projekt in ein Format, das Mapnik verstehen kann:

```bash
carto project.mml > mapnik.xml
```
Sie haben jetzt ein Mapnik XML-Stylesheet unter /home/IhrBenutzerkonto/src/openstreetmap-carto/mapnik.xml .

## Daten laden
Zunächst laden wir nur eine kleine Menge an Testdaten. Es sind andere Download-Standorte verfügbar, aber "download.geofabrik.de" bietet eine breite Palette an Optionen. In diesem Beispiel laden wir die Daten für Schlewig Holstein herunter, die derzeit etwa 32Mb groß sind.

Navigieren Sie zu https://download.geofabrik.de/europe/germany/schleswig-holstein.html und beachten Sie das Datum "Diese Datei wurde zuletzt geändert" (z.B. "2024-04-24T20:21:40Z"). Wir werden das später benötigen, wenn wir die Datenbank mit den nachfolgenden Änderungen der Menschen an OpenStreetMap aktualisieren wollen. Laden Sie es wie folgt herunter:
    
```bash
mkdir ~/data
cd ~/data
wget https://download.geofabrik.de/europe/germany/schleswig-holstein-latest.osm.pbf
osmosis --read-pbf file=schleswig-holstein-latest.osm.pbf --bounding-box left=10.1141 right=10.3716 top=53.7136 bottom=53.6249 --write-pbf file=ahrensburg.pbf

```
Als nächstes müssen wir sicherstellen, dass der Benutzer "_renderd" auf das Stylesheet zugreifen kann. Um dies zu ermöglichen, benötigt er Zugriff auf den Ort, an dem Sie es heruntergeladen haben, und standardmäßig hat er keinen Zugriff auf Ihr Home-Verzeichnis. Wenn es sich in "src" unter Ihrem Benutzerkonto befindet, dann

```bash
chmod a+rx ~
```
wird funktionieren. Wenn Sie dies nicht tun möchten, können Sie es verschieben und die Verweise auf die Dateiorte in den nachfolgenden Befehlen ändern.

Der folgende Befehl wird die zuvor heruntergeladenen OpenStreetMap-Daten in die Datenbank einfügen. Dieser Schritt ist sehr intensiv in Bezug auf die Festplatten-I/O; der Import des gesamten Planeten kann je nach Hardware viele Stunden, Tage oder Wochen dauern. Für kleinere Extrakte ist die Importzeit entsprechend viel schneller, und Sie müssen möglicherweise mit verschiedenen -C-Werten experimentieren, um in den verfügbaren Speicher Ihres Rechners zu passen. Beachten Sie, dass der Benutzer "_renderd" für diesen Prozess verwendet wird.

```bash
sudo -u _renderd osm2pgsql -d gis --create --slim  -G --hstore --tag-transform-script ~/src/openstreetmap-carto/openstreetmap-carto.lua -C 2500 --number-processes 1 -S ~/src/openstreetmap-carto/openstreetmap-carto.style ~/data/ahrensburg.pbf
```
## Erstellen von Indizes
Seit der Version v5.3.0 müssen einige zusätzliche Indizes manuell angewendet werden:
```bash
cd ~/src/openstreetmap-carto/
sudo -u _renderd psql -d gis -f indexes.sql
```
Es sollte 16 Mal mit "CREATE INDEX" antworten.
## Datenbankfunktionen
In Version 5.9.0 von "OSM Carto" (veröffentlicht im Oktober 2024) müssen einige Funktionen manuell in die Datenbank geladen werden. Diese können jederzeit hinzugefügt / neu geladen werden mit:
```bash
cd ~/src/openstreetmap-carto/
sudo -u _renderd psql -d gis -f functions.sql
```
## Shapefile-Download
Obwohl die meisten Daten, die zur Erstellung der Karte verwendet werden, direkt aus der oben heruntergeladenen OpenStreetMap-Datendatei stammen, werden immer noch einige Shapefiles für Dinge wie Ländergrenzen bei niedriger Zoomstufe benötigt. Um diese herunterzuladen und zu indizieren, verwenden wir das gleiche Konto wie zuvor:

```bash
cd ~/src/openstreetmap-carto/
mkdir data
sudo chown _renderd data
sudo -u _renderd scripts/get-external-data.py
```
Dieser Prozess beinhaltet einen erheblichen Download und kann einige Zeit in Anspruch nehmen - während er läuft, wird nicht viel auf dem Bildschirm angezeigt. Einige Daten gehen direkt in die Datenbank, und einige gehen in ein "data"-Verzeichnis unter "openstreetmap-carto". Wenn hier ein Problem auftritt, dann sind die Natural Earth Daten möglicherweise verschoben worden - schauen Sie sich dieses Problem und andere Probleme bei Natural Earth für weitere Details an. Wenn Sie den Download-Ort von Natural Earth ändern müssen, ist Ihre Kopie dieser Datei diejenige, die Sie bearbeiten sollten.


## Schriftarten
In der Version v5.6.0 und höher von Carto müssen Schriftarten manuell installiert werden:
```bash
cd ~/src/openstreetmap-carto/
scripts/get-fonts.sh
```
Unser Testdatenbereich (Ahrensburg) wurde sowohl wegen seiner geringen Größe als auch wegen einiger Ortsnamen in dieser Region ausgewählt, die Namen mit nicht-lateinischen Zeichen enthalten.
## Einrichten Ihres Webservers
### Konfigurieren von renderd
Die Konfigurationsdatei für "renderd" unter Ubuntu 24.04 ist "/etc/renderd.conf". Bearbeiten Sie diese mit einem Texteditor wie nano:
```bash
sudo nano /etc/renderd.conf
```
Ändern Sie die folgenden Zeilen, um sie an Ihre Umgebung anzupassen:
```bash
[s2o]
URI=/hot/
XML=/home/_renderd/src/openstreetmap-carto/mapnik.xml
HOST=localhost
TILESIZE=256
MAXZOOM=20
```
Der Pfad zur XML-Datei "/home/accountname/src/openstreetmap-carto/mapnik.xml" muss auf den tatsächlichen Pfad auf Ihrem System geändert werden. Sie können auch "[s2o]" und "URI=/hot/" ändern, wenn Sie möchten. Wenn Sie mehr als einen Satz von Kacheln von einem Server rendern möchten, können Sie das tun - fügen Sie einfach einen weiteren Abschnitt wie "[s2o]" mit einem anderen Namen hinzu, der auf einen anderen Kartenstil verweist. Wenn Sie möchten, dass es sich auf eine andere Datenbank als die Standarddatenbank "gis" bezieht, können Sie das tun, aber das liegt außerhalb des Rahmens dieses Dokuments. Wenn Sie nur etwa 2Gb Speicher haben, sollten Sie auch "num_threads" auf 2 reduzieren. "URI=/hot/" wurde gewählt, damit die hier generierten Kacheln leichter anstelle der HOT-Kachel-Ebene auf OpenStreetMap.org verwendet werden können. Sie können hier etwas anderes verwenden, aber "/hot/" ist genauso gut wie alles andere.

Als dieser Leitfaden zum ersten Mal geschrieben wurde, war die von Ubuntu 24.04 bereitgestellte Version von Mapnik 3.1, und die Einstellung "plugins_dir" im Abschnitt "[mapnik]" der Datei war "/usr/lib/mapnik/3.1/input". Dieses "3.1" könnte sich in der Zukunft wieder ändern. Wenn beim Versuch, Kacheln zu rendern, ein Fehler auftritt, wie dieser:

```bash
An error occurred while loading the map layer 's2o': Could not create datasource for type: 'postgis' (no datasource plugin directories have been successfully registered)  encountered during parsing of layer 'landcover-low-zoom'
```
Dann schauen Sie in "/usr/lib/mapnik" und sehen Sie, welche Versionsverzeichnisse es gibt, und schauen Sie auch in "/usr/lib/mapnik/(version)/input", um sicherzustellen, dass dort eine Datei "postgis.input" existiert.

Jetzt, da wir "renderd" gesagt haben, wie es auf Kachelrendering-Anfragen reagieren soll, müssen wir dem Apache-Webserver sagen, dass er sie senden soll. Leider wurde die Konfiguration dafür aus den neuesten Versionen von mod_tile entfernt. Sie kann jedoch derzeit von hier installiert werden

```bash
cd /etc/apache2/conf-available/
sudo wget https://raw.githubusercontent.com/openstreetmap/mod_tile/python-implementation/etc/apache2/renderd.conf
sudo a2enconf renderd
sudo systemctl reload apache2
```
### Reload Apache
```bash
sudo nano /usr/lib/systemd/system/renderd.service
sudo systemctl daemon-reload
sudo systemctl restart renderd
sudo systemctl restart apache2
```

### Apache Port ändern
```bash
sudo nano /etc/apache2/ports.conf
```
Ändern Sie den Port von 80 auf 8080
```bash
Listen 8080
```
Apache restarten
```bash
sudo systemctl restart apache2
sudo apt-get install nginx
sudo rm /etc/nginx/sites-enabled/default
sudo systemctl stop nginx
sudo snap install --classic certbot
sudo ln -s /snap/bin/certbot /usr/bin/certbot
sudo systemctl stop nginx
sudo certbot certonly --standalone -d ahrensburg.city -d www.ahrensburg.city
sudo certbot certonly --standalone -d karte.ahrensburg.city
```
## Neue Nutzer hinzufügen
```bash
sudo adduser thorsten
sudo usermod -aG sudo thorsten
exit
```
ssh thorsten@localhost
```
ssh thorsten@
cd $HOME
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql -d thorsten -c "CREATE EXTENSION postgis;" # Erweiterung hinzufügen
psql -d thorsten -c "CREATE EXTENSION hstore;" # Erweiterung hinzufügen
psql -d thorsten -c "ALTER TABLE geometry_columns OWNER TO _renderd;" # Rechte setzen
psql -d thorsten -c "ALTER TABLE spatial_ref_sys OWNER TO _renderd;" # Rechte setzen
psql -d thorsten -c "\password thorsten"
exit # Ausloggen
```
### Herunterladen der Daten
```bash
cd $HOME
wget https://download.geofabrik.de/europe/germany/schleswig-holstein-latest.osm.pbf
osmosis --read-pbf file=schleswig-holstein-latest.osm.pbf --bounding-box left=10.1141 right=10.3716 top=53.7136 bottom=53.6249 --write-pbf file=ahrensburg.pbf

osm2pgsql  -d thorsten --create  -G --hstore  ahrensburg.pbf
```

