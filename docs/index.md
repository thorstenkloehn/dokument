# Dokumentation für meine Entwicklungsumgebung und den Einsatz von Servern

Willkommen in meiner zentralen Dokumentation. Diese Wissensdatenbank dient der Strukturierung und Erfassung aller Konfigurationen, Installationsanleitungen und Technologie-Übersichten für meine Serverlandschaft und lokale Entwicklungsumgebung.

---

## 📁 Dokumentationskategorien

Diese Dokumentation ist in die folgenden Hauptbereiche unterteilt. Jede Kategorie deckt einen spezifischen Bereich ab:

### 1. [KI & Automatisierung](künstliche-intelligenz/index.md)

Strategien, Tools und Best Practices für den Einsatz von künstlicher Intelligenz und Automatisierungstechnologien.

* **Coding mit KI**: [Übersicht](künstliche-intelligenz/coding/index.md) zu KI-gestützter Softwareentwicklung
  * [KI Coding](künstliche-intelligenz/coding/ki-coding.md) - Grundlagen und Best Practices
  * [Eigene KI-Anwendungen](künstliche-intelligenz/coding/ki-anwendungen-programmieren.md)
  * [Schrödinger programmiert KI](künstliche-intelligenz/coding/schroedinger-programmiert-ki.md)
  * [Programmieren lernen mit KI](künstliche-intelligenz/coding/programmieren-lernen-ki.md)
  * [Programmieren mit KI](künstliche-intelligenz/coding/programmieren-mit-ki.md)
  * [Vibe Coding & Engineering](künstliche-intelligenz/coding/vibe-coding-engineering.md)

* **Content-Erstellung mit KI**:
  * [KI Content Creation](künstliche-intelligenz/content/ki-content-creation.md)
  * [Content-Strategie mit KI](künstliche-intelligenz/content/content-strategie.md)
  * [KI-gestützte SEO-Optimierung](künstliche-intelligenz/content/ki-seo-optimierung.md)
  * [Multilinguale Inhalte mit KI](künstliche-intelligenz/content/multilinguale-inhalte.md)
  * [Social Media Automatisierung mit KI](künstliche-intelligenz/content/social-media-ki.md)

* **Desktop-Automatisierung**:
  * [Übersicht](künstliche-intelligenz/automatisierung/index.md) mit KI-Agenten-Kompatibilität
  * [PyAutoGUI Anleitung](künstliche-intelligenz/automatisierung/pyautogui-anleitung.md) für plattformübergreifende GUI-Automatisierung
  * [Playwright Anleitung](künstliche-intelligenz/automatisierung/playwright-anleitung.md) für moderne Web-Automatisierung
  * [ydotool Anleitung](künstliche-intelligenz/automatisierung/ydotool-anleitung.md) für Low-Level-Tastatur-/Maus-Steuerung
  * [Robot Framework Anleitung](künstliche-intelligenz/automatisierung/robot-framework-anleitung.md) für keyword-basierte Testautomatisierung

* **KI-Modelle & Frameworks**:
  * Sprachmodelle (LLMs): Llama, Mistral, Phi, GPT, DeepSeek
  * Diffusionsmodelle: Stable Diffusion, FLUX, Kandinsky
  * Multimodale Modelle: CLIP, BLIP, GPT-4 Vision, LLaVA
  * Embedding-Modelle: Sentence-Transformers, CLAP, BERT
  * Bildverarbeitungsmodelle: YOLO, SAM, ResNet, ViT
  * Sprachverarbeitungsmodelle: Whisper, Kokoro, Wav2Vec

---

### 2. [Entwicklung & Infrastruktur](entwicklung/infrastruktur/index.md)

Dokumentation zur Konfiguration, Installation und Absicherung von Serverdiensten auf dem Produktionsserver (Ubuntu 24.04 LTS) und lokalen Entwicklungsumgebungen.

