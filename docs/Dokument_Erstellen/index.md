# Dokumentenerstellung, Wikis & Notebooks

Diese Kategorie bietet eine strukturierte Übersicht über Systeme zur Dokumentenerstellung, kollaborative Wikis, interaktive Notebooks sowie Werkzeuge zur programmatischen Generierung von Dokumenten und zur Anbindung von KI-Agenten (RAG).

```mermaid
graph TD
    A[Dokumentenerstellung] --> B[Book-First Generatoren]
    A --> C[Notebook-Systeme]
    A --> D[Wikis & Wissensdatenbanken]
    A --> E[Programmatische Office-Automation]
    
    B --> B1[mdBook / MkDocs / Docusaurus]
    C --> C1[Quarto / Jupyter / Marimo]
    D --> D1[Flat-File / RAG-Co-Wikis]
    E --> E1[python-docx / OpenPyXL / Pandoc]
```

---

## 1. Die "Book-First" Generatoren (Markdown/AsciiDoc)

Tools, die speziell für das Erstellen strukturierter Bücher, Handbücher und langlebiger Dokumentationen optimiert sind. Sie nutzen meist Git als Versionskontrolle.

* **mdBook** (Rust): Ein extrem schneller, in Rust geschriebener Generator. Erzeugt schlanke, durchsuchbare HTML-Bücher aus Markdown-Dateien. Ideal für technische Handbücher.
* **Antora** (JavaScript): Ein professioneller Generator für Multi-Repository-Dokumentationen. Basiert auf **AsciiDoc** statt Markdown, was erweiterte Features für Cross-Referenzen und modulare Strukturierung bietet.
* **Starlight** (Astro/TypeScript): Ein modernes, auf Astro basierendes Dokumentations-Framework. Bietet hervorragende Performance (Zero-JS-Standard), integrierte Suche, Internationalisierung und ein modernes UI.
* **MkDocs** (Python): Ein statischer Site-Generator, der einfach über YAML konfiguriert wird. Mit dem **Material for MkDocs** Theme (wie in diesem Projekt genutzt) gehört es zu den optisch ansprechendsten und funktionalsten Lösungen.
* **Docusaurus** (React/TypeScript): Ein von Meta entwickeltes Dokumentations-Framework. Ermöglicht die nahtlose Integration von React-Komponenten in Markdown (MDX), ideal für komplexe Web-Dokumentationen.
* **HonKit** (TypeScript): Ein moderner, aktiv gepflegter Fork von GitBook (Legacy CLI), um Bücher aus Markdown-Dateien zu generieren.

---

## 2. Interaktive & "Executable" Notebook-Systeme

Systeme, die ausführbaren Code, Visualisierungen und erklärenden Text in einem interaktiven Dokument vereinen.

* **Quarto** (CLI): Das moderne Nachfolgesystem von R Markdown. Unterstützt Python, R, Julia und Observable JS. Ermöglicht das Rendern von Notebooks in hochqualitative PDFs, HTML-Seiten, wissenschaftliche Arbeiten und Präsentationen.
* **JupyterLab / Jupyter Book**: Der Industriestandard für Data Science. JupyterLab bietet eine vollständige Entwicklungsumgebung im Browser, während Jupyter Book eine Sammlung von Notebooks als schönes Online-Buch veröffentlicht.
* **Livebook** (Elixir): Ein kollaboratives, interaktives Notebook-System für Elixir mit integrierter Echtzeit-Zusammenarbeit und Unterstützung für Machine-Learning-Pipelines.

### Eigene Notebook-UIs bauen (Core Web Components)
* **JupyterLab Components**: Wiederverwendbare Webkomponenten direkt aus dem JupyterLab-Ökosystem, um eigene Web-UIs mit Notebook-Support zu erstellen.
* **nteract**: Ein Set aus React-Komponenten und SDKs für den Bau individueller Notebook-Anwendungen.

### In-Browser Execution (Ausführung ohne Server-Backend)
* **JupyterLite**: Ein JupyterLab-Derivat, das vollständig im Browser läuft (via WebAssembly / Pyodide). Es benötigt keinen Jupyter-Server im Hintergrund.
* **Marimo** (Python): Ein reaktives Notebook für Python. Im Gegensatz zu Jupyter führt Marimo Code-Zellen bei Änderungen automatisch aus (ähnlich wie eine Excel-Tabelle), verhindert veraltete Zustände und läuft via Pyodide auch komplett serverlos im Browser.
* **Observable**: Ein reaktives Notebook-System für JavaScript, optimiert für Datenvisualisierung (D3.js) und interaktives Prototyping.

