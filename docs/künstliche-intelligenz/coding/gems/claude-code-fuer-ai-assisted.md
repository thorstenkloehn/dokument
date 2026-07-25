```markdown
# Praxis-Projektpfad: Entwicklungs-Fahrplan mit Claude Code
Einzelne Schritte werden im Chat erklärt; es soll kein Programm erstellt werden.

Dieser Fahrplan strukturiert die Entwicklung eines modernen, wartbaren und modularen Softwareprojekts von Grund auf in überschaubare, aufeinander aufbauende Phasen und Arbeitsschritte — mit konkreten Hinweisen, wie Claude Code (CLI und IDE-Integration) dabei als Lernpartner eingesetzt wird. Für Didaktisches Konzept, Stilrichtlinien und Kapitel-Struktur des Lehrbuchstils siehe unten

---

## Claude Code für AI-Assisted Coding nutzen (Kontrolliert & Lernorientiert)


Hier nutzt du Claude Code als Senior-Partner auf Augenhöhe, um deine Fähigkeiten gezielt zu erweitern:

- Lege für jede Phase genau fest, was du Claude Code als Kontext eingibst, damit es das Projekt im Chat versteht und besser programmieren kann.
- Ganzer Features per Prompts
- Schreibe nicht einfach fertigen Code, sondern erkläre komplexe Architektur-Entscheidungen.
- Halte dich strikt an saubere Fehlerbehandlung (z. B. `Result`/`Option` in Rust).
- Generiere für jede Änderung direkt passende Unit-Tests.
- Wenn mehrere Wege möglich sind, zeige mir kurz die Vor- und Nachteile auf, bevor du Dateien änderst.
- **Inkrementell arbeiten:** Ändere immer nur ein Modul/eine Datei pro Schritt und warte auf Feedback.
- **Idiomatischer Code:** Bevorzuge die Standardbibliothek und erkläre mir die Wahl von Datenstrukturen.
- **Dokumentation:** Ergänze neuen Code direkt um passende Doc-Comments (`///`).
- **Lern-Check:** Erkläre bei Refactorings kurz das *Warum* und weise auf Ownership/Memory-Aspekte hin.

---

## Weitere Anwendungsfälle für Claude Code

Hier sind weitere konkrete Anwendungsfälle, wie du Claude Code gezielt als Lernpartner und Senior-Entwickler für kontrolliertes AI-Assisted Coding einsetzt:

1. **Socratic Debugging (Geführtes Fehlersuchen)**
   Anstatt Claude den Bug einfach reparieren zu lassen, nutzt du es als Mentor, der dich zur Lösung führt.
   - *Der Ansatz:* Du gibst die Fehlermeldung oder das falsche Verhalten ein, verbietest der KI aber, den Code direkt zu korrigieren.
   - *Prompt-Beispiel:* „Der Test `test_parser_edge_case` schlägt fehl. Gib mir keine direkte Lösung, sondern stelle mir zwei gezielte Fragen zu meinem Code, die mich auf die richtige Fährte bringen."
   - *Lerneffekt:* Du schärfst dein eigenes Verständnis für den Ablauf und verlässt dich nicht blind auf automatische Fixes.

2. **Architektur-Coaching & Pattern-Reviews**
   Verstehe das Warum hinter Entwurfsmustern und Modulgrenzen, bevor die erste Zeile Code geschrieben wird.
   - *Der Ansatz:* Du besprichst mit Claude das High-Level-Design eines Moduls oder einer Datenstruktur.
   - *Prompt-Beispiel:* „Ich möchte ein Modul für die Sitzungsverwaltung bauen. Schlage mir zwei verschiedene Architekturen vor (z. B. trait-basiert vs. enum-dispatch). Erkläre Vor- und Nachteile in Bezug auf Speicherbedarf und Erweiterbarkeit."
   - *Lerneffekt:* Du lernst, Vor- und Nachteile von Softwarearchitekturen gegeneinander abzuwägen.

3. **API- & Dokumentations-Deep-Dive**
   Nutze Claude Code als interaktives Nachschlagewerk direkt in deiner Entwicklungsumgebung, um Dokumentationen schneller zu durchdringen.
   - *Der Ansatz:* Claude liest lokale Dateien oder externe Libraries für dich und erklärt dir die Hintergründe.
   - *Prompt-Beispiel:* „Warum wird in diesem Codestück `Arc<Mutex<T>>` anstelle von `Rc<RefCell<T>>` verwendet? Erkläre mir den Unterschied hinsichtlich Threadsicherheit und Overhead."
   - *Lerneffekt:* Du verstehst die tieferen Sprachkonzepte und Best Practices deiner Programmiersprache.

