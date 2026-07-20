# AGENTS.md – KI-Regeln

## Projekt
- **Generator**: Zensical 0.0.51 (MkDocs-Nachfolger, liest `mkdocs.yml` nativ)
- **Site**: [dokument.wissen-ahrensburg.de](https://dokument.wissen-ahrensburg.de)
- **Sprache**: Deutsch (außer Code/Befehle)

## Befehle
```bash
.venv/bin/pip install -r requirements.txt  # Setup
.venv/bin/zensical build                   # Build (Validierung)
.venv/bin/zensical serve                   # Lokaler Server
npm run ver                                # Deploy → GitHub Pages
```
❌ Niemals `mkdocs build` oder `mkdocs serve` verwenden.

## Neue Seite erstellen
1. Markdown-Datei in `docs/<bereich>/` anlegen
2. Eintrag in `mkdocs.yml` unter `nav:` ergänzen
3. `.venv/bin/zensical build` – keine Fehler erlaubt
4. `git commit -m "docs: ..."`
5. Optional: `npm run ver` für Live-Deployment

## Regeln
- Dateinamen: kebab-case (z. B. `erste-schritte.md`)
- Interne Links: **relativ** (z. B. `[Seite](../ordner/seite.md)`)
- Admonitions auf Deutsch: `!!! tip "Tipp"`, `!!! warning "Achtung"`
- Mermaid: via ` ```mermaid ` in Superfences

## Subagents & Skills
- **Skill `zensical-docs`**: Vorlagen & Checkliste in `.gemini/skills/zensical-docs/SKILL.md`
- **Subagent `doc-checker`**: Nutze `invoke_subagent` (Role: `Doc-Checker`), um `.venv/bin/zensical build` auszuführen und Navigations- & Relativlinks-Integrität zu prüfen.

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
