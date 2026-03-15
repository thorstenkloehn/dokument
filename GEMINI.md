# Projekt-Kontext: Dokument Ahrensburg City

Dieses Projekt ist eine Dokumentations-Website, die mit **MkDocs** und dem **Material for MkDocs** Theme erstellt wurde. Sie dient als Wissensdatenbank für Server-Konfigurationen, CMS-Systeme und verschiedene IT-Tools.

## Projektstruktur
- `docs/`: Enthält alle Markdown-Quelldateien.
- `mkdocs.yml`: Die Hauptkonfigurationsdatei, einschließlich der Navigationsstruktur.
- `package.json`: Enthält Deployment-Skripte für GitHub Pages (`npm run ver`).

## Richtlinien für Änderungen
- **Sprache:** Die Dokumentation ist auf Deutsch verfasst. Alle neuen Inhalte oder Änderungen müssen in korrektem Deutsch erfolgen.
- **Markdown-Standard:** Verwende Standard-Markdown. Nutze Material-spezifische Features (wie Admonitions) nur, wenn sie bereits im Projekt verwendet werden.
- **Navigation:** Jede neue Seite in `docs/` muss auch in der `nav`-Sektion der `mkdocs.yml` eingetragen werden.
- **Dateibenennung:** Verwende CamelCase oder Unterstriche für Dateinamen in `docs/` (z.B. `Nginx_SSL.md` oder `Postgresql.md`).

## Deployment
- Die Seite wird über GitHub Pages gehostet. 
- Das Deployment erfolgt manuell über `npm run ver`.

## Bekannte Probleme / To-Dos
- Typos in der `mkdocs.yml` Navigation korrigieren (z.B. "Starseite", "Wiedererstellen", "Weiter Software").
