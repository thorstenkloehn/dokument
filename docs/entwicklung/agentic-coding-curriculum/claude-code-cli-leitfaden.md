# End-to-End Leitfaden: Softwareentwicklung mit Claude Code CLI

> **Vollständiger Praxis-Guide:** Von der Ersteinrichtung (`claude init`), Skills (`SKILL.md`), Subagenten (`.claude/agents/`) und Hooks über den Agentic Coding Workflow bis hin zum fertigen Production-Release mit **Claude Code**.

!!! note "Hinweis: Herkunft & Verhältnis zum Claude Code Praxis-Handbuch"
    Verarbeitet aus `raw/Claude_Code.md` nach dem [LLM-Wiki-Pattern](../../wissen/dokumentation/llm-wiki-pattern-karpathy.md), Teil der Rubrik [Agentic Coding & Curriculum](index.md). Diese Seite überschneidet sich inhaltlich mit dem bereits bestehenden [Claude Code Praxis-Handbuch](../../künstliche-intelligenz/coding/claude-code-praxis.md) — beide behandeln Setup, `CLAUDE.md`, Skills, Hooks und MCP. Eigenständigen Mehrwert bietet diese Seite vor allem durch die vollständige **Konfigurationsdateien-Referenz** (Abschnitt 1.5) und die Einordnung in den 9-phasigen Entwicklungs-Workflow dieses Curriculums.

---

## Übersicht des Claude Code Entstehungs-Workflows

```mermaid
graph TD
    S1["1. Installation &amp; CLI-Auth"] --> S2["2. Projektsystem: claude init,<br/>CLAUDE.md, Skills, Subagenten,<br/>Hooks &amp; MCP"]
    S2 --> S3["3. Subagenten-Delegation<br/>&amp; Architektur-Planung"]
    S3 --> S4["4. Autonomer TDD-Loop<br/>&amp; Coding"]
    S4 --> S5["5. Multi-File Edits<br/>&amp; Debugging"]
    S5 --> S6["6. Linter, Quality<br/>&amp; Security Audits"]
    S6 --> S7["7. Dokumentation<br/>&amp; Git Integration"]
    S7 --> S8["8. Production Build,<br/>Packaging &amp; Release"]
    S8 --> S9["9. Skalierung: Permissions,<br/>Plugins, Headless-CI<br/>&amp; Team-Rollout"]
```

---

## 1. Phase: Installation, Authentifizierung & `claude init` (Setup)

### 1.1 Systemvoraussetzungen & Installation
* **Voraussetzungen:** Node.js (v18+) & Git im Terminal installiert.
* **Globale Installation via npm:**
  ```bash
  npm install -g @anthropic-ai/claude-code
  ```

### 1.2 Authentifizierung & API Key
* Starten von Claude Code im Terminal:
  ```bash
  claude
  ```
* Erstmalige Authentifizierung über das Web-Terminal oder durch Hinterlegung des Anthropic API-Keys (`ANTHROPIC_API_KEY`).

### 1.3 Automatische Projekt-Initialisierung mit `claude init`
Führe im Wurzelverzeichnis deines Projekts den Befehl `/init` (bzw. `claude init` aus der Shell heraus) aus:
```bash
claude
> /init
```
* **Was `/init` macht:**
    * Scannt automatisch dein Repository, erkennt Sprache (Rust, TypeScript, Python) und Build-Tools (Cargo, npm, pytest).
    * Generiert automatisch eine optimale `CLAUDE.md` Datei mit vordefinierten Build-, Test- und Linter-Kommandos.
    * Existiert bereits eine `CLAUDE.md`, schlägt `/init` nur noch Verbesserungen vor, statt sie zu überschreiben.
    * Liest dabei auch Regeldateien anderer Tools (`.cursor/rules/`, `.cursorrules`, `.github/copilot-instructions.md`) und übernimmt relevante Teile.
    * Mit der Umgebungsvariable `CLAUDE_CODE_NEW_INIT=1` läuft ein interaktiver Mehrphasen-Flow: Claude fragt gezielt nach, welche Artefakte (CLAUDE.md, Skills, Hooks) angelegt werden sollen, erkundet die Codebase per Subagent und legt vor dem Schreiben einen prüfbaren Vorschlag vor. In diesem Modus liest `/init` zusätzlich `AGENTS.md`, `.devin/rules/`, `.windsurf/rules/`/`.windsurfrules` und `.clinerules`.

