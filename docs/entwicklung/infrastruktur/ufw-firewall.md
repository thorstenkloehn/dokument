# UFW-Firewall installieren und steuern

**UFW** steht für **Uncomplicated Firewall**. Das Werkzeug vereinfacht die Verwaltung der Linux-Firewall über verständliche Befehle. Im Hintergrund setzt UFW die Regeln des Systems um, ohne dass jede Firewall-Regel von Hand geschrieben werden muss.

---

## Beschreibung

Eine Firewall entscheidet anhand von Regeln, welche Netzwerkverbindungen erlaubt oder abgewiesen werden. UFW eignet sich besonders für Ubuntu- und Debian-Systeme, auf denen nur bestimmte Dienste von außen erreichbar sein sollen.

Typische Aufgaben sind:

- eingehende Verbindungen standardmäßig blockieren,
- SSH, HTTP oder HTTPS gezielt freigeben,
- Zugriffe auf bestimmte IP-Adressen oder Netze begrenzen,
- ausgehende Verbindungen kontrollieren,
- abgewiesene Verbindungsversuche protokollieren.

!!! note "Hinweis"
    UFW schützt Netzwerkports, ersetzt aber keine sicheren Passwörter, Updates, SSH-Schlüssel oder die Absicherung der jeweiligen Anwendung.

---

## Einsatzgebiete

UFW ist für viele einzelne Linux-Rechner und Server geeignet:

| Einsatzgebiet | Beispiel |
|---|---|
| Webserver | Nur SSH, HTTP und HTTPS erlauben |
| Datenbankserver | Datenbankport nur für einen Anwendungsserver öffnen |
| Entwicklungsrechner | Eingehende Verbindungen blockieren, lokale Dienste schützen |
| Heimserver | Zugriff nur aus dem lokalen Netzwerk zulassen |
| Cloud-Server | Zusätzliche Firewall direkt auf dem Betriebssystem verwenden |

Für große Cluster, dynamische Container-Netzwerke oder zentral verwaltete Unternehmensnetze können spezialisierte Firewall- und Netzwerkwerkzeuge besser geeignet sein.

---

## Installation

Auf Ubuntu wird UFW über die Paketverwaltung installiert:

```bash
sudo apt update
sudo apt install ufw
```

Installation und aktuellen Zustand prüfen:

```bash
ufw --version
sudo ufw status verbose
```

Der Status `inactive` bedeutet, dass UFW installiert, aber noch nicht aktiviert ist.

---

## Sicher aktivieren

!!! warning "Achtung"
    Bei einem entfernten Server muss **vor der Aktivierung** der verwendete SSH-Port freigegeben werden. Andernfalls kann die bestehende SSH-Verbindung nach dem Trennen nicht erneut aufgebaut werden.

Standardrichtlinien setzen:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
```

SSH freigeben und UFW aktivieren:

```bash
sudo ufw allow OpenSSH
sudo ufw enable
sudo ufw status verbose
```

Wird SSH auf einem anderen Port betrieben, muss stattdessen dieser Port freigegeben werden. Beispiel für TCP-Port 2222:

```bash
sudo ufw allow 2222/tcp
```

!!! tip "Tipp"
    Eine bestehende SSH-Sitzung während der Einrichtung geöffnet lassen und die Anmeldung in einem zweiten Terminal testen.

---

## UFW steuern

### Status anzeigen

```bash
sudo ufw status
sudo ufw status verbose
sudo ufw status numbered
```

Die nummerierte Ansicht ist besonders hilfreich, wenn einzelne Regeln gelöscht werden sollen.

### Firewall ein- und ausschalten

```bash
sudo ufw enable
sudo ufw disable
```

`disable` deaktiviert die Firewall, behält aber die konfigurierten Regeln bei.

### Ports erlauben und blockieren

```bash
# HTTP und HTTPS erlauben
sudo ufw allow 80/tcp
sudo ufw allow 443/tcp

# Einen TCP-Port blockieren
sudo ufw deny 8080/tcp

