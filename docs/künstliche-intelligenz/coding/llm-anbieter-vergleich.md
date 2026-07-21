# Multi-LLM- & Sprachmodell-Anbieter im Vergleich

Der Markt für Sprachmodell-Zugriff gliedert sich grob in drei Kategorien: **Aggregatoren**, die mit einer einzigen API auf hunderte Modelle verschiedener Hersteller zugreifen lassen, **native Cloud-Anbieter**, die ihre eigenen Modelle direkt vertreiben, und **selbstgehostete Modelle**, die vollständig auf eigener Hardware laufen. Diese Seite vergleicht alle drei Wege — sortiert von billig zu teuer — und ordnet ein, wann welcher Ansatz sinnvoll ist.

!!! warning "Achtung: Preise ändern sich laufend"
    KI-Anbieter senken und ändern ihre Preise oft im Wochentakt, neue Modelle verschieben ganze Preisstufen. Die Zahlen auf dieser Seite sind eine **Momentaufnahme (Stand: Juli 2026)** und dienen der Größenordnung/Einordnung — vor einer Kaufentscheidung immer die offizielle Preisseite des jeweiligen Anbieters prüfen.

---

## Übersicht

```mermaid
graph TD
    Start{"Welcher Zugriffsweg?"} -->|"Viele Modelle testen, ein API-Key"| Aggregator["Multi-LLM-Aggregator"]
    Start -->|"Bestes Modell eines Herstellers, volle Kontrolle"| Native["Cloud- / natives Anbieter-API"]
    Start -->|"Datenschutz, Offline, Kostenkontrolle bei Dauerlast"| Local["Selbstgehostet (lokal)"]
    Aggregator --> AGoal["Ziel: Flexibilität & Preisvergleich"]
    Native --> NGoal["Ziel: State-of-the-Art & Ökosystem"]
    Local --> LGoal["Ziel: Compliance & volle Datenhoheit"]
```

!!! tip "Tipp: Kosten senken unabhängig vom Anbieter"
    Fast alle Anbieter unterstützen **Prompt Caching** (bis zu 90 % günstigere Wiederholungs-Eingaben) und eine **Batch-API** (oft 50 % Rabatt für nicht-zeitkritische Anfragen). Beides vor der Anbieterwahl mit einplanen — der Effekt auf die Gesamtkosten ist oft größer als der Preisunterschied zwischen zwei Anbietern.

### Token-Abrechnung vs. Abo — der wichtigste Unterschied vor der Anbieterwahl

Fast jeder native Anbieter bietet **zwei parallele Zugriffswege** mit komplett unterschiedlicher Kostenlogik an:

- **Token-Abrechnung (Pay-per-Token, API-Zugriff)** — Abrechnung nach tatsächlich verbrauchten Input-/Output-Tokens in USD pro 1 Mio. Tokens. Skaliert linear mit der Nutzung, planbar bei bekanntem Volumen, aber ohne Obergrenze nach oben. Zielgruppe: Entwickler, Integrationen, Agenten, Server-zu-Server-Anwendungen. **Alle Tabellen auf dieser Seite beziehen sich auf diesen Weg.**
- **Abo (Subscription, Endnutzer-Produkt)** — fester Monatspreis (z. B. ChatGPT Plus, Claude Pro/Max, Google AI Pro/Ultra, SuperGrok, Poe) für ein Nutzungskontingent oder „fair use" in der jeweiligen Chat-Oberfläche. Kosten sind planbar und gedeckelt, aber nicht per API nutzbar bzw. nur eingeschränkt (z. B. Claude Pro/Max inkl. Claude-Code-Kontingent, ChatGPT Plus inkl. begrenztem API-Guthaben). Zielgruppe: Einzelpersonen mit primär interaktiver Chat-Nutzung.

!!! warning "Achtung: Abo-Kontingent ≠ API-Zugriff"
    Ein Chat-Abo (ChatGPT Plus, Claude Pro, Gemini Advanced/AI Pro, SuperGrok) deckt in der Regel **nicht** automatisch die Entwickler-API ab — für eigene Anwendungen, Agenten oder Automatisierung wird trotzdem ein separater API-Key mit Token-Abrechnung benötigt. Umgekehrt lohnt sich für reine, hochfrequente Chat-Nutzung durch eine Einzelperson oft das Abo, da die Token-Kosten bei intensiver Nutzung schnell darüber liegen können.

---

## 1. Multi-LLM-Provider (Aggregatoren) — sortiert von billig zu teuer

Aggregatoren bündeln Modelle vieler Hersteller (OpenAI, Anthropic, Meta, Alibaba, DeepSeek, Mistral, …) hinter einer einheitlichen, meist OpenAI-kompatiblen API. Praktisch für Preisvergleiche, Modell-Routing und Fallback-Strategien, ohne für jeden Hersteller einen eigenen Vertrag/Account zu benötigen.

