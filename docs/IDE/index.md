
## System aktualisieren

Öffnen Sie das Terminal und führen Sie folgende Befehle aus, um Ihr System zu aktualisieren:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt install libsecret-1-0 libsecret-tools libsecret-1-dev libglib2.0-dev
```

## Google Chrome installieren

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```
## PostgreSQL installieren
```
# Import the repository signing key:
sudo apt install curl ca-certificates
sudo install -d /usr/share/postgresql-common/pgdg
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

# Create the repository configuration file:
. /etc/os-release
sudo sh -c "echo 'deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $VERSION_CODENAME-pgdg main' > /etc/apt/sources.list.d/pgdg.list"

# Update the package lists:
sudo apt update

```

## Git installieren und konfigurieren

```bash
sudo apt-get install git gh
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

## GitHub CLI (gh) konfigurieren

```bash
gh auth login
```

## Node.js installieren

```bash
# Download and install nvm:
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash

# in lieu of restarting the shell
\. "$HOME/.nvm/nvm.sh"

# Download and install Node.js:
nvm install 25

# Verify the Node.js version:
node -v # Should print "v25.4.0".

# Verify npm version:
npm -v # Should print "11.7.0".

```


## Google Antigravity
```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://us-central1-apt.pkg.dev/doc/repo-signing-key.gpg | \
  sudo gpg --dearmor --yes -o /etc/apt/keyrings/antigravity-repo-key.gpg
echo "deb [signed-by=/etc/apt/keyrings/antigravity-repo-key.gpg] https://us-central1-apt.pkg.dev/projects/antigravity-auto-updater-dev/ antigravity-debian main" | \
  sudo tee /etc/apt/sources.list.d/antigravity.list > /dev/null

  sudo apt update


sudo apt install antigravity
antigravity --install-extension Google.geminicodeassist
antigravity --install-extension Google.gemini-cli-vscode-ide-companion
```

## Visual Studio Code und Neovim installieren

```bash
sudo snap install code --classic
sudo apt-get install neovim
```

### Wichtige VS Code Erweiterungen installieren

```bash
code --install-extension GitHub.copilot
code --install-extension RoweWilsonFrederiskHolme.wikitext
code --install-extension anthropic.claude-code
code --install-extension Google.gemini-cli-vscode-ide-companion

```

## Datenbank: PostgreSQL und PostGIS
### PostgreSQL installieren und Benutzer einrichten

```bash
sudo apt-get install postgresql-18
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql -c "\password thorsten"
psql -c "ALTER USER dein_benutzername CREATEDB;"
exit
```

### PostgreSQL Version anzeigen

```bash
psql --version
```

### PostGIS Installation (Ubuntu 23.04)

```bash
sudo apt-get install postgis postgresql-18-postgis-3
sudo -u postgres -i
psql -d thorsten -c "CREATE EXTENSION postgis;"
psql -d thorsten -c "CREATE EXTENSION postgis_topology;"
exit

cd $HOME
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql -d thorsten -c "CREATE EXTENSION postgis;" # Erweiterung hinzufügen
psql -d thorsten -c "CREATE EXTENSION hstore;" # Erweiterung hinzufügen
psql -d thorsten -c "ALTER TABLE geometry_columns OWNER TO thorsten;" # Rechte setzen
psql -d thorsten -c "ALTER TABLE spatial_ref_sys OWNER TO thorsten;" # Rechte setzen
psql -d thorsten -c "\password thorsten"
exit # Ausloggen
cd $HOME
wget https://download.geofabrik.de/europe/germany/schleswig-holstein-latest.osm.pbf
osmosis --read-pbf file=schleswig-holstein-latest.osm.pbf --bounding-box left=10.1141 right=10.3716 top=53.7136 bottom=53.6249 --write-pbf file=ahrensburg.pbf

osm2pgsql -d thorsten -H localhost -U thorsten --create -G --hstore -W ahrensburg.pbf
```

## C und C++ Entwicklungsumgebung

```bash
sudo apt install curl
sudo apt install build-essential
code --install-extension ms-vscode.cpptools-extension-pack
sudo apt-get install cmake
sudo apt-get install gdb
```

## Python installieren

```bash
sudo apt install python3 python3-pip python3-venv python-is-python3
code --install-extension ms-python.python
```

## Rust installieren

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
code --install-extension rust-lang.rust-analyzer
```
## Go (Golang) installieren

