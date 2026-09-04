# Desktop- und GUI-Automatisierung: Software, Bibliotheken & Frameworks

Eine Übersicht über Tools, Bibliotheken und Frameworks zur Automatisierung von Betriebssystemen, Benutzeroberflächen (Desktop/Web) und zur Bildschirmaufnahme.

---

## 🤖 Eignung für KI-Agenten (AI Agent Compatibility)

Für den Einsatz von **KI-Agenten** (z. B. LLM-basierten Agenten mit Tool-Calling oder Vision-Fähigkeiten) zur Systemsteuerung gelten je nach Automatisierungsart unterschiedliche Voraussetzungen:

| Automatisierungs-Typ / Tool-Kategorie | Eignung für KI-Agenten | Vorteile | Herausforderungen für KI-Modelle |
| :--- | :---: | :--- | :--- |
| **Objekt-/DOM-basiert (Web)** <br>*(Playwright, Puppeteer, Selenium)* | **Hervorragend (5/5)** | Agenten können direkt im DOM-Tree nach IDs, Texten und ARIA-Labels suchen. Sehr stabil und präzise. | Beschränkt auf Browser; nützt nichts bei nativen Desktop-Apps. |
| **Accessibility-basiert (Desktop)** <br>*(Dogtail, pywinauto, AT-SPI)* | **Sehr gut (4/5)** | Zugriff auf den Barrierefreiheits-Tree der OS-GUI. Der Agent erhält semantische Strukturen statt nur Pixeln. | Komplexere APIs; OS-spezifisch; nicht alle Apps pflegen Accessibility-Daten sauber. |
| **Koordinaten- & Bildbasiert** <br>*(PyAutoGUI, SikuliX, OpenCV)* | **Mittel bis Gut (3/5)** | Universell einsetzbar auf jedem OS; ideal für Multimodale LLMs (Vision), die Klick-Koordinaten auf Screenshots schätzen. | Anfällig für Layoutänderungen, Skalierung und Latenz; benötigt Vision-Modelle (VLM). |
| **Low-Level / Virtual Input** <br>*(ydotool, evdev, wtype)* | **Mittel (Spezialfall)** | Funktioniert zuverlässig in Headless-Umgebungen (z. B. Docker-Containern) und unter Wayland. | Gibt kein visuelles oder semantisches Feedback zurück (muss mit Screen-Capturing kombiniert werden). |

---

## 1. UI- & GUI-Automatisierung (Desktop)

### Für Python-Entwickler (Code-First)
* **PyAutoGUI**: Eine plattformübergreifende (Windows, macOS, Linux) Python-Bibliothek zur Steuerung von Maus und Tastatur. Ideal für einfache Makros und Klicksimulationen.
* **keyboard** & **mouse**: Reine Python-Bibliotheken zum globalen Abfangen und Simulieren von Tastatur- und Mausereignissen (benötigt unter Linux oft Root-Rechte).
* **pywinauto**: Spezialisierte Windows-Bibliothek zur Automatisierung von Windows-GUI-Elementen (Win32, MS UI Automation).
* **Atomac**: macOS-spezifische Bibliothek zur Automatisierung von nativen Cocoa-Anwendungen mithilfe der Apple Accessibility API.
* **Dogtail** / **LDTP (Linux Desktop Testing Project)**: Bibliotheken zur Automatisierung von Linux-Desktops über die Barrierefreiheits-Schnittstelle AT-SPI (besonders gut für GNOME/KDE).

### Für JavaScript/Node.js & andere Sprachen
* **Nut.js**: Ein modernes, plattformübergreifendes Desktop-Automatisierungsframework für Node.js mit Unterstützung für Bildsuche, Tastatur- und Maussteuerung.
* **RobotJS**: Ein klassisches Node.js-Modul zur Steuerung von Maus, Tastatur und zum Auslesen des Bildschirms.
* **RobotGo**: Ein sehr umfangreiches GUI-Automatisierungs-Framework für Go (Golang), das plattformübergreifend funktioniert.
* **Enigo**: Eine Rust-Bibliothek zur Simulation von Tastatur- und Maus-Inputs unter Windows, macOS und Linux (unterstützt X11 und experimentell Wayland).

---

## 2. Linux-spezifische Schnittstellen & Tools (X11 & Wayland)

### Wayland-kompatibel (Modern & Zukunftssicher)
* **ydotool**: Ein CLI-Tool zur Simulation von Tastatur- und Mausaktionen, das direkt über das Kernel-Modul `uinput` kommuniziert. Funktioniert unabhängig vom Display-Server (Wayland & X11) und benötigt keine grafische Umgebung.
* **wtype**: Ein Wayland-spezifisches CLI-Tool zur Simulation von Tastatureingaben (funktioniert auf Wayland-Compositoren, die das Virtual-Keyboard-Protokoll unterstützen, wie Sway oder Wayfire).
* **evdev** & **python-uinput**: Low-Level-Bibliotheken zur Interaktion mit Linux-Eingabegeräten im `/dev/input/`-Subsystem. Ermöglicht das Lesen und Erstellen virtueller Eingabegeräte.
* **pywayland**: Python-Bindings für das Wayland-Protokoll zur direkten Kommunikation mit dem Compositor.

