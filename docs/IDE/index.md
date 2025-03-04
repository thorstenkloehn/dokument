## Aktualisieren

- Öffne Sie das Terminal und auf ihrem Ubuntu-Desktop
- Führen Sie folgenden Befehl aus,um System zu aktualisieren.
```bash
sudo apt-get update 
sudo apt-get upgrade
```
## Google Chrome Installieren

```bash

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb

```

## Git Installieren
```bash
sudo apt-get install git  gh
git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```
## gh Konfigurieren

```bash
gh auth login
```
## Nodejs Installieren
```bash
sudo apt-get install curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 22
# Verify the Node.js version:
node -v # Should print "v22.12.0".
nvm current # Should print "v22.12.0".
# Verify npm version:
npm -v # Should print "10.9.0".
```
## Visual Studio Code 
### Installieren
```bash
sudo snap install code --classic
```
### Pflugin
In Visual Studio Code, öffnen Sie das Terminal und führen Sie folgende Befehle aus.
```bash
code --install-extension GitHub.copilot
code --install-extension ckolkman.vscode-postgres
code --install-extension  ms-ossdata.vscode-postgresql
code --install-extension RoweWilsonFrederiskHolme.wikitext
code --install-extension ms-windows-ai-studio.windows-ai-studio
```
## Datenbank
### PostgreSQL
#### Installation

```bash
sudo apt-get install postgresql-all
```
### PosgreSQL Version zeigen
```bash
psql --version
```

### Postgis Installation in Ubuntu 23.04
```bash
sudo apt install postgis postgresql-16-postgis-3 postgresql-16-postgis-3-scripts postgresql-16-pgvector
```
### Installation von osm2pgsql und osmosis
```bash
sudo apt-get install osm2pgsql osmosis
```

### Datenbank erstellen
```bash
sudo adduser thorsten
sudo usermod -aG sudo thorsten
```

## Benutzer thorsten zu Gruppe postgres hinzufügen
```bash

ssh thorsten@
cd $HOME
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql -d thorsten -c "CREATE EXTENSION postgis;" # Erweiterung hinzufügen
psql -d thorsten -c "CREATE EXTENSION hstore;" # Erweiterung hinzufügen
psql -d thorsten -c "CREATE EXTENSION vector;" # Erweiterung hinzufügen
psql -d thorsten -c "ALTER TABLE geometry_columns OWNER TO thorsten;" # Rechte setzen
psql -d thorsten -c "ALTER TABLE spatial_ref_sys OWNER TO thorsten;" # Rechte setzen
psql -d thorsten -c "\password thorsten"
exit # Ausloggen
```
## Passwort für den Benutzer postgres setzen
```bash
\password thorsten
\q
exit

```
Herunterladen der Daten
```bash
cd $HOME
wget https://download.geofabrik.de/europe/germany/schleswig-holstein-latest.osm.pbf
osmosis --read-pbf file=schleswig-holstein-latest.osm.pbf --bounding-box left=10.1141 right=10.3716 top=53.7136 bottom=53.6249 --write-pbf file=ahrensburg.pbf

osm2pgsql  -d thorsten --create  -G --hstore  ahrensburg.pbf
```
### Datenbank Löschen
```bash
sudo -u postgres -i
psql
GRANT ALL PRIVILEGES ON DATABASE thorsten TO postgres;
drop database thorsten;
\q
```

## C und Rust Installieren
```bash
sudo apt  install curl 
sudo apt install build-essential
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh
code --install-extension  ms-vscode.cpptools-extension-pack
code --install-extension rust-lang.rust-analyzer
sudo apt-get install cmake
sudo apt-get install gdb
```
## Golang Installieren
```
cd $HOME
wget https://go.dev/dl/go1.24.1.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.24.1.linux-amd64.tar.gz
echo 'export PATH=$PATH:/usr/local/go/bin' >> ~/.bashrc
echo 'export GOPATH=$HOME/go' >> ~/.bashrc
echo 'export PATH=$PATH:$GOPATH/bin' >> ~/.bashrc
source ~/.bashrc


```

## Python Installieren
```bash
sudo apt install python3 python3-pip python3-venv  python-is-python3
code --install-extension  ms-python.python
```

## Ollama Installieren
```

curl -fsSL https://ollama.com/install.sh | sh

```
## Spring boot
```
sudo apt install openjdk-21-jdk # Installiert OpenJDK 21
sudo apt install maven # Installiert Maven
code --install-extension  vscjava.vscode-java-pack # Installiert Java Extension Pack für Visual Studio Code
code --install-extension  vmware.vscode-boot-dev-pack # Installiert Spring Boot Extension Pack für Visual S
```
## dotnet

```
sudo apt-get update # Aktualisiert die Paketliste
sudo apt-get install -y dotnet-sdk-9.0 # Installation des .NET SDK
sudo apt-get install -y dotnet-sdk-8.0 # Installation des .NET SDK
echo 'export PATH=$HOME/.dotnet/tools:$PATH' >> ~/.bashrc # Hinzufügen des Pfads zum .bashrc
source ~/.bashrc  # Aktualisierung der .bashrc
code --install-extension ms-dotnettools.csdevkit # Installiert die C# Dev Kit Erweiterung

```


## Anki
Anki ist ein Programm zum Lernen von Vokabeln und anderen Inhalten. Es ist für Windows, Linux und Mac OS X verfügbar. Anki ist Open Source und kostenlos. Es ist auch für Android und iOS verfügbar, aber diese Versionen sind nicht kostenlos.

### Anforderungen
```bash
sudo apt install libxcb-xinerama0 libxcb-cursor0 libnss3

```
### Anki herunterladen
```bash
cd $HOME
wget https://github.com/ankitects/anki/releases/download/25.02/anki-25.02-linux-qt6.tar.zst
```
### Anki installieren
```bash
tar xaf anki-25.02-linux-qt6.tar.zst
cd  anki-25.02-linux-qt6
sudo ./install.sh
QT_DEBUG_PLUGINS=1 anki
```

### Erweiterungen

#### Erweiterungen installieren
```bash
1436550454 1933645497 1463041493 1190756458
```

## Python Virtual Environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```


## Python Voraussetzung
### Ubuntu
```bash
sudo apt-get install build-essential libssl-dev zlib1g-dev libncurses5-dev libncursesw5-dev libreadline-dev libsqlite3-dev  libgdbm-dev libdb5.3-dev libbz2-dev libexpat1-dev liblzma-dev tk-dev libffi-dev uuid-dev#
```
#### hinunterladen von Python
```bash
cd /home/thorsten
wget https://www.python.org/ftp/python/3.12.2/Python-3.12.2.tgz
```
#### entpacken von Python
```bash
tar -xvf Python-3.12.2.tgz
```
#### wechseln in das Python Verzeichnis
```bash
cd Python-3.12.2
```
#### Installieren von Python
```bash
./configure
make
sudo make altinstall 
```

## Visual Studio Code Erweiterungen
```bash

code --install-extension  ms-vscode-remote.remote-ssh
code --install-extension  ms-vscode.remote-server
```
#### Quellangabe
* Quelle: [Download](https://www.python.org/downloads)
* Quelle: [Installieren Anleitung](https://wiki.ubuntuusers.de/Python/)