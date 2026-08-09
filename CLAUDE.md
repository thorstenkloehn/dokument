# CLAUDE.md

Reines Content-Repo (keine App, kein Build-Code) für die Doku-Seite **Wissen Ahrensburg** (dokument.wissen-ahrensburg.de), gebaut mit **Zensical** (Nachfolger von MkDocs + Material, liest `mkdocs.yml` nativ).

> **Niemals `mkdocs build` / `mkdocs serve` verwenden** — nur `.venv/bin/zensical build` / `serve`. Migration Juli 2026.

## Workflows & Befehle

Siehe `.claude/skills/zensical-docs/SKILL.md` (Vorschau/Build/Deployment, neue Seite anlegen, Seitenvorlage) und `.claude/skills/mermaid-validator/SKILL.md` (Quoting-Regeln). Vor Commits/Deployment: Subagent `doc-checker`. Für Setup/Installation: Subagent `setup-installer` (nur spawnen, wenn `requirements.txt`/`package-lock.json` neuer als installierte Abhängigkeiten sind).

## Struktur

- `docs/<bereich>/` — Content, `bereich` ∈ `künstliche-intelligenz`, `entwicklung`, `kreativ`, `wissen`, `rechtliches`. Jede Seite braucht einen gespiegelten Eintrag in `mkdocs.yml` unter `nav:`, sonst gilt sie als "verwaist".
- `raw/` — unveränderliche Rohquellen (Notizen, Transkripte, Rohtext) nach dem [LLM-Wiki-Pattern (Karpathy-Muster)](docs/wissen/dokumentation/llm-wiki-pattern-karpathy.md); wird nur gelesen, nie editiert, ist nicht Teil des Builds/der Nav. Siehe `raw/README.md`.
- `mkdocs.yml` — einzige Config-/Nav-Quelle.
- `site/` — Build-Output, nicht von Hand editieren.
- `.gemini/hooks/pre-commit`, `.gemini/scripts/check_orphaned_files.py` — CLI-agnostisch, aktiv im Einsatz (Pre-Commit-Hook). Übrige `.gemini/skills/` und `.gemini/subagents/` gehören zur parallel genutzten Antigravity/Gemini-CLI, nicht zu Claude Code — nicht löschen, nicht als Referenz für Claude-Code-Workflows nutzen.

## Konventionen

Content auf Deutsch, Dateinamen/Code/Befehle auf Englisch/kebab-case.