### Jupyter-Protokoll & Kernel-Management (Das Backend)
* **JupyterHub / Kernel Gateway**: Zentralisierte Server-Infrastrukturen zur Bereitstellung von Notebook-Umgebungen für Teams und zum programmatischen Ausführen von Code über APIs.
* **Voila**: Konvertiert Jupyter Notebooks in eigenständige, interaktive Webanwendungen und Dashboards, indem der darunterliegende Code vor dem Endnutzer verborgen wird.

### Full-Stack Programmatic Notebook Engines
* **Papermill**: Erlaubt die Parametrisierung und automatisierte Ausführung von Jupyter Notebooks über die Kommandozeile oder APIs.
* **Nbconvert**: Das Standard-Utility-Tool zur Konvertierung von Notebooks (`.ipynb`) in HTML, PDF, Markdown oder ausführbare Skripte.

---

## 3. Lokale Dokumentations-Wikis & Wissensdatenbanken

Systeme zur Organisation und Durchsuchung von Notizen, firmeninternem Wissen oder technischen Wikis.

### Flat-File-Wikis (Ohne relationale Datenbank)
* **DokuWiki**: Ein bewährtes, PHP-basiertes Wiki, das alle Seiten als einfache Textdateien speichert. Extrem wartungsfreundlich und ohne Datenbank-Overhead.
* **BookStack**: Ein modernes, einfach zu bedienendes Wiki mit einer hierarchischen Struktur (Bücher, Kapitel, Seiten), das sich hervorragend für Teamblogs und strukturierte Anleitungen eignet.
* **Wiki.js**: Ein mächtiges, modernes Wiki auf Node.js-Basis. Bietet Git-Sync, Markdown-Editoren und flexible Suchmaschinen wie **FlexSearch** oder lokale Front-Matter-Parser.

### Rein statische Generatoren (Git-basiert / Local-First)
* **Obsidian**: Eine hochgradig anpassbare Local-First-Notiz-App, die auf einem lokalen Ordner von Markdown-Dateien basiert und Verknüpfungen (Backlinks) visualisieren kann.
* **Logseq**: Eine datenschutzfreundliche Outliner-Wissensdatenbank (Local-First) mit PDF-Annotationen und Flashcards, basierend auf Markdown- oder Org-Mode-Dateien.
* **Quartz (v4)** (TypeScript): Ein statischer Generator, der Obsidian-Tresore (Markdown-Dateien mit Wiki-Links) direkt in eine schnelle, interaktive Website übersetzt.

### Die Schwergewichte (Multi-Tenancy & Strukturierte Daten)
* **MediaWiki**: Das PHP-Schwergewicht hinter Wikipedia. Perfekt für riesige Enzyklopädien und stark strukturierte Wikitext-Inhalte.
* **XWiki**: Ein Enterprise-Wiki auf Java-Basis, das strukturierte Daten, eigene Applikationen innerhalb von Wiki-Seiten und tiefgreifende Rechteverwaltung unterstützt.
* **Tiptap / Tiptap Collab**: Eine headless WYSIWYG-Editor-Bibliothek für moderne Web-UIs, die kollaboratives Schreiben in Echtzeit (wie in Google Docs oder Notion) ermöglicht.

---

## 4. RAG- & KI-Zentrierte Wissensdatenbanken (RAG-Co-Wikis)

Systeme und Pipelines, die Wikis und Dokumente für Large Language Models (LLMs) aufbereiten oder als intelligente Co-Wikis mit RAG-Anbindung fungieren.

### RAG- & KI-Wiki-Tools
* **Anytype** (Local-First): Ein verschlüsseltes, objektbasiertes Wiki (Notion-Alternative), das auf dem IPFS-Netzwerk basiert.
* **Affine.pro**: Ein kollaborativer Workspace, der klassischen Text-Editor (Notion-Style) und unendliches Whiteboard (Miro-Style) in einem Open-Source-Tool vereint.
* **Outline**: Ein wunderschönes, schnelles Open-Source-Wiki für Teams mit nativer Markdown-Unterstützung und exzellenter API.
* **Danswer**: Ein Open-Source-RAG-System, das sich mit all deinen Datenquellen (Slack, Google Drive, Wikis) verbindet und direkte Antworten auf Nutzerfragen liefert.

