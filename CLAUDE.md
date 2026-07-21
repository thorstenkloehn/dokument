# CLAUDE.md

Diese Datei bietet Claude Code (claude.ai/code) Orientierung für die Arbeit mit dem Code in diesem Repository.

## Projektübersicht

Dieses Repository enthält die Quelldateien einer deutschsprachigen Dokumentations-Webseite (**Wissen Ahrensburg**), veröffentlicht unter [dokument.wissen-ahrensburg.de](https://dokument.wissen-ahrensburg.de). Es handelt sich um reinen Content — Markdown-Seiten plus Site-Konfiguration — nicht um eine Anwendung; es gibt keinen Anwendungscode, keine Build-Pipeline und keine Testsuite über den reinen Docs-Build hinaus.

Die Seite wird mit **Zensical** (`>=0.0.51`) gebaut, dem Nachfolger von MkDocs + Material for MkDocs, entwickelt vom gleichen Team. Zensical liest die bestehende `mkdocs.yml` nativ.

> **Niemals `mkdocs build` / `mkdocs serve` verwenden.** Das Projekt wurde im Juli 2026 von MkDocs 1.6.1 + Material 9.7.6 auf Zensical migriert. Nur die unten stehenden `zensical`-Befehle sind korrekt.

## Befehle

```bash
# Setup (einmalig)
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
npm install

# Lokaler Entwicklungsserver mit Live-Reload — http://127.0.0.1:8000
.venv/bin/zensical serve

# Statische Seite nach site/ bauen (dient zugleich als Validierung — muss fehlerfrei durchlaufen)
.venv/bin/zensical build

# Prüft, ob .md-Dateien unter docs/ existieren, die nicht in mkdocs.yml unter nav: eingetragen sind
python3 .gemini/scripts/check_orphaned_files.py

# Deployment: baut mit Zensical und pusht anschließend site/ in den gh-pages-Branch
npm run ver
```

Ein `pre-commit`-Git-Hook (`.gemini/hooks/pre-commit`) führt bereits automatisch vor jedem Commit `.venv/bin/zensical build` aus und bricht den Commit bei einem fehlgeschlagenen Build ab.

## Neue Seite erstellen oder bearbeiten

1. Markdown-Datei unter `docs/<bereich>/` anlegen (Dateiname in kebab-case, z. B. `erste-schritte.md`).
2. Passenden Eintrag im `nav:`-Baum in `mkdocs.yml` ergänzen — Seiten, die dort nicht gelistet sind, gelten als "verwaist" (erkennbar via `check_orphaned_files.py`) und erscheinen nicht in der Seitennavigation, obwohl Zensical sie trotzdem baut.
3. Interne Links müssen **relativ** sein (z. B. `[Seite](../ordner/seite.md)`), nicht absolut.
4. Admonitions auf Deutsch mit der Material-Syntax schreiben: `!!! tip "Tipp"`, `!!! warning "Achtung"`, `!!! note "Hinweis"`.
5. Vor dem Commit `.venv/bin/zensical build` ausführen — keine Fehler erlaubt.

## Mermaid-Diagramme

Diagramme nutzen ` ```mermaid `-Fences über `pymdownx.superfences` (konfiguriert in `mkdocs.yml`). **Jede Knoten- oder Kantenbeschriftung mit Sonderzeichen muss in doppelte Anführungszeichen gesetzt werden**, sonst wirft Mermaid.js im Browser einen Parser-Fehler:

- Sonderzeichen, die Quoting erfordern: `/`, `:`, `&`, `(`, `)`, `?`, `+`, `=`, `→`, Emojis.
- Falsch: `Root[/ Root Directory]`, `API[REST API: /v1/users & /v1/posts]`, `Choice{Welches OS?}`
- Richtig: `Root["/ Root Directory"]`, `API["REST API: /v1/users & /v1/posts"]`, `Choice{"Welches OS?"}`
- Formen: Standard-Knoten `ID["Text"]`, Entscheidung `ID{"Frage?"}`, Zylinder/DB `ID[("Datenbank")]`, Stadion `ID(["Start / Ende"])`.

## Architektur / Struktur

- `docs/` — sämtlicher Content, gegliedert nach Hauptbereichen, jeweils gespiegelt unter einem `nav:`-Schlüssel in `mkdocs.yml`:
  - `künstliche-intelligenz/` — KI-Coding, LLM & Serving, Frameworks & Agenten, Content-Erstellung, Desktop-Automatisierung
  - `entwicklung/` — Webentwicklung, Server & Infrastruktur (Nginx, PostgreSQL, Docker), Systemprogrammierung, IDE
  - `kreativ/` — Design, Audio, Video
  - `wissen/` — Daten, E-Learning, Tools, Dokumentation
  - `rechtliches/` — rechtliche Seiten (Impressum etc.)
  - `docs/index.md` ist die Startseite, `docs/tags.md` steuert das `tags`-Plugin.
- `mkdocs.yml` ist die zentrale Quelle für Site-Konfiguration und Navigation: `theme` (Material-kompatible Palette/Features/Icons, `custom_dir: overrides`), `plugins` (`search`, `tags`, `git-revision-date`, `git-authors`, `minify`), `extra` (Cookie-Consent, Social Links, Feedback-Widget) und `markdown_extensions` (Superfences/Mermaid, Tabbed, Emoji, Admonition, Footnotes, TOC, Snippets etc.). Jede Änderung an Navigation oder Theme erfolgt hier — es gibt keine andere Routing-/Konfigurationsebene.
- `overrides/partials/` — Material-Theme-Partials (`copyright.html`, `footer.html`), eingebunden über `theme.custom_dir`.
- `docs/stylesheets/extra.css` — eigenes CSS, eingebunden über `extra_css` in `mkdocs.yml`.
- `site/` — generierter Build-Output (Zensical-Build-Ziel / Quelle für gh-pages-Deployment). Nicht von Hand bearbeiten; wird durch `zensical build` neu erzeugt.
- `.gemini/` — Tooling für KI-Agenten in diesem Repo (ursprünglich für eine Gemini-basierte CLI geschrieben): `hooks/pre-commit` (Git-Hook, CLI-agnostisch) und `scripts/check_orphaned_files.py` (Python, CLI-agnostisch). Die dort ebenfalls enthaltenen Skill-/Subagent-Definitionen sind Gemini-spezifisch und für Claude Code durch `.claude/skills/` und `.claude/agents/` ersetzt — siehe unten.
- `.claude/` — native Claude-Code-Tooling für dieses Repo:
  - `skills/zensical-docs/SKILL.md` — Haupt-Workflow (Vorschau, Systemprüfung, Deployment) und Seiten-Vorlage.
  - `skills/mermaid-validator/SKILL.md` — Mermaid-Quoting-Regeln (siehe auch Abschnitt "Mermaid-Diagramme" oben).
  - `agents/doc-checker.md` — Subagent für Build-/Nav-/Link-/Mermaid-Prüfung vor Commits oder Deployment.
  Bei Doku-Aufgaben in diesem Repo zuerst prüfen, ob eines dieser Skills bzw. der `doc-checker`-Subagent zutrifft, statt die `.gemini/`-Workflows direkt nachzubauen.
- `test/` — aktuell nur eine leere Platzhalterdatei; es gibt keine echte Testsuite in diesem Repository.

## Konventionen

- Sämtlicher Content wird auf Deutsch verfasst; Code, Befehle und Dateinamen bleiben auf Englisch/kebab-case.
- Dateinamen: kebab-case (`erste-schritte.md`).
- `nav:`-Einträge in `mkdocs.yml` und die Dateiablage unter `docs/` synchron halten — jede neue Seite braucht beides.
