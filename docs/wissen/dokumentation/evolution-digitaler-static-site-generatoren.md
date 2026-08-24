# Evolution und Architekturen digitaler Static-Site-Generatoren

Die [Evolution und Architekturen digitaler Docs-as-Code](evolution-digitaler-docs-as-code.md) verfolgt eine spezifische Anwendung dieser Werkzeuggattung: den kollaborativen, git-basierten Workflow für **technische Dokumentation** (Versionierung, Review-Prozess, API-Dokumentation aus Code). Dieser Artikel nimmt die breitere Perspektive ein — die **Static-Site-Generatoren** selbst, als allgemeine Technik, aus Quelltexten (Markdown, Templates, Daten) vorgerenderte, serverlos ausgelieferte Webseiten zu erzeugen: persönliche Blogs, Marketing-Seiten, Portfolios und Dokumentation gleichermaßen. Beide Chronologien überschneiden sich bei einzelnen Werkzeugen (MkDocs/Zensical, Sphinx, Docusaurus erscheinen in beiden), verfolgen aber unterschiedliche Entwicklungslinien: Docs-as-Code entlang des Kollaborations- und Review-Workflows, dieser Artikel entlang der **Rendering-Architektur** (Build-Zeit-Kompilierung, Templating-Modell, Hydration-Strategie).

!!! note "Hinweis: Rendering-Architektur statt Anwendungsfall als Ordnungsprinzip"
    Wo [Docs-as-Code](evolution-digitaler-docs-as-code.md) nach dem **Anwendungsfall** (technische Doku) und Kollaborationsmodell ordnet, ordnet dieser Artikel nach **technischer Rendering-Strategie**: Wie viel JavaScript läuft im Browser, wie wird Interaktivität nachgeliefert, und wie schnell ist der Build-Prozess selbst? Diese Achse erklärt, warum z. B. Gatsby und Astro trotz ähnlichem Anwendungsbereich architektonisch grundverschieden sind.

---

## Generation 1: Blog-Compiler & frühe Templating-Skripte, 2002 – 2008

Die Gründergeneration löst ein einfaches Problem: statische HTML-Dateien aus Textdateien generieren, ohne dynamischen Server-Prozess pro Anfrage.

**Architektur:** ein einmalig laufender Kompilierungsschritt liest Quelltextdateien (meist einfache Textdateien mit Datum im Dateinamen) und erzeugt daraus statisches HTML — kein Datenbankzugriff zur Laufzeit, keine serverseitige Logik nach dem Build.