| Anbieter | Preisniveau (Beispiel: Llama 3.3 70B, USD/1M Tokens In/Out) | Abrechnung | Modellauswahl | Besonderheit |
|---|---|---|---|---|
| **DeepInfra** | ≈ $0,23 / $0,40 — meist der Preis-Boden am Markt | Token (Prepaid-Guthaben) | groß (Llama, Qwen, DeepSeek, Mistral, GLM, …) | Serverless-GPU-Backend, unterbietet die meisten Konkurrenten auf offenen Modellen |
| **Groq** | $0,59 / $0,79 | Token (auch kostenloses Kontingent) | mittel (Llama, Mixtral, Gemma) | eigene LPU-Hardware statt GPU → extrem niedrige Latenz/Tokens pro Sekunde |
| **Fireworks AI** | ≈ $0,90 (flat) | Token | groß | „FireAttention"-Inferenz-Optimierung, gute Fine-Tuning-Anbindung |
| **Together AI** | $0,88–1,04 / $0,88–1,04 | Token | groß | eigene GPU-Cluster mietbar, Fine-Tuning & Custom-Deployments |
| **Novita AI** | niedrig bis mittel | Token | groß, plus GPU-Cloud-Miete | Kombination aus Serverless-Inferenz und dedizierten GPU-Instanzen |
| **Replicate** | variabel, pay-per-Sekunde GPU-Zeit statt reinem Token-Preis | Nutzungsbasiert (GPU-Zeit statt Token) | sehr groß (auch Bild-/Audio-Modelle) | einfaches Deployment eigener Modelle/Container, breiter als reine LLM-APIs |
| **OpenRouter** | Pass-Through der Originalpreise ($0,01–150 pro 1M Tokens je nach Modell) + 5,5 % Gebühr beim Guthabenkauf | Token (Prepaid-Guthaben) | sehr groß (987+ Modelle, praktisch alle Hersteller) | eine API für nahezu den gesamten Markt, automatisches Routing/Fallback zwischen Anbietern, kostenlose Modelle im Kontingent verfügbar |
| **Poe (Quora)** | Abo-/Punkte-Modell statt Pay-per-Token ($20–1000+/Monat je nach Plan) | **Abo** (Punkte-Kontingent/Monat) | groß | primär Chat-Endnutzer-Produkt, API-Zugriff nachrangig |

