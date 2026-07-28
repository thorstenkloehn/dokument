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

datei roadmap.md Javascipt
```markdown
# 🟨 TypeScript, JavaScript (Node.js/CLI) & Rust-Anbindung — Moderne Technik von 2026

## 🟢 L1 Grundlagen (Reines JS/TS & Konsole)
- Variablen (`let`, `const`, `var` & Hoisting)
- Datentypen & Type Coercion (Implicit Conversions)
- Strict vs. Loose Equality (`===` vs `==`)
- Truthy- und Falsy-Werte
- Nullish Coalescing (`??`) & Optional Chaining (`?.`)
- Operatoren (arithmetisch, Vergleich, logisch)
- Ein-/Ausgabe (`console.log()`, Nutzereingabe via `readline`)
- Template Strings & String-Methoden
- Kontrollstrukturen (`if` / `else`, `switch`) & Schleifen (`for`, `while`, `for...of`, `for...in`)
- Arrays, Objekte, Maps und Sets

## 🟡 L2 Fortgeschritten
- Destructuring (Array & Objekt) & Rest- / Spread-Operator (`...`)
- Referenzen & Kopieren (Shallow vs. Deep Copy, `structuredClone`)
- Funktionen und Arrow Functions
- Lexikalischer Scope & Closures
- Das `this`-Keyword & Bindung (`bind()`, `call()`, `apply()`)
- Callbacks & Array-Methoden (`map`, `filter`, `reduce`)
- Fehlerbehandlung (`try` / `catch` / `finally`)
- Promises und `async` / `await`
- C-FFI / Native Addon Grundlagen (Node.js `node-ffi-napi`)

## 🟠 L3 Profi
- Module (`import` / `export`, CommonJS `require`)
- Prototypen & Prototypenkette (`prototype`, `Object.create`)
- TypeScript-Typen (Interfaces, Types, Unions, Intersections, Enums, Tuples)
- TypeScript Generics (`<T>`) & Utility Types (`Partial`, `Record`, `Pick`, `Omit`)
- Type Guards & Narrowing (`typeof`, `instanceof`, custom `is`-Predicates)
- Klassen und Objekte (OOP in TypeScript)
- Iteratoren & Generatoren (`Symbol.iterator`, `function*`, `yield`)
- Rust-Anbindung Grundlagen:
  * Node-API (N-API) Grundlagen für Rust Native Addons
  * Erstes `napi-rs` Setup für Node.js Native Modules (`.node`)

## 🔴 L4 Experte (High-Performance Rust Bindings & Node.js CLI)
- Native Node.js Addons in Rust entwickeln mit `napi-rs` (`#[napi]`)
- Automatische TypeScript `.d.ts` Typendefinitionen aus Rust-Code generieren
- Multithreading & Asynchronität (Rust Async/Tokio ↔ JS Promises via `napi::bindgen_prelude::AsyncTask`)
- Runtimes & Paketverwaltung (Node.js, Bun, Deno, `npm`, `pnpm`, `package.json`, `tsconfig.json`)
- System- & CLI-Interaktion (`fs/promises`, `path`, `process`, `child_process`, `commander`)
- Dateiformate & APIs (`JSON.parse` / `stringify`, `dotenv`, Native `fetch`, `axios`)
- Textverarbeitung & Regex (`RegExp`, `match`, `replace`)
- Testing, Logging & Code-Qualität (`winston`, `pino`, `Vitest`, `Jest`, `ESLint`, `Prettier`)
- Advanced TypeScript & Concurrency (Conditional Types, Worker Threads, Bundling via `tsup` / `esbuild`)
```
datei roadmap.md kotlin
```markdown
# 🟣 Kotlin-Lernpfad Roadmap — Konsolen-Anwendungen, Android-Apps & Rust-Anbindung (2026)

## 🟢 L1 Grundlagen (Sprache & Konsole)
- Variablen (`val`, `var`), Datentypen & Typinferenz
- String Templates & Multi-line Raw Strings (`"""`)
- Null Safety (`?`, Safe Calls `?.`, Elvis Operator `?:`, Non-Null Assertion `!!`)
- Kontrollfluss (`if` als Ausdruck, `when`-Expressions, `for`, `while`)
- Sammlungen & Collections Basics (`listOf`, `mutableListOf`, `mapOf`, `setOf`)
- Funktionen, Default- & Benannte Argumente (`fun greet(name: String = "Guest")`)
- Single-Expression Functions (`fun add(a: Int, b: Int) = a + b`)
- Konsolen-Ein-/Ausgabe (`println()`, `readln()`) & CLI-Argumente (`args: Array<String>`)

## 🟡 L2 Fortgeschritten (OOP & C-FFI / Native Basics)
- Classes & Constructors (Primary, Secondary, `init`-Blöcke)
- Properties, Custom Getter/Setter & Backing Fields (`field`)
- Data Classes & Destructuring (`val (a, b) = pair`)
- Sealed Classes & Sealed Interfaces (Zustandsmodellierung für UI & CLI)
- Extension Functions & Extension Properties
- Higher-Order Functions & Lambdas (`it`-Syntax, Trailing Lambdas)
- Scope Functions (`let`, `run`, `with`, `apply`, `also`)
- Collection Operations & Sequences (`map`, `filter`, `fold`, `asSequence()`)
- Native Deklarationen in Kotlin (`external fun`) & Bibliotheken laden (`System.loadLibrary()`)