**Sprachwahl-Logik:** Perl (Blosxom) und Python (PyBlosxom) dominieren als bereits etablierte Skriptsprachen mit starker Textverarbeitung — dieselbe Logik, die in [Generation 1 der Wissenssysteme-Programmiersprachen](evolution-digitaler-wissenssystem-programmiersprachen.md#generation-1-perl-c-cgi-skriptsprachen-der-pionierzeit-1995-2001) bereits Perl für CGI-Wikis begründet.

| System | Sprache | Jahr | Besonderheit |
|---|---|---|---|
| **Blosxom** | Perl | 2002 | Datei-Datum-basiertes Blog-Compiler-Prinzip, unter 1000 Zeilen Code |
| **PyBlosxom** | Python | 2003 | Python-Port von Blosxom mit Plugin-System |
| **webgen** | Ruby | 2004 | Früher generischer (nicht blog-spezifischer) Static-Site-Ansatz |

---

## Generation 2: Ruby-Pioniere & GitHub-Pages-Integration, 2008 – 2013

**Jekyll** definiert die Kategorie „Static Site Generator" als eigenständigen Begriff neu und wird durch die native Integration in **GitHub Pages** (2008) zum De-facto-Einstiegspunkt einer ganzen Entwicklergeneration.

**Architektur:** Front-Matter-YAML-Header in Markdown-Dateien für Metadaten, Liquid-Templating für Layouts, Konvention-über-Konfiguration nach dem Vorbild von Ruby on Rails (vgl. [Generation 1a der Batteries-Included-Zeitachse](../../entwicklung/webentwicklung/evolution-digitaler-batteries-included-frameworks.md#1a-ruby-on-rails-convention-over-configuration-2004)).

**Sprachwahl-Logik:** Rubys „Convention over Configuration"-Philosophie senkt die Einstiegshürde drastisch — ein neuer Blog braucht nur wenige Zeilen Konfiguration statt eines vollständigen Build-Skripts wie in Generation 1.

| System | Jahr | Besonderheit |
|---|---|---|
| **Jekyll** | 2008 | Native GitHub-Pages-Integration macht Hosting kostenlos und Deployment trivial |
| **Middleman** | 2011 | Flexibleres Templating (Sinatra-Fundament) für Nicht-Blog-Websites |
| **Nanoc** | 2007 (2011 stabilisiert) | Pipeline-basierte Transformation statt festem Konventionsschema |

---

## Generation 3: Performance-Generatoren jenseits von Ruby, 2013 – 2017

Rubys Interpreter-Geschwindigkeit wird bei wachsenden Websites (tausende Seiten) zum spürbaren Flaschenhals — die dritte Generation löst genau dieses Problem mit kompilierten Sprachen.

**Architektur:** Single-Binary-Distribution ohne Laufzeitabhängigkeiten, hochparallelisierter Build-Prozess über mehrere CPU-Kerne.

**Sprachwahl-Logik:** **Hugo** (Go, 2013) reduziert Build-Zeiten für große Sites von Minuten auf Sekunden — Gos eingebaute Nebenläufigkeit (Goroutines) parallelisiert das Rendern tausender Seiten nativ, ohne dass Nutzer selbst nebenläufigen Code schreiben müssen.

| System | Sprache | Jahr | Besonderheit |
|---|---|---|---|
| **Hugo** | Go | 2013 | Bis heute eine der schnellsten Build-Zeiten der gesamten Kategorie |
| **Pelican** | Python | 2010 | Python-Alternative zu Jekyll für das wissenschaftliche/technische Ökosystem |
| **Metalsmith** | Node.js/JavaScript | 2014 | Radikal minimalistisch — jede Funktion (Markdown, Templating) ist ein austauschbares Plugin |

---

## Generation 4: JavaScript-Frameworks & die JAMstack-Bewegung, 2015 – 2020

Mit dem Aufstieg von React und Vue verschiebt sich die Static-Site-Generierung in dieselben Frontend-Frameworks, die zuvor nur für dynamische Single-Page-Apps standen — der Begriff **JAMstack** (JavaScript, APIs, Markup) fasst diese Bewegung.

**Architektur:** Komponenten-basiertes Templating in derselben Sprache wie interaktive Frontend-Logik, GraphQL-Datenschicht (Gatsby) zur Aggregation heterogener Content-Quellen, vollständige Client-Hydration nach dem initialen HTML-Laden.

**Sprachwahl-Logik:** JavaScript/TypeScript eliminiert den Kontextwechsel zwischen statischem Templating und interaktiven Komponenten — dieselbe Logik wie [Generation 5 der Wissenssysteme-Programmiersprachen](evolution-digitaler-wissenssystem-programmiersprachen.md#generation-5-javascripttypescript-clojure-vollstack-und-funktionale-sprachen-moderner-pkm-web-apps-ab-2012), hier auf Static-Site-Generierung übertragen.

| System | Sprache | Jahr | Besonderheit |
|---|---|---|---|
| **Gatsby** | React/Node.js | 2015 | GraphQL-Datenschicht aggregiert CMS-, API- und Dateiquellen einheitlich |
| **Next.js** (Static Export) | React/Node.js | 2016 | Hybridmodell — dieselbe Codebasis kann statisch **und** serverseitig gerendert werden |
| **VuePress** | Vue/Node.js | 2018 | Offizielles Vue-Dokumentationswerkzeug, später von VitePress abgelöst |
| **Docusaurus** | React/Node.js | 2017 | Versionierte Dokumentation mit MDX, siehe [Generation 4 der Docs-as-Code-Zeitachse](evolution-digitaler-docs-as-code.md#generation-4-komponentenbasierte-interaktive-docs-frameworks-2020-2023) |

---

## Generation 5: Islands Architecture & Partial Hydration, 2017 – 2023

Vollständige Client-Hydration (Generation 4) lädt JavaScript für Komponenten, die nie interaktiv werden — eine fünfte Generation löst dieses Overengineering-Problem gezielt.

**Architektur:** „Islands" — nur einzelne, explizit als interaktiv markierte Komponenten laden JavaScript im Browser, der Rest der Seite bleibt reines, sofort ladendes HTML. **Zero-JS-by-default** als Grundprinzip statt Ausnahme.

**Sprachwahl-Logik:** Astro bleibt bewusst framework-agnostisch (React-, Vue-, Svelte-Komponenten in derselben Seite kombinierbar) — ein architektonischer Bruch mit der Framework-Bindung aus Generation 4. Zola (Rust) verfolgt parallel dasselbe Performance-Ziel wie Hugo (Generation 3), diesmal mit Rusts Speichersicherheit statt Gos Garbage Collection.

| System | Sprache | Jahr | Besonderheit |
|---|---|---|---|
| **Eleventy (11ty)** | Node.js/JavaScript | 2017 | Zero-Config-Philosophie, keine feste Templating-Sprache vorgeschrieben |
| **Astro** | Node.js/JavaScript | 2021 | Islands Architecture als Kernprinzip, framework-agnostisch |
| **Zola** | Rust | 2018 | Single-Binary ohne Abhängigkeiten, vergleichbar mit Hugos Go-Ansatz |
| **VitePress** | Vue/Node.js (Vite) | 2021 | Vite-basierte Build-Geschwindigkeit löst VuePress als offizielles Vue-Docs-Tool ab |

---

## Generation 6: KI-native & agentische Static-Site-Generatoren, ab 2024

Die jüngste Generation integriert LLM-gestützte Content-Pipelines und agentische Build-Prozesse direkt in den Generator — parallel zu [Generation 6 der Docs-as-Code-Zeitachse](evolution-digitaler-docs-as-code.md#generation-6-agentische-docs-as-code-autonome-pflege-durch-ki-agenten-ab-ca-2025) und [Generation 6 der Rust-Wissenssysteme](evolution-digitaler-rust-wissenssysteme.md#generation-6-rust-im-kern-ki-nativer-docs-as-code-plattformen-ab-2025).

**Architektur:** Rust-Kern für Build-Performance kombiniert mit Python- oder JavaScript-Konfigurationsschicht für Zugänglichkeit — derselbe Hybrid-Ansatz, den [Zensical](evolution-digitaler-rust-wissenssysteme.md#generation-6-rust-im-kern-ki-nativer-docs-as-code-plattformen-ab-2025) für dieses Repository nutzt.

!!! tip "Bezug zu diesem Repository"
    Wissen Ahrensburg wird mit **Zensical** gebaut, dem Nachfolger von MkDocs + Material — ein direktes Beispiel für Generation 6 dieser Zeitachse. Details zur Build-Engine selbst: `CLAUDE.md` sowie [Generation 6 der Rust-Wissenssysteme-Zeitachse](evolution-digitaler-rust-wissenssysteme.md#generation-6-rust-im-kern-ki-nativer-docs-as-code-plattformen-ab-2025).

---

## Alternative Sortier- & Klassifikationskriterien für Static-Site-Generatoren

### 1. Hydration-Modell

- **Vollständige Client-Hydration** — Gatsby, Next.js SPA-Modus (Generation 4): gesamte Seite wird im Browser als React-App reaktiviert.
- **Partial Hydration / Islands** — Astro, Eleventy mit Web-Components (Generation 5): nur explizit markierte Komponenten laden JavaScript.
- **Keine Hydration** — Hugo, Zola, Jekyll (Generation 2–3): reines statisches HTML ohne Client-seitige Framework-Laufzeit.

### 2. Build-Geschwindigkeit bei großen Seitenzahlen

- **Kompiliert, hochparallel** — Hugo, Zola (Generation 3, 5): Sekunden statt Minuten bei tausenden Seiten.
- **Interpretiert, moderat parallelisiert** — Eleventy, Astro (Node.js-Event-Loop, Generation 5): gute Geschwindigkeit, aber langsamer als kompilierte Alternativen.
- **Interpretiert, wenig parallelisiert** — Jekyll, Pelican (Generation 2–3): bei sehr großen Sites spürbarer Flaschenhals.

### 3. Framework-Bindung

- **Framework-agnostisch** — Astro, Eleventy, Hugo, Zola: beliebige oder gar keine UI-Komponenten-Bibliothek.
- **Framework-gebunden** — Gatsby/Next.js (React), VitePress/VuePress (Vue), Docusaurus (React/MDX).

---

## Verwandte Themen

- [Evolution und Architekturen digitaler Docs-as-Code](evolution-digitaler-docs-as-code.md) — Schwester-Chronologie nach Anwendungsfall/Kollaborationsmodell statt Rendering-Architektur
- [Beste Static-Site- & Docs-Generatoren 2026 (Top 20)](static-site-generatoren-2026-topliste.md) — aktuelle Top-20-Topliste, die diese Chronologie in eine Momentaufnahme 2026 übersetzt
- [Evolution und Architekturen digitaler Wissenssysteme](evolution-digitaler-wissenssysteme.md) — übergeordnetes Generationenmodell, dessen „Generatoren-Arten"-Abschnitt dieser Artikel vertieft
- [Evolution und Architekturen digitaler Rust-Wissenssysteme](evolution-digitaler-rust-wissenssysteme.md) — vertiefend zu Generation 6 dieses Artikels
- [Evolution und Architekturen digitaler Programmiersprachen für Wissenssysteme](evolution-digitaler-wissenssystem-programmiersprachen.md) — Sprachökosystem-Perspektive, die sich mit Generation 1–5 dieses Artikels überschneidet
- [Evolution und Architekturen digitaler Batteries-Included-Web-Frameworks](../../entwicklung/webentwicklung/evolution-digitaler-batteries-included-frameworks.md) — Rubys „Convention over Configuration"-Prinzip aus Generation 2 dieses Artikels, dort sprachübergreifend vertieft
- [Evolution und Architekturen digitaler SPA-Frameworks](../../entwicklung/webentwicklung/evolution-digitaler-spa-frameworks.md) — React/Vue-Grundlagen hinter Generation 4–5 dieses Artikels
