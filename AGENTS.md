# AGENTS.md – KI-Regeln und Projekt-Guidelines

Diese Richtlinien müssen von allen KI-Agenten bei der Bearbeitung dieses Repositories zwingend befolgt werden.

## 🛠️ Projektübersicht
* **Projekt**: Statische Dokumentation basierend auf **Zensical** (Nachfolger von Material for MkDocs, vom gleichen Team entwickelt).
* **Konfiguration**: `mkdocs.yml` wird von Zensical nativ gelesen – keine separate Konfigurationsdatei nötig.
* **Sprache**: Gesamter Content ist in deutscher Sprache (Ausnahme: technische Begriffe).
* **Ziel**: Strukturierte Dokumentation der Serverlandschaft, lokalen Entwicklungsumgebung, Automatisierungstools, Video-/Audioverarbeitung und KI-Integration.

> **Hinweis**: MkDocs 2.0 ist ein inkompatibler Rewrite ohne Plugin-Unterstützung und wird **nicht** verwendet. Zensical ist die empfohlene Nachfolge-Lösung.

## 📁 Verzeichnisstruktur (unter `docs/`)
Die Dokumentation ist in folgende Hauptbereiche unterteilt:
* `docs/künstliche-intelligenz/`
  * `coding/` - KI-Coding, Vibe Coding, Programmieren lernen
  * `content/` - KI Content-Creation, SEO, Social Media, Multilinguale Inhalte
  * `automatisierung/` - PyAutoGUI, Playwright, ydotool, Robot Framework
* `docs/entwicklung/`
  * `webentwicklung/` - KI Webentwicklung, Frontend, Backend, Deployment, Performance
  * `infrastruktur/` - Server-Konfigurationen (Nginx, PostgreSQL, Tomcat, Kachelserver etc.)
  * `system/` - Assembler, Compiler, Rust/C/C++, Linux-Systemprogrammierung
  * `ide/` - Lokale Entwicklungsumgebung, KI-Coding-Tools, Android Setup
* `docs/kreativ/`
  * `design/` - KI-gestützte Design-Ideenfindung & Methoden
  * `audio/` - KI Audio, Audacity, DAW, MIDI, Audio-Processing
  * `video/` - KI in Film- und Videoproduktion
* `docs/wissen/`
  * `daten/` - Datenbanken & Datenerfassung (OpenDataKit)
  * `e-learning/` - Konzepte für digitales Lernen & KI in der Lehre
  * `tools/` - Pandoc, Analysetool, Benchmark
  * `dokumentation/` - MediaWiki, Semantisches MediaWiki, XWiki
* `docs/rechtliches/` - Impressum & Datenschutz

## 📌 Wichtige Regeln & Best Practices

### 1. Navigation & Struktur (`mkdocs.yml`)
* **Zwingendes Navigations-Update**: Jede neu hinzugefügte Markdown-Datei unter `docs/` **muss** im Navigations-Menü (`nav`) in `mkdocs.yml` eingetragen werden.
* **Validierung**: Nach dem Hinzufügen von Seiten muss `.venv/bin/zensical build` ausgeführt werden. Es dürfen keine Fehler oder Warnungen auftreten.

### 2. Markdown & Mermaid
* **Dateinamen**: Kleingeschrieben oder in CamelCase/Kebab-Case, passend zur Kategorie.
* **Interne Links**: Immer relativ verlinken (z. B. `[PostgreSQL](Server/Postgresql.md)`). Keine absoluten Pfade verwenden.
* **Mermaid-Diagramme**: Werden nativ via `superfences` unterstützt. Immer in exakt dieser Form schreiben:
  ```markdown
  ```mermaid
  graph TD
      A --> B
  ```
  ```

### 3. Befehle & Deployment
* **Abhängigkeiten installieren**:
  * Python: `.venv/bin/pip install -r requirements.txt`
  * Node.js: `npm install`
* **Lokal testen**:
  * Build erstellen: `.venv/bin/zensical build`
  * Lokalen Server starten: `.venv/bin/zensical serve`
* **Deployment**:
  * Deployment auf GitHub Pages: `npm run ver`
  *(Das Skript baut das Verzeichnis und stellt es online unter `dokument.wissen-ahrensburg.de`)*

> **Nicht verwenden**: `.venv/bin/mkdocs build` oder `.venv/bin/mkdocs serve` – MkDocs wurde durch Zensical ersetzt.