### Für X11 / XWayland (Klassiker)
* **xdotool**: Das Standard-CLI-Tool für X11 zur Simulation von Tastatur-/Mauseingaben, Fensterverwaltung und Abfrage von Fensterzuständen. Funktioniert unter Wayland nur innerhalb von XWayland-Fenstern.
* **AutoKey**: Ein Desktop-Automatisierungs- und Text-Expander-Tool für Linux (X11), das Python-Skripte zur Makrosteuerung unterstützt.

---

## 3. Web- & Browser-Automatisierung

* **Playwright**: Ein modernes, extrem schnelles und stabiles Framework von Microsoft zur Automatisierung von Chromium, Firefox und WebKit. Unterstützt Node.js, Python, Java und .NET.
* **Selenium**: Der Klassiker unter den Web-Testframeworks. Unterstützt fast alle Programmiersprachen und Browser (Multi-Language), ist jedoch schwerfälliger als moderne Alternativen.
* **Puppeteer**: Eine von Google entwickelte Node.js-Bibliothek zur Steuerung von Chrome oder Chromium über das Chrome DevTools Protocol (CDP).

---

## 4. Visuelle Automatisierung & Bilderkennung

* **SikuliX**: Ein Tool, das OpenCV-Bilderkennung nutzt, um GUI-Elemente anhand von Screenshots zu identifizieren und zu steuern. Programmierbar mit Jython, JRuby oder Java.
* **UI.Vision RPA**: Ein Browser-Add-on und Desktop-Tool für visuelle Automatisierung (Web & Desktop), das OCR- und Bilderkennungstechnologien integriert.
* **OpenCV + Python/C++**: Eine mächtige Computer-Vision-Bibliothek, die in Kombination mit Screenshot-Tools (wie `mss` oder `PyAutoGUI`) für maßgeschneiderte, hochperformante visuelle Erkennung in Automatisierungsskripten genutzt wird.

---

## 5. Test- & RPA-Frameworks (Robotic Process Automation)

* **Robot Framework**: Ein generisches Open-Source-Automatisierungsframework für Akzeptanztests und RPA. Kann hervorragend mit Selenium, Playwright oder SikuliX kombiniert werden.
* **Appium**: Ein Framework zur Automatisierung von nativen, hybriden und mobilen Web-Apps auf iOS, Android und Desktop-Plattformen (Windows/macOS).
* **OpenRPA**: Ein quelloffenes, robustes RPA-Tool zur visuellen Erstellung von Workflows (ähnlich wie UiPath).

---

## 6. Macro Scripting (Makro-Recorder & Text-Expander)

* **AutoHotkey (AHK)**: Die wohl bekannteste Skriptsprache für Windows zur Tastaturbelegung, Erstellung von Makros und GUI-Automatisierung.
* **Hammerspoon**: Ein mächtiges Automatisierungs-Tool für macOS, das vollständig über Lua-Skripte konfiguriert wird und tiefen Systemzugriff bietet.
* **Keyboard Maestro**: Ein visueller Makro-Editor für macOS zur Automatisierung von Arbeitsabläufen ohne Programmierkenntnisse.
* **Espanso**: Ein plattformübergreifender (Linux, macOS, Windows) und in Rust geschriebener Text-Expander, der via YAML-Dateien konfiguriert wird.

---

## 7. Bildschirmaufnahme & Capturing

### Desktop-Anwendungen (Software)
* **OBS Studio**: Der De-facto-Standard für Open-Source-Bildschirmaufnahme und Streaming. Unterstützt moderne Linux-Schnittstellen (PipeWire).
* **Kazam**: Ein einfacher und leichtgewichtiger Screen-Recorder für Linux (hauptsächlich X11).
* **Kooha**: Ein moderner, minimalistischer Screen-Recorder für GNOME/Wayland mit nativer Unterstützung für PipeWire.
* **Gromit-MPX**: Ein Tool, mit dem man direkt auf dem Bildschirm zeichnen kann (wichtig für Präsentationen und Tutorials während der Aufnahme).

### APIs & Protokolle (Low-Level / System)
* **PipeWire & GStreamer**: Der moderne Linux-Standard für Audio- und Video-Streaming. PipeWire regelt das sichere Screensharing und Recording unter Wayland.
* **XDG Desktop Portal**: Ermöglicht sandboxed Anwendungen (z. B. Flatpaks) den sicheren Zugriff auf den Bildschirm via PipeWire.

### Entwickler-Bibliotheken (Capturing)
* **libobs**: Der C++ Core von OBS Studio. Kann als Bibliothek in eigene Projekte integriert werden, um professionelles Recording/Streaming umzusetzen.
* **mss (Multiple Screenshots)**: Eine extrem schnelle, reine Python-Bibliothek zur Aufnahme von Screenshots.
* **desktopCapturer (Electron/Node.js)**: Ein Electron-API-Modul zum Abgreifen von Audio- und Videoquellen des Desktops für Web- und Desktop-Apps.