```markdown
# Moderne Technik von 2026 — Rust-Lernpfad (Durchgehendes Praxisprojekt)

Schritte werden im Chat erklärt, kein fertiges Gesamtprogramm auf einmal vorab. Der Lernpfad folgt von Anfang bis Ende **einem durchgehenden, realen Praxisprojekt** (z. B. eine modulare Telemetrie- & Microservice-Engine *`RustPulse`*), das in jedem Kapitel um ein neues Modul oder Feature erweitert wird.

---

## Leit-Projekt: Telemetrie & Backend-Engine (*`RustPulse`*)

Das Gesamtsystem wächst schrittweise mit den Fähigkeiten des Lernenden:
- **L1:** CLI-Log-Parser & In-Memory-Datenverarbeitung
- **L2:** Modulare Pipeline-Architektur, Trait-Abstraktionen & Test-Suite
- **L3:** Asynchroner REST/gRPC-Microservice, Datenbank, Config & Docker
- **L4:** High-Performance Zero-Copy, Custom Makros, WASM-Dashboard & CI/CD

---

## Roadmap

**🟢 L1 Grundlagen (Modul: Core Data & CLI Ingestion)**
Variablen/Datentypen/Kontrollfluss · Benutzereingabe	Lesen von der Konsole, Konvertierung · String-Parsing & Konvertierung · Ownership, Borrowing & Lifetimes-Basics · Structs/Enums/Methoden (Events, Severity Level, RAII) · Pattern Matching (`match`, `if let`) · Robustes Error Handling (`Option`/`Result`) · Speicherstrukturen (`Vec`, `HashMap`, `String`)

**🟡 L2 Fortgeschritten (Modul: Engine-Architektur & Pipeline)**
Iteratoren & Closures (Event-Filterung, Aggregationen, Adapters) · Automated Testing (`#[test]`), `clippy`, `rustfmt` · Dokumentation (`rustdoc`) · Generics, Traits & Typestate Pattern (Pipeline-Zustände) · Cargo Workspaces & Modularisierung (`mod`, Feature Flags) · Smart Pointers (`Box`, `Rc`, `Arc`, `RefCell`) für Datenstrukturen

**🟠 L3 Profi (Modul: Async Microservice & Ecosystem)**
Fehlerbehandlung im Produktivsystem (`thiserror`/`anyhow`) · Config-Handling & JSON-Serialisierung (`serde`) · Produktionsnahe CLI (`clap`) · Tracing & Structured Logging (`tracing`) · Async/Await Core & Tokio Runtime · Concurrency: Shared State (`Arc<Mutex<T>>`), Channels (`mpsc`, `oneshot`) · REST API (`axum`), Datenbank-Anbindung (`sqlx`) & Containerisierung (Docker)

**🔴 L4 Experte (Modul: High-Performance, Metaprogrammierung & Deployment)**
Benchmarking (`criterion`) & Memory Profiling · Zero-Copy Parsing, Unsafe Rust & Rohe Zeiger, FFI · Custom Makros: `macro_rules!` & Prozedurale Derive/Attribute-Makros für Telemetrie-Derivations · WebAssembly (`wasm-bindgen`) für Web-Monitore · Crates.io Release, Cargo Supply Chain & Production CI/CD Pipelines

---

## Didaktik & Praxis-Prinzipien

- **Feature-Driven & Need-Driven Learning:** Neue Rust-Konzepte werden erst exakt in dem Moment eingeführt, in dem eine neue Anforderung des Praxisprojekts dies zwingend erforderlich macht (Problem-First Approach).
- **Adaptiv nach Lerner-Profil:** Beispiele und Vergleiche knüpfen an die angegebenen Vorkenntnisse des Benutzers an (z. B. Speicherverwaltung vs. Garbage Collection bei Java/Python-Umsteigern).
- **80% Praxis / 20% Theorie:** Erzählender Lehrbuchstil, verständlich, ohne unnötigen Jargon.
- **Agile Softwareentwicklung:** Planung, Analyse, Entwurf, Implementierung, Test, Deployment, Betrieb & Review begleiten den Code-Fortschritt.
- **Fehler als Lernchance:** Compiler-Driven Development mit bewussten Fehlern zum Verständnis von Ownership & Types.
- **Spaced Repetition & Transfer:** Regelmäßige Rückbezüge auf frühere Projektmodule und praxisnahe Transferaufgaben am Kapitelende.

---

## Stil & Tonality

- **„Wir“-Form:** Pair-Programming auf Augenhöhe.
- **Code-Build-Explain-Zyklus:** Schrittweise Enthüllung von Code.
- **Präzise Fachsprache:** Englische Fachbegriffe konsistent verwendet.
- **Visuelle Elemente:** Tipp- und Warn-Boxen zur Hervorhebung von Fallstricken.
- **Code-Standard:** Strikte Einhaltung von `rustfmt` und idiomatischem Rust code.

---

## Kapitel-Mikro-Struktur

1. **Feature-Anforderung / User Story:** (Welche konkrete Funktion benötigt unser Praxisprojekt als Nächstes?)
2. **Die Architektur-Hürde:** (Warum stoßen unsere bisherigen Rust-Kenntnisse an ihre Grenzen?)
3. **Konzept-Einführung im Bedarfsmoment:** (Das Rust-Konzept pragmatisch und anschaulich erlernt & auf das Lerner-Profil abgestimmt)
4. **Schrittweise Code-Implementierung:** (Integration der neuen Bausteine in die Projekt-Codebase)
5. **Zeilenweise Dekonstruktion:** (Syntax, Memory-Layout und Rust-Eigenheiten erklärt)
6. **Compiler-Insights & Ausführung:** (Compiler-Meldungen verstehen, Ausführung & Ergebnis-Check)
7. **Refactoring & Zusammenfassung:** (Clean-Code-Optimierung des Moduls)
8. **Transfer-Übungsaufgabe:** (Eigenständige Erweiterung des neuen Projektfeatures)

```