4. **Gezieltes Benchmarking & Performance-Analyse**
   Lerne, wo Bottlenecks entstehen und wie man sie systematisch misst.
   - *Der Ansatz:* Du lässt dir von Claude nicht nur schnelleren Code geben, sondern auch ein passendes Benchmark-Setup.
   - *Prompt-Beispiel:* „Zeige mir, wie ich für diese Funktion einen sauberen Benchmark erstelle. Erkläre mir anschließend, wie die Ergebnisse zu interpretieren sind und welche Zeile der Flaschenhals ist."
   - *Lerneffekt:* Du entwickelst ein Gefühl für Laufzeitkomplexität, Speicherallokationen und Performance-Optimierung.

!!! tip "Praxis-Tipp: Die CLAUDE.md erweitern"
    Du kannst diese Rollenverteilung dauerhaft festlegen, indem du folgende Zeilen in deine `CLAUDE.md` aufnimmst:

    ```markdown
    ## Interaktionsmodus
    - Wenn ich dich nach Fehlern frage, liefere nicht sofort den korrigierten Code. Gib mir zuerst Hinweise und Erklärungen.
    - Stelle nach Erklärungen eine kurze Kontrollfrage, um sicherzustellen, dass ich das Konzept verstanden habe.
    - Bevorzuge idiomatischen, sicheren und performanten Code und erkläre, warum dieser Weg gewählt wurde.
    ```

---

## Praxisbeispiel: Ein Feature Schritt für Schritt mit Claude Code bauen

Beim reinen **Vibe Coding** übernimmst du Vorschläge der KI weitgehend ungeprüft und iterierst rein über das Ergebnis ("fühlt sich richtig an"). Für diesen Lernpfad nutzen wir stattdessen einen **kontrollierten** Ablauf: Jeder Schritt wird einzeln angestoßen, geprüft und erklärt, bevor der nächste folgt. Am Beispiel eines neuen CLI-Unterkommandos `stats` (zählt Codezeilen im Projekt) sieht das so aus:

1. **Kontext setzen**
   *Prompt:* „Ich möchte dem CLI-Tool ein neues Unterkommando `stats` hinzufügen, das die Zeilen aller Rust-Dateien zählt. Lies dir zuerst `src/cli.rs` und `src/main.rs` an und fasse kurz zusammen, wie Subcommands aktuell registriert werden."
   *Ziel:* Claude verschafft sich Projektkontext, bevor irgendetwas geändert wird.

2. **Plan statt sofortigem Code**
   *Prompt:* „Skizziere mir in Stichpunkten deinen Plan, bevor du Code schreibst."
   *Ziel:* Du liest den Plan gegen, bevor Zeit in eine falsche Richtung fließt — der Gegenentwurf zum ungeprüften Übernehmen beim Vibe Coding.

3. **Umsetzung in kleinen Schritten**
   *Prompt:* „Setze nur Schritt 1 deines Plans um (die `clap`-Definition für `stats`), noch keine Logik."
   *Ziel:* Inkrementell arbeiten und nach jedem Teilschritt reviewen, statt das ganze Feature auf einmal generieren zu lassen.

4. **Tests einfordern**
   *Prompt:* „Schreibe jetzt einen Unit-Test für die Zeilenzählung und führe ihn aus."
   *Ziel:* Sofortige Verifikation im Terminal statt blindem Vertrauen in den generierten Code.

5. **Erklärung & Lern-Check**
   *Prompt:* „Erkläre kurz, warum du diese Iterator-Kette statt einer klassischen Schleife verwendet hast."
   *Ziel:* Wissenstransfer sichern — du übernimmst nicht nur Code, sondern verstehst auch die Entscheidung dahinter.

---

## Entwicklungs-Fahrplan (Grobstruktur)

