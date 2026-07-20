# IDE & Entwicklungsumgebung: System-Setup und Installation

Detaillierte Anleitungen zur Einrichtung des lokalen Entwicklungsrechners unter Ubuntu 25.10.

---

## Systemvoraussetzungen

### System aktualisieren

Öffnen Sie das Terminal und führen Sie folgende Befehle aus, um Ihr System zu aktualisieren:

```bash
sudo apt-get update
sudo apt-get upgrade
sudo apt install libsecret-1-0 libsecret-tools libsecret-1-dev libglib2.0-dev
sudo ubuntu-drivers install
```

---

## Sprachruntimes installieren

### Java und Entwicklungswerkzeuge

```bash
sudo apt install openjdk-26-jdk
sudo apt install maven
```


### Python installieren

```bash
sudo apt install python3 python3-pip python3-venv python-is-python3
```

### Node.js installieren

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

### Go (Golang) installieren

```bash
cd $HOME
sudo rm -rf /usr/local/go
wget https://go.dev/dl/go1.26.4.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.26.4.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc
```

### Rust installieren

```bash
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
```

### C und C++ Entwicklungsumgebung

```bash
sudo apt install curl
sudo apt install build-essential
sudo apt-get install cmake
sudo apt-get install gdb
```

---

## Datenbanken installieren

### PostgreSQL installieren

```bash
# Import the repository signing key:
sudo apt install curl ca-certificates
sudo install -d /usr/share/postgresql-common/pgdg
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

# Create the repository configuration file:
. /etc/os-release
sudo sh -c "echo 'deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $VERSION_CODENAME-pgdg main' > /etc/apt/sources.list.d/pgdg.list"

# Update the package lists:
sudo apt update

# PostgreSQL installieren
sudo apt install postgresql-18

# PostGIS Erweiterung installieren
sudo apt-get install postgis postgresql-18-postgis-3 postgresql-18
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql -d thorsten -c "CREATE EXTENSION postgis;"
psql -d thorsten -c "CREATE EXTENSION hstore;"
psql -d thorsten -c "ALTER TABLE geometry_columns OWNER TO thorsten;"
psql -d thorsten -c "ALTER TABLE spatial_ref_sys OWNER TO thorsten;"
psql -d thorsten -c "\password thorsten"
psql -c "ALTER USER dein_benutzername CREATEDB;"
exit
```

### PostgreSQL Passwort-Authentifizierung konfigurieren

Erstelle die `.pgpass` Datei in deinem Home-Verzeichnis:

```bash
nano ~/.pgpass
```

Füge die Daten im folgenden Format ein:

```text
localhost:5432:*:dein_user:dein_passwort
```

Setze die korrekten Berechtigungen:

```bash
chmod 0600 ~/.pgpass
```

---

## Entwicklungstools installieren

### Sudo ohne Passwort konfigurieren (NOPASSWD)

Öffnen Sie die Konfigurationsdatei mit:

```bash
sudo visudo
```

Fügen Sie am Ende der Datei folgende Zeile für Ihren Benutzer hinzu:

```text
dein_benutzername ALL=(ALL) NOPASSWD:ALL
```

Speichern und schließen Sie den Editor.

### Google Chrome installieren

```bash
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```

### Git installieren und konfigurieren

```bash
sudo apt-get install git gh
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### GitHub CLI (gh) konfigurieren

```bash
gh auth login
```

---

## Editoren & IDEs installieren

### Google Antigravity

```bash
# 1. In das temporäre Verzeichnis wechseln
cd /tmp

# 2. Download mit fest definiertem Dateinamen (-O)
wget "https://edgedl.me.gvt1.com/edgedl/release2/j0qc3/antigravity/stable/2.1.1-6123990880747520/linux-x64/Antigravity%20IDE.tar.gz" -O antigravity.tar.gz

# 3. Zielverzeichnis erstellen
sudo mkdir -p /opt/Antigravity_IDE

# 4. Entpacken
sudo tar -xzf antigravity.tar.gz -C /opt/Antigravity_IDE --strip-components=1

# 5. Desktop-Datei erstellen
sudo bash -c 'cat > /usr/share/applications/antigravity.desktop' << 'EOF'
[Desktop Entry]
Version=1.0
Type=Application
Name=Antigravity IDE
Comment=Google Antigravity Development Platform
Exec=/opt/Antigravity_IDE/antigravity-ide --no-sandbox
Icon=/opt/Antigravity_IDE/icon.svg
Terminal=false
Categories=Development;IDE;
StartupWMClass=antigravity-ide
EOF

# 6. Datenbank aktualisieren
sudo update-desktop-database
```

### Visual Studio Code und Neovim installieren

```bash
sudo snap install code --classic
sudo apt-get install neovim
```

### Wichtige VS Code Erweiterungen installieren

```bash
code --install-extension GitHub.copilot
code --install-extension anthropic.claude-code
code --install-extension openai.chatgpt
code --install-extension vscjava.vscode-java-pack
code --install-extension vmware.vscode-boot-dev-pack
code --install-extension ms-vscode.cpptools-extension-pack
code --install-extension ms-python.python
code --install-extension rust-lang.rust-analyzer
```

### Zed installieren

```bash
curl -f https://zed.dev/install.sh | sh
```

### Jetbrains IDEs installieren

```bash
sudo snap install intellij-idea --classic
```

---

## KI-Tools installieren

### KI CLIs installieren

```bash
curl -fsSL https://claude.ai/install.sh | bash
curl -fsSL https://chatgpt.com/codex/install.sh | sh
curl -fsSL https://antigravity.google/cli/install.sh | bash
```

---

## Geodaten-Verarbeitung

### PostGIS und OSM-Daten

```bash
cd $HOME
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql -d thorsten -c "CREATE EXTENSION postgis;"
psql -d thorsten -c "CREATE EXTENSION hstore;"
psql -d thorsten -c "ALTER TABLE geometry_columns OWNER TO thorsten;"
psql -d thorsten -c "ALTER TABLE spatial_ref_sys OWNER TO thorsten;"
psql -d thorsten -c "\password thorsten"
psql -c "ALTER USER dein_benutzername CREATEDB;"
exit

cd $HOME
wget https://download.geofabrik.de/europe/germany/schleswig-holstein-latest.osm.pbf
sudo apt-get install osmosis osm2pgsql
osmosis --read-pbf file=schleswig-holstein-latest.osm.pbf --bounding-box left=10.1141 right=10.3716 top=53.7136 bottom=53.6249 --write-pbf file=ahrensburg.pbf
osm2pgsql -d thorsten -H localhost -U thorsten --create -G --hstore -W ahrensburg.pbf
```

### QGIS Verbindungstypen

* **Vektorkacheln (Vector Tiles):** Verbindungen zu Vektor-Tileservern
* **XYZ-Kacheln (XYZ Tiles):** Einbindung von Raster-Kacheln (Basemaps)
* **PostgreSQL:** Verbindungen zu PostGIS-Datenbanken
* **WMS/WMTS / WFS / WCS:** Standardisierte Web-Dienste (OGC-Dienste)
* **Cloud:** Direkter Zugriff auf Cloud-Speicherdienste
* **Szenen (Scenes):** 3D-Daten und dreidimensionale Modelle
