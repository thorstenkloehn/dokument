# Dokumentation für meine Entwicklungsumgebung und den Einsatz von Servern

Willkommen in meiner zentralen Dokumentation. Diese Wissensdatenbank dient der Strukturierung und Erfassung aller Konfigurationen, Installationsanleitungen und Technologie-Übersichten für meine Serverlandschaft und lokale Entwicklungsumgebung.

---

## 📁 Dokumentationskategorien

Diese Dokumentation ist in die folgenden Hauptbereiche unterteilt. Jede Kategorie deckt einen spezifischen Bereich ab:

### 1. [Server & Infrastruktur](Server/Software.md)
Dieser Bereich befasst sich mit der Konfiguration, Installation und Absicherung von Serverdiensten auf dem Produktionsserver (Ubuntu 24.04 LTS) und lokalen Entwicklungsumgebungen. Er umfasst:

* **Datenbanken**: Einrichtung und Verwaltung von [PostgreSQL](Server/Postgresql.md) mit PostGIS für räumliche Daten.
* **Kachelserver (Tileserver)**: Detaillierte Schritt-für-Schritt-Anleitungen zur Einrichtung eines OpenStreetMap-Kachelservers unter verschiedenen Ubuntu-Versionen ([Ubuntu 20.04](Server/Kachelserver/Server204.md), [Ubuntu 22.04](Server/Kachelserver/Server224.md) und [Ubuntu 24.04](Server/Kachelserver/Server244.md)).
* **Webserver & Reverse Proxy**: Konfiguration von [Nginx](Server/nginx.md), Einbindung von [SSL-Zertifikaten (Let's Encrypt)](Server/Nginx_SSL.md) und die [Kopplung von Nginx mit dem Apache-Webserver](Server/Apache_Nginx.md).
* **Servlet-Container**: Installation und Verwaltung von Apache [Tomcat](Server/Tomcat.md) für Java-Webanwendungen.
* **KI/ML-Infrastrukturen**: [Skalierbare KI/ML-Lösungen](Server/ki-ml-infrastrukturen.md) von Single-Node bis Cluster-Skalierung.
* **System-Installation**: [Grundlegende Softwareinstallation](Server/installation.md) für Ubuntu-Server.

---

### 2. [Sicherheit & Datenschutz für KI](Sicherheit/index.md)
Eine zentralisierte Übersicht über Sicherheitsbedrohungen, Schutzmaßnahmen und Datenschutz für künstliche Intelligenz-Systeme – von der Entwicklung bis zum Produktivbetrieb.

* **Bedrohungsmodelle**: OWASP Top 10 für LLMs, Prompt Injection, Model Extraction, Data Poisoning
* **Schutzmaßnahmen**: Input Validation, Output Filtering, Rate Limiting, Authentication, Model Sandboxing
* **Datenschutz**: DSGVO-Compliance, Anonymisierung, Pseudonymisierung, Differential Privacy
* **Modell-Sicherheit**: Integrität, Robustheit, Vertrauenswürdige KI
* **Compliance**: EU AI Act, NIST AI RMF, ISO/IEC 23894
* **Tools & Frameworks**: Guardrails AI, Promptfoo, Presidio, Lakera GNU, TensorFlow Privacy

---

### 3. [IDE & Entwicklungsumgebung](IDE/index.md)
Dokumentation zur Einrichtung des lokalen Entwicklungsrechners unter Ubuntu 25.10.

* **System-Setup**: Paketinstallationen, Einrichtung von passwortlosem `sudo`, Installation von Google Chrome und PostgreSQL ([detaillierte Anleitung](IDE/setup.md)).
* **KI-Unterstützung**: Integration moderner KI-Coding-Assistenten wie GitHub Copilot, Claude Code, CODEX CLI und Antigravity CLI.
* **Lokale KI-Frontends**: [Web-UIs für lokale KI-Modelle](IDE/lokale-ki-frontends.md) (Open WebUI, LibreChat, Oobabooga).
* **Android-Entwicklung**: Einrichtung der SDKs und IDEs für die mobile [Android-Entwicklung](IDE/Android.md).

### 4. [Content & KI-gestützte Inhalte](Content/index.md)
Strategien, Tools und Best Practices für die Erstellung, Optimierung und Verwaltung von digitalen Inhalten mit KI-Unterstützung.

* **KI Content Creation**: [Grundlagen der KI-gestützten Inhaltserstellung](Content/ki-content-creation.md)
* **Content-Strategie mit KI**: [Planung, Erstellung und Optimierung von Inhalten](Content/content-strategie.md) mit KI-Tools
* **KI-gestützte SEO-Optimierung**: [Suchmaschinenoptimierung mit künstlicher Intelligenz](Content/ki-seo-optimierung.md) – von Keyword-Recherche bis zur technischen Analyse
* **Multilinguale Inhalte mit KI**: [Automatisierte Übersetzungen, Lokalisierung und kulturelle Anpassung](Content/multilinguale-inhalte.md) für globale Zielgruppen
* **Social Media Automatisierung**: [KI-gestützte Planung, Erstellung und Analyse](Content/social-media-ki.md) für soziale Netzwerke

### 4. [Video & Animation](Video/index.md)
Eine umfassende Übersicht über Frameworks und Tools zur programmatischen Generierung, Bearbeitung und Animation von Videos und 3D-Grafiken.

* **DOM-basierte Generierung**: Vorstellung von Remotion, Revideo und Hyperframes.
* **Browser-Automatisierung**: Headless-Rendering mittels Puppeteer und Playwright.
* **Mathematische & 2D/3D-Animation**: Einsatz von Manim, Motion Canvas, p5.js und Processing.
* **Medienverarbeitung & 3D-Suiten**: Low-Level-Tools wie FFmpeg und OpenCV sowie fortgeschrittene Automatisierung in Blender und Godot 4.

### 6. [Webentwicklung & KI](Webentwicklung/index.md)
Wie künstliche Intelligenz die Entwicklung moderner Webanwendungen transformiert – von Frontend-Design bis Backend-Optimierung.

* **KI in der Webentwicklung**: [Grundlagen und Anwendungsfälle](Webentwicklung/ki-webentwicklung.md)
* **Frontend mit KI**: [Moderne Web-Anwendungen](Webentwicklung/frontend-ki.md) mit KI-gestützter Code-Generierung, Design-Optimierung und automatisiertem Testing
* **Backend-Integration mit KI**: [Intelligente Backend-Systeme](Webentwicklung/backend-integration.md) mit KI-basierten APIs, Datenverarbeitung und automatisierter Logik
* **Deployment mit KI**: [Automatisierte Bereitstellung](Webentwicklung/deployment.md) und Skalierung von Webanwendungen mit KI-Unterstützung
* **Performance-Optimierung mit KI**: [Ladezeiten, Caching und Ressourcen-Management](Webentwicklung/performance.md) durch KI-gestützte Analyse

### 7. [Desktop Automation](Desktop_Automation/index.md)
Automatisierung von Betriebssystemen, Benutzeroberflächen und GUI-Interaktionen – für Tests, RPA und Prozessautomatisierung.

* **Übersicht**: [Vollständige Tool-Übersicht](Desktop_Automation/index.md) mit KI-Agenten-Kompatibilität und Plattform-Unterstützung
* **PyAutoGUI**: [Praktische Anleitung](Desktop_Automation/pyautogui-anleitung.md) zur plattformübergreifenden GUI-Automatisierung mit Python
* **Playwright**: [Praktische Anleitung](Desktop_Automation/playwright-anleitung.md) für moderne Web-Automatisierung und Testing
* **ydotool**: [Praktische Anleitung](Desktop_Automation/ydotool-anleitung.md) für Low-Level-Tastatur-/Maus-Steuerung unter Linux (Wayland & X11)
* **Robot Framework**: [Praktische Anleitung](Desktop_Automation/robot-framework-anleitung.md) für keyword-basierte Testautomatisierung

### 8. [KI-Modelle & Frameworks](KI-Modelle/index.md)
Eine zentralisierte Übersicht über Sprachmodelle (LLMs), Diffusionsmodelle, multimodale Modelle, Embeddings und Frameworks für Entwicklung, Training und Deployment.

* **Sprachmodelle (LLMs)**: Llama, Mistral, Phi, GPT, DeepSeek
* **Diffusionsmodelle**: Stable Diffusion, FLUX, Kandinsky
* **Multimodale Modelle**: CLIP, BLIP, GPT-4 Vision, LLaVA
* **Embedding-Modelle**: Sentence-Transformers, CLAP, BERT
* **Bildverarbeitungsmodelle**: YOLO, SAM, ResNet, ViT
* **Sprachverarbeitungsmodelle**: Whisper, Kokoro, Wav2Vec

---

### 9. [Datenbanken & Big Data](Datenbanken/index.md)
Eine zentralisierte Übersicht über Datenbanken, Big-Data-Technologien und Datenpipelines speziell für KI-Anwendungen.

* **Vektordatenbanken**: Milvus, Weaviate, Qdrant, Pinecone, Chroma
* **Zeitreihendatenbanken**: InfluxDB, TimescaleDB, Prometheus
* **Graphdatenbanken**: Neo4j, Amazon Neptune, Dgraph
* **Relationale Datenbanken**: PostgreSQL, MySQL, SQLite mit KI-Erweiterungen
* **NoSQL-Datenbanken**: MongoDB, Elasticsearch, Redis, Cassandra
* **Data Lakes & Storage**: MinIO, Ceph, Hadoop HDFS, Iceberg
* **ETL & Pipelines**: Apache Airflow, Dagster, Kafka, Spark
* **Big Data Frameworks**: Hadoop, Spark, Flink

---

### 10. [E-Learning-Autorentools](E-Learning-Autorentool/index.md)
Konzepte und Werkzeuge zur Erstellung interaktiver Lerninhalte und moderner Lernumgebungen.

* **Klassifizierung**: Abgrenzung von Software, Bibliotheken, Frameworks und KI-Agenten.
* **KI-Tutoren**: Einsatz und Steuerung autonomer Lernagenten (z. B. via Google Antigravity SDK oder LangGraph).
* **Architektur & Lücken**: Analyse aktueller Herausforderungen wie z. B. der nahtlosen Integration von Code-Sandboxes.

---

### 11. [Audio & Musik](Audio/index.md)
Programmatische Erzeugung, Synthese, Bearbeitung und wissenschaftliche Analyse von Audiodaten mit KI-Unterstützung.

* **KI und Audio**: [Umfassende Übersicht](Audio/ki-audio.md) zu KI-Anwendungen in der Audio-Verarbeitung – von Sprachsynthese bis Musikgenerierung
* **Audacity mit KI**: [Professionelle Audiobearbeitung](Audio/audacity-ki.md) mit KI-Plugins für Rauschunterdrückung, Stem-Separation und Transkription
* **DAW-Integration mit KI**: [KI in Digital Audio Workstations](Audio/daw-integration.md) wie Ardour, LMMS, Qtractor und REAPER
* **MIDI-Programmierung mit KI**: [Intelligente Musiksteuerung](Audio/midi-programmierung.md) durch KI-generierte und analysierte MIDI-Daten
* **Audio-Processing mit KI**: [Signalverarbeitung mit neuronalen Netzen](Audio/audio-processing.md) für Spracherkennung, Musikgenerierung und Echtzeit-Effekte

### 12. [Datenerfassung](Datenerfassung/index.md)
Tools, Methoden und Workflows zur systematischen Erfassung, Validierung und Verarbeitung von Daten – für Feldstudien, Forschung und betriebliche Anwendungen.

* **Mobile Datenerfassung**: [OpenDataKit (ODK)](Datenerfassung/OpenDataKit.md) für Offline-Datenerfassung auf Android
* **Formular-Design**: XLSForm für Excel-basierte Formularerstellung
* **Daten-Synchronisation**: Offline-First Ansatz mit späterer Synchronisation
* **Datenvalidierung**: Constraints, Skip-Logik und automatische Prüfungen
* **Server-Lösungen**: ODK Central für zentrale Datenverwaltung

---

### 13. [Dokument Erstellen & Notebooks](Dokument_Erstellen/index.md)
Pipelines, Generatoren und Notebook-Systeme zur Erstellung von strukturierten Dokumenten, Büchern und Wissensdatenbanken.

* **Book-Generators**: MkDocs, mdBook, Antora, Starlight und Docusaurus.
* **Notebook-Systeme**: Quarto, JupyterLab, JupyterLite, Voila, Papermill und Marimo.
* **Local Wikis**: DokuWiki, BookStack und dateibasierte Wissensdatenbanken (Obsidian, Quartz).

---

### 14. [Tools & Hilfswerkzeuge](Tools/index.md)
Spezialisierte Hilfsmittel zur Entwicklungsunterstützung, Code-Analyse, Performance-Optimierung und Systemverwaltung.

* **Dokumenten-Konvertierung**: Nutzung von [Pandoc](Tools/Pandoc.md) zum Konvertieren von Formaten (z. B. Markdown zu MediaWiki).
* **Abhängigkeiten & Sicherheit**: Analyse von Abhängigkeiten und Schwachstellenscans mit [Snyk & OSV Scanner](Tools/Analysetool.md).
* **Performance**: Benchmarking-Plattformen für Web-Frameworks ([TechEmpower & Web Frameworks Benchmark](Tools/Benchmark.md)).
* **Kategorien**: [Übersicht](Tools/index.md) aller Tools nach Anwendungsbereich (Containerisierung, Monitoring, CI/CD, Testing, etc.)

---

## 🖥️ Serverlandschaft: Technologieübersicht

### Produktionsserver (Ubuntu 24.04 LTS)
Der Produktionsserver ist darauf ausgelegt, maximale Datenkontrolle und Datenschutz zu gewährleisten. Durch die lokale Datenverarbeitung sind keine Cookie-Banner erforderlich.

* **Web- & Application-Server**: Nginx (Webserver/Reverse Proxy), Tomcat 10 (Java Servlet Container), Switch2OSM Tileserver (OSM-Kartendaten).
* **Datenbank**: PostgreSQL.
* **Laufzeiten & Tools**: ASP.NET Core 10, Java, Python, Git & GitHub CLI (`gh`).

### Entwicklungsrechner (Ubuntu 25.10)
Umfassend ausgestattetes System zur Erstellung, zum Testen und zur lokalen Bereitstellung von Anwendungen.

* **Sprachen & Frameworks**: .NET SDK, Node.js, Python, Java, Golang, Rust, C/C++.
* **Editoren & KI-Assistenten**: Visual Studio Code, Google Antigravity IDE, GitHub Copilot, Claude Code, Antigravity CLI, Claude CLI (`claude`), CODEX CLI.
* **Lokale Dienste & Web**: PostgreSQL, Nginx, Google Chrome.