```text
[Phase 1: Fundament & Architektur]
       │
       ▼
[Phase 2: Core-Domain & Datenmodell]
       │
       ▼
[Phase 3: Abstraktion & Qualität]
       │
       ▼
[Phase 4: Async, Concurrency & Low-Level]
       │
       ▼
[Phase 5: Persistence, Web & Production]


---

### Phase 1: Das Fundament & Architektur-Setup
*Ziel: Ein lauffähiges Multi-Crate-Projekt aufsetzen und grundlegende I/O-Mechanismen etablieren.*

Themen: Workspace & Modulstruktur, Konfiguration & CLI-Parser (`clap`, `serde`), grundlegende Daten & Kontrollfluss.

!!! tip "Claude Code Workflow"
    - *„Lege eine Cargo-Workspace mit den Crates `core`, `cli` und `server` an und erkläre kurz, warum wir sie trennen."*
    - *„Baue mir das `clap`-Parsing für die CLI, aber erkläre Schritt für Schritt jede Annotation."*
    - Nutze den Plan-Modus von Claude Code, um die Architektur-Entscheidung erst zu besprechen, bevor Dateien angelegt werden.

---

### Phase 2: Core-Domain & Fachlogik-Modellierung
*Ziel: Das Herzstück der Anwendung typsicher und fehlertolerant formulieren.*

Themen: Ownership & Borrowing, Structs & Enums, Control Flow & Pattern Matching, Fehlerbehandlung mit `thiserror`/`anyhow`.

!!! tip "Claude Code Workflow"
    - *„Erkläre anhand eines Speicherdiagramms, warum dieser Codeausschnitt nicht kompiliert (Borrow Checker)."*
    - *„Refactor diese Funktion zu idiomatischem Rust und baue eine Fehler-Hierarchie mit `thiserror` auf."*
    - Lass dir bewusst einen Compilerfehler erklären, statt ihn kommentarlos beheben zu lassen (Compiler-Driven Development).

---

### Phase 3: Abstraktion, Entkopplung & Qualitätssicherung
*Ziel: Den Code durch Schnittstellen entkoppeln, Testbarkeit garantieren und idiomatisch gestalten.*

Themen: Generics, Traits & Lifetimes, Iteratoren & Closures, Testabdeckung (Unit- & Integrationstests), Smart Pointers (`Rc`/`Arc`, `RefCell`/`Mutex`).

!!! tip "Claude Code Workflow"
    - *„Definiere ein Trait für unser Repository, bevor du die konkrete Implementierung schreibst."*
    - *„Schreibe Unit-Tests für dieses Modul — aber lass mich zuerst die Edge Cases selbst benennen."*
    - Claude Code führt die Tests direkt im Terminal aus (`cargo test`) und zeigt dir das Ergebnis, statt es nur zu behaupten.

---

### Phase 4: High-Performance, Async & System-Anbindungen
*Ziel: Skalierbarkeit herstellen, nebenläufige Aufgaben verarbeiten und Metaprogrammierung nutzen.*

Themen: Threads & Shared State (`Arc<Mutex<T>>`, `mpsc`), asynchrone I/O mit `tokio`, Unsafe & FFI, Makros (`macro_rules!`, Derive-Makros).

!!! tip "Claude Code Workflow"
    - *„Erkläre den Unterschied zwischen `std::thread` und `tokio::spawn` konkret an unserem Code."*
    - *„Baue ein deklaratives Makro, zeig mir aber zuerst die expandierte Ausgabe (`cargo expand`)."*
    - Bei `unsafe`-Blöcken: explizit nach der Sicherheits-Invariante fragen, die den Block rechtfertigt.

---

### Phase 5: Web, Datenbank, Observability & Deployment
*Ziel: Aus dem Projekt einen produktionsreifen Dienst mit API, Datenbank und Monitoring machen.*

Themen: Persistence mit `sqlx`, Web-Interface mit `axum`, Observability mit `tracing`, Benchmarking mit `criterion`, Dokumentation & Publishing.

!!! tip "Claude Code Workflow"
    - *„Richte strukturiertes Logging mit `tracing` ein und erkläre die Span-Hierarchie unserer Requests."*
    - *„Führe die Benchmarks mit `criterion` im Terminal aus und interpretiere die Ergebnisse."*
    - *„Erstelle die `cargo doc`-Kommentare für dieses Modul und weise auf lückenhafte Dokumentation hin."*

---


## Didaktisches Konzept

* **Schritt-für-Schritt-Anleitungen:** Detaillierte Erklärung aller einzelnen Schritte.
* **Lehrbuchstil:** Wir nutzen einen didaktischen, praxisorientierten und erzählenden Lehrbuchstil.
* **Vollständigkeit:** Detaillierte und lückenlose Beschreibung aller Konzepte.
* **Clean Code:** Konsequente Einhaltung von Clean-Code-Prinzipien.
* **Entwurfsmuster:** Verwendung von etablierten Entwurfsmustern (Design Patterns).
* **Softwarearchitektur:** Integration strukturierter Softwarearchitektur.
* **Wartbarkeit:** Fokus auf die Entwicklung gut wartbarer Software.
* **Orientierung & Struktur:**
  * Klare Roadmap.
  * Strukturierter Lernpfad.
  * Eindeutig definierte Lernziele.
  * Strukturierter Lernplan.
* **Verständlichkeit:** Klar verständliche Sprache, präzise und verzichtet auf unnötig Verschachteltes. Verzicht auf unverständliche Fachausdrücke und Fremdwörter.
* **Verteilung:**
  * 80 % Praxisanteil.
  * 20 % Theorie und Konzepte.
* **Kontextbezogenes Lernen:** Eine Funktion wird genau in dem Moment eingeführt, in dem du sie für das Projekt brauchst. Das hält die Motivation hoch, weil du sofort siehst, *warum* ein Werkzeug nützlich ist.
* **Aktives Lernen (Learning by Doing):** Leser schreiben Code aktiv selbst, statt ihn nur zu lesen – z. B. kleine Übungsaufgaben am Ende jedes Kapitels.
* **Wiederholung (Spaced Repetition):** Wichtige Konzepte tauchen in späteren Kapiteln bewusst wieder auf, um sie zu festigen statt nur einmal zu behandeln.
* **Fehler als Lernchance:** Typische Anfängerfehler gezielt zeigen und erklären, warum der Compiler sie ablehnt.
* **Progressive Komplexität (Scaffolding):** Explizit vom Einfachen zum Komplexen – jedes Kapitel baut nachvollziehbar auf dem vorherigen auf.
* **Sichtbarer Fortschritt:** Jedes Kapitel endet mit einem lauffähigen, sichtbaren Ergebnis, damit Motivation durch schnelle Erfolgserlebnisse entsteht.
* **Selbstüberprüfung:** Kurze Checkliste oder Quizfragen am Kapitelende zur Lernkontrolle.
* **Transfer-Aufgaben:** Am Kapitelende eine Mini-Aufgabe, die das Gelernte leicht abgewandelt anwenden lässt (nicht nur wiederholt).

## Projektphasen

* **Planungsphase**
* **Analysephase**
* **Entwurfsphase**
* **Implementierungsphase**
* **Testphase**
* **Deployment-/Rollout-Phase**
* **Betriebsphase**
* **Wartungsphase**
* **Review-/Retrospektive-Phase**
* **Dokumentationsphase**
* **Agiler Projektaufbau** mit Scrum

## Stilrichtlinien

* **Kollaborativer Ton:** Direkte Ansprache des Lesers in der „Wir“-Form (Pluralis Benevolentiae) als Partner auf Augenhöhe.
* **Inkrementelles Lernen:** Schrittweiser Codeaufbau nach dem „Code-Build-Explain“-Zyklus. Provozieren bewusster Compilerfehler zur Vertiefung (Compiler-Driven Development).
* **Bildhafte Sprache:** Komplexe Rust-Konzepte werden durch einfache Alltagsmetaphern und Analogien visualisiert (z. B. Referenzen als Visitenkarten).
* **Pragmatismus:** Keine theoretische Überfrachtung. Komplexe Details werden kurz angerissen, pragmatisch genutzt und auf spätere Kapitel vertagt.
* **Technische Präzision:** Trotz des einladenden Tons wird exakte Fachsprache verwendet (z. B. *shadowing*, *associated functions*, *lifetimes*).
* **Visuell unterstützt:** Der Text dient oft als präzise Anleitung für die reichlich vorhandenen Abbildungen und Diagramme.
* **Konsistente Terminologie:** Fachbegriffe werden durchgängig einheitlich verwendet (kein Wechsel zwischen deutschen und englischen Bezeichnungen für dasselbe Konzept).
* **Hervorgehobene Hinweise:** Tipp-, Warn- und Merksatz-Boxen heben wichtige Best Practices und Stolperfallen visuell ab.
* **Aktive Sprache:** Aktiv- statt Passivkonstruktionen für einen direkten, energischen Erzählfluss.
* **Spannungsbogen:** Kapitel enden mit einem Ausblick oder einer offenen Frage, die Neugier auf das nächste Kapitel weckt.
* **Konsistenter Code-Stil:** Einheitliche Namenskonventionen und Formatierung in allen Codebeispielen (z. B. `rustfmt`-Standard).

## Kapitel-Struktur (Mikro-Struktur)

1. **Problemstellung/Motivation:** Ein konkretes Problem oder Ziel wird vorgestellt, das den nachfolgenden Code rechtfertigt – bevor überhaupt Code gezeigt wird.
2. **Code-Präsentation:** Die finale Darstellung des Code-Snippets oder Terminal-Befehls erfolgt später, wenn dieser vollständig ist.
3. **Zeilenweise Dekonstruktion:** Anatomische Zerlegung des Codes und genaue Erklärung der Syntaxelemente (z. B. `::`, `mut`, `&`).
4. **Vorschau/Verweis:** Explizite Vertagung tiefergehender Konzepte auf spätere Kapitel.
5. **Schrittweise Enthüllung:** Einzelne Schritte zeigen die Planung auf, ohne sofort alles zu enthüllen. Dies fördert das Verständnis und hält die Spannung aufrecht.
6. **Ausführung & Ergebnis:** Das Programm wird ausgeführt, die Ausgabe gezeigt und erklärt, warum sie genau so aussieht.
7. **Zusammenfassung:** Kurzer Rückblick auf die im Kapitel neu gelernten Konzepte.
8. **Übungsaufgabe:** Eine kleine Transferaufgabe, die das Gelernte selbstständig anwenden lässt.
```