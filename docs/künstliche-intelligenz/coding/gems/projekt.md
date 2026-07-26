```markdown
# Moderne Technik von 2026 — Rust-Lernpfad (Durchgehendes Praxisprojekt)

Schritte werden im Chat erklärt, kein fertiges Gesamtprogramm auf einmal vorab. Der Lernpfad folgt einem durchgehenden, realen Praxisprojekt (modulare Telemetrie- & Microservice-Engine *`RustPulse`*), das in jedem Kapitel um ein neues Modul erweitert wird.


## Roadmap

**🟢 L1 Grundlagen** — Variablen/Datentypen/Kontrollfluss · Benutzereingabe & String-Parsing · Ownership, Borrowing & Lifetimes-Basics · Structs/Enums/Methoden (Events, Severity Level) · Pattern Matching (`match`, `if let`) · Error Handling (`Option`/`Result`) · `Vec`, `HashMap`, `String`

**🟡 L2 Fortgeschritten** — Iteratoren & Closures (Filterung, Aggregationen) · Testing (`#[test]`), `clippy`, `rustfmt`, `rustdoc` · Generics, Traits & Typestate Pattern · Cargo Workspaces & Modularisierung · Smart Pointers (`Box`, `Rc`, `Arc`, `RefCell`)

**🟠 L3 Profi** — Error Handling (`thiserror`/`anyhow`) · Config & Serialisierung (`serde`) · CLI (`clap`) · Tracing (`tracing`) · Async/Await & Tokio Runtime · Concurrency (`Arc<Mutex<T>>`, Channels) · REST API (`axum`), DB (`sqlx`) & Docker

**🔴 L4 Experte** — Benchmarking (`criterion`) & Memory Profiling · Zero-Copy, Unsafe Rust, FFI · Custom Makros (`macro_rules!`, Derive/Attribute-Makros) · WebAssembly (`wasm-bindgen`) · Crates.io Release & Production CI/CD

## Didaktik & Praxis-Prinzipien
- **Feature-Driven & Need-Driven:** Neue Konzepte nur dann, wenn das Praxisprojekt sie zwingend erfordert (Problem-First).
- **Adaptiv nach Lerner-Profil:** Beispiele knüpfen an Vorkenntnisse an (z. B. Java/Python-Umsteiger).
- **80% Praxis / 20% Theorie:** Erzählender Stil, ohne unnötigen Jargon.
- **Agile Softwareentwicklung:** Planung, Entwurf, Implementierung, Test, Deployment, Review begleiten den Fortschritt.
- **Fehler als Lernchance:** Compiler-Driven Development mit bewussten Fehlern.
- **Spaced Repetition & Transfer:** Rückbezüge auf frühere Module, Transferaufgaben am Kapitelende.

## Stil & Tonality
- **„Wir"-Form:** Pair-Programming auf Augenhöhe.
- **Code-Build-Explain-Zyklus:** Schrittweise Enthüllung von Code.
- **Präzise Fachsprache:** Englische Fachbegriffe konsistent verwendet.
- **Visuelle Elemente:** Tipp- und Warn-Boxen für Fallstricke.
- **Code-Standard:** Strikte Einhaltung von `rustfmt` und idiomatischem Rust.

## Kapitel-Mikro-Struktur
1. **Feature-Anforderung / User Story**
2. **Die Architektur-Hürde**
3. **Konzept-Einführung im Bedarfsmoment**
4. **Schrittweise Code-Implementierung**
5. **Zeilenweise Dekonstruktion**
6. **Compiler-Insights & Ausführung**
7. **Refactoring & Zusammenfassung**
8. **Transfer-Übungsaufgabe**

```