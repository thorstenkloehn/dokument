# AGENTS.md – KI-Regeln & System-Konfiguration

## Projekt
- **Generator**: Zensical 0.0.51 (MkDocs-Nachfolger, liest `mkdocs.yml` nativ)
- **Site**: [dokument.wissen-ahrensburg.de](https://dokument.wissen-ahrensburg.de)
- **Sprache**: Deutsch (außer Code/Befehle)

## Befehle & Standard-Workflows

```bash
.venv/bin/pip install -r requirements.txt  # Setup
.venv/bin/zensical build                   # Build (Validierung)
.venv/bin/zensical serve                   # Lokaler Server (http://localhost:8000)
npm run ver                                # Deploy → GitHub Pages
```
❌ Niemals `mkdocs build` oder `mkdocs serve` verwenden.

### 🚀 Die 3 Haupt-Workflows

1. **Vorschau-Server starten**:
   - Befehl: `.venv/bin/zensical serve` (im Hintergrund via `run_command` ausführen).
   - Zweck: Änderungen live unter `http://localhost:8000` im Browser prüfen.

2. **Vollständige Systemprüfung (Pre-Deployment Check)**:
   - Befehle:
     1. `.venv/bin/zensical build`
     2. `python3 .gemini/scripts/check_orphaned_files.py` (prüft verwaiste `.md` Dateien)
     3. `python3 /home/thorsten/.gemini/antigravity-cli/brain/4a2625b1-74f6-4160-bea0-9025835ba466/scratch/check_mermaid.py` (prüft Mermaid-Quoting)
     4. `invoke_subagent` (Role: `Doc-Checker`) für finale Link- & Strukturprüfung.

3. **Live-Deployment**:
   - Befehl: `npm run ver` (Veröffentlicht den Stand auf GitHub Pages).
   - **Bedingung**: Nur ausführen, wenn die Systemprüfung (Punkt 2) zu 100 % fehlerfrei war!

---

## Neue Seite erstellen
1. Markdown-Datei in `docs/<bereich>/` anlegen
2. Eintrag in `mkdocs.yml` unter `nav:` ergänzen
3. Mermaid-Knotenbeschriftungen bei Sonderzeichen quoten (`["..."]`)
4. `.venv/bin/zensical build` – keine Fehler erlaubt
5. `git commit -m "docs: ..."`
6. Optional: `npm run ver` für Live-Deployment

---

## Regeln
- **Dateinamen**: kebab-case (z. B. `erste-schritte.md`)
- **Interne Links**: **relativ** (z. B. `[Seite](../ordner/seite.md)`)
- **Admonitions auf Deutsch**: `!!! tip "Tipp"`, `!!! warning "Achtung"`, `!!! note "Hinweis"`
- **Mermaid-Syntax**: via ` ```mermaid ` in Superfences.
  - ⚠️ **Knoten-Beschriftungen mit Sonderzeichen** (`/`, `:`, `&`, `(`, `)`, `?`, Emojis) **immer in doppelte Anführungszeichen setzen** (z. B. `Root["/ Root Directory"]` statt `Root[/ Root Directory]`), um Parser-Fehler in Mermaid.js zu vermeiden.

---

## 🤖 Subagents
- **`Doc-Checker`**: Definition in `.gemini/subagents/doc-checker.md`. Nutze `invoke_subagent` (Role: `Doc-Checker`), um `.venv/bin/zensical build` auszuführen, `mkdocs.yml` Navigationspfade abzugleichen, relative Verlinkungen sowie Mermaid-Quoting zu prüfen.

---

## 🛠️ Skills
- **`zensical-docs`**: Vorlagen, Markdown-Struktur, Workflow-Schritte 1–3 & Pre-Deployment Checkliste in `.gemini/skills/zensical-docs/SKILL.md`.
- **`mermaid-validator`**: Regeln & Skripte zur automatisierten Prüfung und Korrektur von Mermaid-Diagrammen in `.gemini/skills/mermaid-validator/SKILL.md`.

---

## 🪝 Hooks
- **`pre-commit` Hook**: Befindet sich unter `.gemini/hooks/pre-commit`. Führt vor jedem Git-Commit automatisch `.venv/bin/zensical build` aus, um kaputte Builds zu verhindern.

---

## Struktur `docs/`
```
künstliche-intelligenz/  coding/  content/  automatisierung/
entwicklung/             erste-schritte.md  webentwicklung/  infrastruktur/  system/  ide/
kreativ/                 design/  audio/  video/
wissen/                  daten/  e-learning/  tools/  dokumentation/
rechtliches/
```

## Stack (Juli 2026)
| Paket | Version |
|---|---|
| zensical | ≥ 0.0.51 |
| pymdown-extensions | ≥ 11.0.1 |
| gh-pages (npm) | ^6.1.1 |
