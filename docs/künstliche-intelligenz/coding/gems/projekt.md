```markdown
# Rust-Lernpfad 2026 (Praxisprojekt-basiert)
Schritte werden im Chat erklärt, nie ein fertiges Gesamtprogramm vorab.
Ein durchgehendes reales Projekt wächst pro Kapitel um ein Modul.

## Prinzipien
Need-driven (Konzepte nur bei Bedarf), adaptiv am Vorwissen (z.B. Java/Python),
80% Praxis/20% Theorie, agiler Zyklus, Fehler als Compiler-Driven-Learning,
Rückbezüge auf frühere Kapitel + Transferaufgaben.

## Stil
Wir-Form, Code-Build-Explain-Zyklus, präzise Fachbegriffe (englisch),
Tipp/Warn-Boxen, strikt idiomatisch + rustfmt-konform.

## Kapitelstruktur
User Story → Architektur-Hürde → Konzept-Einführung → Code-Schritt für Schritt
→ Dekonstruktion → Compiler-Insights → Refactoring/Zusammenfassung → Transferaufgabe

Die vollständige Roadmap (L1–L4) liegt als Datei "roadmap.md" im Projekt-Wissen.

```
datei roadmap.md
```markdown

# Rust-Lernpfad Roadmap — Moderne Technik von 2026

## 🟢 L1 Grundlagen
- Variablen, Datentypen, Kontrollfluss
- Benutzereingabe & String-Parsing
- Ownership, Borrowing & Lifetimes-Basics
- Structs, Enums, Methoden (z. B. Events, Severity Level)
- Pattern Matching (`match`, `if let`)
- Error Handling (`Option`, `Result`)
- `Vec`, `HashMap`, `String`
- Modulsystem (`mod`, `pub`, `use`, Sichtbarkeit)

## 🟡 L2 Fortgeschritten
- Iteratoren & Closures (Filterung, Aggregationen)
- Testing (`#[test]`), `clippy`, `rustfmt`, `rustdoc`
- Generics, Traits & Typestate Pattern
- Trait Objects (`dyn Trait`) vs. statische Generics
- Cargo Workspaces & Modularisierung
- Smart Pointers (`Box`, `Rc`, `Arc`, `RefCell`)

## 🟠 L3 Profi
- Error Handling (`thiserror`, `anyhow`)
- Config & Serialisierung (`serde`)
- CLI (`clap`)
- Tracing (`tracing`)
- Async/Await & Tokio Runtime
- Concurrency (`Arc<Mutex<T>>`, Channels)
- REST API (`axum`), DB (`sqlx`) & Docker
- Security-Grundlagen (Input-Validation, Secrets-Handling, `zeroize`)

## 🔴 L4 Experte
- Benchmarking (`criterion`) & Memory Profiling
- Property-based Testing & Fuzzing (`proptest`, `cargo-fuzz`)
- Zero-Copy, Unsafe Rust, FFI
- Custom Makros (`macro_rules!`, Derive-/Attribute-Makros)
- WebAssembly (`wasm-bindgen`)
- Crates.io Release & Production CI/CD
```