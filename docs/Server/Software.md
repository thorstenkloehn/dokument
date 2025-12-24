<!--
Dieses Dokument beschreibt die Installation verschiedener Software-Komponenten auf einem Linux-Server. 

1. **.NET installieren**  
    - Die .NET-Laufzeitumgebungen (`aspnetcore-runtime-10.0`, `9.0`, `8.0`) werden benötigt, um moderne .NET-Anwendungen (z.B. Web-APIs oder Webanwendungen) auszuführen. Die Installation mehrerer Versionen stellt sicher, dass Anwendungen, die auf unterschiedlichen .NET-Versionen basieren, parallel betrieben werden können.  
    - Das Hinzufügen des `dotnet/backports`-Repositories ermöglicht den Zugriff auf aktuelle und ältere .NET-Versionen, die nicht standardmäßig in den Ubuntu-Paketquellen enthalten sind.

2. **Java installieren**  
    - Java wird für viele serverseitige Anwendungen und Dienste benötigt, insbesondere für solche, die auf der Java Virtual Machine (JVM) laufen. Die Installation von `openjdk-21-jre-headless` stellt eine aktuelle, schlanke Java-Laufzeitumgebung bereit, die für den Serverbetrieb optimiert ist (ohne grafische Komponenten).

3. **Python installieren**  
    - Python ist eine weit verbreitete Programmiersprache für Automatisierung, Skripte und Webanwendungen. Die Pakete `python3`, `python3-pip` und `python3-venv` ermöglichen die Ausführung von Python-Programmen, die Verwaltung von Abhängigkeiten und die Nutzung von virtuellen Umgebungen. `python-is-python3` sorgt dafür, dass der Befehl `python` auf Python 3 verweist.

4. **PHP installieren**  
    - PHP ist eine serverseitige Skriptsprache, die häufig für Webanwendungen verwendet wird. Die aufgelisteten PHP-Module erweitern die Funktionalität von PHP, z.B. für Datenbankzugriffe (`php-pgsql`), XML-Verarbeitung (`php-xml`), Bildbearbeitung (`php-gd`, `php-imagick`), Internationalisierung (`php-intl`), Caching (`php-apcu`), mathematische Operationen (`php-bcmath`, `php-gmp`) und weitere wichtige Funktionen für moderne Webanwendungen.

Diese Installationsschritte sind essenziell, um einen Server für den Betrieb vielfältiger moderner Anwendungen vorzubereiten.
-->

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

## PHP installieren

```bash
# Installiert PHP-FPM und zahlreiche Module für Webanwendungen, Datenbanken, Bildbearbeitung, Caching, etc.
sudo apt install php-fpm php-pgsql php-xml php-curl php-gd php-mbstring php-xmlrpc php-zip php-intl php-json php-cli php-common php-apcu php-bcmath php-soap php-ldap php-imagick php-zip php-gmp -y
```