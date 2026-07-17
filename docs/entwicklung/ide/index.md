# IDE & Entwicklungsumgebung: Übersicht

Eine zentralisierte Übersicht über Entwicklungsumgebungen, Editoren, KI-Assistenten und Tools zur Einrichtung einer produktiven lokalen Entwicklungsumgebung unter Ubuntu.

---

## Entwicklungsumgebungen im Überblick

Moderne IDEs (Integrated Development Environments) und Code-Editoren bieten Entwicklern mächtige Werkzeuge zur effizienten Softwareentwicklung. Mit der Integration von KI-Assistenten wird die Produktivität noch einmal deutlich gesteigert.

### Entwicklungsumgebungs-Kategorien

| Kategorie | Beschreibung | Typische Tools |
|-----------|--------------|----------------|
| **Full-featured IDEs** | Komplette Entwicklungsumgebungen mit Debugging, Refactoring, Projektmanagement | IntelliJ IDEA, VS Code, PyCharm, WebStorm |
| **Code Editoren** | Leichte, schnelle Editoren mit Erweiterungsmöglichkeiten | VS Code, Sublime Text, Neovim, Zed |
| **Cloud IDEs** | Browser-basierte Entwicklungsumgebungen | GitHub Codespaces, Gitpod, Replit |
| **KI-IDE** | IDEs mit integrierter KI-Unterstützung | Google Antigravity, Cursor, GitHub Copilot |

---

## Hauptthemen

### 1. [System-Setup und Installation](setup.md)
**Detaillierte Anleitungen zur Einrichtung des lokalen Entwicklungsrechners** unter Ubuntu 25.10.

* **Systemvoraussetzungen**: Paketinstallationen, Updates, Abhängigkeiten
* **System-Setup**: passwortloses sudo, Treiber, Bibliotheken
* **Sprachruntimes**: Java, .NET, Python, Node.js, Go, Rust, C/C++
* **Datenbanken**: PostgreSQL, PostGIS, OSM-Datenverarbeitung
* **Entwicklungstools**: Git, GitHub CLI, Chrome, VS Code

**Unterstützte Sprachen & Frameworks:**
- .NET SDK, Node.js, Python, Java, Golang, Rust, C/C++
- Maven, npm, pip, cargo, etc.

**Ideal für:** Entwickler, die eine lokale Entwicklungsumgebung einrichten wollen.

---

### 2. [Lokale KI-Frontends](lokale-ki-frontends.md)
**Open-Source Web-UIs für lokale KI-Modelle** – Professionelle Alternativen zu Cloud-basierten KI-Assistenten.

* **Open WebUI** – Beste Integration für Ollama mit RAG und Dokumenten-Upload
* **LibreChat** – Multi-Provider-Unterstützung (OpenAI, Anthropic, Ollama, etc.)
* **Text-generation-webui (Oobabooga)** – Für Power-User mit manueller Modell-Kontrolle

**Architektur-Übersicht:**
```mermaid
graph TD
    A[Benutzer-Anfrage] --> B[Web-UI]
    B -->|API-Schnittstelle| C[Docker-Netzwerk]
    C -->|Port 11434| D[Ollama (lokale Modelle)]
    C -->|Externe API| E[Cloud APIs]
```

**Hauptmerkmale:**
- Direkte Ollama-Integration: Automatische Modell-Erkennung
- Integriertes RAG: Dokumenten-Upload und Vektorisierung
- Web-Search: Integration mit Suchmaschinen
- Benutzerverwaltung: Admin/User Rollen, Authentifizierung

---

### 3. Android-Entwicklung

[Detaillierte Anleitung zur Android-Entwicklung](android.md)

* **Android Studio**: Offizielle IDE für Android-Entwicklung
* **SDK & Tools**: Android SDK, Emulator, Build-Tools
* **Sprachen**: Kotlin (bevorzugt), Java
* **Frameworks**: Jetpack Compose, AndroidX, Material Design
* **.NET MAUI**: Cross-Platform mit .NET für mobile Apps

---

## Editoren & IDEs im Detail

### Full-featured IDEs

#### JetBrains Familie

| IDE | Primäre Sprache | Hauptmerkmale | Preis |
|-----|-----------------|---------------|-------|
| **IntelliJ IDEA** | Java, Kotlin | Java-Entwicklung, Spring, Android | Kostenlos / Ultimate |
| **PyCharm** | Python | Data Science, Web-Development | Kostenlos / Professional |
| **WebStorm** | JavaScript/TypeScript | Frontend-Entwicklung | Kostenpflichtig |
| **GoLand** | Go | Go-Entwicklung, Debugging | Kostenpflichtig |
| **RustRover** | Rust | Rust-Entwicklung | Kostenpflichtig |
| **CLion** | C/C++ | C/C++-Entwicklung | Kostenpflichtig |

#### Microsoft Visual Studio Familie

| IDE | Plattform | Hauptmerkmale |
|-----|-----------|---------------|
| **Visual Studio** | Windows | .NET, C++, Windows-Apps |
| **Visual Studio Code** | Cross-Platform | Erweiterbar, leicht, KI-Integration |

### Code Editoren

#### Visual Studio Code (VS Code)

**Vorteile:**
- Cross-Platform (Windows, macOS, Linux)
- Leicht und schnell
- Große Erweiterungbibliothek
- Integrierte Terminal- und Debugging-Tools
- Git-Integration