```bash
cd $HOME
wget https://go.dev/dl/go1.25.6.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.25.6.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc
```

## .NET installieren und konfigurieren

```bash
sudo apt-get update
sudo apt-get install -y dotnet-sdk-10.0
sudo apt-get install -y dotnet-sdk-9.0
sudo apt-get install -y dotnet-sdk-8.0
dotnet tool install --global dotnet-ef
dotnet tool install --global dotnet-aspnet-codegenerator
dotnet tool install -g Microsoft.Web.LibraryManager.Cli
echo 'export PATH=$HOME/.dotnet/tools:$PATH' >> ~/.bashrc
source ~/.bashrc
code --install-extension ms-dotnettools.csdevkit

```


## Java und Entwicklungswerkzeuge installieren

```bash
sudo apt install openjdk-26-jdk
sudo apt install maven
code --install-extension vscjava.vscode-java-pack
code --install-extension vmware.vscode-boot-dev-pack
```
## KI Cli
```
npm install -g @google/gemini-cli
npm install -g @github/copilot
curl -fsSL https://claude.ai/install.sh | bash
```


In dieser Anleitung wird erklärt, wie das Geoinformationssystem **QGIS Desktop** auf Ubuntu 25.10 installiert wird.

## Wichtiger Hinweis: Wayland vs. X11
QGIS in einer Wayland-Sitzung zu verwenden beeinträchtigt das Nutzungserlebnis durch Beschränkungen der zugrundeliegenden Qt-Bibliothek und den aktuellen Versionen des Wayland-Protokolls. Es wird empfohlen, für ein besseres Nutzungserlebnis auf eine traditionelle X11-Sitzung umzuschalten.

**So wechseln Sie zu einer X11-Sitzung in Ubuntu:**
1. Speichern Sie Ihre Arbeit und **melden Sie sich** von Ihrer aktuellen Ubuntu-Sitzung ab.
2. Klicken Sie auf dem Anmeldebildschirm auf Ihren **Benutzernamen**.
3. Bevor Sie Ihr Passwort eingeben, klicken Sie auf das kleine **Zahnrad-Symbol** (meist unten rechts).
4. Wählen Sie aus dem Menü **"Ubuntu on Xorg"** (oder ähnlich) anstelle der standardmäßigen "Ubuntu"-Option (welche Wayland nutzt).
5. Geben Sie Ihr Passwort ein und melden Sie sich an. Sie verwenden nun eine X11-Sitzung, mit der QGIS optimal funktioniert.

## Voraussetzungen
* Ein installiertes Ubuntu 25.10 System.
* Administratorrechte (sudo), um Pakete installieren zu können.
* Eine aktive Internetverbindung.

## Installationsschritte

Die Installation von QGIS erfolgt am besten über die offiziellen Paketquellen von QGIS, um stets die aktuelle Version zu erhalten, oder alternativ direkt aus den Ubuntu-Standardquellen.

### 1. System aktualisieren & Open Sans Schriftart installieren
Vor jeder Installation sollten die bestehenden Systempakete auf den neuesten Stand gebracht werden. Zudem ist es **zwingend erforderlich**, die Schriftart **Open Sans** zu installieren, da QGIS andernfalls nicht fehlerfrei startet. 