### Orchestrierung & RAG-Pipelines
* **Dify.ai / Flowise**: Visuelle Editoren zum Erstellen von LLM-Anwendungen, RAG-Pipelines und KI-Agenten, die direkt auf Dokumenten-Repositorys zugreifen.
* **LangChain / LangGraph / LlamaIndex**: Frameworks zur datenbezogenen Orchestrierung, dem Laden, Splitten, Einbetten (Embedding) und Abfragen von Dokumenten-Wikis.
* **ChromaDB / LanceDB** (Embedded): Leichtgewichtige, eingebettete Vektordatenbanken für lokale Setups ohne Server-Infrastruktur.
* **Qdrant / Milvus** (Production): Skalierbare Enterprise-Vektordatenbanken für Millionen von Dokumenten-Vektoren mit komplexer Metadaten-Filterung.
* **Model Context Protocol (MCP)**: Ein Standard von Anthropic. Anstatt einer KI rohen Text zu geben, baut man einen MCP-Server vor sein Wiki, über den Agenten standardisierte Tools (`search_wiki`, `get_article`, `list_categories`) nutzen können.

---

## 5. Office Suites & Programmatische Dokumentenerstellung

Werkzeuge zur automatisierten Generierung und Bearbeitung von Office-Dokumenten (Word, Excel, PowerPoint) direkt aus Code heraus.

### Office-Suiten (Das Frontend)
* **LibreOffice / ONLYOFFICE / WPS Office**: Standard-Office-Suiten. ONLYOFFICE eignet sich durch seine HTML5-Canvas-Rendering-Engine hervorragend zur Integration in eigene Webanwendungen.

### Programmatische Generierung (Code-Bibliotheken)
* **LibreOffice UNO**: Die API von LibreOffice, um Dokumente im Hintergrund (headless) zu manipulieren oder in andere Formate (z. B. DOCX/PPTX zu PDF) zu konvertieren.
* **python-docx** (Python): Ermöglicht das automatisierte Erstellen und Modifizieren von Microsoft Word (`.docx`) Dateien.
* **Apache POI** (Java): Die mächtigste Bibliothek zur Java-basierten Manipulation aller Microsoft Office-Formate.
* **OpenPyXL** (Python) / **libxlsxwriter** (C/C++): Bibliotheken zum Schreiben und Lesen von Excel-Tabellen (`.xlsx`) inklusive Diagrammen und Formatierungen.
* **Calamine** (Rust): Ein extrem schneller Excel-Reader in reinem Rust.
* **python-pptx** (Python): Zum programmatischen Erstellen von PowerPoint-Präsentationen.
* **DuckX** (C++): Eine leichtgewichtige C++-Bibliothek zum Lesen und Schreiben von DOCX-Dateien.
* **Pandoc** (Haskell): Das "Schweizer Taschenmesser" der Dokumentenkonvertierung. Konvertiert fast jedes Format (Markdown, HTML, DOCX, LaTeX, MediaWiki, ePub) per Kommandozeile in ein anderes.

---

## 🤖 KI-Agenten-Tauglichkeit & RAG-Integration

Für autonome Entwickler-Agenten (wie Claude Code, Antigravity CLI) und RAG-Systeme eignen sich die dokumentenbasierten Pipelines unterschiedlich gut:

1. **Markdown & Git (z. B. MkDocs, mdBook, Quartz)** – **Hervorragend geeignet:**
   Da alle Seiten als reine Textdateien im Git-Repository liegen, können KI-Agenten Inhalte direkt bearbeiten, neue Seiten erstellen, Links anpassen und Commits erstellen. Zudem ist Markdown extrem token-effizient für LLMs.
2. **MCP-Server vor Wikis (z. B. Wiki.js, Outline)** – **Sehr gut geeignet:**
   Erlaubt es Agenten, gezielte Suchen über standardisierte APIs auszuführen, anstatt das gesamte Dokumentationsarchiv in den Prompt laden zu müssen.
3. **Pandoc-Pipelines** – **Sehr gut geeignet:**
   KI-Agenten können Pandoc nutzen, um formatierte Berichte aus Markdown-Dateien zu kompilieren (z. B. Markdown -> PDF) oder Eingabedokumente (z. B. Word-Dateien) vor dem Einlesen in Markdown zu übersetzen.
4. **Notebooks (z. B. Papermill, Jupyter-Kernel)** – **Sehr gut geeignet:**
   Agenten können Datenanalyse-Skripte direkt in Notebook-Zellen schreiben und ausführen, um Daten zu bereinigen und interaktive Visualisierungen zu generieren.
5. **Relational- & NoSQL-Wikis (z. B. MediaWiki)** – **Bedingt geeignet:**
   Änderungen erfordern oft Datenbank-Queries oder die Nutzung komplexer Web-APIs, was für Agenten fehleranfälliger und unübersichtlicher ist als direkte Datei-Interaktionen.