# Docker auf Ubuntu Server 24.04 installieren

> Diese Anleitung zeigt dir Schritt für Schritt, wie du Docker Engine (Community Edition) auf einem frischen **Ubuntu Server 24.04 LTS** installierst – die offizielle Methode über das Docker-Repository, nicht über den veralteten `snap`-Paketmanager.

---

## Voraussetzungen

- Ubuntu Server 24.04 LTS (frische Installation oder bestehende)
- Benutzer mit `sudo`-Rechten
- Internetzugang auf dem Server
- Mindestens 2 GB RAM und 10 GB freier Speicherplatz

!!! note "Hinweis: Warum nicht `snap install docker`?"
    Der `snap`-Paketmanager liefert eine ältere, eingeschränkte Docker-Version, die in vielen Produktionsszenarien Probleme verursacht. Die offizielle Docker-Methode über das apt-Repository ist stabiler, aktueller und vollständig unterstützt.

---

## Schritt 1 — System aktualisieren

Beginne mit einem vollständigen Systemupdate, bevor du Software installierst:

```bash
sudo apt update && sudo apt upgrade -y
```

Nach einem Kernel-Update kann ein Neustart erforderlich sein:

```bash
sudo reboot
```

---

## Schritt 2 — Alte Docker-Versionen entfernen

Stelle sicher, dass keine alten oder inoffiziellen Docker-Pakete installiert sind:

```bash
for pkg in docker.io docker-doc docker-compose docker-compose-v2 podman-docker containerd runc; do
  sudo apt remove -y $pkg 2>/dev/null
done
```

!!! tip "Tipp"
    Diese Pakete sind möglicherweise gar nicht installiert – der Befehl gibt dann einfach eine Meldung aus und fährt fort. Das ist kein Fehler.

---

## Schritt 3 — Abhängigkeiten installieren

Docker benötigt einige Pakete für den sicheren HTTPS-Abruf aus dem offiziellen Repository:

```bash
sudo apt install -y \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```

---

## Schritt 4 — GPG-Schlüssel hinzufügen

Docker signiert seine Pakete mit einem GPG-Schlüssel. Importiere ihn wie folgt:

```bash
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg \
    -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
```

Überprüfe, ob der Schlüssel korrekt heruntergeladen wurde:

```bash
ls -la /etc/apt/keyrings/docker.asc
```

Erwartete Ausgabe (Dateigröße ca. 2.800 Bytes):

```
-rw-r--r-- 1 root root 2812 Jul 21 22:00 /etc/apt/keyrings/docker.asc
```

---

## Schritt 5 — Docker-Repository hinzufügen

Füge das offizielle Docker-APT-Repository für Ubuntu 24.04 (Noble Numbat) hinzu:

```bash
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Aktualisiere anschließend die Paketliste:

```bash
sudo apt update
```

---

## Schritt 6 — Docker Engine installieren

Installiere Docker Engine, CLI, Containerd und die Compose-Erweiterung:

```bash
sudo apt install -y \
    docker-ce \
    docker-ce-cli \
    containerd.io \
    docker-buildx-plugin \
    docker-compose-plugin
```

| Paket | Beschreibung |
|---|---|
| `docker-ce` | Docker Community Edition (Daemon) |
| `docker-ce-cli` | Docker-Kommandozeilenwerkzeug |
| `containerd.io` | Container-Laufzeitumgebung |
| `docker-buildx-plugin` | Erweitertes Build-System (multi-arch) |
| `docker-compose-plugin` | Docker Compose V2 als Plugin |

---

## Schritt 7 — Installation überprüfen

Starte den Docker-Dienst und stelle sicher, dass er beim Systemstart automatisch startet:

```bash
sudo systemctl start docker
sudo systemctl enable docker
```

Überprüfe den Status:

```bash
sudo systemctl status docker
```

Erwartete Ausgabe (Auszug):

```
● docker.service - Docker Application Container Engine
     Loaded: loaded (/lib/systemd/system/docker.service; enabled)
     Active: active (running) since Mon 2026-07-21 22:00:00 UTC; 5s ago
