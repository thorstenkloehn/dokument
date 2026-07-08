# Dokumentation (MkDocs & Material Theme)

Dieses Repository enthält die Quelldateien für die Dokumentations-Webseite. Die Seite wird mit **MkDocs** und dem modernen **Material for MkDocs** Theme generiert.

---

## Voraussetzungen

Stellen Sie sicher, dass folgende Software auf Ihrem System installiert ist:
* **Python 3.8+** (inklusive `pip` und `venv`)
* **Node.js & npm** (für die Veröffentlichung via GitHub Pages)

---

## Installation & Einrichtung

Folgen Sie diesen Schritten, um die Entwicklungsumgebung lokal einzurichten:

### 1. Python Virtuelle Umgebung einrichten
Erstellen und aktivieren Sie eine virtuelle Umgebung im Projektverzeichnis, um die Python-Pakete isoliert zu installieren:

```bash
# Virtuelle Umgebung erstellen
python3 -m venv .venv

# Virtuelle Umgebung aktivieren (Linux/macOS)
source .venv/bin/activate

# Virtuelle Umgebung aktivieren (Windows - Command Prompt)
# .venv\Scripts\activate.bat

# Virtuelle Umgebung aktivieren (Windows - PowerShell)
# .venv\Scripts\Activate.ps1
```

### 2. Python-Abhängigkeiten installieren
Installieren Sie MkDocs, das Material-Theme sowie die benötigten Markdown-Erweiterungen innerhalb der aktivierten virtuellen Umgebung:

```bash
pip install mkdocs mkdocs-material pymdown-extensions
```

### 3. Node.js-Abhängigkeiten installieren
Installieren Sie die für das Deployment benötigten npm-Pakete (z. B. `gh-pages`):

```bash
npm install
```

---

## Lokale Entwicklung

Starten Sie den lokalen MkDocs-Entwicklungsserver, um Änderungen in Echtzeit im Browser zu sehen:

```bash
# Stellen Sie sicher, dass die virtuelle Umgebung (.venv) aktiv ist!
mkdocs serve
```

Die Webseite ist anschließend unter [http://127.0.0.1:8000](http://127.0.0.1:8000) erreichbar. Änderungen an den Markdown-Dateien oder der Konfiguration werden automatisch neu geladen.

---

## Build & Veröffentlichung (Deployment)

### 1. Statische Seite lokal bauen
Wenn Sie die Seite lokal als statische HTML-Dateien generieren möchten:

```bash
mkdocs build
```
Die fertigen Dateien werden im Ordner `site/` abgelegt.

### 2. Auf GitHub Pages veröffentlichen
Die Veröffentlichung auf der konfigurierten Domain `dokument.wissen-ahrensburg.de` erfolgt automatisiert über ein npm-Skript:

```bash
npm run ver
```
*Dieses Skript baut die Seite automatisch und pusht den Inhalt des `site/`-Ordners in den `gh-pages`-Branch.*
