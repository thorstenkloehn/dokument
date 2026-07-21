# Hermes Agent — Docker

> **Quelle:** [hermes-agent.nousresearch.com/docs/user-guide/docker](https://hermes-agent.nousresearch.com/docs/user-guide/docker)

Es gibt zwei grundlegende Arten, wie Docker mit dem Hermes Agent zusammenspielt:

1. **Hermes IN Docker betreiben** – der Agent selbst läuft innerhalb eines Containers (das ist der Hauptfokus dieser Seite)
2. **Docker als Terminal-Backend** – der Agent läuft auf dem Host, führt aber jeden Befehl innerhalb eines einzelnen, persistenten Docker-Sandbox-Containers aus, der über Tool-Aufrufe, `/new` und Subagenten hinweg für die Lebensdauer des Hermes-Prozesses erhalten bleibt (siehe [Konfiguration → Docker Backend](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#docker-backend))

Diese Seite behandelt Option 1. Der Container speichert alle Benutzerdaten (Konfiguration, API-Keys, Sessions, Skills, Erinnerungen) in einem einzigen Verzeichnis, das vom Host unter `/opt/data` eingebunden wird. Das Image selbst ist zustandslos und kann durch Ziehen einer neuen Version aktualisiert werden, ohne dass Konfigurationen verloren gehen.

---

## Schnellstart

Wenn du Hermes Agent zum ersten Mal ausführst, erstelle ein Datenverzeichnis auf dem Host und starte den Container interaktiv, um den Einrichtungsassistenten zu starten:

!!! warning "Browser-basierte VPS-Konsolen bei der Installation meiden"
    Einige VPS-Anbieter (Hetzner Cloud und mehrere andere) bieten eine browserbasierte Konsole zur Verwaltung von Hosts an. Diese Konsolen übertragen Sonderzeichen falsch – `:` kann als `;` ankommen, `@` wird möglicherweise falsch dargestellt, und nicht-englische Tastaturlayouts sind noch schlimmer –, was `docker run`-Argumente wie `-v ~/.hermes:/opt/data`, `-e KEY=value` und eingefügte API-Keys/Tokens lautlos beschädigt.

    **Verbinde dich stattdessen über SSH** (`ssh root@<host>`), um sicher kopieren und einfügen zu können. Wenn du die Browser-Konsole unbedingt nutzen musst, tippe die Befehle manuell ein statt sie einzufügen und überprüfe jedes `:`, `@`, `=` und `/` im Ergebnis vor dem Drücken der Eingabetaste.

```sh
mkdir -p ~/.hermes
docker run -it --rm \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent setup
```

Dadurch gelangst du in den Einrichtungsassistenten, der dich nach deinen API-Keys fragt und diese in `~/.hermes/.env` schreibt. Du musst dies nur einmal durchführen. Es wird dringend empfohlen, an dieser Stelle ein Chat-System für das Gateway einzurichten.

!!! tip "Tipp"
    Führe innerhalb des Containers einmalig `hermes setup --portal` aus – das Refresh-Token bleibt im eingebundenen `~/.hermes`-Volume gespeichert. Siehe [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal).

---

## Im Gateway-Modus betreiben

Sobald konfiguriert, führe den Container im Hintergrund als persistentes Gateway aus (Telegram, Discord, Slack, WhatsApp usw.):

```sh
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  nousresearch/hermes-agent gateway run
```

Port 8642 stellt den [OpenAI-kompatiblen API-Server](https://hermes-agent.nousresearch.com/docs/user-guide/features/api-server) und den Health-Endpunkt des Gateways bereit. Er ist optional, wenn du nur Chat-Plattformen (Telegram, Discord usw.) verwendest, aber erforderlich, wenn du möchtest, dass das Dashboard oder externe Tools das Gateway erreichen.

!!! note "Hinweis: Gateway läuft überwacht"
    Im offiziellen Docker-Image wird `gateway run` **automatisch von s6-overlay überwacht**: Wenn der Gateway-Prozess abstürzt, wird er innerhalb von Sekunden neu gestartet, ohne den Container zu verlieren. Der `gateway run`-CMD-Prozess selbst ist ein `sleep infinity`-Heartbeat, der den Container am Leben hält, während s6 den eigentlichen Gateway-Prozess verwaltet – `docker stop` fährt also trotzdem alles sauber herunter, aber `docker logs` zeigt die Ausgabe des überwachten Gateways.

    Um das zu deaktivieren und die historische Semantik "Gateway ist der Hauptprozess des Containers" zu erhalten, übergib `--no-supervise` oder setze `HERMES_GATEWAY_NO_SUPERVISE=1`. Der Opt-out ist nützlich für CI-Smoke-Tests, die den Container mit dem Status-Code des Gateways beenden sollen; für Produktionsdeployments ist die überwachte Variante streng besser.

!!! note "Hinweis: Tool-Loop-Schutz für unbeaufsichtigte Gateways"
    Die Einstellung `tool_loop_guardrails.hard_stop_enabled` ist standardmäßig `false`. Operatoren, die Schutzschalter-Verhalten wünschen, sollten Hard Stops explizit in der `config.yaml` des Profils aktivieren:

    ```yaml
    tool_loop_guardrails:
      hard_stop_enabled: true
      hard_stop_after:
        exact_failure: 5
        idempotent_no_progress: 5
    ```

!!! note "Hinweis: Wo die Gateway-Logs landen"
    Siehe den Abschnitt [Wo die Logs landen](#wo-die-logs-landen) weiter unten für die vollständige Routing-Übersicht.

Der API-Server wird durch `API_SERVER_ENABLED=true` aktiviert. Um ihn über `127.0.0.1` innerhalb des Containers hinaus zugänglich zu machen, setze außerdem `API_SERVER_HOST=0.0.0.0` und einen `API_SERVER_KEY` (mindestens 8 Zeichen – generiere einen mit `openssl rand -hex 32`):

```sh
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  -e API_SERVER_ENABLED=true \
  -e API_SERVER_HOST=0.0.0.0 \
  -e API_SERVER_KEY="$(openssl rand -hex 32)" \
  -e API_SERVER_CORS_ORIGINS='*' \
  nousresearch/hermes-agent gateway run
```

!!! warning "Achtung"
    Das Öffnen eines Ports auf einer dem Internet zugewandten Maschine ist ein Sicherheitsrisiko. Tu dies nur, wenn du die Risiken verstehst.

---

## Dashboard betreiben

Das integrierte Web-Dashboard läuft als überwachter s6-rc-Dienst zusammen mit dem Gateway im selben Container. Setze `HERMES_DASHBOARD=1`, um es zu starten:

```sh
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  -p 9119:9119 \
  -e HERMES_DASHBOARD=1 \
  nousresearch/hermes-agent gateway run
```

Das Dashboard wird von s6 überwacht – wenn es abstürzt, wird es von `s6-supervise` automatisch nach kurzem Backoff neu gestartet.

| Umgebungsvariable | Beschreibung | Standard |
|---|---|---|
| `HERMES_DASHBOARD` | Auf `1` (oder `true` / `yes`) setzen, um den überwachten Dashboard-Dienst zu aktivieren | *(nicht gesetzt – Dienst ist registriert, aber bleibt unten)* |
| `HERMES_DASHBOARD_HOST` | Bind-Adresse für den Dashboard-HTTP-Server | `0.0.0.0` |
| `HERMES_DASHBOARD_PORT` | Port für den Dashboard-HTTP-Server | `9119` |
| `HERMES_DASHBOARD_INSECURE` | **Veraltet / kein Effekt.** Früher wurde das Auth-Gate damit umgangen; seit dem Hardening im Juni 2026 deaktiviert es die Authentifizierung nicht mehr. | *(ignoriert – konfiguriere stattdessen einen Provider)* |

Das Dashboard innerhalb des Containers bindet standardmäßig an `0.0.0.0`. Das Auth-Gate wird automatisch aktiviert, wenn beides zutrifft:

1. Der Bind-Host ist nicht loopback (z. B. der Standard `0.0.0.0` innerhalb des Containers), **und**
2. Ein `DashboardAuthProvider`-Plugin ist registriert.

Es gibt drei integrierte Möglichkeiten, die zweite Bedingung zu erfüllen:

- **Benutzername/Passwort** – am einfachsten für selbst gehostete / On-Prem / Homelab-Container in einem vertrauenswürdigen Netzwerk oder hinter einem VPN: setze `HERMES_DASHBOARD_BASIC_AUTH_USERNAME` + `HERMES_DASHBOARD_BASIC_AUTH_PASSWORD` (und `HERMES_DASHBOARD_BASIC_AUTH_SECRET` für restart-stabile Sessions). Nicht geeignet für direkte Exposition im öffentlichen Internet.
- **OAuth (Nous Portal)** – für gehostete/öffentliche Deployments: der Provider `dashboard_auth/nous` wird aktiviert, sobald `HERMES_DASHBOARD_OAUTH_CLIENT_ID` gesetzt ist.
- **Self-hosted OIDC** – zur Authentifizierung gegen deinen eigenen Identity-Provider via Standard-OpenID-Connect: der Provider `dashboard_auth/self_hosted` wird aktiviert, wenn `HERMES_DASHBOARD_OIDC_ISSUER` + `HERMES_DASHBOARD_OIDC_CLIENT_ID` gesetzt sind.

!!! warning "Warum `--insecure` entfernt wurde"
    Ein nicht authentifiziertes öffentliches Dashboard war der Einstiegspunkt für die MCP-Konfigurations-Persistenz-Kampagne vom Juni 2026: Internet-Scanner erreichten exponierte Dashboards (und OpenAI-API-Server) und brachten den Agenten dazu, einen SSH-Key-Backdoor zu installieren. Das Auth-Gate ist jetzt auf jedem Nicht-Loopback-Bind verpflichtend. Für eine vertrauenswürdige LAN / Homelab-Box ist der integrierte Benutzername/Passwort-Provider die Zero-Infrastruktur-Möglichkeit, dies zu erfüllen.

---

## Interaktiv betreiben (CLI-Chat)

Um eine interaktive Chat-Session gegen ein laufendes Datenverzeichnis zu öffnen:

```sh
docker run -it --rm \
  -v ~/.hermes:/opt/data \
  nousresearch/hermes-agent
```

Oder wenn du bereits ein Terminal in deinem laufenden Container geöffnet hast (z. B. über Docker Desktop), führe einfach aus:

```sh
/opt/hermes/.venv/bin/hermes
```

---

## Persistente Volumes

Das `/opt/data`-Volume ist die einzige Wahrheitsquelle für den gesamten Hermes-Zustand. Es wird auf das Verzeichnis `~/.hermes/` deines Hosts abgebildet und enthält:

| Pfad | Inhalt |
|---|---|
| `.env` | API-Keys und Secrets |
| `config.yaml` | Gesamte Hermes-Konfiguration |
| `SOUL.md` | Agenten-Persönlichkeit/-Identität |
| `sessions/` | Gesprächsverlauf |
| `memories/` | Persistenter Speicher |
| `skills/` | Installierte Skills |
| `home/` | Pro-Profil HOME für Hermes Tool-Subprozesse (`git`, `ssh`, `gh`, `npm` und Skill-CLIs) |
| `cron/` | Definitionen geplanter Jobs |
| `hooks/` | Event-Hooks |
| `logs/` | Laufzeitlogs |
| `skins/` | Benutzerdefinierte CLI-Skins |

### Unveränderlicher Install-Baum

In gehosteten und veröffentlichten Docker-Images ist `/opt/hermes` der installierte Anwendungsbaum. Er gehört Root und ist für den Laufzeit-`hermes`-Benutzer schreibgeschützt, sodass Agenten-Turns, Gateway-Sessions, Dashboard-Aktionen und normale `docker exec hermes hermes ...`-Befehle den Kern-Quellcode, das gebündelte `.venv`, `node_modules` oder das TUI-Bundle nicht bearbeiten können.

Aller veränderlicher Hermes-Zustand gehört unter `/opt/data`: Konfiguration, `.env`, Profile, Skills, Erinnerungen, Sessions, Logs, Dashboard-Uploads, Plugins und andere benutzerverwaltete Dateien.

!!! warning "Achtung"
    Führe niemals zwei Hermes-**Gateway**-Container gleichzeitig gegen dasselbe Datenverzeichnis aus – Session-Dateien und Speicherstores sind nicht für gleichzeitigen Schreibzugriff ausgelegt.

---

## Multi-Profil-Unterstützung

Hermes unterstützt [mehrere Profile](https://hermes-agent.nousresearch.com/docs/reference/profile-commands) – separate `~/.hermes/`-Unterverzeichnisse, die es dir ermöglichen, unabhängige Agenten (verschiedene SOUL, Skills, Erinnerungen, Sessions, Zugangsdaten) von einer einzigen Installation aus zu betreiben. **Im offiziellen Docker-Image behandelt der s6-Supervision-Baum jedes Profil als einen erstklassigen überwachten Dienst**, daher ist das empfohlene Deployment **ein Container, der alle Profile hostet**.

Jedes mit `hermes profile create <name>` erstellte Profil erhält:

- Einen dedizierten s6-Service-Slot unter `/run/service/gateway-<name>/`, dynamisch vom Laufzeitsystem registriert – kein Rebuild des Containers erforderlich.
- Automatischen Neustart bei Absturz, backoff-verwaltet von `s6-supervise`.
- Pro-Profil rotierende Logs unter `${HERMES_HOME}/logs/gateways/<name>/current` (10 Archive × 1 MB).
- Zustandspersistenz über Container-Neustarts hinweg.

Die Lifecycle-Befehle, die du auf dem Host verwenden würdest, funktionieren genauso von innerhalb des Containers:

```sh
# Profil erstellen – registriert den gateway-<name> s6-Slot.
docker exec hermes hermes profile create coder

# Starten / Stoppen / Neustarten
docker exec hermes hermes -p coder gateway start
docker exec hermes hermes -p coder gateway stop
docker exec hermes hermes -p coder gateway restart

# Status – meldet `Manager: s6 (container supervisor)` innerhalb des Containers.
docker exec hermes hermes -p coder gateway status

# Profil entfernen – baut auch den s6-Slot ab.
docker exec hermes hermes profile delete coder
```

### Mehr als ein Profil von außerhalb des Containers erreichen

**Hermes Desktop (und das Web-Dashboard):** Die Desktop-App spricht mit einem `hermes dashboard`-Backend (Standard **Port 9119**, aktiviert durch `HERMES_DASHBOARD=1`). Ein Dashboard-Backend bedient **alle** co-lokierten Profile: Der Profil-Switcher der App sendet das Zielprofil mit jeder Anfrage. Du benötigst also **keinen** zweiten Port pro Profil für Desktop.

**OpenAI-kompatible API-Clients (Open WebUI, LobeChat, `/v1/...`):** Diese sprechen mit dem **API-Server** jedes Profils, der **Port 8642 für jedes Profil** bindet. Wenn du möchtest, dass ein Client ein *bestimmtes* zweites Profil erreicht, gib diesem Profil einen eigenen `API_SERVER_PORT` in seiner eigenen `.env`-Datei:

```sh
# Profil erstellen (registriert seinen gateway-<name> s6-Slot)
docker exec hermes hermes profile create work

# API-Server auf einen freien Port zeigen lassen (in die .env des Profils schreiben)
cat >> /opt/data/profiles/work/.env <<'EOF'
API_SERVER_ENABLED=true
API_SERVER_PORT=8643
EOF

docker exec hermes hermes -p work gateway restart
```

### Warum ein Container mit vielen Profilen statt viele Container

| | Ein Container, viele Profile | Ein Container pro Profil |
|---|---|---|
| Festplattenaufwand | Ein Image, eine gebündelte venv, ein Playwright-Cache | N Images / N Caches |
| Speicheraufwand | Geteilter Python-Interpreter-Cache, geteilte node_modules | Pro Container dupliziert |
| Profilerstellung | `docker exec ... hermes profile create <name>` (Sekunden) | Neuer `docker run`-Aufruf + Port-Zuweisung + Bind-Mount-Konfiguration |
| Absturzwiederherstellung | `s6-supervise` Auto-Neustart | Dockers `--restart unless-stopped` (langsamer) |
| Logs | Pro-Profil rotierende Datei via `s6-log` | `docker logs <name>` pro Container – keine eingebaute Rotation |
| Backup | Ein `~/.hermes`-Verzeichnis | N Verzeichnisse zu koordinieren |

### Wann ein separater Container sinnvoll ist

Führe einen separaten Container pro Profil nur aus, wenn du einen spezifischen Grund hast:

- **Ressourcenisolierung pro Workload** – z. B. eine außer Kontrolle geratene Browser-Tool-Session in Profil A soll Profil B nicht zum OOM bringen. Container geben dir `--memory` / `--cpus` pro Profil.
- **Unabhängiges Image-Pinning** – verschiedene Upstream-Image-Tags pro Workload.
- **Netzwerksegmentierung** – verschiedene Docker-Netzwerke pro Profil.
- **Compliance / Explosionsradius** – verschiedene Zugangsdaten teilen niemals einen OS-Prozessbaum.

In diesen Fällen deklariere einen Dienst pro Profil mit unterschiedlichem `container_name`, `volumes` und `ports`:

```yaml
services:
  hermes-work:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-work
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"
    volumes:
      - ~/.hermes-work:/opt/data

  hermes-personal:
    image: nousresearch/hermes-agent:latest
    container_name: hermes-personal
    restart: unless-stopped
    command: gateway run
    ports:
      - "8643:8642"
    volumes:
      - ~/.hermes-personal:/opt/data
```

---

## Wo die Logs landen

Der s6-Container hat vier verschiedene Log-Oberflächen:

| Quelle | Wo es landet | Wie man es liest |
|---|---|---|
| **Pro-Profil-Gateway** (`hermes gateway run` und pro-Profil-Gateways unter s6) | Verzweigt zu zwei Orten: `docker logs <container>` (Echtzeit) **und** `${HERMES_HOME}/logs/gateways/<profile>/current` (rotierend, 10 Archive × 1 MB) | `docker logs -f hermes` oder `tail -F ~/.hermes/logs/gateways/default/current` auf dem Host |
| **Dashboard** (wenn `HERMES_DASHBOARD=1`) | `docker logs <container>` (kein Präfix) | `docker logs -f hermes` – vermischt mit Gateway-Zeilen |
| **Boot-Abgleicher** (zeichnet auf, welche Profil-Gateways bei jedem Container-Start wiederhergestellt wurden) | `${HERMES_HOME}/logs/container-boot.log` (Append-Only-Auditlog) | `tail -F ~/.hermes/logs/container-boot.log` |
| **Allgemeine Hermes-Logs** (`agent.log`, `errors.log`) | `${HERMES_HOME}/logs/` (profilbewusst) | `docker exec hermes hermes logs --follow [--level WARNING] [--session <id>]` |

---

## Umgebungsvariablen weiterleiten

API-Keys werden aus `/opt/data/.env` innerhalb des Containers gelesen. Du kannst Umgebungsvariablen auch direkt übergeben:

```sh
docker run -it --rm \
  -v ~/.hermes:/opt/data \
  -e ANTHROPIC_API_KEY="sk-ant-..." \
  -e OPENAI_API_KEY="sk-..." \
  nousresearch/hermes-agent
```

Direkte `-e`-Flags überschreiben Werte aus `.env`. Dies ist nützlich für CI/CD- oder Secrets-Manager-Integrationen, bei denen du keine Keys auf der Festplatte haben möchtest.

---

## Docker Compose Beispiel

Für ein persistentes Deployment mit Gateway und Dashboard ist eine `docker-compose.yaml` praktisch:

```yaml
services:
  hermes:
    image: nousresearch/hermes-agent:latest
    container_name: hermes
    restart: unless-stopped
    command: gateway run
    ports:
      - "8642:8642"   # Gateway API
      - "9119:9119"   # Dashboard (nur erreichbar wenn HERMES_DASHBOARD=1)
    volumes:
      - ~/.hermes:/opt/data
    environment:
      - HERMES_DASHBOARD=1
      # Auskommentieren, um bestimmte Umgebungsvariablen statt der .env-Datei weiterzuleiten:
      # - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
      # - OPENAI_API_KEY=${OPENAI_API_KEY}
      # - TELEGRAM_BOT_TOKEN=${TELEGRAM_BOT_TOKEN}
```

Starte mit:

```sh
docker compose up -d
```

---

## Docker-Image aktualisieren

```sh
# Neueste Version des Images herunterladen
docker pull nousresearch/hermes-agent:latest

# Laufenden Container stoppen und entfernen
docker stop hermes
docker rm hermes

# Container mit dem neuen Image neu starten
docker run -d \
  --name hermes \
  --restart unless-stopped \
  -v ~/.hermes:/opt/data \
  -p 8642:8642 \
  nousresearch/hermes-agent gateway run
```

Oder mit Docker Compose:

```sh
docker compose pull
docker compose up -d
```

Da alle Benutzerdaten im eingebundenen `/opt/data`-Volume (d. h. `~/.hermes/`) gespeichert werden, gehen bei einem Image-Update keine Konfigurationen, Sessions oder Erinnerungen verloren.

---

## Nützliche Docker-Befehle

```sh
# Logs in Echtzeit verfolgen
docker logs -f hermes

# Interaktive Shell im laufenden Container öffnen
docker exec -it hermes bash

# Hermes-Befehl im laufenden Container ausführen
docker exec hermes hermes gateway status

# Container-Statistiken anzeigen
docker stats hermes

# Container stoppen
docker stop hermes

# Container starten
docker start hermes

# Container neustarten
docker restart hermes
```

---

## Weiterführende Links

!!! tip "Tipp: Docker noch nicht installiert?"
    Falls Docker auf deinem Ubuntu Server 24.04 noch nicht eingerichtet ist, folge zunächst der Schritt-für-Schritt-Anleitung: [Docker auf Ubuntu Server 24.04 installieren](../../../entwicklung/infrastruktur/docker-installation-ubuntu.md)

- [Docker Installation (Ubuntu 24.04)](../../../entwicklung/infrastruktur/docker-installation-ubuntu.md) — Voraussetzung für diese Seite
- [Offizielle Docker-Dokumentation (englisch)](https://hermes-agent.nousresearch.com/docs/user-guide/docker)
- [Konfiguration → Docker Backend](https://hermes-agent.nousresearch.com/docs/user-guide/configuration#docker-backend)
- [Konfiguration → Modelle](https://hermes-agent.nousresearch.com/docs/user-guide/configuring-models)
- [Nous Portal](https://hermes-agent.nousresearch.com/docs/integrations/nous-portal)
- [Web Dashboard](https://hermes-agent.nousresearch.com/docs/user-guide/features/web-dashboard)
- [Profile verwalten](https://hermes-agent.nousresearch.com/docs/reference/profile-commands)
