# SSH-Tunnel: Portweiterleitung über SSH

Ein SSH-Tunnel leitet TCP-Verbindungen durch eine bestehende, verschlüsselte SSH-Verbindung weiter. Für die getunnelte Anwendung sieht es aus, als käme die Verbindung ganz normal von `localhost` — tatsächlich läuft sie verschlüsselt über SSH zu einem entfernten Rechner. Damit lassen sich Dienste erreichen, die nicht öffentlich freigegeben sind, ohne eine eigene VPN-Infrastruktur zu betreiben.

---

## Funktionsprinzip

Das SSH-Protokoll überträgt mehrere logische **Channels** über eine einzige TCP-Verbindung (üblicherweise Port 22). Ein Channel trägt die interaktive Shell-Sitzung, ein anderer kann eine reine Portweiterleitung sein. Die weitergeleiteten Daten selbst brauchen kein eigenes Verschlüsselungsprotokoll — SSH übernimmt das für den gesamten Kanal.

!!! note "Hinweis"
    Ein SSH-Tunnel ersetzt keine Firewall-Regeln. Er kann sie im Gegenteil faktisch umgehen, wenn SSH-Zugang zu weitreichend vergeben ist — siehe Abschnitt „Absicherung auf dem Server" weiter unten.

---

## Die drei Varianten

### Local Forwarding (`-L`)

```bash
ssh -L LOKALER_PORT:ZIEL_HOST:ZIEL_PORT user@ssh-server
```

Öffnet einen Port auf dem **eigenen** Rechner. Verbindungen dorthin werden über den SSH-Server zu `ZIEL_HOST:ZIEL_PORT` weitergeleitet. `ZIEL_HOST` muss nicht der SSH-Server selbst sein — er muss nur *von dort aus* erreichbar sein.

```bash
# Admin-Oberfläche, die nur auf localhost:3000 des Servers lauscht
ssh -L 3000:127.0.0.1:3000 admin@server.example.org

# Datenbank auf einem internen Host hinter dem SSH-Server erreichen
ssh -L 5432:db-internal.example.org:5432 admin@server.example.org
```

Typische Einsatzzwecke: Admin-Oberflächen, Datenbank-Clients, interne Dashboards, einmalige Ersteinrichtungen.

### Remote Forwarding (`-R`)

```bash
ssh -R REMOTE_PORT:ZIEL_HOST:ZIEL_PORT user@ssh-server
```

Öffnet einen Port **auf dem entfernten Server**. Verbindungen dorthin werden zurück zum lokalen Rechner (oder einem von dort erreichbaren Ziel) geleitet.

```bash
# lokalen Entwicklungsserver kurzzeitig über einen öffentlichen Server erreichbar machen
ssh -R 8080:127.0.0.1:3000 user@public-server.example.org
```

Typischer Einsatz: ein Rechner **hinter NAT oder Firewall ohne eingehende Verbindungen** (z. B. ein Raspberry Pi im Heimnetz) baut selbst eine ausgehende SSH-Verbindung zu einem öffentlichen Server auf und macht sich darüber von außen erreichbar.

!!! warning "Achtung"
    Standardmäßig lauscht der geöffnete Port auf dem Server nur auf `localhost` des Servers selbst (`GatewayPorts no`). Damit er auch von außen erreichbar ist, muss der Server das explizit erlauben — siehe Abschnitt „Absicherung auf dem Server".

### Dynamic Forwarding (`-D`)

```bash
ssh -D 1080 user@ssh-server
```

Öffnet lokal einen SOCKS5-Proxy. Anwendungen, die SOCKS unterstützen (Browser, `curl --socks5`), können darüber beliebige Ziele ansprechen, die vom SSH-Server aus erreichbar sind — das Ziel wird zur Laufzeit von der Anwendung bestimmt, nicht beim Tunnelaufbau. Faktisch ein Mini-VPN für einzelne Programme.

```bash
curl --socks5 localhost:1080 http://internal-service.example.org/
```

---

## Tunnel zu Unix-Sockets

SSH kann Verbindungen nicht nur zu TCP-Ports, sondern auch zu **Unix-Domain-Sockets** weiterleiten — auf beiden Seiten des Tunnels:

```bash
# lokalen TCP-Port zu einem Unix-Socket auf dem Server weiterleiten
ssh -L 8080:/var/lib/tomcat10/xwiki-socket/xwiki.sock user@server

# lokalen Unix-Socket zu einem entfernten TCP-Ziel weiterleiten
ssh -L /tmp/local.sock:127.0.0.1:5432 user@server
```

Das ist unter anderem nützlich, um einen Dienst, der absichtlich nur über einen Unix-Socket lauscht — etwa nach der Anleitung [XWiki über Unix-Socket anbinden](../../wissen/dokumentation/xwiki/xwiki-nginx-unix-socket.md) — für eine Wartungssitzung testweise ohne Nginx direkt zu erreichen.

---

## Nützliche Optionen

| Option | Wirkung |
|---|---|
| `-N` | keine Shell öffnen, nur tunneln |
| `-f` | nach Verbindungsaufbau in den Hintergrund gehen |
| `-C` | Kompression aktivieren (bei langsamen Leitungen) |
| `-T` | kein Pseudo-Terminal anfordern |
| `-o ServerAliveInterval=60` | Keepalive-Pakete gegen tote Verbindungen |
| `-o ExitOnForwardFailure=yes` | Tunnelaufbau abbrechen, wenn die Portweiterleitung fehlschlägt (nützlich in Skripten) |

