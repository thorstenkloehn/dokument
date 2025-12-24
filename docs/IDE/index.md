# Entwicklungsumgebung unter Ubuntu einrichten

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
sudo apt-get install curl
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash
source ~/.bashrc
nvm install 22
node -v    # Sollte "v22.12.0" ausgeben
nvm current # Sollte "v22.12.0" ausgeben
npm -v     # Sollte "10.9.0" ausgeben
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
code --install-extension ms-windows-ai-studio.windows-ai-studio
```

## Datenbank: PostgreSQL und PostGIS

### PostgreSQL installieren und Benutzer einrichten

```bash
sudo apt-get install postgresql-all
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
sudo apt-get install postgis postgresql-16-postgis-3
sudo -u postgres -i
psql -d thorsten -c "CREATE EXTENSION postgis;"
psql -d thorsten -c "CREATE EXTENSION postgis_topology;"
exit
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
wget https://go.dev/dl/go1.25.5.linux-amd64.tar.gz
sudo tar -C /usr/local -xzf go1.25.5.linux-amd64.tar.gz
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
dotnet new install OrchardCore.ProjectTemplates::2.2.1
```

## PHP installieren

```bash
sudo apt install php-fpm php-pgsql php-xml php-curl php-gd php-mbstring php-xmlrpc php-zip php-intl php-json php-cli php-common php-apcu php-bcmath php-soap php-ldap php-imagick php-zip php-gmp -y
```

## Composer installieren

```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php composer-setup.php
php -r "unlink('composer-setup.php');"
sudo mv composer.phar /usr/local/bin/composer
```

## nginx installieren

```bash
sudo apt-get install nginx
sudo rm /etc/nginx/sites-enabled/default
```

## Java und Entwicklungswerkzeuge installieren

```bash
sudo apt install openjdk-26-jdk
sudo apt install maven
code --install-extension vscjava.vscode-java-pack
code --install-extension vmware.vscode-boot-dev-pack

```
