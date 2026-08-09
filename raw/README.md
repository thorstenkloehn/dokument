# raw/ — Rohquellen (unveränderlich)

Dieser Ordner ist die **Rohquellen-Schicht** nach dem [LLM-Wiki-Pattern (Karpathy-Muster)](../docs/wissen/dokumentation/llm-wiki-pattern-karpathy.md): unverarbeitetes Ausgangsmaterial (Artikel, PDFs, Notizen, Transkripte, Rohtext), das ein Agent liest, um daraus strukturierte Wiki-Seiten unter `docs/` zu synthetisieren.

## Konvention

- **Nur lesen, nie umschreiben**: Dateien hier werden von einem Agenten beim Ingest gelesen, aber nicht verändert. Korrekturen/Ergänzungen laufen über neue Dateien, nicht durch Editieren bestehender Quellen — so bleibt nachvollziehbar, was Rohmaterial war und was daraus gemacht wurde.
- **Kein fertiger Content**: Was hier liegt, ist *nicht* Teil der veröffentlichten Doku. Es landet nicht in `mkdocs.yml`/`nav:` und wird nicht von Zensical gebaut. Fertige, redaktionell aufbereitete Seiten gehören nach `docs/<bereich>/` (siehe `.claude/skills/zensical-docs/SKILL.md`).
- **Beliebiges Format**: Markdown, Text, PDFs, Transkripte — was als Quelle dient, nicht wie ein publiziertes Dokument.
- **Struktur frei**: Unterordner nach Thema/Datum/Quelle sind erlaubt, es gibt keine vorgeschriebene Gliederung wie unter `docs/`.

## Workflow (Ingest)

1. Neue Rohquelle wird hier abgelegt.
2. Ein Agent liest sie und ordnet die Erkenntnisse ein: neue Wiki-Seite unter `docs/<bereich>/` anlegen oder bestehende aktualisieren (inkl. Nav-Eintrag in `mkdocs.yml`, siehe `zensical-docs`-Skill).
3. Die Rohquelle selbst bleibt unverändert liegen — sie ist die Nachvollziehbarkeits-Spur, nicht das Endprodukt.

Details zum Muster (Architektur, Ingest/Query/Lint, Bezug zu diesem Repo): [LLM-Wiki-Pattern (Karpathy-Muster)](../docs/wissen/dokumentation/llm-wiki-pattern-karpathy.md).