Reiner Hintergrund-Tunnel ohne Shell:

```bash
ssh -N -f -o ExitOnForwardFailure=yes -L 5432:localhost:5432 user@server
```

---

## Dauerhafte Tunnel

Ein per Hand gestarteter Tunnel bricht bei Netzwerkunterbrechungen ab. Für dauerhafte Verbindungen eignet sich **autossh**, das die SSH-Verbindung bei Abbruch automatisch neu aufbaut:

```bash
sudo apt install autossh
autossh -M 0 -N -o ServerAliveInterval=30 -o ServerAliveCountMax=3 \
  -L 5432:localhost:5432 user@server
```

`-M 0` deaktiviert den klassischen autossh-Monitor-Port und verlässt sich stattdessen auf die SSH-eigenen Keepalive-Optionen — das ist die heute übliche Empfehlung, da der Monitor-Port selbst einen zusätzlichen offenen Port bedeuten würde.

Für einen dauerhaft laufenden Tunnel als Systemdienst eignet sich ein eigener `systemd`-Service, siehe [systemd-Dienste erstellen](../system/systemd-service-creation.md).

---

## Kurzform per SSH-Config

Häufig genutzte Tunnel lassen sich in `~/.ssh/config` als Alias hinterlegen:

```text
Host db-tunnel
    HostName server.example.org
    User admin
    LocalForward 5432 localhost:5432
    ServerAliveInterval 60
```

Danach genügt:

```bash
ssh -N db-tunnel
```

---

## Absicherung auf dem Server

Auf dem SSH-Server (`/etc/ssh/sshd_config`) lässt sich steuern, ob und wie Tunnel überhaupt erlaubt sind:

| Option | Bedeutung | Empfehlung |
|---|---|---|
| `AllowTcpForwarding` | `yes` (Default), `no`, `local` oder `remote` — steuert, ob Portweiterleitung grundsätzlich erlaubt ist | auf reinen Jump-Hosts oder Servern mit strengen Policies auf `no` setzen |
| `GatewayPorts` | `no` (Default), `yes` oder `clientspecified` — steuert, ob bei Remote Forwarding auch andere Rechner auf den geöffneten Port zugreifen dürfen | im Zweifel bei `no` belassen |
| `PermitOpen` | schränkt bei erzwungenen Befehlen (`ForceCommand`) die erlaubten Ziele einer Weiterleitung ein | für Nutzer mit reinem Tunnel-Zugang (keine Shell) sinnvoll |

```bash
sudo nano /etc/ssh/sshd_config
sudo systemctl reload sshd
```

!!! warning "Achtung"
    Ein SSH-Nutzer mit erlaubter Portweiterleitung kann darüber praktisch jeden vom Server aus erreichbaren Dienst ansprechen — auch wenn eine Firewall wie [UFW](ufw-firewall.md) den direkten Zugriff von außen blockiert. SSH-Zugänge deshalb genauso restriktiv vergeben wie offene Ports.

---

## Fehlerbehandlung

### `bind: Address already in use`

Der lokale Port ist bereits belegt — durch einen alten Tunnel oder eine andere Anwendung.

```bash
sudo ss -ltnp | grep PORT
```

### `channel N: open failed: administratively prohibited`

Der Server erlaubt keine Portweiterleitung für diesen Nutzer oder generell (`AllowTcpForwarding no`). Serverseitige `sshd_config` prüfen.

### `channel N: open failed: connect failed`

Der SSH-Server konnte das eigentliche Ziel (`ZIEL_HOST:ZIEL_PORT`) nicht erreichen — Zieladresse, Zielport oder Netzwerkroute vom Server aus prüfen, nicht vom eigenen Rechner aus.

### Tunnel scheint zu stehen, reagiert aber nicht mehr

Meist eine tote TCP-Verbindung ohne Keepalive. Mit `ServerAliveInterval`/`ServerAliveCountMax` arbeiten (siehe oben) oder auf `autossh` umsteigen.

---

## Wichtige Befehle im Überblick

| Aufgabe | Befehl |
|---|---|
| Lokalen Port weiterleiten | `ssh -L LOKALER_PORT:ZIEL_HOST:ZIEL_PORT user@server` |
| Entfernten Port weiterleiten | `ssh -R REMOTE_PORT:ZIEL_HOST:ZIEL_PORT user@server` |
| SOCKS-Proxy öffnen | `ssh -D LOKALER_PORT user@server` |
| Nur tunneln, keine Shell, im Hintergrund | `ssh -N -f -L … user@server` |
| Laufende Tunnel finden | `ps aux \| grep "ssh -"` |
| Belegten lokalen Port finden | `sudo ss -ltnp \| grep PORT` |

---

## Verwandte Themen

- [UFW-Firewall installieren und steuern](ufw-firewall.md)
- [systemd-Dienste erstellen](../system/systemd-service-creation.md)
- [XWiki über Unix-Socket anbinden](../../wissen/dokumentation/xwiki/xwiki-nginx-unix-socket.md)
