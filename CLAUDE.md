# CLAUDE.md

Reines Content-Repo (keine App/Build-Code) für **Wissen Ahrensburg** (dokument.wissen-ahrensburg.de), gebaut mit **Zensical** (MkDocs-Nachfolger, liest `mkdocs.yml` nativ).

> **Nie `mkdocs build`/`serve`** — nur `.venv/bin/zensical build`/`serve`.

## Workflows

Details in den Skills: `zensical-docs` (Vorschau/Build/Deploy, neue Seite, Vorlage), `mermaid-validator` (Quoting-Regeln). Vor Commit/Deploy: Subagent `doc-checker`. Setup: Subagent `setup-installer` (nur wenn `requirements.txt`/`package-lock.json` neuer als installiert).

## Struktur

- `docs/<bereich>/` — Content; `bereich` ∈ `künstliche-intelligenz`, `entwicklung`, `kreativ`, `wissen`, `rechtliches`. Jede Seite braucht einen `nav:`-Eintrag in `mkdocs.yml`, sonst "verwaist".
- `raw/` — unveränderliche Rohquellen ([LLM-Wiki-Pattern](docs/wissen/dokumentation/llm-wiki-pattern-karpathy.md)); nur lesen, nicht Teil des Builds. Siehe `raw/README.md`.
- `mkdocs.yml` — einzige Config-/Nav-Quelle. `site/` — Build-Output, nicht editieren.
- `.gemini/hooks/pre-commit` + `.gemini/scripts/check_orphaned_files.py` — aktiver Pre-Commit-Hook, CLI-agnostisch. Übrige `.gemini/` gehört zur Gemini-/Antigravity-CLI — nicht löschen, nicht als Claude-Code-Referenz nutzen.

## Konventionen

Content auf Deutsch, Dateinamen/Code/Befehle Englisch/kebab-case.
