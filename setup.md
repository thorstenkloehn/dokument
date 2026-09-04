
### 1. Python Virtuelle Umgebung einrichten

```bash
# Virtuelle Umgebung erstellen
python3 -m venv .venv

# Virtuelle Umgebung aktivieren (Linux/macOS)
source .venv/bin/activate
```

### 2. Python-Abhängigkeiten installieren

Installieren Sie Zensical sowie die benötigten Markdown-Erweiterungen:

```bash
pip install -r requirements.txt
```

### 3. Node.js-Abhängigkeiten installieren

```bash
npm install
```

### 4. Git-Hooks aktivieren

Der Pre-Commit-Hook (`.gemini/hooks/pre-commit`) führt vor jedem Commit automatisch `zensical build` aus und bricht bei Fehlern ab. Git verwendet Hooks nur aus `.git/hooks/` oder einem per `core.hooksPath` konfigurierten Verzeichnis — diese Einstellung liegt in `.git/config` und wird **nicht** von Git selbst versioniert, muss also nach jedem frischen Checkout einmalig gesetzt werden:

```bash
git config core.hooksPath .gemini/hooks
```

---

## Lokale Entwicklung

Starten Sie den lokalen Entwicklungsserver, um Änderungen in Echtzeit zu sehen:

```bash
.venv/bin/zensical serve
```

Die Webseite ist anschließend unter [http://127.0.0.1:8000](http://127.0.0.1:8000) erreichbar. Änderungen an den Markdown-Dateien oder der Konfiguration werden automatisch neu geladen.

---

## Build & Veröffentlichung (Deployment)

### 1. Statische Seite lokal bauen

```bash
.venv/bin/zensical build
```

Die fertigen Dateien werden im Ordner `site/` abgelegt.

### 2. Auf GitHub Pages veröffentlichen

Die Veröffentlichung auf `dokument.wissen-ahrensburg.de` erfolgt automatisiert:

```bash
npm run ver
```

*Dieses Skript baut die Seite mit Zensical und pusht den Inhalt des `site/`-Ordners in den `gh-pages`-Branch.*

---

## Migration von MkDocs zu Zensical (Juli 2026)

| | Vorher | Nachher |
|---|---|---|
| Framework | MkDocs 1.6.1 + Material 9.7.6 | **Zensical 0.0.51** |
| Build-Befehl | `mkdocs build` | `zensical build` |
| Serve-Befehl | `mkdocs serve` | `zensical serve` |
| Build-Zeit | ~11s | ~6s |
| Konfiguration | `mkdocs.yml` | `mkdocs.yml` *(unverändert)* |
| Plugin-System | mkdocs-git-authors, minify, tags | Built-in in Zensical |