Öffnen Sie ein Terminal (`Strg + Alt + T`) und führen Sie folgenden Befehl aus, um das System zu aktualisieren und die Schriftart zu installieren:

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install fonts-open-sans -y
```

### 2. Installation über die Standardpaketquellen (Empfohlen für einfache Setups)
Ubuntu 25.10 bringt QGIS bereits in seinen Repositories mit. Dies ist der unkomplizierteste Weg:

```bash
sudo apt install qgis qgis-plugin-grass -y
```
Das `qgis-plugin-grass` Paket wird installiert, um erweiterte Geoverarbeitungsfunktionen nutzen zu können.

### 3. Offizielles QGIS-Repository (Für spezifische oder LTR-Versionen)
Möchten Sie sicherstellen, dass Sie immer die aktuellste "Long Term Release" (LTR) Version oder das neueste Release von den QGIS-Entwicklern erhalten:

Installieren Sie zuerst benötigte Werkzeuge und laden Sie den GPG-Schlüssel herunter:
```bash
sudo apt install software-properties-common gnupg -y
curl -fsSL https://qgis.org/downloads/qgis-archive.key | sudo gpg --dearmor -o /etc/apt/keyrings/qgis-archive-keyring.gpg
```

Fügen Sie danach das QGIS-Repository in Ihre Quellenliste ein und aktualisieren Sie den Paket-Cache:
```bash
sudo bash -c 'cat << EOF > /etc/apt/sources.list.d/qgis.sources
Types: deb deb-src
URIs: https://qgis.org/ubuntu-ltr
Suites: plucky
Architectures: amd64
Components: main
Signed-By: /etc/apt/keyrings/qgis-archive-keyring.gpg
EOF'

sudo apt update
sudo apt install qgis qgis-plugin-grass -y
```
*Hinweis: "plucky" fungiert hierbei als Codename für die Ubuntu 25.10 Veröffentlichung.*

## Das QGIS Browser-Bedienfeld

Nach der erfolgreichen Installation und dem Start von QGIS finden Sie auf der linken Seite das sogenannte **Browser-Bedienfeld** (Browser Panel). Es fungiert als eine Art „Datei-Explorer“ oder „Adressbuch“ für QGIS, in dem Sie festlegen, woher die Software ihre Kartendaten beziehen soll. In dieser Liste werden alle verschiedenen Datenquellen und Verbindungsarten aufgeführt, aus denen QGIS geografische Daten (Karten, Punkte, Linien, Satellitenbilder) laden kann:

Für Ihre Arbeit mit eigenen Karten-Servern (wie z. B. einem lokalen OSM-Tileserver wie Martin) sind besonders folgende Punkte wichtig:

* **Vektorkacheln (Vector Tiles):** Hier können Sie Verbindungen zu Vektor-Tileservern einrichten. Wenn Sie hier einen Rechtsklick machen und „Neue generische Verbindung“ wählen, können Sie die URL Ihres lokalen Servers (z. B. `http://localhost:3000/IhrLayer/{z}/{x}/{y}.pbf`) eintragen, um Ihre selbst gehosteten OpenStreetMap-Daten in QGIS als Ebene hereinzuladen und beliebig zu stylen.
* **XYZ-Kacheln (XYZ Tiles):** Hierüber binden Sie Raster-Kacheln (fertig gerenderte Bildchen) ein. Dies ist der typische Weg, um einfache Hintergrundkarten (Basemaps) wie die Standard-OpenStreetMap-Karte oder Satellitenbilder aus dem Internet in QGIS anzuzeigen (oft in Form von Links wie `https://tile.openstreetmap.org/{z}/{x}/{y}.png`).
* **PostgreSQL:** Verbindungen zu vollwertigen Datenbank-Servern. Diese werden genutzt, wenn man mit riesigen Mengen an Geodaten in einem Netzwerk arbeitet (z. B. mit der Erweiterung *PostGIS* für PostgreSQL).
* **WMS/WMTS / WFS / WCS:** Standardisierte Web-Dienste (OGC-Dienste). Viele Behörden und staatliche Stellen veröffentlichen darüber offizielle Daten, wie bspw. freie Luftbilder, die Sie direkt in QGIS laden können, ohne sie vorher herunterladen zu müssen.
* **Cloud:** Erlaubt den direkten Zugriff auf Cloud-Speicherdienste (wie Amazon S3, Google Cloud Storage), auf denen häufig enorme Mengen an Geodaten gespeichert sind.
* **Szenen (Scenes):** Dieser Punkt wird für komplexe 3D-Daten und dreidimensionale Gebäude- und Stadtmodelle genutzt. Man spricht hierbei oft von "3D Tiles" (z.B. von Cäsiium), um ganze Städte begehbar und räumlich darzustellen.

