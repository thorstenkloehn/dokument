# AGENTS.md – KI-Regeln und Projekt-Guidelines

Diese Richtlinien müssen von allen KI-Agenten bei der Bearbeitung dieses Repositories zwingend befolgt werden.

## 🛠️ Projektübersicht
* **Projekt**: Statische Dokumentation basierend auf **MkDocs** mit dem **Material Theme**.
* **Sprache**: Gesamter Content ist in deutscher Sprache (Ausnahme: technische Begriffe).
* **Ziel**: Strukturierte Dokumentation der Serverlandschaft, lokalen Entwicklungsumgebung, Automatisierungstools, Video-/Audioverarbeitung und KI-Integration.

## 📁 Verzeichnisstruktur (unter `docs/`)
Die Dokumentation ist in folgende Hauptbereiche unterteilt:
* `docs/Server/` - Server-Konfigurationen (Nginx, PostgreSQL, Tomcat, Kachelserver etc.)
* `docs/IDE/` - Lokale Entwicklungsumgebung, KI-Coding-Tools, Android Setup
* `docs/Video/` - Video- & Animationstools (Remotion, FFmpeg, Blender, Manim etc.)
* `docs/Content/` - KI-gestützte Content-Erstellung
* `docs/Design/` - Design & Ideenfindung mit KI
* `docs/Webentwicklung/` - Webentwicklung mit KI-Unterstützung
* `docs/Coding/` - KI-Coding-Guides und Programmierkonzepte
* `docs/Desktop_Automation/` - GUI- und Desktop-Automatisierung
* `docs/E-Learning-Autorentool/` - Konzepte für digitales Lernen
* `docs/Audio/` - Programmatische Audio- & Musikverarbeitung
* `docs/Datenerfassung/` - Datenerhebungstools (z. B. OpenDataKit)
* `docs/Dokument_Erstellen/` - Wissensdatenbanken & Generatoren (Mediawiki, Xwiki, Notebooks)
* `docs/Tools/` - Allgemeine Hilfswerkzeuge (Pandoc, Analysetool, Benchmark)

## 📌 Wichtige Regeln & Best Practices

### 1. Navigation & Struktur (`mkdocs.yml`)
* **Zwingendes Navigations-Update**: Jede neu hinzugefügte Markdown-Datei unter `docs/` **muss** im Navigations-Menü (`nav`) in `mkdocs.yml` eingetragen werden.
* **Validierung**: Nach dem Hinzufügen von Seiten muss `.venv/bin/mkdocs build` ausgeführt werden. Es dürfen keine Warnungen wie `"The following pages exist in the docs directory, but are not included in the 'nav' configuration"` auftreten.

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
  * Build erstellen: `.venv/bin/mkdocs build`
  * Lokalen Server starten: `.venv/bin/mkdocs serve`
* **Deployment**:
  * Deployment auf GitHub Pages: `npm run ver`
  *(Das Skript baut das Verzeichnis und stellt es online unter `dokument.wissen-ahrensburg.de`)*

