# Dokumentation (Zensical)

Dieses Repository enthält die Quelldateien für die Dokumentations-Webseite unter **[dokument.wissen-ahrensburg.de](https://dokument.wissen-ahrensburg.de)**. Die Seite wird mit **[Zensical](https://zensical.org)** generiert – dem modernen Nachfolger von Material for MkDocs, entwickelt vom gleichen Team.

> **Hinweis:** Das Projekt wurde im Juli 2026 von MkDocs + Material Theme auf **Zensical** migriert.
> MkDocs 2.0 ist ein inkompatibler Rewrite und wird **nicht** verwendet.
> Zensical liest die bestehende `mkdocs.yml` nativ – der gesamte Content bleibt unverändert.

---

## Voraussetzungen

Stellen Sie sicher, dass folgende Software auf Ihrem System installiert ist:

* **Python 3.8+** (inklusive `pip` und `venv`)
* **Node.js & npm** (für die Veröffentlichung via GitHub Pages)

---

## Installation & Einrichtung

Folgen Sie diesen Schritten, um die Entwicklungsumgebung lokal einzurichten:

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
