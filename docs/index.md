# Dokumentation für meine Entwicklungsumgebung und den Einsatz von Servern
## Serverinstallation
Mein Server verwendet Ubuntu 24.04 als Betriebssystem, während mein Entwicklungsrechner mit Ubuntu 26.04 läuft. Dies ermöglicht eine klare Trennung zwischen Produktions- und Entwicklungsumgebung und erleichtert die Verwaltung von Abhängigkeiten und Updates.
### Verwendete Technologien auf dem Produktionsserver

Der Produktionsserver setzt folgende Technologien ein:

- **Forgejo**: Selbstgehostete Git-Server-Lösung zur Verwaltung von Quellcode-Repositories.
- **Git**: Versionskontrollsystem für die Quellcodeverwaltung.
- **GitHub CLI (`gh`)**: Kommandozeilenwerkzeug zur Interaktion mit GitHub-Repositories.
- **ASP.NET Core 10**: Framework für die Entwicklung und Bereitstellung von Webanwendungen.
- **Java**: Programmiersprache und Laufzeitumgebung für verschiedene Anwendungen.
- **PHP**: Skriptsprache für Webentwicklung und serverseitige Anwendungen.
- **PostgreSQL**: Relationale Datenbank für die Speicherung und Verwaltung von Daten.
- **Nginx**: Webserver und Reverse Proxy zur Auslieferung von Webinhalten.
- **Python**: Programmiersprache für Automatisierung, Skripte und Webanwendungen.
- **MediaWiki**: Open-Source-Wiki-Software zur Erstellung und Verwaltung von Wissensdatenbanken und Dokumentationen.
- **Xwiki**: Open-Source-Wiki-Software zur Verwaltung und Dokumentation von Wissen, ähnlich wie MediaWiki, aber mit 
erweiterten Funktionen für Zusammenarbeit und Anpassung.
- **Wiki.js**: Moderne, benutzerfreundliche Wiki-Software zur Erstellung, Verwaltung und Veröffentlichung von Dokumentationen. Wiki.js bietet eine intuitive Weboberfläche, unterstützt Markdown und verschiedene Authentifizierungsmethoden und lässt sich leicht anpassen sowie in bestehende Systeme integrieren.
- **Drupal**: Open-Source-Content-Management-System (CMS) zur Erstellung und Verwaltung von Websites und Webanwendungen. Drupal zeichnet sich durch hohe Flexibilität, eine große Auswahl an Erweiterungen (Modulen) und eine aktive Community aus. Es eignet sich sowohl für einfache Webseiten als auch für komplexe, mehrsprachige Portale und bietet umfangreiche Möglichkeiten zur Anpassung von Design und Funktionalität.
- **Typo3**: Open-Source-Content-Management-System (CMS), das sich durch hohe Flexibilität, Skalierbarkeit und eine große Auswahl an Erweiterungen auszeichnet. Typo3 eignet sich besonders für komplexe, mehrsprachige Websites und bietet umfangreiche Möglichkeiten zur Anpassung von Design und Funktionalität.
- **Orchard Cms**: Open-Source-Content-Management-System (CMS) auf Basis von ASP.NET Core. Orchard CMS ermöglicht die flexible Erstellung und Verwaltung von Websites und Webanwendungen. Es bietet ein modulares System, mit dem sich Funktionen durch Module und Themes erweitern lassen. Orchard eignet sich besonders für Entwickler, die individuelle Lösungen auf .NET-Basis benötigen, und unterstützt Mehrsprachigkeit, rollenbasierte Benutzerverwaltung sowie eine moderne API für Integrationen.
**Switch2OSM Tileserver**: OpenStreetMap-Tileserver-Lösung zur Bereitstellung von Kartendaten für Webanwendungen.

**Hinweis:** Der Produktionsserver ist so konfiguriert, dass möglichst keine Cookie-Banner erforderlich sind, da alle Daten ausschließlich auf dem eigenen Server verarbeitet und gespeichert werden. Externe Dienste werden vermieden, um Datenschutz und Kontrolle über die Daten zu gewährleisten.

### Verwendete Technologien auf meinem Entwicklungsrechner

Auf meinem Entwicklungsrechner kommen folgende Technologien zum Einsatz:

- **Visual Studio Code**: Quelltexteditor mit zahlreichen Erweiterungen für verschiedene Programmiersprachen.
- **Git**: Versionskontrollsystem zur Verwaltung von Quellcode.
- **Node.js**: JavaScript-Laufzeitumgebung für serverseitige Anwendungen und Tools.
- **Python**: Programmiersprache für Skripte, Automatisierung und Webentwicklung.
- **.NET SDK**: Entwicklungsumgebung für .NET-Anwendungen.
- **PostgreSQL**: Relationale Datenbank für lokale Entwicklungs- und Testzwecke.
- **PHP**: Skriptsprache für Webentwicklung und lokale Tests.
- **Nginx**: Webserver für lokale Entwicklungsumgebungen.
- **Chrome**: Webbrowser zur Entwicklung und zum Testen von Webanwendungen.
- **Java** : Programmiersprache und Laufzeitumgebung für die Entwicklung und das Testen von vpn Java-Anwendungen.
- **Golang**: Programmiersprache, die für die Entwicklung von effizienten und skalierbaren Anwendungen verwendet wird, insbesondere für Netzwerk- und Backend-Services.
- **Rust**:Moderne Programmiersprache mit Fokus auf Sicherheit und Performance, ideal für Systemprogrammierung und performante Anwendungen.
- **C/C++**: Klassische Programmiersprachen für System- und Anwendungsentwicklung, werden in meiner Umgebung jedoch nur selten genutzt, z. B. für spezielle Performance- oder Kompatibilitätsanforderungen.
### Testen von CMS-Funktionen und Datenbanken

Ich teste regelmäßig neue Funktionen in den Content-Management-Systemen **MediaWiki**, **Drupal**, **Typo3** und **Orchard** auf meinem Entwicklungsrechner. Dabei prüfe ich gezielt die Kompatibilität und das Verhalten sowohl mit **SQLite3** als auch mit **PostgreSQL** als Datenbank-Backend. Bisher traten dabei keine Probleme auf; beide Datenbanksysteme funktionieren zuverlässig mit den genannten CMS-Lösungen.

**Hinweis:** Die Entwicklungsumgebung ist so konfiguriert, dass sie möglichst nah an der Produktionsumgebung arbeitet, um Kompatibilitätsprobleme zu vermeiden.Verwendete Technologien auf mein Entwicklungsrechner

### Dokumentation und Veröffentlichung mit MediaWiki und MkDocs

#### MediaWiki

Für die interne Dokumentation wird **MediaWiki** auf dem Server betrieben. Die Installation erfolgt über die offiziellen Pakete oder per Download von [mediawiki.org](https://www.mediawiki.org/). Nach der Grundinstallation werden folgende Schritte durchgeführt:

1. **Konfiguration:**  
    - Datenbankzugangsdaten und Admin-Benutzer einrichten.
    - Lokale Anpassungen in `LocalSettings.php` vornehmen (z. B. Sprache, Logo, Erweiterungen).
2. **Erweiterungen:**  
    - Installation nützlicher Extensions wie `VisualEditor`, `SyntaxHighlight_GeSHi` und `Cite`.
3. **Backup:**  
    - Regelmäßige Sicherung der Datenbank und des `images`-Verzeichnisses mittels Cronjob.

Die Dokumentation wird direkt im Browser gepflegt. Änderungen sind sofort sichtbar und versioniert.

#### MkDocs

Für die statische Dokumentation und Veröffentlichung nach außen wird **MkDocs** verwendet:

1. **Installation:**  
    ```bash
    pip install mkdocs mkdocs-material
    ```
2. **Projekt anlegen:**  
    ```bash
    mkdocs new mein-projekt
    cd mein-projekt
    ```
3. **Bearbeitung:**  
    - Markdown-Dateien im `docs/`-Verzeichnis erstellen und anpassen.
    - `mkdocs.yml` für Navigation und Theme konfigurieren.
4. **Bauen und Bereitstellen:**  
    ```bash
    mkdocs build
    rsync -av site/ user@server:/var/www/html/docs/
    ```
    Alternativ kann MkDocs auch direkt auf dem Server laufen und per Nginx ausgeliefert werden.

**Hinweis:**  
Sowohl MediaWiki als auch MkDocs werden regelmäßig aktualisiert. Die Dokumentation wird versioniert im Git-Repository gepflegt und automatisiert auf den Server übertragen.