* **Server & Infrastruktur**:
  * [PostgreSQL](entwicklung/infrastruktur/postgresql.md) mit PostGIS für räumliche Daten
  * **Kachelserver (Tileserver)**: Detaillierte Anleitungen für OpenStreetMap-Kachelserver
    * [Ubuntu 20.04](entwicklung/infrastruktur/kachelserver/server204.md)
    * [Ubuntu 22.04](entwicklung/infrastruktur/kachelserver/server224.md)
    * [Ubuntu 24.04](entwicklung/infrastruktur/kachelserver/server244.md)
    * [Alternative Kachelserver](entwicklung/infrastruktur/kachelserver/alternative-kachelserver.md) (TileServer-GL, MapProxy, OSRM, etc.)
  * **Webserver & Reverse Proxy**:
    * [Nginx](entwicklung/infrastruktur/nginx.md)
    * [Nginx SSL (Let's Encrypt)](entwicklung/infrastruktur/nginx-ssl.md)
    * [Apache + Nginx Kopplung](entwicklung/infrastruktur/apache-nginx.md)
  * [Tomcat](entwicklung/infrastruktur/tomcat.md) für Java-Webanwendungen
  * [Skalierbare KI/ML-Infrastrukturen](entwicklung/infrastruktur/ki-ml-infrastrukturen.md)
  * [Grundlegende Softwareinstallation](entwicklung/infrastruktur/installation.md)
  * [Sicherheit](entwicklung/infrastruktur/sicherheit/index.md)

* **Webentwicklung**:
  * [Übersicht](entwicklung/webentwicklung/index.md)
  * [KI Web/entwicklung](entwicklung/webentwicklung/ki-webentwicklung.md) - Grundlagen und Anwendungsfälle
  * [Frontend mit KI](entwicklung/webentwicklung/frontend-ki.md) - Code-Generierung, Design-Optimierung, automatisiertes Testing
  * [Backend-Integration mit KI](entwicklung/webentwicklung/backend-integration.md) - Intelligente Backend-Systeme
  * [Deployment mit KI](entwicklung/webentwicklung/deployment.md) - Automatisierte Bereitstellung
  * [Performance-Optimierung mit KI](entwicklung/webentwicklung/performance.md)

* **Systemprogrammierung**:
  * [Übersicht](entwicklung/system/index.md)
  * [Assembler](entwicklung/system/assembler.md)
  * [Assembler Fehler & Sicherheit](entwicklung/system/assembler-fehler-sicherheit.md)
  * [Compiler](entwicklung/system/compiler.md)
  * [Rust, C & C++ Integration](entwicklung/system/rust-c-cpp-integration.md)
  * [Linux-Systemprogrammierung](entwicklung/system/linux-systemprogrammierung.md)

* **IDE & Entwicklungsumgebung**:
  * [Übersicht](ide/index.md) - Einrichtung des lokalen Entwicklungsrechners
  * [System-Setup](ide/setup.md) - Paketinstallationen, passwortloses sudo, Chrome, PostgreSQL
  * [KI-Unterstützung](ide/lokale-ki-frontends.md) - GitHub Copilot, Claude Code, CODEX CLI, Antigravity CLI
  * [Android-Entwicklung](ide/android.md) - SDKs und IDEs für mobile Entwicklung

---

### 3. [Kreativ & Design](kreativ/design/index.md)

Inspiration und Anleitungen zum Einsatz von KI in kreativen Designprozessen.

* **Design mit KI**:
  * [Design nach KI](kreativ/design/design-nach-ki.md) - Wie KI das Design entwickelt
  * [Ideenfindung mit KI](kreativ/design/ideenfindung-ki.md) - Kreativität fördern
  * [Leseprobe: KI für Kreative](kreativ/design/leseprobe-ki-kreative.md)

* **Audio & Musik**:
  * [Übersicht](kreativ/audio/index.md) - KI-Anwendungen in der Audio-Verarbeitung
  * [KI und Audio](kreativ/audio/ki-audio.md) - Von Sprachsynthese bis Musikgenerierung
  * [Audacity mit KI](kreativ/audio/audacity-ki.md) - Rauschunterdrückung, Stem-Separation, Transkription
  * [DAW-Integration mit KI](kreativ/audio/daw-integration.md) - KI in Ardour, LMMS, REAPER
  * [MIDI-Programmierung mit KI](kreativ/audio/midi-programmierung.md) - Intelligente Musiksteuerung
  * [Audio-Processing mit KI](kreativ/audio/audio-processing.md) - Signalverarbeitung mit neuronalen Netzen

* **Video & Film**:
  * [Übersicht](kreativ/video/index.md)
  * [KI in der Film- und V/ideoproduktion](kreativ/video/ki-filmproduktion.md)

---

### 4. [Wissen & Dokumentation](wissen/dokumentation/index.md)

Pipelines, Generatoren und Systeme zur Erstellung von strukturierten Dokumenten und Wissensdatenbanken.

* **Daten & Datenerfassung**:
  * [Datenbanken Übersicht](daten/datenbanken/index.md) - Vektordatenbanken, Zeitreihendatenbanken, Graphdatenbanken
  * [Datenerfassung](daten/datenerfassung/index.md):
    * [OpenDataKit (ODK)](daten/datenerfassung/opendatakit.md) für Offline-Datenerfassung auf Android

* **E-Learning**:
  * [Übersicht](wissen/e-learning/index.md) - Konzepte und Werkzeuge für interaktive Lerninhalte
  * [KI in Lehre & Weiterbildung](wissen/e-learning/ki-lehre-weiterbildung.md) - KI-Tutoren, Lernagenten

* **Tools & Hilfswerkzeuge**:
  * [Übersicht](wissen/tools/index.md) aller Tools nach Anwendungsbereich
  * [Pandoc](wissen/tools/pandoc.md) - Dokumenten-Konvertierung
  * [Analysetool](wissen/tools/analysetool.md) - Abhängigkeiten & Sicherheit mit Snyk & OSV Scanner
  * [Benchmark](wissen/tools/benchmark.md) - Performance Benchmarking

* **Dokumentenerstellung**:
  * [Übersicht](wissen/dokumentation/index.md) - Book-Generators, Notebook-Systeme, Local Wikis
  * **MediaWiki**:
    * [Installieren](wissen/dokumentation/mediawiki/index.md)
    * [Backup](wissen/dokumentation/mediawiki/backup.md)
    * [Wiederherstellen](wissen/dokumentation/mediawiki/wiederherstellen.md)
  * **Semantisches MediaWiki**:
    * [Installieren](wissen/dokumentation/semantische-mediawiki/installieren.md)
    * [Kurzform](wissen/dokumentation/semantische-mediawiki/kurzform.md)
    * [Erweiterungen](wissen/dokumentation/semantische-mediawiki/wichtige-erweiterungen.md)
  * **XWiki**:
    * [Installieren](wissen/dokumentation/xwiki/installieren.md)

---

### 5. [Tags & Kategorien](tags.md)

Thematische Navigation durch alle Seiten mittels Tags.

---

### 6. [Rechtliches](rechtliches/impressum.md)

* [Impressum](rechtliches/impressum.md)
* [Datenschutz](rechtliches/datenschutz.md)

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
