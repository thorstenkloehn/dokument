<!--
Quelle: https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
Autor: Andrej Karpathy
Abgerufen: 2026-08-09
Hinweis: Deutsche Übersetzung der Rohquelle — verarbeitete/synthetisierte
Fassung siehe docs/wissen/dokumentation/llm-wiki-pattern-karpathy.md
-->

# LLM Wiki - Rohinhalt (Deutsche Übersetzung)

## LLM Wiki

Ein Muster zum Aufbau persönlicher Wissensdatenbanken mit LLMs.

Dies ist eine Ideensammlung. Sie ist dafür gedacht, in deinen eigenen LLM-Agenten kopiert zu werden (z. B. OpenAI Codex, Claude Code, OpenCode / Pi etc.). Ihr Ziel ist es, die grundlegende Idee zu vermitteln; dein Agent wird die Details in Zusammenarbeit mit dir ausarbeiten.

### Die Kernidee

Die Erfahrung der meisten Menschen mit LLMs und Dokumenten ähnelt RAG (Retrieval-Augmented Generation): Du lädst eine Sammlung von Dateien hoch, das LLM ruft zum Zeitpunkt der Anfrage relevante Abschnitte ab und generiert eine Antwort. Das funktioniert, aber das LLM entdeckt das Wissen bei jeder Frage aufs Neue von Grund auf. Es gibt keine Akkumulation. Stellt man eine subtile Frage, die die Synthese von fünf Dokumenten erfordert, muss das LLM die relevanten Fragmente jedes Mal aufs Neue suchen und zusammenfügen. Es baut sich nichts auf. NotebookLM, ChatGPT-Dateiuploads und die meisten RAG-Systeme funktionieren auf diese Weise.

Die Idee hier ist eine andere. Anstatt zum Anfragezeitpunkt nur aus Rohdokumenten abzurufen, baut und pflegt das LLM **inkrementell ein persistentes Wiki** — eine strukturierte, untereinander verlinkte Sammlung von Markdown-Dateien, die zwischen dir und den Rohquellen liegt. Wenn du eine neue Quelle hinzufügst, indiziert das LLM diese nicht nur für den späteren Abruf. Es liest sie, extrahiert die Schlüsselinformationen und integriert sie in das bestehende Wiki — aktualisiert Entitätsseiten, überarbeitet Themenzusammenfassungen, vermerkt, wo neue Daten alten Behauptungen widersprechen, und stärkt oder hinterfragt die sich entwickelnde Synthese. Das Wissen wird einmal kompiliert und dann *aktuell gehalten*, anstatt bei jeder Anfrage neu abgeleitet zu werden.

Das ist der entscheidende Unterschied: **Das Wiki ist ein persistentes, sich aufbauendes Artefakt.** Die Querverweise sind bereits vorhanden. Die Widersprüche wurden bereits markiert. Die Synthese spiegelt bereits alles wider, was du gelesen hast. Das Wiki wird mit jeder hinzugefügten Quelle und jeder gestellten Frage reichhaltiger.

Du schreibst das Wiki fast nie (oder selten) selbst — das LLM schreibt und pflegt alles davon. Du bist zuständig für die Beschaffung der Quellen, die Exploration und das Stellen der richtigen Fragen. Das LLM übernimmt die gesamte Knochenarbeit — das Zusammenfassen, Verlinken, Einordnen und die Buchhaltung, die eine Wissensdatenbank im Laufe der Zeit überhaupt erst nützlich macht. In der Praxis habe ich den LLM-Agenten auf der einen Seite und Obsidian auf der anderen Seite geöffnet. Das LLM nimmt auf Basis unseres Gesprächs Bearbeitungen vor, und ich durchstöbere die Ergebnisse in Echtzeit — folge Links, prüfe die Graph-Ansicht, lese die aktualisierten Seiten. Obsidian ist die IDE; das LLM ist der Programmierer; das Wiki ist die Codebasis.

Dies lässt sich auf viele verschiedene Kontexte anwenden. Ein paar Beispiele:

*   **Persönlich**: Verfolgen eigener Ziele, Gesundheit, Psychologie, Selbstoptimierung — Ablegen von Tagebucheinträgen, Artikeln, Podcast-Notizen und schrittweiser Aufbau eines strukturierten Bildes über sich selbst im Laufe der Zeit.
*   **Forschung**: Wochen- oder monatelanges tiefes Eintauchen in ein Thema — Lesen von Papers, Artikeln, Berichten und inkrementeller Aufbau eines umfassenden Wikis mit einer sich entwickelnden These.
*   **Ein Buch lesen**: Ablegen jedes Kapitels beim Lesen, Aufbau von Seiten für Charaktere, Themen, Handlungsstränge und deren Verbindungen. Am Ende hast du ein reichhaltiges Begleit-Wiki. Denke an Fan-Wikis wie [Tolkien Gateway](https://tolkiengateway.net/wiki/Main_Page) — Tausende miteinander verlinkte Seiten über Charaktere, Orte, Ereignisse und Sprachen, die von einer Community von Freiwilligen über Jahre hinweg aufgebaut wurden. Du könntest so etwas persönlich beim Lesen aufbauen, wobei das LLM alle Querverweise und die Wartung übernimmt.
*   **Business/Team**: Ein internes, von LLMs gepflegtes Wiki, das aus Slack-Threads, Meeting-Transkripten, Projektdokumenten und Kundenanrufen gespeist wird. Möglicherweise mit Menschen in der Schleife, die Aktualisierungen prüfen. Das Wiki bleibt aktuell, weil das LLM die Wartung übernimmt, auf die niemand im Team Lust hat.
*   **Wettbewerbsanalyse, Due Diligence, Reiseplanung, Vorlesungsskripte, Hobby-Vertiefungen** — alles, wo du Wissen im Laufe der Zeit ansammelst und es organisiert statt verstreut haben möchtest.

### Architektur

Es gibt drei Schichten:

**Rohquellen** (*Raw sources*) — deine kuratierte Sammlung von Quelldokumenten. Artikel, Papers, Bilder, Datendateien. Diese sind unveränderlich — das LLM liest daraus, modifiziert sie aber niemals. Das ist deine Quelle der Wahrheit (*Source of Truth*).

**Das Wiki** — ein Verzeichnis von LLM-generierten Markdown-Dateien. Zusammenfassungen, Entitätsseiten, Konzeptseiten, Vergleiche, eine Übersicht, eine Synthese. Das LLM besitzt diese Schicht vollständig. Es erstellt Seiten, aktualisiert sie, wenn neue Quellen eintreffen, pflegt Querverweise und hält alles konsistent. Du liest es; das LLM schreibt es.

**Das Schema** — ein Dokument (z. B. CLAUDE.md für Claude Code oder AGENTS.md für Codex), das dem LLM mitteilt, wie das Wiki strukturiert ist, welche Konventionen gelten und welchen Workflows beim Erfassen von Quellen, Beantworten von Fragen oder Warten des Wikis zu folgen ist. Dies ist die zentrale Konfigurationsdatei — sie macht das LLM zu einem disziplinierten Wiki-Warter statt zu einem generischen Chatbot. Du und das LLM entwickelt dieses Schema im Laufe der Zeit gemeinsam weiter, während ihr herausfindet, was für eure Domäne am besten funktioniert.

### Operationen

**Ingest (Erfassen).** Du legst eine neue Quelle in die Rohsammlung ab und weist das LLM an, sie zu verarbeiten. Ein Beispielablauf: Das LLM liest die Quelle, bespricht die wichtigsten Erkenntnisse mit dir, schreibt eine Zusammenfassungsseite im Wiki, aktualisiert den Index, aktualisiert relevante Entitäts- und Konzeptseiten im gesamten Wiki und fügt einen Eintrag in das Logbuch ein. Eine einzelne Quelle kann 10–15 Wiki-Seiten berühren. Ich persönlich bevorzuge es, Quellen nacheinander zu erfassen und eingebunden zu bleiben — ich lese die Zusammenfassungen, prüfe die Aktualisierungen und leite das LLM an, worauf der Schwerpunkt gelegt werden soll. Du könntest aber auch viele Quellen auf einmal mit weniger Überwachung im Batch-Verfahren erfassen. Es liegt an dir, den Workflow zu entwickeln, der zu deinem Stil passt, und ihn im Schema für zukünftige Sitzungen zu dokumentieren.

**Query (Abfragen).** Du stellst Fragen an das Wiki. Das LLM sucht nach relevanten Seiten, liest sie und synthetisiert eine Antwort mit Zitaten/Belegen. Antworten können je nach Frage unterschiedliche Formen annehmen — eine Markdown-Seite, eine Vergleichstabelle, ein Folienstapel (Marp), ein Diagramm (matplotlib), ein Canvas. Die wichtige Erkenntnis: **Gute Antworten können als neue Seiten wieder in das Wiki zurückgeführt werden.** Ein von dir angeforderter Vergleich, eine Analyse, eine von dir entdeckte Verbindung — diese sind wertvoll und sollten nicht im Chatverlauf verschwinden. Auf diese Weise bauen sich deine Nachforschungen in der Wissensdatenbank ebenso auf wie erfasste Quellen.

**Lint (Prüfen/Warten).** Bitte das LLM regelmäßig um einen Gesundheitscheck des Wikis. Suche nach: Widersprüchen zwischen Seiten, veralteten Aussagen, die durch neuere Quellen überholt wurden, verwaisten Seiten ohne eingehende Links, wichtigen Konzepten, die erwähnt werden, aber keine eigene Seite haben, fehlenden Querverweisen, Datenlücken, die durch eine Websuche gefüllt werden könnten. Das LLM ist gut darin, neue Fragen zur Untersuchung und neue Quellen zur Recherche vorzuschlagen. Dies hält das Wiki gesund, während es wächst.

### Indexierung und Protokollierung

Zwei spezielle Dateien helfen dem LLM (und dir), im wachsenden Wiki zu navigieren. Sie dienen unterschiedlichen Zwecken:

**index.md** ist inhaltsorientiert. Es ist ein Katalog von allem im Wiki — jede Seite wird mit einem Link, einer einzeiligen Zusammenfassung und optional Metadaten wie Datum oder Anzahl der Quellen aufgeführt. Organisiert nach Kategorie (Entitäten, Konzepte, Quellen etc.). Das LLM aktualisiert ihn bei jedem Ingest. Bei der Beantwortung einer Anfrage liest das LLM zuerst den Index, um relevante Seiten zu finden, und vertieft diese dann. Das funktioniert überraschend gut bei moderater Skalierung (~100 Quellen, ~Hunderte von Seiten) und vermeidet die Notwendigkeit einer Embedding-basierten RAG-Infrastruktur.

**log.md** ist chronologisch. Es ist ein Protokoll (Append-Only) dessen, was wann passiert ist — Ingests, Abfragen, Lint-Durchläufe. Ein nützlicher Tipp: Wenn jeder Eintrag mit einem konsistenten Präfix beginnt (z. B. `## [2026-04-02] ingest | Artikeltitel`), wird das Log mit einfachen Unix-Tools parsebar — `grep "^## \[" log.md | tail -5` gibt dir die letzten 5 Einträge. Das Log liefert dir eine Zeitleiste der Entwicklung des Wikis und hilft dem LLM zu verstehen, was kürzlich getan wurde.

### Optional: CLI-Tools

Ab einem gewissen Punkt möchtest du vielleicht kleine Tools bauen, die dem LLM helfen, effizienter auf dem Wiki zu arbeiten. Eine Suchmaschine über den Wiki-Seiten ist das naheliegendste — bei kleiner Skalierung reicht die Indexdatei aus, aber wenn das Wiki wächst, wünschst du dir eine echte Suche. [qmd](https://github.com/tobi/qmd) ist eine gute Option: Es ist eine lokale Suchmaschine für Markdown-Dateien mit hybrider BM25/Vektor-Suche und LLM-Reranking, all-on-device. Es verfügt sowohl über eine CLI (sodass das LLM Befehle ausführen kann) als auch über einen MCP-Server (sodass das LLM es als natives Tool nutzen kann). Du könntest auch selbst etwas Einfacheres bauen — das LLM kann dir dabei helfen, bei Bedarf ein einfaches Suchskript per Vibe-Coding zu erstellen.

### Tipps und Tricks

*   **Obsidian Web Clipper** ist eine Browser-Erweiterung, die Webartikel in Markdown umwandelt. Sehr nützlich, um Quellen schnell in deine Rohsammlung zu bekommen.
*   **Bilder lokal herunterladen.** In Obsidian Einstellungen → Dateien & Links den "Ordnerpfad für Anhänge" auf ein festes Verzeichnis setzen (z. B. `raw/assets/`). Dann unter Einstellungen → Hotkeys nach "Herunterladen" suchen, um "Anhänge für aktuelle Datei herunterladen" zu finden und auf ein Tastenkürzel zu legen (z. B. Strg+Umschalt+D). Nach dem Clipsen eines Artikels das Tastenkürzel drücken, und alle Bilder werden auf die lokale Festplatte heruntergeladen. Das ist optional, aber nützlich — es ermöglicht dem LLM, Bilder direkt anzuzeigen und zu referenzieren, anstatt sich auf URLs zu verlassen, die brechen könnten. Beachte, dass LLMs Markdown mit eingebetteten Bildern nicht nativ in einem Durchgang lesen können — der Workaround besteht darin, dass das LLM zuerst den Text liest und dann einige oder alle referenzierten Bilder separat betrachtet, um zusätzlichen Kontext zu gewinnen. Das ist etwas umständlich, funktioniert aber gut genug.
*   **Obsidians Graph-Ansicht** ist der beste Weg, die Form deines Wikis zu sehen — was womit verbunden ist, welche Seiten Knotenpunkte (*Hubs*) sind, welche verwaist sind.
*   **Marp** ist ein Markdown-basiertes Folien-Format. Obsidian hat ein Plugin dafür. Nützlich, um Präsentationen direkt aus Wiki-Inhalten zu generieren.
*   **Dataview** ist ein Obsidian-Plugin, das Abfragen über den Frontmatter von Seiten ausführt. Wenn dein LLM YAML-Frontmatter zu Wiki-Seiten hinzufügt (Tags, Daten, Anzahl der Quellen), kann Dataview dynamische Tabellen und Listen generieren.
*   Das Wiki ist einfach ein Git-Repository aus Markdown-Dateien. Du erhältst Versionsverlauf, Branching und Zusammenarbeit geschenkt.

### Warum das funktioniert

Der mühsame Teil bei der Pflege einer Wissensdatenbank ist nicht das Lesen oder Denken — es ist die Buchhaltung. Aktualisieren von Querverweisen, Aufrechterhalten aktueller Zusammenfassungen, Vermerken, wenn neue Daten alten Behauptungen widersprechen, Wahren der Konsistenz über Dutzende von Seiten hinweg. Menschen geben Wikis auf, weil der Wartungsaufwand schneller wächst als der Nutzen. LLMs langweilen sich nicht, vergessen nicht, einen Querverweis zu aktualisieren, und können 15 Dateien in einem Durchgang bearbeiten. Das Wiki bleibt gepflegt, weil die Wartungskosten nahezu null sind.

Die Aufgabe des Menschen ist es, Quellen zu kuratieren, die Analyse zu lenken, gute Fragen zu stellen und darüber nachzudenken, was das alles bedeutet. Die Aufgabe des LLM ist alles andere.

Die Idee ist vom Geist her verwandt mit Vannevar Bushs Memex (1945) — einem persönlichen, kuratierten Wissensspeicher mit assoziativen Pfaden zwischen Dokumenten. Bushs Vision war dem näher als dem, was das Web wurde: privat, aktiv kuratiert, wobei die Verbindungen zwischen Dokumenten genauso wertvoll sind wie die Dokumente selbst. Der Teil, den er nicht lösen konnte, war, wer die Wartung übernimmt. Das LLM übernimmt das.

### Hinweis

Dieses Dokument ist bewusst abstrakt gehalten. Es beschreibt die Idee, nicht eine spezifische Implementierung. Die genaue Ordnerstruktur, die Schema-Konventionen, die Seitenformate, die Werkzeuge — all das hängt von deiner Domäne, deinen Präferenzen und dem LLM deiner Wahl ab. Alles oben Erwähnte ist optional und modular — wähle, was nützlich ist, ignoriere, was es nicht ist. Zum Beispiel: Deine Quellen könnten nur aus Text bestehen, sodass du überhaupt keine Bildverarbeitung benötigst. Dein Wiki könnte klein genug sein, dass die Indexdatei alles ist, was du brauchst, keine Suchmaschine erforderlich. Folienstapel sind dir vielleicht egal und du willst nur Markdown-Seiten. Vielleicht möchtest du ein völlig anderes Set an Ausgabeformaten. Der richtige Weg, dies zu nutzen, besteht darin, es mit deinem LLM-Agenten zu teilen und zusammenzuarbeiten, um eine Version zu instanziieren, die zu deinen Bedürfnissen passt. Die einzige Aufgabe dieses Dokuments ist es, das Muster zu vermitteln. Dein LLM kann den Rest herausfinden.
