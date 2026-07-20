# AGENTS.md – KI-Regeln und Projekt-Guidelines

Diese Richtlinien müssen von allen KI-Agenten bei der Bearbeitung dieses Repositories zwingend befolgt werden.

## 🛠️ Projektübersicht

* **Projekt**: Statische Dokumentation basierend auf **Zensical** (Nachfolger von Material for MkDocs, vom gleichen Team entwickelt).
* **Website**: [dokument.wissen-ahrensburg.de](https://dokument.wissen-ahrensburg.de)
* **Konfiguration**: `mkdocs.yml` wird von Zensical nativ gelesen – keine separate Konfigurationsdatei nötig.
* **Sprache**: Gesamter Content ist in **deutscher Sprache** (Ausnahme: technische Begriffe, Code, Befehle).
* **Ziel**: Strukturierte Dokumentation zu KI, Entwicklung, Kreativ-Workflows und Wissensmanagement.

> **Wichtig – MkDocs 2.0**: MkDocs 2.0 ist ein inkompatibler Rewrite ohne Plugin-Unterstützung und wird **nicht** verwendet. Zensical ist die empfohlene Nachfolge-Lösung.

---

## 📁 Verzeichnisstruktur

```
dokument/
├── docs/                        # Gesamter Markdown-Content
│   ├── index.md                 # Startseite
│   ├── tags.md                  # Tags-Übersicht (auto-generiert)
│   ├── stylesheets/
│   │   └── extra.css            # Custom CSS
│   ├── künstliche-intelligenz/
│   │   ├── coding/              # KI-Coding, Vibe Coding, LLMs, Agenten
│   │   ├── content/             # KI Content-Creation, SEO, Social Media
│   │   └── automatisierung/     # PyAutoGUI, Playwright, ydotool, Robot Framework
│   ├── entwicklung/
│   │   ├── erste-schritte.md    # Einstieg Entwicklung
│   │   ├── webentwicklung/      # Frontend, Backend, Deployment, Performance
│   │   ├── infrastruktur/       # Nginx, PostgreSQL, Tomcat, Docker, Kachelserver
│   │   ├── system/              # Assembler, Compiler, Rust/C/C++, Linux
│   │   └── ide/                 # Setup, Android, Lokale KI-Frontends
│   ├── kreativ/
│   │   ├── design/              # KI Design, ComfyUI, Blender
│   │   ├── audio/               # Audacity, DAW, MIDI, Audio-Processing
│   │   └── video/               # FFmpeg, Manim, Remotion
│   ├── wissen/
│   │   ├── daten/               # Datenbanken, pgvector, OpenDataKit
│   │   ├── e-learning/          # KI in der Lehre
│   │   ├── tools/               # Pandoc, Analysetool, Benchmark
│   │   └── dokumentation/       # MediaWiki, Semantisches MediaWiki, XWiki
│   └── rechtliches/             # Impressum, Datenschutz
├── overrides/                   # Zensical/MkDocs Theme-Overrides
├── mkdocs.yml                   # Haupt-Konfiguration (nav, theme, plugins)
├── requirements.txt             # Python-Abhängigkeiten (Zensical)
├── package.json                 # npm-Skripte (Deployment)
├── AGENTS.md                    # Diese Datei – KI-Regeln
└── README.md                    # Projektbeschreibung
```

---

## 📌 Wichtige Regeln & Best Practices

### 1. Navigation & Struktur (`mkdocs.yml`)

* **Zwingendes Navigations-Update**: Jede neu hinzugefügte Markdown-Datei unter `docs/` **muss** im Navigations-Menü (`nav`) in `mkdocs.yml` eingetragen werden.
* **Validierung**: Nach dem Hinzufügen oder Ändern von Seiten immer `.venv/bin/zensical build` ausführen. Es dürfen **keine Fehler oder Warnungen** auftreten.
* **Struktur einhalten**: Neue Seiten immer in den passenden Unterordner einordnen (s. Verzeichnisstruktur oben).

### 2. Markdown & Inhalte

* **Dateinamen**: Kebab-Case, kleingeschrieben (z. B. `ki-coding.md`, `erste-schritte.md`).
* **Sprache**: Deutsch – auch Überschriften, Admonitions und Beschreibungen.
* **Interne Links**: Immer **relativ** verlinken (z. B. `[PostgreSQL](../infrastruktur/postgresql.md)`). Keine absoluten Pfade.
* **Bilder**: Unter `docs/assets/` ablegen und relativ verlinken.
* **Admonitions** (Hinweisboxen) in Deutsch:
  ```markdown
  !!! tip "Tipp"
      Inhalt hier.

  !!! warning "Achtung"
      Wichtiger Hinweis.

  !!! note "Hinweis"
      Ergänzende Information.
  ```

### 3. Mermaid-Diagramme

Werden nativ via `superfences` unterstützt. Immer **exakt** in dieser Form schreiben:

````markdown
```mermaid
graph TD
    A --> B
```
````

### 4. Tabs (Content Tabs)

```markdown
=== "Tab 1"
    Inhalt Tab 1

=== "Tab 2"
    Inhalt Tab 2
```

---

## 🔧 Befehle & Deployment

### Abhängigkeiten installieren

```bash
# Python-Umgebung einrichten
python3 -m venv .venv
source .venv/bin/activate

# Zensical und Erweiterungen installieren
.venv/bin/pip install -r requirements.txt

# Node.js-Pakete (für Deployment)
npm install
```

### Lokal entwickeln

```bash
# Lokalen Server starten (Hot-Reload)
.venv/bin/zensical serve

# Nur bauen (ohne Server)
.venv/bin/zensical build
```

### Deployment

```bash
# Auf GitHub Pages veröffentlichen (baut + deployed automatisch)
npm run ver
```

*Publiziert unter: `dokument.wissen-ahrensburg.de`*

> ❌ **Nicht verwenden**: `.venv/bin/mkdocs build` oder `.venv/bin/mkdocs serve` – MkDocs wurde durch Zensical ersetzt.

---

## 🤖 KI-Agenten: Workflow beim Erstellen neuer Seiten

Wenn ein KI-Agent eine neue Dokumentationsseite erstellt, **muss** er folgende Schritte in dieser Reihenfolge durchführen:

1. **Markdown-Datei erstellen** im richtigen Unterordner unter `docs/`
2. **Navigation eintragen** – Eintrag in `mkdocs.yml` unter `nav:` ergänzen
3. **Build ausführen** – `.venv/bin/zensical build` – keine Fehler erlaubt
4. **Git commit** – sinnvolle Commit-Message auf Deutsch oder Englisch
5. **Optional: Deployment** – `npm run ver` wenn die Änderung live gehen soll

### Commit-Message-Format

```
docs: Kurze Beschreibung was hinzugefügt/geändert wurde

- Detail 1
- Detail 2
```

---

## 🚫 Verbotene Aktionen

* `mkdocs build` oder `mkdocs serve` aufrufen (veraltet)
* MkDocs 2.0 installieren oder verwenden
* Markdown-Dateien ohne Nav-Eintrag in `mkdocs.yml` hinzufügen
* Absolute Pfade in internen Links verwenden
* Englischsprachige Inhalte erstellen (außer Code/Befehle)
* Dateien in `site/` oder `node_modules/` bearbeiten (auto-generiert)

---

## 📦 Abhängigkeiten (Stand Juli 2026)

| Paket | Version | Zweck |
|---|---|---|
| `zensical` | ≥ 0.0.51 | Static Site Generator (MkDocs-Nachfolger) |
| `pymdown-extensions` | ≥ 11.0.1 | Mermaid, Tabs, Highlights, Snippets |
| `gh-pages` (npm) | ^6.1.1 | GitHub Pages Deployment |

---

## 🌐 Technischer Stack

| Komponente | Technologie |
|---|---|
| Site Generator | Zensical 0.0.51 |
| Konfiguration | `mkdocs.yml` (von Zensical nativ gelesen) |
| Theme | Material Design (in Zensical built-in) |
| Deployment | GitHub Pages via `gh-pages` npm-Paket |
| Domain | `dokument.wissen-ahrensburg.de` |
| Python-Env | `.venv/` (nicht in Git) |
