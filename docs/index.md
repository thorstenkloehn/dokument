# Dokumentation für meine Entwicklungsumgebung und den Einsatz von Servern
## Serverinstallation
Mein Server verwendet Ubuntu 24.04 als Betriebssystem, während mein Entwicklungsrechner mit Ubuntu 25.10 läuft. Dies ermöglicht eine klare Trennung zwischen Produktions- und Entwicklungsumgebung und erleichtert die Verwaltung von Abhängigkeiten und Updates.
### Verwendete Technologien auf dem Produktionsserver

Der Produktionsserver setzt folgende Technologien ein:

- **Git**: Versionskontrollsystem für die Quellcodeverwaltung.
- **GitHub CLI (`gh`)**: Kommandozeilenwerkzeug zur Interaktion mit GitHub-Repositories.
- **ASP.NET Core 10**: Framework für die Entwicklung und Bereitstellung von Webanwendungen.
- **Java**: Programmiersprache und Laufzeitumgebung für verschiedene Anwendungen.
- **PostgreSQL**: Relationale Datenbank für die Speicherung und Verwaltung von Daten.
- **Nginx**: Webserver und Reverse Proxy zur Auslieferung von Webinhalten.
- **Python**: Programmiersprache für Automatisierung, Skripte und Webanwendungen.
- **Switch2OSM Tileserver**: OpenStreetMap-Tileserver-Lösung zur Bereitstellung von Kartendaten für Webanwendungen.

**Hinweis:** Der Produktionsserver ist so konfiguriert, dass möglichst keine Cookie-Banner erforderlich sind, da alle Daten ausschließlich auf dem eigenen Server verarbeitet und gespeichert werden. Externe Dienste werden vermieden, um Datenschutz und Kontrolle über die Daten zu gewährleisten.

### Verwendete Technologien auf meinem Entwicklungsrechner

Auf meinem Entwicklungsrechner kommen folgende Technologien zum Einsatz:

- **Visual Studio Code**: Quelltexteditor mit zahlreichen Erweiterungen für verschiedene Programmiersprachen.
- **Google Antigravity**: Im November 2025 vorgestellte, KI-gestützte Entwicklungsumgebung (IDE), die speziell für die Arbeit mit autonomen KI-Agenten entwickelt wurde.
- **VS Code-Erweiterung**
    - **GitHub Copilot**: KI-gestützte Unterstützung bei Code-Vervollständigung, Refactoring und dem Erstellen von Funktionsvorschlägen direkt im Editor.
     - **Claude Code**: Ein KI-gestützter Coding-Assistent von Anthropic, der Entwickler:innen beim Schreiben, Verstehen, Refaktorisieren und Dokumentieren von Code direkt im Entwicklungsworkflow unterstützt.
- **Kommandozeilen-KI (`CLI-Tools`)**: KI-gestützte Assistenten im Terminal zur Codegenerierung, Analyse und Automatisierung von Entwicklungsaufgaben. 
    - **Gemini CLI** ist ein Kommandozeilen-Tool für Google Gemini, mit dem du KI-Funktionen direkt im Terminal nutzen kannst
    (z. B. Prompting, Code-Unterstützung, Automatisierung in Skripten und Workflows).
    - **GitHub Copilot CLI (`gh copilot`)**: KI-gestützte Erweiterung der GitHub CLI, die per natürlicher Sprache Shell-Befehle, Git-Workflows und passende Kommandozeilenvorschläge liefert und so wiederkehrende Aufgaben im Terminal beschleunigt.
    - **Claude Code CLI (`claude`)**: Kommandozeilen-Tool von Anthropic für KI-gestützte Entwicklungsaufgaben direkt im Terminal, z. B. Codegenerierung, Refactoring, Analyse bestehender Projekte und Unterstützung bei wiederkehrenden Workflows.
- **Git**: Versionskontrollsystem zur Verwaltung von Quellcode.
- **Node.js**: JavaScript-Laufzeitumgebung für serverseitige Anwendungen und Tools.
- **Python**: Programmiersprache für Skripte, Automatisierung und Webentwicklung.
- **.NET SDK**: Entwicklungsumgebung für .NET-Anwendungen.
- **PostgreSQL**: Relationale Datenbank für lokale Entwicklungs- und Testzwecke.
- **Nginx**: Webserver für lokale Entwicklungsumgebungen.
- **Chrome**: Webbrowser zur Entwicklung und zum Testen von Webanwendungen.
- **Java** : Programmiersprache und Laufzeitumgebung für die Entwicklung und das Testen von vpn Java-Anwendungen.
- **Golang**: Programmiersprache, die für die Entwicklung von effizienten und skalierbaren Anwendungen verwendet wird, insbesondere für Netzwerk- und Backend-Services.
- **Rust**:Moderne Programmiersprache mit Fokus auf Sicherheit und Performance, ideal für Systemprogrammierung und performante Anwendungen.
- **C/C++**: Klassische Programmiersprachen für System- und Anwendungsentwicklung, werden in meiner Umgebung jedoch nur selten genutzt, z. B. für spezielle Performance- oder Kompatibilitätsanforderungen.

