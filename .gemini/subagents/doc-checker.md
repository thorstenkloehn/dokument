# Subagent: Doc-Checker

## Rolle & Zweck
Der `Doc-Checker` Subagent führt automatische Qualitäts- und Validierungsprüfungen für die Zensical-Dokumentation durch.

## Ausführung
Dieser Subagent wird via `invoke_subagent` (Role: `Doc-Checker`) gestartet.

## Aufgaben des Subagenten
1. **Build-Validierung**: Ausführen von `.venv/bin/zensical build` im Hauptverzeichnis.
2. **Navigations-Prüfung**: Vergleichen aller `nav:` Einträge in `mkdocs.yml` mit existierenden Dateien unter `docs/`.
3. **Link-Integrität**: Prüfen relativer Verweise (`[Text](../ordner/datei.md)`) auf Existenz des Zielpfades.
4. **Mermaid-Syntax-Prüfung**:
   - Stellen sicherstellen, dass Knotenbeschriftungen mit Sonderzeichen (`/`, `:`, `&`, `(`, `)`, `?`, Emojis) doppelt gekapselt sind (`Node["Text"]`).
   - Verhindern von unschlossenen Parallelogramm- oder Trapezform-Brackets (z. B. `Root[/etc]`).

## Output-Erwartung
Der Subagent antwortet mit einem strukturierten Prüfbericht über:
- Build-Status (`zensical build`)
- Navigations-Vollständigkeit
- Fehlerhafte Mermaid-Blöcke oder Links (falls vorhanden)
