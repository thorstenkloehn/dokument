## .NET installieren

```bash
# Installiert notwendige Tools für Repositories
sudo apt install software-properties-common

# Fügt das .NET Backports-Repository hinzu, um verschiedene .NET-Versionen zu erhalten
sudo add-apt-repository ppa:dotnet/backports

# Aktualisiert die Paketquellen
sudo apt-get update

# Installiert mehrere Versionen der ASP.NET Core Runtime für parallele Anwendungskompatibilität
sudo apt-get install -y aspnetcore-runtime-10.0
sudo apt-get install -y aspnetcore-runtime-9.0
sudo apt-get install -y aspnetcore-runtime-8.0
```

## Java installieren

```bash
# Aktualisiert die Paketquellen
sudo apt update

# Installiert eine aktuelle, schlanke Java-Laufzeitumgebung ohne grafische Komponenten
sudo apt install openjdk-21-jre-headless

# Überprüft die installierte Java-Version
java -version
```

## Python installieren

```bash
# Installiert Python 3, pip, venv und setzt 'python' auf Python 3
sudo apt install python3 python3-pip python3-venv python-is-python3
```