**Wichtige Erweiterungen:**
- **GitHub Copilot** – KI-gestützte Code-Vervollständigung
- **Claude Code** – Intelligente Code-Assistenz
- **OpenAI ChatGPT** – ChatGPT-Integration
- **Java Extension Pack** – Java-Unterstützung
- **Python** – Python-Sprachunterstützung
- **C/C++** – C/C++-Entwicklung
- **ESLint** – JavaScript-Linting
- **Prettier** – Code-Formatierung

#### Neovim

**Vorteile:**
- Terminal-basiert
- Extrem anpassbar (VimScript, Lua)
- Plugin-System (LSP, Treesitter, etc.)
- Leicht und schnell
- Cross-Platform

**Beliebte Plugins:**
- **coc.nvim**: Intellisense Engine
- **nvim-treesitter**: Syntax-Highlighting
- **telescope.nvim**: Fuzzy Finder
- **nvim-lspconfig**: LSP-Konfiguration

#### Zed

**Vorteile:**
- Moderner, schneller Editor
- Kollaboratives Coding
- KI-Integration (Zed AI)
- Rust-basiert
- Cross-Platform

---

## KI-Assistenten für Entwickler

### KI-Integration in IDEs

| KI-Tool | IDE/Editor | Hauptmerkmale | Preis |
|---------|------------|---------------|-------|
| **GitHub Copilot** | VS Code, JetBrains, Neovim | Code-Vervollständigung, Chat | $10/Monat |
| **Claude Code** | VS Code, JetBrains | Intelligente Assistenz, Chat | $20/Monat |
| **Antigravity CLI** | Terminal, Antigravity IDE | Lokale & Cloud-KI | Kostenlos |
| **CODEX CLI** | Terminal | Code-Generierung | Kostenlos |
| **Tabnine** | VS Code, JetBrains | Enterprise-KI | Ab $15/Monat |
| **Amazon CodeWhisperer** | VS Code, JetBrains | AWS-integriert | Kostenlos |

### KI-Funktionen in der Entwicklung

#### Code-Generierung
- Automatische Funktionenerstellung basierend auf Kommentaren
- Boilerplate-Code-Generierung (Classes, Interfaces, DTOs)
- Test-Generierung (Unit Tests, Integration Tests)
- Dokumentations-Generierung (Kommentare, READMEs)

#### Code-Analyse & Verbesserung
- Fehlererkennung und Vorschläge zur Behebung
- Code-Refactoring und Optimierungsvorschläge
- Sicherheitsanalysen und Schwachstellenerkennung
- Performance-Optimierungen

---

## Entwicklungs-Workflows mit KI

### Typischer Entwicklungsprozess mit KI

1. **Idee** → 2. **Anforderungen** → 3. **Architektur** → 4. **Code mit KI** → 5. **KI-Review** → 6. **KI-Tests** → 7. **Deployment** → 8. **KI-Monitoring**

### Praxisbeispiel: Feature-Entwicklung

**Schritte:**
1. Anforderungsbeschreibung in natürlicher Sprache
2. KI-gestützte Zerlegung in Aufgaben
3. Code-Generierung für Boilerplate
4. Implementierung mit KI-Assistenz
5. Automatisierte Tests mit KI-Generierung
6. Code-Review mit KI-Analyse
7. Deployment mit KI-Optimierung

**Zeitersparnis:** 40-60% gegenüber traditioneller Entwicklung

---

## IDE-Konfiguration & Best Practices

### VS Code Einstellungen

**Empfohlene Einstellungen (`settings.json`):**
```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.formatOnSave": true,
  "files.autoSave": "onFocusChange"
}
```

---

## Remote-Entwicklung

### SSH Remote Development

**VS Code Remote-SSH:**
- Remote SSH Extension installieren
- Konfiguration in ~/.ssh/config
- Mit Remote Server verbinden

### Container-Entwicklung

**VS Code Dev Containers:**
- Docker-Container als Entwicklungsumgebung
- Konsistente Umgebungen für das Team

---

## Verwandte Themen

* [Tools & Hilfswerkzeuge](../../wissen/tools/index.md) – Entwicklungs- und Analyse-Tools
* [Server/Konfiguration](../infrastruktur/software.md) – Server-Setup und -Verwaltung
* [Webentwicklung/KI Webentwicklung](../webentwicklung/ki-webentwicklung.md) – KI in der Webentwicklung
* [Desktop Automation](../../künstliche-intelligenz/automatisierung/index.md) – Automatisierung von GUI-Interaktionen
* [Content/KI-gestützte Inhalte](../../künstliche-intelligenz/content/index.md) – KI für Content-Erstellung

---

## Weiterführende Ressourcen

### Offizielle Dokumentationen
- [Visual Studio Code](https://code.visualstudio.com/docs)
- [JetBrains IDEs](https://www.jetbrains.com/help/)
- [Neovim](https://neovim.io/doc/)
- [Zed](https://zed.dev/docs)

### KI-Entwicklungstools
- [GitHub Copilot](https://github.com/features/copilot)
- [Claude Code](https://claude.ai/code)
- [Antigravity IDE](https://antigravity.google/)
- [Open WebUI](https://github.com/open-webui/open-webui)
- [LibreChat](https://github.com/danny-avila/LibreChat)

---

*Letzte Aktualisierung: Juli 2026*
