# AGENTS.md – KI-Regeln

* **Projekt**: Statische MkDocs-Dokumentation (Material Theme) in deutscher Sprache.
* **Pfade**: 
  * `docs/`: Markdown-Dateien (z. B. `Server/`, `IDE/`, `Tools/`).
  * `mkdocs.yml`: Konfiguration (Navigations-Menü bei neuen Seiten zwingend aktualisieren!).
* **Mermaid**: Nativ via `superfences` unterstützt. Immer in dieser Form schreiben:
  ```markdown
  ```mermaid
  graph TD
      A --> B
  ```
  ```
* **Befehle**:
  * Build lokal testen: `.venv/bin/mkdocs build`
  * Deployment (gh-pages): `npm run ver`