# Einen UDP-Port erlauben
sudo ufw allow 51820/udp
```

Regeln können auch über einen Portbereich angelegt werden:

```bash
sudo ufw allow 6000:6010/tcp
```

### Anwendungsprofile verwenden

Installierte Programme können UFW-Profile bereitstellen. Verfügbare Profile anzeigen:

```bash
sudo ufw app list
sudo ufw app info "Nginx Full"
```

Ein Profil freigeben:

```bash
sudo ufw allow "Nginx Full"
```

Profile sind lesbarer als einzelne Portnummern und fassen zusammengehörige Ports zusammen.

---

## Zugriff nach IP-Adresse begrenzen

Zugriff von einer einzelnen IP-Adresse erlauben:

```bash
sudo ufw allow from 203.0.113.10
```

SSH nur aus einem internen Netz zulassen:

```bash
sudo ufw allow from 192.168.1.0/24 to any port 22 proto tcp
```

Zugriff einer bestimmten IP-Adresse blockieren:

```bash
sudo ufw deny from 203.0.113.50
```

!!! note "Hinweis"
    Die Netze `192.168.0.0/16`, `172.16.0.0/12` und `10.0.0.0/8` sind private Adressbereiche. Die Beispieladresse `203.0.113.10` ist ausschließlich für Dokumentationen reserviert und muss durch die tatsächliche Adresse ersetzt werden.

---

## Regeln löschen und zurücksetzen

Regel anhand ihrer Nummer löschen:

```bash
sudo ufw status numbered
sudo ufw delete 3
```

Alternativ kann die ursprüngliche Regel angegeben werden:

```bash
sudo ufw delete allow 8080/tcp
```

Alle Regeln auf die Ausgangskonfiguration zurücksetzen:

```bash
sudo ufw reset
```

!!! warning "Achtung"
    `ufw reset` entfernt sämtliche selbst angelegten Regeln und deaktiviert UFW. Auf entfernten Servern anschließend zuerst wieder SSH freigeben.

---

## Protokollierung und Fehlerdiagnose

Logging aktivieren und die gewünschte Detailstufe setzen:

```bash
sudo ufw logging on
sudo ufw logging medium
```

Protokolle mit systemd anzeigen:

```bash
sudo journalctl -k | grep UFW
```

Je nach System können Meldungen zusätzlich in `/var/log/ufw.log` oder `/var/log/kern.log` stehen.

Die Konfiguration neu laden:

```bash
sudo ufw reload
```

Bei Problemen helfen folgende Prüfungen:

```bash
sudo ufw status verbose
sudo ss -tulpn
sudo systemctl status ufw
```

Dabei zeigt `ss`, ob die Anwendung tatsächlich auf dem erwarteten Port lauscht. Eine UFW-Freigabe startet keinen Dienst und öffnet keinen Port, auf dem kein Programm läuft.

---

## Beispiel: Webserver absichern

Das folgende Beispiel erlaubt SSH sowie HTTP und HTTPS. Andere eingehende Verbindungen werden standardmäßig blockiert:

```bash
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow OpenSSH
sudo ufw allow "Nginx Full"
sudo ufw enable
sudo ufw status verbose
```

---

## Wichtige Befehle im Überblick

| Aufgabe | Befehl |
|---|---|
| Status anzeigen | `sudo ufw status verbose` |
| Regeln nummerieren | `sudo ufw status numbered` |
| Aktivieren | `sudo ufw enable` |
| Deaktivieren | `sudo ufw disable` |
| Regel erlauben | `sudo ufw allow PORT/PROTOKOLL` |
| Regel blockieren | `sudo ufw deny PORT/PROTOKOLL` |
| Regel löschen | `sudo ufw delete NUMMER` |
| Konfiguration neu laden | `sudo ufw reload` |
| Alle Regeln zurücksetzen | `sudo ufw reset` |

---

## Verwandte Themen

- [Server und Infrastruktur](index.md)
- [Sicherheit und Datenschutz](sicherheit/index.md)
- [SSH-Tunnel: Portweiterleitung über SSH](ssh-tunnel.md)
- [Nginx-Grundlagen](nginx.md)
- [Nginx-Hardening](nginx-hardening.md)