### 1.4 Wer erstellt die `CLAUDE.md`? (Mensch vs. KI-Agent)
* **Vom KI-Agenten (Automatisch):** Bei der Ausführung von `/init` scannt der KI-Agent das Repository und generiert automatisch das Erst-Setup der `CLAUDE.md` mit allen erkannten Build-, Test- und Linter-Befehlen.
* **Vom Menschen (Manuell & Verfeinerung):** Der Entwickler kann die `CLAUDE.md` von Hand anlegen oder die von der KI generierte Datei um projektspezifische Qualitäts-, Style- und Architekturregeln ergänzen.
* **Best Practice (Zusammenspiel Mensch & KI):**
    1. Der **KI-Agent** generiert das Grundgerüst automatisch via `/init`.
    2. Der **Mensch** verfeinert und ergänzt individuelle Richtlinien (z. B. Verbot von `unwrap()`, Durchsetzung Hexagonaler Architektur), an die sich der KI-Agent bei allen zukünftigen Sitzungen hält.
    3. Faustregel für den Umfang: **unter 200 Zeilen pro `CLAUDE.md`**. Längere Dateien kosten mehr Kontext und werden weniger zuverlässig befolgt — Details gehören stattdessen in `.claude/rules/` (pfadgebunden) oder in einen Skill (siehe [2.6](#26-hooks-ereignisgesteuerte-automatisierung)).

### 1.5 Vollständige Referenz aller Projekteinstellungen & Konfigurationsdateien

Für eine maximale Kontrolle über Claude Code und Agentic-AI-Projekte stehen **alle folgenden Konfigurationsebenen und Dateien** zur Verfügung. Alle Pfade sind die tatsächlich von der Claude Code CLI gelesenen Speicherorte.

---

#### 1. `CLAUDE.md` (Projekt-Prompts & Verhaltensregeln)
* **Dateipfad (nach Priorität):**
    * `/etc/claude-code/CLAUDE.md` bzw. plattformspezifischer Managed-Policy-Pfad — organisationsweit, per MDM verteilt
    * `~/.claude/CLAUDE.md` — persönliche Vorlieben für alle Projekte
    * `./CLAUDE.md` oder `./.claude/CLAUDE.md` — teamweite Projektregeln (versioniert)
    * `./CLAUDE.local.md` — persönliche, nicht versionierte Projekt-Notizen (gehört in `.gitignore`)
* **Format:** Markdown, wird als User-Message zu Sessionbeginn geladen (nicht Teil des System-Prompts)
* **Inhalt & Parameter:**
    * **Build- & Testkommandos:** Vordefinierte CLI-Befehle (`cargo build`, `cargo test`, `npm test`, `pytest`).
    * **Code-Style & Konventionen:** Formatting-Regeln, Naming Conventions, Fehlerbehandlungs-Policies (z. B. *„Keine `unwrap()` in Produktion"*).
    * **Architektur-Vorgaben:** Hexagonale Architektur, Domain-Driven Design (DDD), Modularisierungsregeln.
    * **`@pfad`-Imports:** Weitere Dateien lassen sich per `@README` oder `@docs/git-instructions.md` einbinden (max. 4 Verschachtelungsebenen).
* **AGENTS.md-Kompatibilität:** Claude Code liest `AGENTS.md` **nicht** nativ. Existiert im Repo bereits ein tool-übergreifendes `AGENTS.md` (z. B. für Cursor/Copilot), bindet man es per Import ein, statt Inhalte zu duplizieren:
  ```markdown
  @AGENTS.md

  ## Claude Code
  Nutze den Plan-Modus für Änderungen unter `src/billing/`.
  ```
  Alternativ funktioniert ein Symlink (`ln -s AGENTS.md CLAUDE.md`), unter Windows nur mit Admin-Rechten/Dev-Mode — dort lieber den Import nutzen.

---

#### 2. `.claude/settings.json` (CLI-Laufzeiteinstellungen & Rechte)
* **Dateipfad & Geltungsbereich (Priorität von niedrig nach hoch):**
    * `~/.claude/settings.json` — User-weit
    * `.claude/settings.json` — Projekt, versioniert, teamweit gültig
    * `.claude/settings.local.json` — Projekt, lokal, **nicht** versionieren (persönliche Overrides)
    * Managed Policy (`managed-settings.json` unter `/etc/claude-code/`, `/Library/Application Support/ClaudeCode/` bzw. `C:\Program Files\ClaudeCode\`) — höchste Priorität, IT-verwaltet
* **Format:** JSON
* **Reales Schema (Auszug der wichtigsten Keys):**

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "claude-sonnet-5",
  "effortLevel": "high",
  "permissions": {
    "allow": ["Bash(npm run *)", "Bash(cargo check)", "Read(~/.zshrc)"],
    "deny": ["Bash(curl *)", "Read(./.env*)", "Read(./**/*.pem)"]
  },
  "env": {
    "RUST_LOG": "debug",
    "DATABASE_URL": "postgresql://user:pass@localhost:5432/mydb_dev"
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "cargo fmt --check" }
        ]
      }
    ]
  },
  "outputStyle": "default",
  "statusLine": { "type": "command", "command": "./scripts/statusline.sh" },
  "cleanupPeriodDays": 30
}
```
  * `permissions.allow` / `permissions.deny` / `permissions.ask` ersetzen ein simples Allow-/Denylist-Konzept durch **Tool-Pattern-Strings** (`Bash(git status)`, `Read(./secrets/**)`, …) — siehe [9.1](#91-permission-modi-plan-mode).
  * Es gibt keine `maxTokens`/`temperature`-Steuerung auf dieser Ebene; Modellwahl läuft über `model`, Denkaufwand über `effortLevel` (`low`/`medium`/`high`/`xhigh`).
  * Ausschluss von Dateien aus dem Kontext läuft über `permissions.deny` bzw. das Beachten von `.gitignore` — ein separates `.claudeignore`-Dateiformat existiert nicht.
  * Vollständige Schlüsselliste (Auswahl weiterer Bereiche): `disableBundledSkills`, `allowedMcpServers`/`deniedMcpServers`, `strictKnownMarketplaces`, `apiKeyHelper`, `autoCompactWindow`, `alwaysThinkingEnabled`, `claudeMd` (nur in Managed Settings), `sandbox.enabled`.

---

#### 3. `.mcp.json` (Model Context Protocol Konfiguration)
* **Dateipfad:** `./.mcp.json` im Projekt-Root (teamweit, versioniert) — Server auf User-Ebene werden dagegen in `~/.claude.json` registriert.
* **Format:** JSON
* **Zweck:** Registrierung von externen Werkzeugen, Datenbanken, APIs und Dateisystem-Kontexten.
* **Vollständiges Schema:**

```json
{
  "mcpServers": {
    "postgres": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "postgresql://user:pass@localhost/db"],
      "env": { "PGPORT": "5432" }
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": { "GITHUB_PERSONAL_ACCESS_TOKEN": "ghp_xxxx..." }
    }
  }
}
```
* Projektspezifische Server aus `.mcp.json` müssen beim ersten Start pro Nutzer bestätigt werden (`enabledMcpjsonServers` in `settings.json` steuert das Auto-Approval); das verhindert, dass ein Repo unbemerkt einen fremden MCP-Server ausführt.

---

#### 4. `.claude/agents/` (Subagenten-Definitionen)
* **Dateipfad:** `.claude/agents/<name>.md` (Projekt) bzw. `~/.claude/agents/<name>.md` (User-weit, projektübergreifend)
* **Format:** Markdown mit YAML-Frontmatter (`name`, `description`, `tools`, `model`)
* **Zweck:** Wiederverwendbare, spezialisierte Subagenten mit eigenem System-Prompt, eigenem Kontextfenster und eingeschränkten Tool-Rechten — siehe [2.4](#24-subagenten-dateien-subagenten-workflow).

---

#### 5. `.claude/skills/` (Skill-System) & `.claude/commands/` (Slash Commands)
* **Dateipfad Skills:** `.claude/skills/<skill_name>/SKILL.md` (Projekt) bzw. `~/.claude/skills/<skill_name>/SKILL.md` (User-weit)
* **Bestandteile eines Skills:**
    * `SKILL.md` (YAML-Frontmatter: `description`, optional `disable-model-invocation`, `argument-hint` + Markdown-Anweisungen)
    * Beliebige Zusatzdateien im selben Ordner (Skripte, Vorlagen, Referenzdokumente) — werden erst bei Bedarf nachgeladen, nicht bei Sessionstart.
* **Dateipfad Commands (Legacy-/Kurzform):** `.claude/commands/<name>.md` (Projekt) bzw. `~/.claude/commands/<name>.md` (User-weit) — eine einzelne flache Markdown-Datei statt eines ganzen Ordners.
    * `.claude/commands/deploy.md` und `.claude/skills/deploy/SKILL.md` erzeugen **beide** denselben Befehl `/deploy` und funktionieren technisch identisch (Slash Commands wurden mit dem Skill-System zusammengeführt).
    * Nutze `.claude/commands/` für kurze Ein-Datei-Befehle ohne Zusatzdateien; nutze `.claude/skills/<name>/` sobald du Skripte/Vorlagen mitliefern, `disable-model-invocation` setzen oder Claude den Skill selbstständig triggern lassen willst.
    * `$ARGUMENTS` im Dateitext wird durch den Text ersetzt, der nach `/name` folgt, z. B. `/deploy staging`.
* **Kein Registrierungs-JSON nötig:** Beide werden automatisch erkannt. Für teamweite/geteilte Skills bzw. Commands nutzt man stattdessen **Plugins** (siehe [9.2](#92-plugins-marketplaces)).

---

#### 6. `.claude/rules/` (Pfadgebundene Zusatzregeln)
* **Dateipfad:** `.claude/rules/*.md`, rekursiv (auch Unterordner wie `frontend/`, `backend/`)
* **Zweck:** Regeln, die nur geladen werden, wenn Claude an passenden Dateien arbeitet — hält `CLAUDE.md` schlank.
* **Beispiel mit Pfadbindung:**
```markdown
---
paths:
  - "src/api/**/*.ts"
---
# API Development Rules
- Alle Endpoints benötigen Input-Validierung.
- Fehlerantworten folgen dem Standardformat.
```
Regeln ohne `paths`-Feld laden unconditional, mit derselben Priorität wie `.claude/CLAUDE.md`.

---

#### 7. Umgebungsvariablen (CLI Environment Variables Overrides)
Im Terminal können globale CLI-Einstellungen durch Umgebungsvariablen überschrieben werden:

| Variable | Beschreibung | Beispiel |
| :--- | :--- | :--- |
| `ANTHROPIC_API_KEY` | Authentifizierungsschlüssel für Claude API | `sk-ant-api03-...` |
| `CLAUDE_CONFIG_DIR` | Benutzerdefinierter Pfad zum Konfigurationsordner | `/home/user/.config/claude` |
| `CLAUDE_CODE_DISABLE_AUTO_MEMORY` | Auto Memory global deaktivieren | `1` |
| `HTTP_PROXY` / `HTTPS_PROXY` | Proxy-Server für Firmennetzwerke | `http://proxy.company.com:8080` |
| `CLAUDE_CODE_NEW_INIT` | Interaktiven Mehrphasen-`/init`-Flow aktivieren | `1` |

---

#### Übersichtstabelle aller Konfigurationsdateien

| Datei / Ordner | Pfad | Format | Hauptfunktion |
| :--- | :--- | :--- | :--- |
| **`CLAUDE.md`** | `./CLAUDE.md` oder `./.claude/CLAUDE.md` | Markdown | KI-Prompts, Build/Test-Befehle, Code-Styles |
| **`settings.json`** | `.claude/settings.json` (+ `~/.claude/`, `.local.json`) | JSON | Rechte (`allow`/`deny`/`ask`), Hooks, Envs, Modellwahl |
| **`.mcp.json`** | `./.mcp.json` | JSON | MCP-Server Registrierung (DB, APIs, Tools) |
| **`.claude/agents/`** | `.claude/agents/*.md` | Markdown + YAML | Subagenten-Definitionen |
| **`SKILL.md`** | `.claude/skills/*/SKILL.md` | YAML + MD | Wiederverwendbare Workflows & Slash Commands |
| **`.claude/commands/`** | `.claude/commands/*.md` | Markdown | Slash Commands als Einzeldatei (Legacy-/Kurzform von Skills) |
| **`.claude/rules/`** | `.claude/rules/*.md` | Markdown + YAML | Pfadgebundene Zusatzregeln |
| **`.claude-plugin/plugin.json`** | `<plugin-root>/.claude-plugin/plugin.json` | JSON | Bündelt Skills/Agents/Hooks/MCP zu einem teilbaren Plugin |
| **`~/.claude.json`** | `~/.claude.json` | JSON | Globale User-Einstellungen, MCP-Server auf User-Ebene |
| **Auto Memory** | `~/.claude/projects/<project>/memory/` | Markdown | Von Claude selbst geschriebene Lernpunkte (siehe [2.7](#27-auto-memory-selbststandiges-lernen)) |

---

## 2. Phase: Agent-Dateien, Skills (`SKILL.md`), Subagenten & Hooks

### 2.1 `CLAUDE.md` als zentrale Regeldatei
Claude Code liest ausschließlich `CLAUDE.md` (nicht `AGENTS.md`) für projektweite Verhaltensregeln — siehe [1.5 Punkt 1](#1-claudemd-projekt-prompts-verhaltensregeln) zur Ladereihenfolge und AGENTS.md-Kompatibilität per Import.

* **Beispiel `CLAUDE.md`:**
  ```markdown
  # Projektregeln

  ## Code-Qualität & Safety
  - Nutze in Rust niemals `unsafe` ohne explizite Sicherheitsbegründung in Kommentaren.
  - Verwende keine Platzhalter oder Stubs; jede Funktion muss vollständig implementiert werden.
  - Führe nach jeder Änderung `cargo check` und `cargo test` durch.

  ## Architektur-Vorgaben
  - Halte strikt die Hexagonale Architektur (Ports & Adapters) ein.
  ```
* Für Regeln, die zwingend und ohne Interpretationsspielraum durchgesetzt werden müssen (z. B. „niemals direkt auf `main` pushen"), reicht `CLAUDE.md` nicht aus — Claude behandelt den Inhalt als Kontext, nicht als harte Vorgabe. Dafür sind **Hooks** (siehe [2.6](#26-hooks-ereignisgesteuerte-automatisierung)) oder `permissions.deny` das richtige Werkzeug.

---

### 2.2 Custom Skills (`SKILL.md`) – Modulare Fähigkeiten
Skills erlauben es, Claude Code wiederverwendbare Anweisungen, Workflows und Skripte beizubringen. Sie werden entweder automatisch von Claude aufgerufen (modellgesteuert, basierend auf der `description`) oder explizit per `/skill-name` getriggert.

* **Struktur eines Skills:** `.claude/skills/<skill_name>/`
    * `SKILL.md` (Enthält YAML-Frontmatter mit `description` sowie Anweisungen)
    * Optional beliebige Zusatzdateien (Skripte, Vorlagen, Referenzdokumente) im selben Ordner

* **Beispiel `.claude/skills/rust_security_audit/SKILL.md`:**
  ```markdown
  ---
  description: Führt ein vollständiges Security-Audit mit cargo audit, clippy und Miri durch. Nutzen bei Sicherheits-Reviews oder vor Releases.
  ---

  # Rust Security Audit Workflow

  1. Führe `cargo audit` aus und fange bekannte Vulnerabilities ab.
  2. Führe `cargo clippy -- -D warnings` aus.
  3. Prüfe alle `unsafe`-Blöcke im Codebase und starte `cargo miri test`.
  ```

* **Argumente an Skills übergeben:** `$ARGUMENTS` im Skill-Text wird durch den Text ersetzt, der nach `/skill-name` folgt, z. B. `/rust_security_audit src/worker.rs`.
* **Nur manuell aufrufbar machen:** `disable-model-invocation: true` im Frontmatter verhindert, dass Claude den Skill selbstständig triggert — sinnvoll für destruktive oder teure Workflows.
* **Teilen im Team:** Für Skills, die über ein einzelnes Projekt hinaus verteilt werden sollen, siehe [Plugins](#92-plugins-marketplaces) statt Kopieren des `.claude/skills/`-Ordners.

---

### 2.3 Custom Slash Commands
Slash Commands und Skills wurden technisch zusammengeführt: eine flache Datei `.claude/commands/deploy.md` und ein Skill-Ordner `.claude/skills/deploy/SKILL.md` erzeugen beide denselben Befehl `/deploy` und funktionieren identisch. Für neue Commands empfiehlt sich die Skill-Ordnerstruktur, weil sie zusätzlich Zusatzdateien, Tool-Beschränkungen und automatische Modellauswahl erlaubt.

* **Eingebaute Commands (Auswahl):** `/init`, `/context`, `/compact`, `/memory`, `/cost`, `/resume`, `/rewind`, `/permissions`, `/plugin`, `/agents`, `/doctor`.

---

### 2.4 Subagenten-Dateien & Subagenten-Workflow
Für komplexe, vielschichtige Aufgaben kann Claude Code **Subagenten** spawnen. Jeder Subagent läuft in seinem eigenen isolierten Kontextfenster mit eigenem System-Prompt, eigenen Tool-Rechten und ggf. eigenem Modell, und gibt nur eine Zusammenfassung an den Hauptagenten zurück.

* **Definitionsdatei:** `.claude/agents/<name>.md` (Projekt) oder `~/.claude/agents/<name>.md` (User-weit)
* **Beispiel `.claude/agents/code-auditor.md`:**
  ```markdown
  ---
  name: code-auditor
  description: Prüft Code-Qualität, Linter-Compliance und Borrow-Checker-Warnungen. Proaktiv nach größeren Refactorings einsetzen.
  tools: Read, Grep, Glob, Bash
  model: sonnet
  ---

  Du bist ein spezialisierter Code-Auditor für Rust-Projekte. Prüfe jede Datei
  auf Clippy-Warnungen, unsauberes Error-Handling und fehlende Tests, bevor
  du eine Zusammenfassung an den Hauptagenten zurückgibst.
  ```
* **Typische Rollen:**
    * **Research-Subagent:** Durchsucht die Codebase oder Dokumentation, ohne Dateien zu verändern.
    * **Test-Generator-Subagent:** Erstellt isoliert Unit-Tests für neue Module.
    * **Code-Auditor-Subagent:** Prüft Code-Qualität, Linter-Compliance und Borrow-Checker.

* **Subagenten per Prompt beauftragen:**
  > *"Starte einen Subagenten zur Recherche der Datenbank-Migrationen. Lass einen zweiten Subagenten parallel die API-Tests in `tests/api.rs` schreiben."*

* **Persistentes Gedächtnis pro Subagent:** Über das Frontmatter-Feld `memory` kann ein Subagent ein eigenes Auto-Memory-Verzeichnis führen, getrennt von dem des Hauptagenten.
* **Sichtbarkeit prüfen:** `/context` zeigt registrierte Subagenten unter „Custom Agents" an.

---

### 2.5 Model Context Protocol (MCP) Integration
Binde externe Tools und Datenbanken über MCP in Claude Code ein:
```bash
claude mcp add postgres -- npx -y @modelcontextprotocol/server-postgres postgresql://user:password@localhost/mydb
```
Das `--` trennt die Claude-Code-eigenen Flags von Kommando und Argumenten des MCP-Servers. Der Server landet je nach gewähltem Scope entweder in `~/.claude.json` (User) oder in `.mcp.json` (Projekt, teamweit versioniert).

---

### 2.6 Hooks — ereignisgesteuerte Automatisierung
Hooks führen bei definierten Lebenszyklus-Ereignissen automatisch ein Shell-Kommando aus — unabhängig davon, was das Modell „entscheidet". Sie sind das richtige Werkzeug für harte Vorgaben, die `CLAUDE.md` nicht garantieren kann (z. B. „nach jedem Edit automatisch formatieren" oder „`rm -rf` immer blockieren").

* **Konfiguriert in:** `hooks` innerhalb von `.claude/settings.json` (oder `hooks/hooks.json` in einem Plugin)
* **Wichtige Ereignisse (Auswahl von über 30):**

| Event | Ausgelöst wenn |
| :--- | :--- |
| `SessionStart` / `SessionEnd` | Session beginnt / endet |
| `UserPromptSubmit` | Prompt abgeschickt, bevor Claude ihn verarbeitet |
| `PreToolUse` | Vor einem Tool-Aufruf — kann ihn blockieren |
| `PostToolUse` | Nach erfolgreichem Tool-Aufruf |
| `Stop` | Claude beendet seine Antwort |
| `SubagentStart` / `SubagentStop` | Subagent wird gestartet / beendet |
| `PreCompact` / `PostCompact` | Vor/nach Kontext-Kompression |

* **Beispiel:** Nach jedem Schreib-/Edit-Zugriff automatisch `cargo fmt` prüfen:
  ```json
  {
    "hooks": {
      "PostToolUse": [
        {
          "matcher": "Write|Edit",
          "hooks": [
            { "type": "command", "command": "cargo fmt --check", "timeout": 30 }
          ]
        }
      ]
    }
  }
  ```
* **Blockieren statt nur beobachten:** Ein `PreToolUse`-Hook kann per Exit-Code bzw. JSON-Antwort (`permissionDecision: "deny"`) einen Tool-Aufruf verhindern — z. B. um `rm -rf` in Bash-Kommandos hart zu unterbinden, egal was das Modell vorschlägt.

---

### 2.7 Auto Memory — selbstständiges Lernen
Neben `CLAUDE.md` (von Menschen geschrieben) führt Claude Code ein zweites, komplementäres Gedächtnis: **Auto Memory**. Claude speichert dort eigenständig Erkenntnisse aus Korrekturen und Präferenzen, die es im nächsten Gespräch wiederverwendet — vollautomatisch, ohne dass jemand eine Datei pflegt.

* **Speicherort:** `~/.claude/projects/<project>/memory/` — ein `MEMORY.md` als Index plus optionale Themendateien (z. B. `debugging.md`).
* **Was hineingehört:** Build-Befehle, Debugging-Erkenntnisse, entdeckte Präferenzen — nicht redundant zu dem, was ohnehin im Code oder in `CLAUDE.md` steht.
* **Ladeverhalten:** Nur die ersten 200 Zeilen / 25 KB von `MEMORY.md` laden automatisch zu Sessionbeginn; Themendateien liest Claude bei Bedarf nach.
* **Ein-/Ausschalten:** `autoMemoryEnabled` in `settings.json`, oder Umschalter im `/memory`-Command.
* **Einsehen & bearbeiten:** `/memory` öffnet CLAUDE.md-Dateien und den Auto-Memory-Ordner zum direkten Editieren — alles ist normales Markdown.

---

## 3. Phase: Projekt-Initialisierung & Architektur-Planung

### 3.1 Workspace-Scan & Analyse
Starten der interaktiven CLI-Session:
```bash
claude
```
* **Prompt zur Erstanalyse:**
  > *"Analysiere die aktuelle Projektstruktur. Lies die `CLAUDE.md` und verfügbaren Skills aus `.claude/skills/`."*

### 3.2 Generierung des Architektur-Plans
Lass Claude Code vor der Implementierung einen detaillierten `implementation_plan.md` erstellen — idealerweise im **Plan-Modus** (siehe [9.1](#91-permission-modi-plan-mode)), damit dabei noch keine Dateien verändert werden:
> *"Erstelle einen meilensteinbasierten Implementierungsplan für ein verteiltes REST-Backend in Rust mit Axum und SQLx. Gliedere den Plan in Datenmodell, Business-Logik, API-Endpoints und Tests."*

---

## 4. Phase: Autonomer TDD-Loop & Subagentic Coding

### 4.1 Test-Driven Development (TDD)
> *"Schreibe zuerst die Unit-Tests für das Benutzer-Authentifizierungs-Modul in `tests/auth_test.rs`. Führe danach `cargo test` aus, damit die Tests fehlschlagen (Red-Phase)."*

### 4.2 Autonome Iterationsschleife
Claude Code führt den folgenden Zyklus eigenständig aus:

1. **Dateiänderung vorschlagen & anwenden** (über File-Editor-Tools).
2. **Kompilierungs- & Test-Befehl ausführen** (`cargo test`).
3. **Compiler- & Borrow-Checker-Ausgaben lesen** und Code anpassen.
4. **Schleife wiederholen**, bis alle Tests grün sind.

---

## 5. Phase: Multi-File Refactoring & Debugging

### 5.1 Dateiübergreifendes Refactoring
> *"Refaktorisier das Error-Handling im gesamten Projekt. Erstelle einen zentralen `AppError`-Enum in `src/error.rs` und passe alle Datenbank- und API-Aufrufe an."*

### 5.2 Debugging mit Subagenten
> *"Beauftrage einen Debugger-Subagenten, um den Stacktrace der Panik in `src/worker.rs` zu analysieren und eine Behebung vorzuschlagen."*

---

## 6. Phase: Qualitäts-Audits & Sicherheit (Quality Engineering)

### 6.1 Ausführen des Custom Security Skills
> *"Führe den Skill `rust_security_audit` aus `.claude/skills/` aus."*

### 6.2 Linter- & Formatting-Checks
> *"Führe `cargo clippy -- -D warnings` und `cargo fmt` aus. Behebe alle Warnungen."*

---

## 7. Phase: Dokumentation & Git-Workflow

### 7.1 Generierung von Rustdoc & Doctests
> *"Erstelle für alle öffentlichen Funktionen in `src/` Rustdoc-Kommentare (`///`) inklusive ausführbarer Code-Beispiele (Doctests)."*

### 7.2 Automatisierter Git-Commit & Pull Request Process
1. **Git Status & Diff analysieren:** `git status` / `git diff`
2. **Commit mit Conventional Message:** `git commit -m "feat(auth): implement JWT validation"`
3. **Pull Request via GitHub CLI:** `gh pr create`

---

## 8. Phase: Production Build, Packaging & Release (Fertiges Produkt)

### 8.1 Release Build & Docker-Containerisierung
> *"Erstelle ein Multi-Stage Dockerfile für eine statisch gelinkte Rust-Anwendung (musl target) auf `scratch`."*

### 8.2 CI/CD-Pipeline Erstellung
> *"Erstelle einen GitHub Actions Workflow `.github/workflows/ci.yml`, der bei jedem Push Tests, Linter (`clippy`), Formatting (`fmt`) und Docker-Builds ausführt."*

---

## 9. Phase: Skalierung — Permissions, Plugins, Headless-CI & Team-Rollout

### 9.1 Permission-Modi & Plan Mode
Claude Code fragt standardmäßig vor riskanten Aktionen (Dateischreibzugriffe, Shell-Kommandos) nach. Das Verhalten lässt sich fein steuern:

* **Plan Mode:** Claude analysiert und plant, verändert aber keine Dateien und führt keine Kommandos aus — ideal für die Architekturphase (siehe [3.2](#32-generierung-des-architektur-plans)).
* **`permissions.allow` / `.deny` / `.ask`** in `settings.json`: Tool-Pattern-Strings wie `"Bash(npm run *)"` oder `"Read(./.env*)"` erlauben granulare Freigaben, statt pauschal „Auto-Approve" zu setzen.
* **`/permissions`**: Zeigt und verwaltet die aktuell wirksamen Regeln in der Session.
* **Sandbox-Isolation:** `sandbox.enabled` (i. d. R. über Managed Settings gesetzt) kapselt Tool-Ausführung zusätzlich auf Betriebssystemebene.

### 9.2 Plugins & Marketplaces
Skills, Subagenten, Hooks und MCP-Server lassen sich zu einem **Plugin** bündeln und darüber teamweit oder öffentlich verteilen — die Alternative zum manuellen Kopieren von `.claude/`-Ordnern.

* **Struktur:** `.claude-plugin/plugin.json` (Manifest mit `name`, `description`, `version`) plus `skills/`, `agents/`, `hooks/hooks.json`, `.mcp.json` auf Plugin-Root-Ebene.
* **Lokal testen:**
  ```bash
  claude --plugin-dir ./my-plugin
  ```
* **Verteilen:** Über eine **Marketplace**-Registrierung (`/plugin marketplace add <repo>`) installieren Teammitglieder das Plugin mit `/plugin install`. Anthropic pflegt zusätzlich eine offizielle (`claude-plugins-official`) und eine kuratierte Community-Marketplace (`claude-community`).
* **Schnellstart im eigenen Skills-Ordner:** `claude plugin init my-tool` legt ein Plugin direkt unter `~/.claude/skills/` an, das ohne Marketplace automatisch lädt.

### 9.3 Headless-Modus für CI/CD & Skripting
Neben dem interaktiven Terminal lässt sich Claude Code nicht-interaktiv aus Skripten und Pipelines heraus aufrufen:
```bash
claude -p "Prüfe, ob alle öffentlichen Funktionen Doctests haben, und liste Lücken auf." --output-format json
```
* Damit lassen sich Reviews, Migrationen oder Doku-Checks in eine bestehende CI/CD-Pipeline einbetten, zusätzlich zum in [8.2](#82-cicd-pipeline-erstellung) beschriebenen generierten Workflow.
* Für GitHub-native Automatisierung steht die offizielle `claude-code-action` bereit (`/install-github-app` richtet sie im jeweiligen Repo ein).

### 9.4 Session-Management & Kontextkontrolle
* **`--resume`** / **`/resume`**: Eine unterbrochene Session fortsetzen.
* **`/rewind`**: Datei-Änderungen einer Session gezielt zurückrollen (Checkpoints).
* **`/context`**: Zeigt, was aktuell tatsächlich im Kontextfenster geladen ist (CLAUDE.md-Dateien, Subagenten, Rules) — das zentrale Debugging-Werkzeug, wenn Instruktionen scheinbar ignoriert werden.
* **`/compact`** und `autoCompactWindow`: Steuern, wann und wie der Gesprächsverlauf komprimiert wird, ohne projektweite `CLAUDE.md`-Regeln zu verlieren (diese werden nach Compaction automatisch neu geladen).
* **`/cost`**: Laufende Kostenübersicht der Session.

### 9.5 Team- & Enterprise-Rollout
* **Managed Settings:** IT-Abteilungen verteilen `managed-settings.json` sowie eine organisationsweite `CLAUDE.md` zentral (macOS: `/Library/Application Support/ClaudeCode/`, Linux/WSL: `/etc/claude-code/`, Windows: `C:\Program Files\ClaudeCode\`) — per MDM, Group Policy oder Ansible, nicht überschreibbar durch Nutzereinstellungen.
* **`claudeMdExcludes`:** In großen Monorepos lassen sich fremde, irrelevante `CLAUDE.md`-Dateien anderer Teams gezielt ausschließen.
* **IDE-Integration:** VS Code-Extension und JetBrains-Plugin spiegeln denselben Agenten inklusive `CLAUDE.md`/Skills/Hooks in die jeweilige IDE.

---

## Checkliste: Vom Setup bis zum Release mit Claude Code

| Phase | Arbeitsschritt | Befehl / Werkzeug | Status |
| :--- | :--- | :--- | :---: |
| **1. Setup** | CLI Installieren & Anmelden | `npm install -g @anthropic-ai/claude-code && claude` | [x] |
| **1. Setup** | Auto-Init ausführen | `/init` (erzeugt `CLAUDE.md`) | [x] |
| **2. Agent & Skills** | Projektregeln hinterlegen | `CLAUDE.md` anlegen (ggf. `@AGENTS.md`-Import) | [x] |
| **2. Agent & Skills** | Custom Skills definieren | `.claude/skills/<skill>/SKILL.md` | [x] |
| **2. Agent & Skills** | Subagenten definieren | `.claude/agents/<name>.md` | [x] |
| **2. Agent & Skills** | Hooks für harte Vorgaben | `hooks` in `.claude/settings.json` | [x] |
| **3. Subagenten** | Subagenten-Delegation | Prompt: *Starte Subagent für Research/Tests* | [x] |
| **4. Design** | Architektur-Plan generieren | Prompt (Plan Mode): *Erstelle `implementation_plan.md`* | [x] |
| **5. Coding** | Autonomer TDD-Loop | Prompt: *Schreibe Tests & implementiere Logik* | [x] |
| **6. Quality** | Skill & Linter Audit | Skill `rust_security_audit` & `cargo clippy` | [x] |
| **7. Doku & Git** | Rustdoc & Commit/PR | `git commit` & `gh pr create` via Claude | [x] |
| **8. Release** | Docker & CI/CD Pipeline | Multi-Stage Dockerfile & `.github/workflows/ci.yml` | [x] |
| **9. Skalierung** | Rechte & Plan Mode | `permissions.allow/deny` in `settings.json` | [x] |
| **9. Skalierung** | Skills/Agents teilen | Plugin bauen & über Marketplace verteilen | [x] |
| **9. Skalierung** | CI-Integration | `claude -p "…" --output-format json` bzw. `claude-code-action` | [x] |
| **9. Skalierung** | Team-Rollout | Managed Settings & organisationsweite `CLAUDE.md` verteilen | [x] |

---

## Verwandte Themen

* [Claude Code Praxis-Handbuch](../../künstliche-intelligenz/coding/claude-code-praxis.md) — bestehendes, thematisch überlappendes Praxis-Handbuch zu Claude Code
* [Entwickler-Curriculum: Software Engineering, Systems Programming mit Rust & Agentic AI](index.md) — übergeordnetes Curriculum
* [KI-Entwicklungsworkflow für Rust](ki-entwicklungsworkflow-rust.md) — der 9-phasige Rust-spezifische Workflow, den dieser Leitfaden mit Claude-Code-Werkzeugen unterlegt
* [Rust-Praxisprojekte mit Claude Code](rust-praxisprojekte.md) — wendet Skills, Subagenten und Hooks aus dieser Seite auf drei konkrete Projekte an
* [Evolution und Architekturen digitaler Versionskontrollsysteme](../system/evolution-digitaler-versionskontrollsysteme.md) — der Git-Workflow aus Phase 7 dieser Seite als Generation 6 der Versionskontroll-Architektur-Zeitachse
