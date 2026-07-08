# Dokumentation für meine Entwicklungsumgebung und den Einsatz von Servern

Willkommen in meiner zentralen Dokumentation. Diese Wissensdatenbank dient der Strukturierung und Erfassung aller Konfigurationen, Installationsanleitungen und Technologie-Übersichten für meine Serverlandschaft und lokale Entwicklungsumgebung.

---

## 📁 Dokumentationskategorien

Diese Dokumentation ist in die folgenden Hauptbereiche unterteilt. Jede Kategorie deckt einen spezifischen Bereich ab:

### 1. [Server](Server/Software.md)
Dieser Bereich befasst sich mit der Konfiguration, Installation und Absicherung von Serverdiensten auf dem Produktionsserver (Ubuntu 24.04 LTS). Er umfasst:

* **Datenbanken**: Einrichtung und Verwaltung von [PostgreSQL](Server/Postgresql.md).
* **Kachelserver (Tileserver)**: Detaillierte Schritt-für-Schritt-Anleitungen zur Einrichtung eines OpenStreetMap-Kachelservers unter verschiedenen Ubuntu-Versionen ([Ubuntu 20.04](Server/Kachelserver/Server204.md), [Ubuntu 22.04](Server/Kachelserver/Server224.md) und [Ubuntu 24.04](Server/Kachelserver/Server244.md)).
* **Webserver & Reverse Proxy**: Konfiguration von [Nginx](Server/nginx.md), Einbindung von [SSL-Zertifikaten (Let's Encrypt)](Server/Nginx_SSL.md) und die [Kopplung von Nginx mit dem Apache-Webserver](Server/Apache_Nginx.md).
* **Servlet-Container**: Installation und Verwaltung von Apache [Tomcat](Server/Tomcat.md) für Java-Webanwendungen.
* **Zusatzsoftware**: Verwaltung [weiterer Softwarekomponenten](Server/Software.md).

### 2. [IDE & Entwicklungsumgebung](IDE/index.md)
Dokumentation zur Einrichtung des lokalen Entwicklungsrechners unter Ubuntu 25.10.

* **System-Setup**: Paketinstallationen, Einrichtung von passwortlosem `sudo`, Installation von Google Chrome und PostgreSQL.
* **KI-Unterstützung**: Integration moderner KI-Coding-Assistenten wie GitHub Copilot, Claude Code sowie der [Antigravity CLI](IDE/index.md#ki-cli) und CODEX CLI.
* **Android-Entwicklung**: Einrichtung der SDKs und IDEs für die mobile [Android-Entwicklung](IDE/Android.md).

### 3. [Video & Animation](Video/index.md)
Eine umfassende Übersicht über Frameworks und Tools zur programmatischen Generierung, Bearbeitung und Animation von Videos und 3D-Grafiken.

* **DOM-basierte Generierung**: Vorstellung von Remotion, Revideo und Hyperframes.
* **Browser-Automatisierung**: Headless-Rendering mittels Puppeteer und Playwright.
* **Mathematische & 2D/3D-Animation**: Einsatz von Manim, Motion Canvas, p5.js und Processing.
* **Medienverarbeitung & 3D-Suiten**: Low-Level-Tools wie FFmpeg und OpenCV sowie fortgeschrittene Automatisierung in Blender und Godot 4.

### 4. [Desktop Automation](Desktop_Automation/index.md)
Fokus auf Desktop- und GUI-Automatisierung sowie die Interaktion mit dem Betriebssystem.

* **KI-Agenten-Kompatibilität**: Bewertung der Eignung von Automatisierungstools für autonome LLM-Agenten.
* **GUI-Frameworks**: Bibliotheken für Python (PyAutoGUI, pywinauto, Dogtail), Node.js (Nut.js, RobotJS), Go (RobotGo) und Rust (Enigo).
* **Linux-Plattformen**: Werkzeuge für Wayland (`ydotool`, `wtype`) und X11 (`xdotool`).

### 5. [E-Learning-Autorentools](E-Learning-Autorentool/index.md)
Konzepte und Werkzeuge zur Erstellung interaktiver Lerninhalte und moderner Lernumgebungen.

* **Klassifizierung**: Abgrenzung von Software, Bibliotheken, Frameworks und KI-Agenten.
* **KI-Tutoren**: Einsatz und Steuerung autonomer Lernagenten (z. B. via Google Antigravity SDK oder LangGraph).
* **Architektur & Lücken**: Analyse aktueller Herausforderungen wie z. B. der nahtlosen Integration von Code-Sandboxes.

### 6. [Audio & Musik](Audio/index.md)
Programmatische Erzeugung, Synthese, Bearbeitung und wissenschaftliche Analyse von Audiodaten.

* **Python-Libraries**: Feature-Extraktion und Signalverarbeitung mit Librosa, PyDub und SciPy.
* **Sprachsynthese**: Lokale Offline-Sprachgenerierung mittels Kokoro-ONNX.
* **Systemnahe Programmierung**: High-Performance-Audiomanipulation in C++ (JUCE, libsndfile) und Rust (symphonia, hound) sowie FAUST.
* **Web-Audio & Live Coding**: Interaktive Web-Audio-Bibliotheken (Tone.js) und Echtzeit-Live-Coding (SuperCollider, Sonic Pi, TidalCycles).

### 7. [Dokument Erstellen & Notebooks](Dokument_Erstellen/index.md)
Pipelines, Generatoren und Notebook-Systeme zur Erstellung von strukturierten Dokumenten, Büchern und Wissensdatenbanken.

* **Book-Generators**: MkDocs, mdBook, Antora, Starlight und Docusaurus.
* **Notebook-Systeme**: Quarto, JupyterLab, JupyterLite, Voila, Papermill und Marimo.
* **Local Wikis**: DokuWiki, BookStack und dateibasierte Wissensdatenbanken (Obsidian, Quartz).

### 8. [Tools & Hilfswerkzeuge](Tools/Pandoc.md)
Spezialisierte Hilfsmittel zur Entwicklungsunterstützung und Code-Analyse.

* **Dokumenten-Konvertierung**: Nutzung von [Pandoc](Tools/Pandoc.md) zum Konvertieren von Formaten (z. B. Markdown zu MediaWiki).
* **Abhängigkeiten & Sicherheit**: Analyse von Abhängigkeiten und Schwachstellenscans mit [Snyk & OSV Scanner](Tools/Analysetool.md).
* **Performance**: Benchmarking-Plattformen für Web-Frameworks ([TechEmpower & Web Frameworks Benchmark](Tools/Benchmark.md)).

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