```

Teste die Installation mit dem offiziellen Hello-World-Container:

```bash
sudo docker run hello-world
```

Wenn du diese Ausgabe siehst, ist Docker korrekt installiert:

```
Hello from Docker!
This message shows that your installation appears to be working correctly.
```

---

## Schritt 8 — Docker ohne `sudo` nutzen (empfohlen)

Standardmäßig erfordert Docker `sudo`. Füge deinen Benutzer der `docker`-Gruppe hinzu:

```bash
sudo usermod -aG docker $USER
```

Damit die Änderung wirksam wird, musst du dich neu einloggen oder die Gruppe temporär aktivieren:

```bash
newgrp docker
```

Teste ohne `sudo`:

```bash
docker run hello-world
```

!!! warning "Sicherheitshinweis"
    Mitglieder der `docker`-Gruppe haben effektiv root-äquivalente Rechte auf dem System, da Docker-Container als root laufen können. Füge nur vertrauenswürdige Benutzer hinzu.

---

## Schritt 9 — Docker Compose überprüfen

Docker Compose V2 ist bereits als Plugin installiert. Überprüfe die Version:

```bash
docker compose version
```

Erwartete Ausgabe:

```
Docker Compose version v2.x.x
```

---

## Schritt 10 — Systemstart-Konfiguration prüfen

Stelle sicher, dass der Docker-Daemon und der Containerd-Dienst bei jedem Systemstart automatisch gestartet werden:

```bash
sudo systemctl is-enabled docker
sudo systemctl is-enabled containerd
```

Beide Befehle sollten `enabled` ausgeben.

---

## Docker-Grundbefehle im Überblick

```bash
# Docker-Version anzeigen
docker version

# Systeminformationen anzeigen
docker info

# Alle laufenden Container anzeigen
docker ps

# Alle Container anzeigen (auch gestoppte)
docker ps -a

# Alle heruntergeladenen Images anzeigen
docker images

# Container stoppen
docker stop <container-name>

# Container entfernen
docker rm <container-name>

# Image entfernen
docker rmi <image-name>

# Ungenutzte Ressourcen bereinigen (Vorsicht: löscht gestoppte Container, ungenutzte Images!)
docker system prune
```

---

## Netzwerk- und Volume-Grundlagen

### Volumes (persistenter Datenspeicher)

Docker-Container sind zustandslos – alle Daten gehen beim Löschen verloren. Volumes sichern Daten dauerhaft auf dem Host:

```bash
# Volume erstellen
docker volume create mein-volume

# Alle Volumes anzeigen
docker volume ls

# Container mit eingebundenem Volume starten
docker run -d \
  --name mein-container \
  -v mein-volume:/app/data \
  ubuntu

# Oder Host-Verzeichnis direkt einbinden (Bind Mount)
docker run -d \
  --name mein-container \
  -v /home/user/daten:/app/data \
  ubuntu
```

### Netzwerke

```bash
# Alle Netzwerke anzeigen
docker network ls

# Eigenes Netzwerk erstellen (empfohlen für Container-Kommunikation)
docker network create mein-netzwerk

# Container im eigenen Netzwerk starten
docker run -d \
  --name backend \
  --network mein-netzwerk \
  mein-image
```

---

## Docker deinstallieren (falls nötig)

```bash
# Docker-Pakete entfernen
sudo apt purge -y docker-ce docker-ce-cli containerd.io \
    docker-buildx-plugin docker-compose-plugin

# Images, Container, Volumes und Konfiguration löschen
sudo rm -rf /var/lib/docker
sudo rm -rf /var/lib/containerd
sudo rm /etc/apt/sources.list.d/docker.list
sudo rm /etc/apt/keyrings/docker.asc
```

---

## Weiterführende Links

- [Hermes Agent mit Docker betreiben](../../../künstliche-intelligenz/coding/hermes-agent-docker.md) — Docker-basierter Betrieb des Hermes KI-Agenten
- [Docker KI-Stack](docker-ki-stack.md) — KI-Werkzeuge mit Docker betreiben
- [KI/ML-Infrastrukturen](ki-ml-infrastrukturen.md) — Überblick über KI-Infrastruktur-Setups
- [Offizielle Docker-Dokumentation](https://docs.docker.com/engine/install/ubuntu/) (englisch)