!!! note "Hinweis: OpenRouter als Preis-Referenz"
    Da OpenRouter die Originalpreise nahezu unverändert durchreicht, eignet sich [openrouter.ai/pricing](https://openrouter.ai/pricing) gut als tagesaktuelle Vergleichsquelle über praktisch alle Hersteller hinweg — auch wenn direkt beim Hersteller bestellt wird.

---

## 2. Cloud- & native KI-Anbieter — sortiert von billig zu teuer

Native Anbieter verkaufen ausschließlich ihre eigenen Modelle, meist mit dem größten Funktionsumfang (Tool-Use, Reasoning-Modi, Vision, größte Kontextfenster) und den kürzesten Vorlaufzeiten für neue Modell-Releases.

| Anbieter | Günstigstes Modell (USD/1M In/Out) | Flaggschiff-Modell (USD/1M In/Out) | Abrechnung | Fokus |
|---|---|---|---|---|
| **Mistral AI** | Mistral Small: $0,20 / $0,60 | Mistral Large: deutlich darüber | Token (API) + Abo „Le Chat Pro" (Chat-Produkt) | europäischer Anbieter, Open-Weight-Historie, DSGVO-Standort |
| **DeepSeek** | DeepSeek V3: $0,27 / $1,10 | DeepSeek R2 (Reasoning): teurer, aber weiterhin günstig im Marktvergleich | Token (API), Chat-App kostenlos nutzbar | starkes Preis-Leistungs-Verhältnis bei Reasoning-Modellen |
| **Google (Gemini)** | Gemini 2.0 Flash: $0,10 / $0,40 | Gemini 3.1 Pro: $2,00 / $12,00 | Token (API) + Abo „Google AI Pro/Ultra" (Gemini-App) | riesige Kontextfenster, native Multimodalität (Text/Bild/Audio/Video) |
| **xAI (Grok)** | Grok 4.20: $1,25 / $2,50 | Grok 4: $3,00 / $15,00 | Token (API) + Abo „SuperGrok" (X/Grok-App) | Echtzeit-Wissen über X-Integration |
| **OpenAI** | GPT-5.6 Luna: $1,00 / $6,00 | GPT-5.6 Sol: $5,00 / $30,00 | Token (API) + Abo „ChatGPT Plus/Pro/Team" (Chat-Produkt) | größtes Ökosystem, breiteste Tool-/SDK-Unterstützung |
| **Anthropic (Claude)** | Claude Haiku 4.5: $1,00 / $5,00 | Claude Fable 5: $10,00 / $50,00 | Token (API) + Abo „Claude Pro/Max" (Chat- & Claude-Code-Kontingent) | starkes Agentic Coding, sehr lange Kontexte, Prompt Caching |
| **Cohere** | Command-Modelle im mittleren Preissegment | — | Token (API), primär Enterprise-Verträge | Enterprise-Fokus: RAG, Reranking, mehrsprachige Embeddings |
| **AWS Bedrock / Azure OpenAI / Google Vertex AI** | Reselling der o. g. Modelle plus hauseigene Modelle (z. B. Amazon Nova) | Enterprise-Tarife mit Provisioned-Throughput/Committed-Use | Token (Pay-per-Token) oder Kapazitäts-Abo (PTU/Committed-Use) | VPC-Anbindung, Compliance-Zertifizierungen, ein Vertrag für die gesamte Cloud-Rechnung |

!!! note "Hinweis: Cloud-Wrapper (Bedrock, Azure, Vertex) sind kein vierter Preis-Layer"
    AWS Bedrock, Azure OpenAI und Google Vertex AI bieten dieselben (oder sehr ähnliche) Modelle wie die nativen Anbieter an, meist zu vergleichbaren oder leicht höheren Token-Preisen — der Mehrwert liegt in Enterprise-Verträgen, Datenresidenz und der Abrechnung über die bestehende Cloud-Rechnung, nicht in einem günstigeren Preis.

---

## 3. Kostenlos nutzbare APIs (Free Tiers)

Ein Teil der Anbieter lässt sich ganz ohne Zahlung testen oder sogar dauerhaft im Rahmen eines Kontingents produktiv einsetzen — praktisch für Prototyping, Side-Projects oder um ein Modell vor einer Kaufentscheidung zu prüfen.

| Anbieter | Kostenloses Kontingent | Einschränkungen | Bemerkung |
|---|---|---|---|
| **Google Gemini (AI Studio)** | 1.500 Requests/Tag auf Gemini Flash, kein Ablaufdatum | Rate-Limits pro Minute, im Free-Tier ggf. Nutzung der Daten zur Produktverbesserung | aktuell das großzügigste dauerhaft kostenlose Kontingent am Markt |
| **Groq** | kostenloses Kontingent (Requests/Min. & Tages-Token-Limit je Modell) | niedrige Kontingente, kein Kreditkarte nötig | extrem niedrige Latenz, gut zum Testen |
| **OpenRouter** | dauerhaft kostenlose `:free`-Modellvarianten (u. a. Llama-, Mistral-, Qwen-Modelle) | 20 Req/Min, 50–1.000 Req/Tag je nach Guthabenstand des Accounts | kein kostenloser Zugriff auf Flaggschiff-Modelle, aber breite Auswahl kleinerer Modelle |
| **Cerebras** | kostenloses Kontingent | Modellauswahl schwankt spürbar (kann sich wöchentlich ändern) | Wafer-Scale-Hardware, sehr hohe Tokens/Sekunde |
| **Mistral (La Plateforme)** | kostenloses Entwickler-Tier mit Rate-Limits | eingeschränkte Requests/Tokens pro Minute | Zugriff auf Mistral Small, Codestral u. a. |
| **GitHub Models** | kostenloser Zugriff auf viele Modelle (OpenAI, Meta, Mistral, xAI, …) über den GitHub-Account | Rate-Limits an den GitHub-Plan gekoppelt, nicht für Produktion gedacht | guter Einstieg für Entwickler mit bestehendem GitHub-Account |
| **OpenAI / Anthropic** | kein dauerhaftes Free-Tier; teils einmaliges Start-Guthaben für neue Accounts | Guthaben läuft nach wenigen Tagen/Wochen ab | nur zum kurzen Ausprobieren, danach Token-Abrechnung nötig |

!!! warning "Achtung: Free Tiers ändern sich wöchentlich"
    Kostenlose Kontingente werden häufiger angepasst als bezahlte Preise — Modellauswahl, Rate-Limits und Verfügbarkeit können sich kurzfristig ändern. Vor Produktiv-Einsatz immer die aktuelle Dokumentation des Anbieters prüfen, nicht nur Marketing-Seiten.

!!! note "Hinweis: Datenschutz bei kostenlosen Kontingenten beachten"
    Bei mehreren kostenlosen Tiers (u. a. Google AI Studio) behält sich der Anbieter vor, gesendete Daten zur Produktverbesserung/zum Modelltraining zu nutzen — anders als bei bezahlten API-Tarifen, die das i. d. R. ausschließen. Für sensible oder personenbezogene Daten sind kostenlose Tiers daher meist ungeeignet — hier sind selbstgehostete Modelle die bessere Wahl (siehe Abschnitt „Einsatzgebiete" weiter unten).

---

## 4. Selbstgehostete Sprachmodelle (Lokale Ausführung)

Bei selbstgehosteten Modellen entfallen laufende Token-Kosten vollständig — bezahlt wird stattdessen die eigene Hardware (Anschaffung/Strom) oder gemietete GPU-Zeit. Details zur Einrichtung: [Lokales RAG & LLM-Serving](lokales-rag-ollama.md) (Ollama) und [vLLM High-Throughput Serving](vllm-high-throughput-serving.md).

### Werkzeuge

| Werkzeug | Zielgruppe | Besonderheit |
|---|---|---|
| **Ollama** | Einsteiger, Entwickler | ein Befehl zum Installieren, ein Befehl zum Ausführen; verwaltet Downloads & Quantisierung automatisch |
| **LM Studio** | Einsteiger mit GUI-Präferenz | grafische Oberfläche, lokaler OpenAI-kompatibler Server per Klick |
| **llama.cpp** | fortgeschrittene Nutzer, Edge-Geräte | minimaler Ressourcenverbrauch, läuft auch auf reiner CPU/Raspberry Pi |
| **vLLM** | Produktion, hoher Durchsatz | PagedAttention, OpenAI-kompatible API, für GPU-Server ausgelegt |
| **text-generation-webui / Open WebUI** | Chat-Oberfläche über beliebigem Backend | ChatGPT-ähnliche UI vor lokalem Modell-Server |

### Aktuell empfehlenswerte offene Modelle (Stand Juli 2026)

| Modell | Größe | Einsatzbereich |
|---|---|---|
| **Qwen 3.7 / 3.6** | 8B–72B (auch als 8B-Edge-Variante) | starke Allround- und Coding-Leistung, Apache-2.0-Lizenz |
| **GLM-5.1** | mehrere Größen | führt Coding-Benchmarks an, MIT-Lizenz |
| **DeepSeek V4 Pro** | groß (MoE) | starkes Reasoning, MIT-Lizenz |
| **Llama 3.3 70B** | 70B | breite Tool-Unterstützung, großes Ökosystem an Feintuning-Rezepten |
| **Gemma 3 (4B/12B)** | klein | beste Wahl für Edge-Geräte und Speicherbeschränkungen |
| **Mistral Small 4** | klein–mittel | Apache-2.0, keine Nutzungsbeschränkungen |

!!! tip "Tipp: Hardware-Faustregel"
    Als grobe Richtwerte für quantisierte GGUF-Modelle (Q4): **7–8B-Modelle** benötigen ca. 6 GB VRAM, **13–14B** ca. 10 GB, **70B-Modelle** 40 GB+ bzw. mehrere GPUs. Auf reiner CPU sollten Modelle unter 8B Parametern bleiben, um brauchbare Antwortzeiten zu erhalten.

### Einsatzgebiete für selbstgehostete Modelle

- **Datenschutz & Compliance** — Gesundheitswesen, Recht, Finanzen, Behörden: Daten verlassen niemals das eigene Netz, keine Auftragsverarbeitungsverträge mit Drittanbietern nötig.
- **Air-Gapped-/Offline-Umgebungen** — Industrieanlagen, kritische Infrastruktur, militärische oder isolierte Netze ohne Internetzugang.
- **Kostenkontrolle bei sehr hohem Volumen** — eigene Hardware amortisiert sich gegenüber Pay-per-Token-APIs, sobald die Dauerlast hoch genug ist.
- **Custom Fine-Tuning & Domain-Adaption** — eigene Trainings-/Firmendaten verlassen nie die eigene Infrastruktur.
- **Latenzkritische Edge-Anwendungen** — lokale Inferenz ohne Netzwerk-Roundtrip, z. B. auf Fahrzeugen, Robotik oder IoT-Geräten.
- **Entwicklung & Testing** — Prototyping ohne laufende API-Kosten, bevor eine Cloud-Anbindung entschieden wird.

---

## 🔗 Verwandte Themen

- [Lokales RAG & LLM-Serving](lokales-rag-ollama.md) — Ollama vs. vLLM im Detail
- [vLLM High-Throughput Serving](vllm-high-throughput-serving.md) — produktionsreifes Self-Hosting
- [Local LLM Fine-Tuning (Unsloth)](lora-finetuning-unsloth.md) — eigene Modelle anpassen
- [Skalierbare KI/ML-Infrastrukturen](../../entwicklung/infrastruktur/ki-ml-infrastrukturen.md) — Server-Infrastruktur für Self-Hosting
