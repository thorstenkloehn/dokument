# Systemprogrammierung – Übersicht

Willkommen im Bereich **Systemprogrammierung**! Hier findest du umfassende Dokumentation zu niedrigstufiger Programmierung, Assembler, Compilern und der Integration von **Rust, C++ und C** auf **Linux**.



## 📌 Themenbereiche

### [Assembler (ASM)](assembler.md)
Die niedrigste Abstraktionsebene: Direkte Steuerung der CPU durch Maschinenbefehle.

- **Grundlagen**: Register, Instruktionen, Speicheradressierung
- **Syntax**: AT&T vs. Intel-Syntax
- **System Calls**: Interaktion mit dem Linux-Kernel
- **Tools**: `as`, `ld`, `objdump`, `gdb`
- **Inline-Assembler**: Integration in C/C++/Rust
- **Praktische Beispiele**: x86-64, ARM, RISC-V



### [Compiler](compiler.md)
Wie Hochsprachen (C, C++, Rust) in Maschinencode übersetzt werden.

- **Phasen**: Preprocessing → Kompilieren → Assemblieren → Linken
- **GCC vs. Clang vs. Rustc**: Vergleich der Compiler
- **Optimierungen**: `-O1`, `-O2`, `-O3`, `-Os`
- **Debug-Symbole**: `-g` und Debugging mit `gdb`
- **Cross-Compiling**: Für andere Architekturen kompilieren
- **Statische vs. Dynamische Bibliotheken**: `.a` vs. `.so`



### [C Praxis-Handbuch](c-praxis.md)
Umfassendes Handbuch zur C-Systemprogrammierung, Pointer-Mechanik, Speicherverwaltung (malloc/free), Structs, Makefiles, GDB & Valgrind.

### [Rust Praxis-Handbuch](rust-praxis.md)
Das umfassende Handbuch zu Rust-Sprachkonzepten, Ownership, Lifetimes, Tokio Async und dem Rust-Ökosystem.

### [Rust, C++ & C Integration](rust-c-cpp-integration.md)
Interoperabilität zwischen den Sprachen auf Linux.

- **C-ABI**: Die stabile Schnittstelle für Sprachübergreifenden Code
- **Rust ↔ C**: `extern "C"`, `#[no_mangle]`, `bindgen`, `cbindgen`
- **C++ ↔ C**: `extern "C"` für ABI-Kompatibilität
- **Rust ↔ C++**: Über C-Wrapper oder `cpp!`-Macro
- **Inline-Assembler**: `asm!` in Rust, `__asm__` in C/C++
- **Praktische Beispiele**: Bibliotheken teilen, Funktionen aufrufen



### [Linux Praxis-Handbuch](linux-praxis.md)
Umfassendes Handbuch zur Linux-Administration, FHS, Rechteverwaltung, Textverarbeitung (grep/awk/sed), LVM, systemd, Netzwerk & Bash-Scripting.

### [Linux-Systemprogrammierung](linux-systemprogrammierung.md)
Niedrigstufige Programmierung mit Linux-spezifischen Features.

- **System Calls**: `syscall()`, `write()`, `read()`, `open()`
- **Process Management**: `fork()`, `exec()`, `wait()`
- **File I/O**: Dateioperationen mit `open()`, `mmap()`
- **Signals**: `signal()`, `sigaction()`
- **Threads**: `pthread` in C, `std::thread` in Rust
- **Memory Management**: `malloc()`, `mmap()`, `brk()`
- **Kernel-Module**: Einführung in Kernel-Programmierung



## 🎯 Für wen ist dieser Bereich?

- **Entwickler**, die niedrigstufige Programmierung lernen möchten
- **Systemarchitekten**, die Performance-Optimierungen benötigen
- **Embedded-Entwickler**, die mit Hardware interagieren
- **Sicherheitsforscher**, die Binaries analysieren
- **Compiler-Enthusiasten**, die verstehen wollen, wie Code übersetzt wird



## 🚀 Quick Start

### 1. Erstes Assembler-Programm
```bash
# Datei: hello.s (x86-64 AT&T-Syntax)
.section .data
msg: .ascii "Hello, Linux ASM!\n"
len = . - msg

.section .text
.global _start
_start:
    mov $1, %rax          # sys_write
    mov $1, %rdi          # stdout
    mov $msg, %rsi        # buffer
    mov $len, %rdx        # length
    syscall
    
    mov $60, %rax         # sys_exit
    xor %rdi, %rdi        # status 0
    syscall
```

**Kompilieren & Ausführen:**
```bash
as --64 hello.s -o hello.o
ld hello.o -o hello
./hello
```


### 2. C-Programm disassemblieren
```bash
# Datei: test.c
echo 'int main() { return 42; }' > test.c

# Kompilieren mit ASM-Output
gcc -S test.c -o test.s

# oder direkt disassemblieren
gcc -c test.c -o test.o
objdump -d test.o
```


### 3. Rust mit C integrieren
```rust
// Datei: lib.rs
#[no_mangle]
pub extern "C" fn rust_add(a: i32, b: i32) -> i32 {
    a + b
}
```

**C-Programm, das Rust aufruft:**
```c
// Datei: call_rust.c
extern int rust_add(int, int);

int main() {
    return rust_add(5, 7); // 12
}
```

**Kompilieren:**
```bash
# Rust-Bibliothek kompilieren
cargo build --release

# C-Programm mit Rust-Bibliothek linkengcc call_rust.c -L./target/release -l<crate_name> -o program
```



## 📚 Lernpfad

| Stufe | Thema | Dauer |
|-------|-------|-------|
| **Anfänger** | Assembler-Grundlagen | 1-2 Wochen |
| **Fortgeschritten** | Compiler-Phasen & Optimierungen | 2-3 Wochen |
| **Experte** | Sprachübergreifende Integration | 1-2 Wochen |
| **Master** | Linux-Kernel-Programmierung | 4+ Wochen |



## 🔗 Verwandte Bereiche

- [Coding](../../künstliche-intelligenz/coding/index.md) – Allgemeine Programmierkonzepte
- [Tools](../../wissen/tools/index.md) – Nützliche Werkzeuge für Entwickler
- [Server](../infrastruktur/index.md) – Server-Administration und -Optimierung



## 📖 Ressourcen

### Bücher
- [Programming from the Ground Up](https://savannah.gnu.org/projects/pgubook/) – Assembler-Tutorial
- [The Rust Programming Language](https://doc.rust-lang.org/book/) – Offizielles Rust-Buch
- [Linux Kernel Development](https://www.amazon.com/Linux-Kernel-Development-Robert-Love/dp/0672329468) – Kernel-Programmierung

### Online-Kurse
- [Nand2Tetris](https://www.nand2tetris.org/) – Baue einen Computer von Grund auf
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/) – Rust-Praxisbeispiele
- [Linux Insides](https://0xax.gitbooks.io/linux-insides/content/) – Linux-Kernel-Internals

### Tools
- [Godbolt Compiler Explorer](https://godbolt.org/) – ASM-Output vergleichen
- [Rust Playground](https://play.rust-lang.org/) – Rust online testen
- [GDB Debugger](https://www.gnu.org/software/gdb/) – Debugging-Werkzeug



---

*Letzte Aktualisierung: {{ git_revision_date_localized() }}*
