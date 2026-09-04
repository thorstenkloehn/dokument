---
description: Doku bauen (Zensical) und auf GitHub Pages veröffentlichen (npm run ver)
---

Führe den Build- und Veröffentlichungs-Workflow für die Doku-Seite aus:

1. **Prüfung**: Subagent `doc-checker` aufrufen (Build, Navigation, Links, Mermaid-Syntax). Bei Fehlern abbrechen und diese zuerst beheben.
2. **Build**: `.venv/bin/zensical build` ausführen — niemals `mkdocs build` verwenden.
3. **Veröffentlichung**: `npm run ver` ausführen (baut erneut mit Zensical und pusht `site/` in den `gh-pages`-Branch, live auf dokument.wissen-ahrensburg.de).

Schritt 3 ist eine sichtbare, kaum umkehrbare Aktion (öffentliches Deployment). Vor der Ausführung von `npm run ver` explizit die Bestätigung des Nutzers einholen, außer der Nutzer hat das Deployment bereits ausdrücklich angewiesen (z. B. durch Aufruf dieses Commands mit dem Ziel zu veröffentlichen).