## 🟠 L3 Profi (Coroutines, Android & Rust-JNI Anbindung)
- Coroutines Basics (`suspend`, `launch`, `async`, `Dispatchers.IO`, `Dispatchers.Main`)
- Structured Concurrency & Exception Handling (`CoroutineScope`, `SupervisorJob`)
- Reactive Streams mit Flows (`Flow`, `StateFlow`, `SharedFlow`)
- Jetpack Compose Grundlagen (Composables, State Management, `remember`, `mutableStateOf`)
- Android Architecture Components (ViewModel, UI-State, Unidirectional Data Flow)
- Rust-JNI Anbindung:
  * Rust NDK-Setup (`cargo-ndk` für Android ABIs: `arm64-v8a`, `x86_64`)
  * JNI-Basics mit Rust (`jni-rs` Crate)
  * Datentyp-Mapping (Primitives, Strings, Byte-Arrays zwischen Kotlin & Rust)
- Network & JSON APIs (Ktor Client / Retrofit, `kotlinx.serialization`)
- Dependency Injection & Testing (`Hilt` / `Koin`, `JUnit 5`, `MockK`)

## 🔴 L4 Experte (Android App Mastery, CLI Tooling & High-Performance Rust Bindings)
- Advanced Rust-Kotlin Binding mit UniFFI (`uniffi-rs` für automatische Kotlin-Bindings)
- Memory Management & Safety über FFI-Grenzen (Prävention von Double Free, Leaks)
- Panic- & Exception-Handling zwischen Rust und der Kotlin JVM
- Asynchrone FFI-Bridge (Rust Async / Tokio ↔ Kotlin Coroutines `suspend`)
- Jetpack Compose Advanced (Custom Layouts, Canvas, Animationen, Navigation Compose)
- Android System & Background Processing (WorkManager, Services, Broadcast Receiver)
- Lokale Datenhaltung (Room Database, DataStore Preferences)
- Rich CLI Tools in Kotlin mit Rust-Backends (High-Performance Native Extensions)
- Cross-Compiling & Build-Pipelines (Gradle Native Plugins, Cargo Workspaces, Production APK/Bundle Release)
```

datei roadmap.md Python
```markdown

# 🐍 Python-Lernpfad Roadmap — Moderne Technik & Rust-Anbindung (2026)

## 🟢 L1 Grundlagen
- Variablen und Datentypen
- Mutabilität vs. Immutabilität
- Operatoren (arithmetisch, Vergleich, logisch)
- Ein-/Ausgabe (`print()`, `input()`)
- Grundlegende Type Hints (`int`, `str`, `float`, `bool`)
- String-Methoden, Slicing & String-Formatierung (f-Strings, `.format()`)
- Kontrollstrukturen (`if` / `elif` / `else`) & Schleifen (`for`, `while`)
- Datenstrukturen (Listen, Tupel, Mengen, Dictionaries)

## 🟡 L2 Fortgeschritten
- Referenzen, Shallow Copy vs. Deep Copy (`copy`-Modul)
- Funktionen, Default-Argumente & Variable Argumente (`*args`, `**kwargs`)
- Geltungsbereiche & LEGB-Regel (`global`, `nonlocal`)
- Closures (innere Funktionen) & Lambda-Funktionen
- Comprehensions (List, Dict, Set)
- Fehlerbehandlung (`try` / `except` / `else` / `finally`)
- Dateiverarbeitung (Lesen/Schreiben von Dateien)
- Module und Pakete (`import`, `__init__.py`)
- C-FFI / Native Grundlagen (`ctypes`, `cffi`)

## 🟠 L3 Profi
- Kontextmanager (`with`-Statement, `__enter__` / `__exit__`)
- Objektorientierte Programmierung (Klassen, Objekte, `__init__`)
- Dunder- / Magic-Methoden (`__str__`, `__repr__`, `__len__`, `__eq__`)
- Vererbung, Polymorphie & Abstrakte Klassen (`abc.ABC`)
- Dekoratoren (`@property`, `@staticmethod`, `@classmethod`, eigene Dekoratoren)
- Iteratoren & Generatoren (`iter()`, `next()`, `yield`)
- Erweiterte Type Hints (`typing`-Modul: `Union`, `Optional`, `Callable`)
- Rust-Anbindung Grundlagen:
  * Rust C-ABI Export (`extern "C"`, `#[no_mangle]`) für `ctypes` / `cffi`
  * Erstes `PyO3`-Setup (`pyo3` Crate für Python-Extensions)

## 🔴 L4 Experte (High-Performance Rust Extensions)
- Native Python-Module in Rust entwickeln mit `PyO3` (`#[pyfunction]`, `#[pyclass]`, `#[pymodule]`)
- Build- & Packaging-Pipeline für Rust-Module (`maturin`, `setuptools-rust`, Wheel Building)
- GIL-Freigabe (Global Interpreter Lock) in Rust (`py.allow_threads`) für echte Parallelität
- Type Hinting Stubs (`.pyi`) für Rust-Module generieren (`pyo3-stub-gen` / `maturin generate-stubs`)
- Virtuelle Umgebungen & Paketverwaltung (`venv`, `uv`, `poetry`, `pip`, `pyproject.toml`)
- Dateisystem- & CLI-Interaktion (`pathlib`, `os`, `subprocess`, `argparse`, `typer`)
- Dateiformate & APIs (`json`, `csv`, `yaml`, `dotenv`, `requests`, `httpx`)
- Textverarbeitung & Regex (`re`-Modul)
- Testing, Logging & Code-Qualität (`logging`, `pytest`, `black`, `flake8`, `mypy`)
- Asynchronität & Concurrency (`asyncio`, `async` / `await`, `threading`, `multiprocessing`)

```