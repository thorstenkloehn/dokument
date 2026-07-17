# Rust, C++ & C Integration auf Linux

Die **Interoperabilität** zwischen **Rust, C und C++** ist ein mächtiges Werkzeug für Systemprogrammierung auf Linux. Diese Dokumentation zeigt, wie du Code zwischen den Sprachen teilen, **C-ABI** nutzen und **Inline-Assembler** in alle drei Sprachen einbinden kannst.



## 📌 Warum Sprachintegration?

| Szenario | Nutzen |
|----------|--------|
| **Bestehende Bibliotheken nutzen** | C/C++-Bibliotheken (z. B. OpenSSL, libcurl) in Rust verwenden |
| **Performance-kritische Teile** | Zeitkritische Code-Teile in C/Assembler schreiben |
| **Legacy-Code** | Altes C/C++-Code in moderne Rust-Projekte integrieren |
| **Hardware-Zugriff** | Direkter Hardware-Zugriff via C/Assembler |
| **Kernel-Module** | Linux-Kernel-Module (C) mit Rust-Komponenten kombinieren |
| **Embedded Systems** | Plattformspezifischen Code in C, Logik in Rust |



---



## 🔌 Grundlagen: C-ABI (Application Binary Interface)



### Was ist die C-ABI?

Die **C-ABI** (Application Binary Interface) definiert:
- Wie **Funktionen aufgerufen** werden (Calling Convention)
- Wie **Argumente übergeben** werden (Register/Stack)
- Wie **Rückgabewerte** zurückgegeben werden
- Wie **Datenstrukturen** im Speicher layoutet sind

**Wichtig**: **C++ hat keine stabile ABI** (aufgrund von Name Mangling, Exceptions, etc.). Für Interoperabilität muss C++-Code als `extern "C"` exponiert werden.



### Calling Convention (x86-64 Linux – System V ABI)

| Argument | Register | Stack |
|----------|----------|-------|
| 1. Argument | `rdi` | - |
| 2. Argument | `rsi` | - |
| 3. Argument | `rdx` | - |
| 4. Argument | `rcx` | - |
| 5. Argument | `r8` | - |
| 6. Argument | `r9` | - |
| 7.+ Argument | - | Auf Stack (von rechts nach links) |
| Rückgabewert | `rax` (64 Bit), `rax:rdx` (128 Bit) | - |
| Floating Point | `xmm0`–`xmm7` | - |



### Name Mangling (C++ Problem)

C++ Dekoriert Funktionsnamen für Overloading:

**C++-Code:**
```cpp
// test.cpp
void foo(int) {}
void foo(double) {}
```

**Symbol-Namen nach dem Kompilieren:**
```bash
nm test.o | grep foo
# _Z3fooIiEvT_  (foo(int))
# _Z3fooIdEvT_  (foo(double))
```

**Lösung:** `extern "C"` deaktiviert Name Mangling:

```cpp
// test.cpp
extern "C" {
    void foo(int x) {
        // Wird als _foo (nicht dekoriert) exportiert
    }
}
```



---



## 🦀 Rust ↔ C Integration



### 1. Rust ruft C-Funktionen auf



#### Schnelleinstieg

**C-Header (`libmath.h`):**
```c
// libmath.h
#ifndef LIBMATH_H
#define LIBMATH_H

#ifdef __cplusplus
extern "C" {
#endif

int add(int a, int b);

#ifdef __cplusplus
}
#endif

#endif
```

**C-Implementation (`libmath.c`):**
```c
// libmath.c
#include "libmath.h"

int add(int a, int b) {
    return a + b;
}
```

**Rust-Code (`main.rs`):**
```rust
// main.rs
// Deklaration der externen C-Funktion
extern "C" {
    fn add(a: i32, b: i32) -> i32;
}

fn main() {
    // Aufruf der C-Funktion (unsafe, da der Compiler nicht prüfen kann)
    let result = unsafe { add(5, 7) };
    println!("5 + 7 = {}", result); // 12
}
```



#### Kompilieren und Linken

**Manuell:**
```bash
# 1. C-Bibliothek kompilieren
gcc -c libmath.c -o libmath.o

# 2. Rust-Programm kompilieren
rustc main.rs -o main

# 3. Manuell linken (Rust sucht automatisch nach libmath)
# Oder explizit:
rustc main.rs -L. -lmath -o main
```

**Mit `build.rs` (empfohlen für Cargo):**

**`Cargo.toml`:**
```toml
[package]
name = "rust-c-integration"
version = "0.1.0"
edition = "2021"

[build-dependencies]
cc = "1.0"  # Für C-Compiler-Integration
```

**`build.rs`:**
```rust
// build.rs
fn main() {
    // Kompiliere libmath.c zu libmath.a
    cc::Build::new()
        .file("src/libmath.c")
        .compile("libmath.a");
    
    // Füge den Linker-Pfad hinzu
    println!("cargo:rustc-link-search=native=target");
    println!("cargo:rustc-link-lib=static=math");
}
```

**Verzeichnisstruktur:**
```
project/
├── Cargo.toml
├── build.rs
├── src/
│   ├── main.rs
│   └── libmath.c
└── target/
```

**Kompilieren:**
```bash
cargo build
cargo run
```



### 2. C ruft Rust-Funktionen auf



#### Schnelleinstieg

**Rust-Bibliothek (`lib.rs`):**
```rust
// lib.rs
// Deaktiviere Name Mangling für Rust
#[no_mangle]
pub extern "C" fn rust_add(a: i32, b: i32) -> i32 {
    a + b
}

// Optional: C-Header generieren (für C-Programme)
#[no_mangle]
pub extern "C" fn rust_sub(a: i32, b: i32) -> i32 {
    a - b
}
```

**`Cargo.toml` (als Bibliothek):**
```toml
[package]
name = "rust_math"
version = "0.1.0"
edition = "2021"

[lib]
name = "rust_math"
crate-type = ["cdylib"]  # Dynamische Bibliothek
# crate-type = ["staticlib"]  # Statische Bibliothek
```

**Kompilieren:**
```bash
# Für dynamische Bibliothek
cargo build --release

# Für statische Bibliothek
cargo rustc --release --crate-type staticlib
```



**C-Programm (`call_rust.c`):**
```c
// call_rust.c
// Deklaration der Rust-Funktionen
extern int rust_add(int a, int b);
extern int rust_sub(int a, int b);

int main() {
    int result = rust_add(10, 5);
    printf("10 + 5 = %d\n", result); // 15
    return 0;
}
```

**Kompilieren & Linken:**
```bash
# 1. Rust-Bibliothek kompilieren
cargo build --release

# 2. C-Programm mit Rust-Bibliothek linken
# Für dynamische Bibliothek:
gcc call_rust.c -L./target/release -lrust_math -o call_rust

# Für statische Bibliothek:
gcc call_rust.c -L./target/release -l:librust_math.a -o call_rust

# Ausführen
export LD_LIBRARY_PATH=./target/release:$LD_LIBRARY_PATH
./call_rust
```



### 3. Bindgen: Automatische Rust-Bindings aus C-Headern



[**bindgen**](https://github.com/rust-lang/rust-bindgen) generiert **Rust-Bindings** aus C-Headern.

**Installation:**
```bash
cargo install bindgen
```



**Beispiel:**

**C-Header (`math.h`):**
```c
// math.h
#ifndef MATH_H
#define MATH_H

int add(int a, int b);
double square(double x);

#endif
```

**C-Implementation (`math.c`):**
```c
// math.c
#include "math.h"

int add(int a, int b) { return a + b; }
double square(double x) { return x * x; }
```



**`build.rs` mit bindgen:**
```rust
// build.rs
extern crate bindgen;

use std::path::PathBuf;

fn main() {
    // Generiere Rust-Bindings aus math.h
    let bindings = bindgen::Builder::default()
        .header("math.h")
        .parse_callbacks(Box::new(bindgen::CargoCallbacks))
        .generate()
        .expect("Unable to generate bindings");
    
    // Speichere Bindings in src/bindings.rs
    let out_path = PathBuf::from(std::env::var("OUT_DIR").unwrap());
    bindings
        .write_to_file(out_path.join("bindings.rs"))
        .expect("Couldn't write bindings!");
    
    // Kompiliere die C-Bibliothek
    cc::Build::new()
        .file("math.c")
        .compile("libmath.a");
    
    // Linker-Optionen
    println!("cargo:rustc-link-search=native=target");
    println!("cargo:rustc-link-lib=static=math");
}
```



**Rust-Code (`main.rs`):**
```rust
// main.rs
// Binde die generierten Bindings ein
include!(concat!(env!("OUT_DIR"), "/bindings.rs"));

fn main() {
    // bindgen generiert sichere Wrapper-Funktionen
    let result = unsafe { add(5, 7) };
    println!("5 + 7 = {}", result); // 12
    
    let square = unsafe { square_(2.5) };  // Achtung: bindgen fügt _ hinzu bei Konflikten
    println!("2.5^2 = {}", square);
}
```



### 4. Cbindgen: C-Header aus Rust generieren



[**cbindgen**](https://github.com/eqrion/cbindgen) generiert **C-Header** aus Rust-Code für die Verwendung in C/C++.

**Installation:**
```bash
cargo install cbindgen
```



**Beispiel:**

**Rust-Code (`lib.rs`):**
```rust
// lib.rs
#[no_mangle]
pub extern "C" fn rust_multiply(a: i32, b: i32) -> i32 {
    a * b
}

#[no_mangle]
pub extern "C" fn rust_greeting(name: *const c_char) -> *const c_char {
    unsafe {
        let name_str = CStr::from_ptr(name);
        let greeting = format!("Hello, {}!", name_str.to_string_lossy());
        CString::new(greeting).unwrap().into_raw()
    }
}
```

**`build.rs` mit cbindgen:**
```rust
// build.rs
extern crate cbindgen;

use std::path::PathBuf;

fn main() {
    // Generiere C-Header
    let crate_dir = PathBuf::from(std::env::var("CARGO_MANIFEST_DIR").unwrap());
    cbindgen::Builder::new()
        .with_crate(crate_dir)
        .generate()
        .expect("Unable to generate bindings")
        .write_to_file(crate_dir.join("target/rust_math.h"));
    
    println!("cargo:rustc-link-search=native=target");
    println!("cargo:rustc-link-lib=static=rust_math");
}
```



**Generierter Header (`rust_math.h`):**
```c
// rust_math.h
#ifndef RUST_MATH_H
#define RUST_MATH_H

#include <stdint.h>
#include <stdlib.h>

int32_t rust_multiply(int32_t a, int32_t b);

char* rust_greeting(const char* name);

#endif
```



---



## 📌 Rust ↔ C++ Integration



### Grundlagen

Da **C++ keine stabile ABI** hat, gibt es zwei Ansätze:

1. **C-Wrapper**: C++-Funktionen in `extern "C"` exponieren
2. **C++-ABI-Tools**: Spezielle Tools wie `cpp!`-Macro (experimentell)



### 1. C-Wrapper für C++



**C++-Header (`math.hpp`):**
```cpp
// math.hpp
#ifndef MATH_HPP
#define MATH_HPP

// C++-Funktion
int cpp_add(int a, int b);

// C-Wrapper
#ifdef __cplusplus
extern "C" {
#endif

int c_add(int a, int b);

#ifdef __cplusplus
}
#endif

#endif
```



**C++-Implementation (`math.cpp`):**
```cpp
// math.cpp
#include "math.hpp"

// C++-Funktion
int cpp_add(int a, int b) {
    return a + b;
}

// C-Wrapper
int c_add(int a, int b) {
    return cpp_add(a, b);
}
```



**Rust-Code (`main.rs`):**
```rust
// main.rs
extern "C" {
    fn c_add(a: i32, b: i32) -> i32;
}

fn main() {
    let result = unsafe { c_add(10, 20) };
    println!("10 + 20 = {}", result); // 30
}
```



**Kompilieren:**
```bash
# 1. C++-Code kompilieren
g++ -c math.cpp -o math.o

# 2. Rust-Code kompilieren
rustc main.rs -o main

# 3. Linken (manuell)
g++ main.o math.o -o main
# oder mit Rust:
rustc main.rs -L. -l:math.o -o main
```



### 2. Rust ruft C++-Klassen auf (erweitert)



#### Problem: C++-Klassen haben keine C-ABI

**Lösung:** Factory-Funktionen und Wrapper erstellen.



**C++-Code (`myclass.hpp`):**
```cpp
// myclass.hpp
class MyClass {
public:
    MyClass(int value);
    int get_value() const;
    void set_value(int value);
    int compute(int x);

private:
    int m_value;
};

// C-Wrapper
#ifdef __cplusplus
extern "C" {
#endif

// Opaque Pointer (versteckt die Klasse vor C)
typedef void* MyClassHandle;

// Factory-Funktionen
MyClassHandle MyClass_create(int value);
void MyClass_destroy(MyClassHandle handle);
int MyClass_get_value(MyClassHandle handle);
void MyClass_set_value(MyClassHandle handle, int value);
int MyClass_compute(MyClassHandle handle, int x);

#ifdef __cplusplus
}
#endif
```



**C++-Implementation (`myclass.cpp`):**
```cpp
// myclass.cpp
#include "myclass.hpp"

// C++-Klasse
MyClass::MyClass(int value) : m_value(value) {}
int MyClass::get_value() const { return m_value; }
void MyClass::set_value(int value) { m_value = value; }
int MyClass::compute(int x) { return m_value * x; }

// C-Wrapper-Implementation
MyClassHandle MyClass_create(int value) {
    return new MyClass(value);
}

void MyClass_destroy(MyClassHandle handle) {
    delete static_cast<MyClass*>(handle);
}

int MyClass_get_value(MyClassHandle handle) {
    return static_cast<MyClass*>(handle)->get_value();
}

void MyClass_set_value(MyClassHandle handle, int value) {
    static_cast<MyClass*>(handle)->set_value(value);
}

int MyClass_compute(MyClassHandle handle, int x) {
    return static_cast<MyClass*>(handle)->compute(x);
}
```



**Rust-Code (`main.rs`):**
```rust
// main.rs
type MyClassHandle = *mut std::ffi::c_void;

extern "C" {
    fn MyClass_create(value: i32) -> MyClassHandle;
    fn MyClass_destroy(handle: MyClassHandle);
    fn MyClass_get_value(handle: MyClassHandle) -> i32;
    fn MyClass_set_value(handle: MyClassHandle, value: i32);
    fn MyClass_compute(handle: MyClassHandle, x: i32) -> i32;
}

fn main() {
    unsafe {
        // Objekt erstellen
        let handle = MyClass_create(42);
        
        // Methoden aufrufen
        println!("Value: {}", MyClass_get_value(handle));
        MyClass_set_value(handle, 100);
        println!("New value: {}", MyClass_get_value(handle));
        println!("Compute(5): {}", MyClass_compute(handle, 5));
        
        // Objekt zerstören
        MyClass_destroy(handle);
    }
}
```



### 3. Automatische Bindings mit bindgen (für C-Wrapper)



**`build.rs`:**
```rust
// build.rs
extern crate bindgen;
extern crate cc;

use std::path::PathBuf;

fn main() {
    // C++-Code als C-Wrapper kompilieren
    cc::Build::new()
        .cpp(true)
        .file("myclass.cpp")
        .compile("libmyclass.a");
    
    // Bindings generieren
    let bindings = bindgen::Builder::default()
        .header("myclass.hpp")
        .parse_callbacks(Box::new(bindgen::CargoCallbacks))
        .generate()
        .expect("Unable to generate bindings");
    
    bindings
        .write_to_file(PathBuf::from(std::env::var("OUT_DIR").unwrap()).join("bindings.rs"))
        .expect("Couldn't write bindings!");
    
    println!("cargo:rustc-link-search=native=target");
    println!("cargo:rustc-link-lib=static=myclass");
}
```



---



## 🔧 Inline-Assembler in C, C++ und Rust



### Grundlagen

**Inline-Assembler** erlaubt das **direkte Einbetten von Assembler-Code** in Hochsprachen.



### 1. Inline-Assembler in C/C++ (GCC/Clang)



#### AT&T-Syntax (GCC Standard)

```c
// inline_asm.c
#include <stdio.h>

int main() {
    int a = 10, b = 20, result;
    
    // Einfacher Assembler
    __asm__ volatile (
        "addl %1, %0"   // %0 = %0 + %1
        : "=r" (result) // Ausgabe-Operand
        : "r" (a), "0" (b) // Eingabe-Operanden (0 = selben Register wie Ausgabe)
    );
    
    printf("Result: %d\n", result); // 30
    return 0;
}
```



#### Intel-Syntax (mit `asm` Attribute)

```c
// inline_asm_intel.c
#include <stdio.h>

int main() {
    int a = 10, b = 20, result;
    
    __asm__ volatile (
        "add eax, ebx"   // Intel-Syntax
        : "=a" (result) // Ausgabe in eax
        : "a" (a), "b" (b) // Eingabe in eax, ebx
        : "cc" // Clobbered Flags
    );
    
    printf("Result: %d\n", result); // 30
    return 0;
}
```



#### Register-Clobbering

```c
// clobber.c
#include <stdio.h>

int main() {
    int a = 5, b = 7, result;
    
    __asm__ volatile (
        "movl %1, %%eax\n"
        "addl %2, %%eax\n"
        "movl %%eax, %0"
        : "=r" (result)
        : "r" (a), "r" (b)
        : "%eax" // eax wird verändert (clobbered)
    );
    
    printf("Result: %d\n", result); // 12
    return 0;
}
```



### 2. Inline-Assembler in Rust



#### Grundlagen

Rust unterstützt Inline-Assembler über das **`asm!`-Macro** (benötigt **Nightly Rust**).

**Aktivieren:**
```bash
rustup default nightly
```



#### Einfaches Beispiel

```rust
// inline_asm.rs
fn main() {
    let a: u64 = 10;
    let b: u64 = 20;
    let mut result: u64;
    
    unsafe {
        asm!(
            "add {}, {}",
            inout("rax") a => result,
            in("rbx") b,
        );
    }
    
    println!("Result: {}", result); // 30
}
```



#### Eingabe-/Ausgabe-Operanden

```rust
// asm_io.rs
fn main() {
    let x: u64 = 5;
    let y: u64 = 7;
    let mut sum: u64;
    let mut product: u64;
    
    unsafe {
        // Addition
        asm!(
            "add {y}, {x}",
            x = inout(rax) x => sum,
            y = in(rbx) y,
        );
        
        // Multiplikation
        asm!(
            "mul {y}",
            x = inout(rax) x => product,
            y = in(rax) y,
            options(nostack),
        );
    }
    
    println!("Sum: {}, Product: {}", sum, product);
}
```



#### Clobbered Register

```rust
// asm_clobber.rs
fn main() {
    let a: u64 = 100;
    let mut result: u64;
    
    unsafe {
        asm!(
            "mov rax, {}",
            "add rbx, rax",
            in(rax) a,
            out("rax") result,
            clobber_abi("C"), // Alle Register, die die C-ABI beeinflussen
        );
    }
    
    println!("Result: {}", result);
}
```



#### Label

```rust
// asm_label.rs
fn main() {
    let mut x: u64 = 10;
    
    unsafe {
        asm!(
            "cmp {}, 0",
            "je {label}",
            "dec {}",
            "jmp {skip}",
            "{label}:",
            "mov {}, 1",
            "{skip}:",
            x = inout(rax) x,
            label = sym label,
            skip = sym skip,
        );
    }
    
    println!("x: {}", x);
}
```



### 3. Inline-Assembler mit Syscalls



**Beispiel: write() Syscall in Rust**

```rust
// asm_syscall.rs
fn main() {
    let msg = "Hello, ASM Syscall!\n";
    let len = msg.len() as u64;
    
    unsafe {
        asm!(
            "mov rax, 1",      // sys_write
            "mov rdi, 1",      // stdout
            "mov rsi, {msg}", // buffer
            "mov rdx, {len}", // length
            "syscall",
            msg = in(rsi) msg.as_ptr(),
            len = in(rdx) len,
            clobber_abi("C"),
        );
    }
}
```



---



## 📦 Datenstrukturen zwischen Sprachen



### Grundlegende Typen



| C/C++ Typ | Rust Typ | Größe (64-bit) | Beschreibung |
|-----------|----------|----------------|--------------|
| `char` | `i8` / `u8` | 1 Byte | Zeichen |
| `short` | `i16` / `u16` | 2 Bytes | Kurze Ganzzahl |
| `int` | `i32` / `u32` | 4 Bytes | Ganzzahl |
| `long` | `i64` / `u64` | 8 Bytes | Lange Ganzzahl |
| `long long` | `i64` / `u64` | 8 Bytes | Sehr lange Ganzzahl |
| `float` | `f32` | 4 Bytes | Gleitkommazahl |
| `double` | `f64` | 8 Bytes | Doppeltgenaue Gleitkommazahl |
| `void*` | `*mut c_void` | 8 Bytes | Zeiger |
| `char*` | `*const c_char` | 8 Bytes | String-Zeiger |



### Strukturen (structs)



**Wichtig**: Die **Speicherlayout** von Strukturen muss zwischen den Sprachen kompatibel sein!



#### Beispiel: Einfache Struktur

**C-Code:**
```c
// point.h
typedef struct {
    int x;
    int y;
} Point;

Point create_point(int x, int y);
void print_point(Point p);
```

**C-Implementation:**
```c
// point.c
#include "point.h"
#include <stdio.h>

Point create_point(int x, int y) {
    Point p = {x, y};
    return p;
}

void print_point(Point p) {
    printf("Point(%d, %d)\n", p.x, p.y);
}
```



**Rust-Code:**
```rust
// main.rs
#[repr(C)] // WICHTIG: C-kompatibles Layout erzwingen
#[derive(Debug, Clone, Copy)]
struct Point {
    x: i32,
    y: i32,
}

extern "C" {
    fn create_point(x: i32, y: i32) -> Point;
    fn print_point(p: Point);
}

fn main() {
    unsafe {
        let p = create_point(10, 20);
        println!("Rust: {:?}", p);
        print_point(p);
    }
}
```



#### Wichtig: `#[repr(C)]`

Ohne `#[repr(C)]` verwendet Rust ein **undefiniertes Layout** für Strukturen. Mit `#[repr(C)]` wird das **C-kompatible Layout** erzwungen.



#### Beispiel: Komplexere Struktur mit Zeigern

**C-Code:**
```c
// person.h
typedef struct {
    char* name;
    int age;
} Person;

Person* create_person(const char* name, int age);
void free_person(Person* p);
void print_person(Person* p);
```



**C-Implementation:**
```c
// person.c
#include "person.h"
#include <stdlib.h>
#include <string.h>
#include <stdio.h>

Person* create_person(const char* name, int age) {
    Person* p = malloc(sizeof(Person));
    p->name = strdup(name);
    p->age = age;
    return p;
}

void free_person(Person* p) {
    free(p->name);
    free(p);
}

void print_person(Person* p) {
    printf("Person(name=%s, age=%d)\n", p->name, p->age);
}
```



**Rust-Code:**
```rust
// main.rs
use std::ffi::{CString, CStr};
use std::os::raw::c_char;

#[repr(C)]
struct Person {
    name: *mut c_char,
    age: i32,
}

extern "C" {
    fn create_person(name: *const c_char, age: i32) -> *mut Person;
    fn free_person(p: *mut Person);
    fn print_person(p: *mut Person);
}

fn main() {
    unsafe {
        // C-String erstellen
        let name = CString::new("Alice").unwrap();
        
        // Person erstellen
        let person = create_person(name.as_ptr(), 30);
        
        // Person verwenden
        print_person(person);
        
        // Person freigeben
        free_person(person);
        
        // CString freigeben (nicht nötig, da create_person eine Kopie erstellt)
    }
}
```



### Enums



**C-Code:**
```c
// color.h
typedef enum {
    COLOR_RED,
    COLOR_GREEN,
    COLOR_BLUE
} Color;

const char* color_to_string(Color c);
```



**Rust-Code:**
```rust
// main.rs
#[repr(i32)] // oder repr(C) für C-Kompatibilität
#[derive(Debug)]
enum Color {
    Red,
    Green,
    Blue,
}

extern "C" {
    fn color_to_string(c: Color) -> *const c_char;
}

fn main() {
    unsafe {
        let color = Color::Red;
        let name = color_to_string(color);
        let name_str = CStr::from_ptr(name).to_string_lossy();
        println!("Color: {}", name_str);
    }
}
```



---



## 🔄 Memory Management zwischen Sprachen



### Ownership-Probleme



| Szenario | Problem | Lösung |
|----------|---------|--------|
| **Rust ruft C auf** | C gibt Zeiger zurück, Rust weiß nicht, wie man sie freigibt | Dokumentation der C-Funktion (wer ist Besitzer?) |
| **C ruft Rust auf** | Rust gibt Zeiger zurück, C weiß nicht, wie man sie freigibt | Rust-Allokator verwenden oder C-kompatible Funktionen bereitstellen |
| **Doppelte Freigabe** | Beide Sprachen versuchen, den gleichen Speicher zu freigeben | Klare Ownership-Regeln definieren |
| **Dangling Pointers** | Zeiger werden nach Freigabe weiterhin verwendet | Lifetime-Management dokumentieren |



### Lösungsansätze



#### 1. Klare Ownership-Regeln

**Beispiel: C-Funktion gibt Speicher zurück, den der Aufrufer freigeben muss**

**C-Code:**
```c
// string_utils.c
#include <stdlib.h>
#include <string.h>

// Aufrufer ist für die Freigabe verantwortlich
char* create_greeting(const char* name) {
    char* greeting = malloc(strlen(name) + 20);
    sprintf(greeting, "Hello, %s!", name);
    return greeting;
}

// Funktion zum Freigeben
void free_greeting(char* greeting) {
    free(greeting);
}
```



**Rust-Code:**
```rust
// main.rs
use std::ffi::CString;

extern "C" {
    fn create_greeting(name: *const c_char) -> *mut c_char;
    fn free_greeting(greeting: *mut c_char);
}

fn main() {
    unsafe {
        let name = CString::new("World").unwrap();
        let greeting = create_greeting(name.as_ptr());
        
        // greeting verwenden
        let greeting_str = CStr::from_ptr(greeting).to_string_lossy();
        println!("{}", greeting_str);
        
        // Speicher freigeben (wie in C definiert)
        free_greeting(greeting);
    }
}
```



#### 2. Box in Raw Pointer umwandeln



**Rust-Code:**
```rust
// lib.rs
use std::ffi::CString;
use std::os::raw::c_char;

#[no_mangle]
pub extern "C" fn rust_create_string(s: *const c_char) -> *mut c_char {
    let rust_str = unsafe { CStr::from_ptr(s).to_string_lossy() };
    let result = format!("Rust: {}", rust_str);
    CString::new(result).unwrap().into_raw()
}

#[no_mangle]
pub extern "C" fn rust_free_string(s: *mut c_char) {
    unsafe {
        CString::from_raw(s); // Gibt den Speicher frei
    }
}
```



**C-Code:**
```c
// call_rust.c
extern char* rust_create_string(const char* s);
extern void rust_free_string(char* s);

int main() {
    char* msg = rust_create_string("Hello");
    printf("%s\n", msg);
    rust_free_string(msg);
    return 0;
}
```



#### 3. Opaque Pointer für komplexe Typen



**Rust-Code:**
```rust
// lib.rs
pub struct MyComplexType {
    data: Vec<u8>,
}

#[no_mangle]
pub extern "C" fn create_complex() -> *mut MyComplexType {
    Box::into_raw(Box::new(MyComplexType {
        data: vec![1, 2, 3],
    }))
}

#[no_mangle]
pub extern "C" fn free_complex(ptr: *mut MyComplexType) {
    unsafe {
        Box::from_raw(ptr);
    }
}

#[no_mangle]
pub extern "C" fn use_complex(ptr: *mut MyComplexType) -> i32 {
    unsafe {
        let obj = &*ptr;
        obj.data.len() as i32
    }
}
```



**C-Code:**
```c
// call_rust.c
typedef void* MyComplexTypeHandle;

extern MyComplexTypeHandle create_complex();
extern void free_complex(MyComplexTypeHandle);
extern int use_complex(MyComplexTypeHandle);

int main() {
    MyComplexTypeHandle handle = create_complex();
    int len = use_complex(handle);
    printf("Length: %d\n", len);
    free_complex(handle);
    return 0;
}
```



---



## 🛠️ Praktische Beispiele



### 1. Rust nutzt OpenSSL (C-Bibliothek)



**`Cargo.toml`:**
```toml
[package]
name = "openssl-example"
version = "0.1.0"
edition = "2021"

[dependencies]
openssl = "0.10"
```



**Rust-Code:**
```rust
// main.rs
use openssl::ssl::{SslConnector, SslMethod};

fn main() {
    let connector = SslConnector::builder(SslMethod::tls()).unwrap().build();
    println!("OpenSSL Version: {:?}", connector.version());
}
```



### 2. C nutzt Rust-Bibliothek für Kryptographie



**Rust-Bibliothek (`lib.rs`):**
```rust
// lib.rs
use sha2::{Sha256, Digest};
use std::ffi::{CString, CStr};
use std::os::raw::c_char;

#[no_mangle]
pub extern "C" fn rust_sha256(input: *const c_char) -> *mut c_char {
    let input_str = unsafe { CStr::from_ptr(input).to_bytes() };
    let mut hasher = Sha256::new();
    hasher.update(input_str);
    let result = hasher.finalize();
    
    let hex_string = format!("{:x}", result);
    CString::new(hex_string).unwrap().into_raw()
}

#[no_mangle]
pub extern "C" fn rust_free_string(s: *mut c_char) {
    unsafe {
        CString::from_raw(s);
    }
}
```



**C-Code (`hash.c`):**
```c
// hash.c
extern char* rust_sha256(const char* input);
extern void rust_free_string(char* s);

#include <stdio.h>

int main() {
    char* hash = rust_sha256("Hello, World!");
    printf("SHA-256: %s\n", hash);
    rust_free_string(hash);
    return 0;
}
```



### 3. C++-Klasse in Rust nutzen (mit C-Wrapper)



**C++-Header (`vector3d.hpp`):**
```cpp
// vector3d.hpp
class Vector3D {
public:
    Vector3D(double x, double y, double z);
    double get_x() const;
    double get_y() const;
    double get_z() const;
    double magnitude() const;
    
    Vector3D operator+(const Vector3D& other) const;

private:
    double m_x, m_y, m_z;
};

// C-Wrapper
#ifdef __cplusplus
extern "C" {
#endif

typedef void* Vector3DHandle;

Vector3DHandle Vector3D_create(double x, double y, double z);
void Vector3D_destroy(Vector3DHandle handle);
double Vector3D_get_x(Vector3DHandle handle);
double Vector3D_get_y(Vector3DHandle handle);
double Vector3D_get_z(Vector3DHandle handle);
double Vector3D_magnitude(Vector3DHandle handle);
Vector3DHandle Vector3D_add(Vector3DHandle a, Vector3DHandle b);

#ifdef __cplusplus
}
#endif
```



**C++-Implementation (`vector3d.cpp`):**
```cpp
// vector3d.cpp
#include "vector3d.hpp"

Vector3D::Vector3D(double x, double y, double z) : m_x(x), m_y(y), m_z(z) {}

double Vector3D::get_x() const { return m_x; }
double Vector3D::get_y() const { return m_y; }
double Vector3D::get_z() const { return m_z; }

double Vector3D::magnitude() const {
    return sqrt(m_x * m_x + m_y * m_y + m_z * m_z);
}

Vector3D Vector3D::operator+(const Vector3D& other) const {
    return Vector3D(m_x + other.m_x, m_y + other.m_y, m_z + other.m_z);
}

// C-Wrapper
Vector3DHandle Vector3D_create(double x, double y, double z) {
    return new Vector3D(x, y, z);
}

void Vector3D_destroy(Vector3DHandle handle) {
    delete static_cast<Vector3D*>(handle);
}

double Vector3D_get_x(Vector3DHandle handle) {
    return static_cast<Vector3D*>(handle)->get_x();
}

double Vector3D_get_y(Vector3DHandle handle) {
    return static_cast<Vector3D*>(handle)->get_y();
}

double Vector3D_get_z(Vector3DHandle handle) {
    return static_cast<Vector3D*>(handle)->get_z();
}

double Vector3D_magnitude(Vector3DHandle handle) {
    return static_cast<Vector3D*>(handle)->magnitude();
}

Vector3DHandle Vector3D_add(Vector3DHandle a, Vector3DHandle b) {
    Vector3D* v1 = static_cast<Vector3D*>(a);
    Vector3D* v2 = static_cast<Vector3D*>(b);
    return new Vector3D((*v1) + (*v2));
}
```



**Rust-Code (`main.rs`):**
```rust
// main.rs
type Vector3DHandle = *mut std::ffi::c_void;

extern "C" {
    fn Vector3D_create(x: f64, y: f64, z: f64) -> Vector3DHandle;
    fn Vector3D_destroy(handle: Vector3DHandle);
    fn Vector3D_get_x(handle: Vector3DHandle) -> f64;
    fn Vector3D_get_y(handle: Vector3DHandle) -> f64;
    fn Vector3D_get_z(handle: Vector3DHandle) -> f64;
    fn Vector3D_magnitude(handle: Vector3DHandle) -> f64;
    fn Vector3D_add(a: Vector3DHandle, b: Vector3DHandle) -> Vector3DHandle;
}

fn main() {
    unsafe {
        let v1 = Vector3D_create(1.0, 2.0, 3.0);
        let v2 = Vector3D_create(4.0, 5.0, 6.0);
        
        let v3 = Vector3D_add(v1, v2);
        
        println!("v3 = ({}, {}, {})", 
                 Vector3D_get_x(v3),
                 Vector3D_get_y(v3),
                 Vector3D_get_z(v3));
        println!("Magnitude: {}", Vector3D_magnitude(v3));
        
        Vector3D_destroy(v1);
        Vector3D_destroy(v2);
        Vector3D_destroy(v3);
    }
}
```



---



## 🔍 Fehlerbehebung



### Häufige Probleme & Lösungen



#### 1. Symbol nicht gefunden (Linker-Fehler)

**Fehler:**
```
ld: cannot find -l<name>
```

**Lösungen:**
- **Bibliothek nicht gefunden**: `-L<path>` angeben
- **Falscher Bibliotheksname**: Prüfe den Dateinamen (z. B. `libmath.a` vs. `-lmath`)
- **Bibliothek nicht kompiliert**: Stelle sicher, dass die Bibliothek existiert

**Beispiel:**
```bash
# Bibliothek im aktuellen Verzeichnis
gcc main.c -L. -lmath -o main
```



#### 2. Undefined Reference (Symbol nicht definiert)

**Fehler:**
```
undefined reference to `add'
```

**Lösungen:**
- **Funktion nicht implementiert**: Stelle sicher, dass die Funktion in einer Objektdatei existiert
- **Falsche Signatur**: Prüfe, dass die Funktionssignatur in C und Rust kompatibel ist
- **Name Mangling**: Verwende `extern "C"` in C++ und `#[no_mangle]` in Rust



#### 3. Typinkompatibilität

**Fehler:**
```
mismatched types: expected `i32`, found `u32`
```

**Lösungen:**
- **Gleiche Typen verwenden**: Stelle sicher, dass die Typen in beiden Sprachen gleich sind
- **`#[repr(C)]` verwenden**: Für Strukturen
- **`#[repr(i32)]` verwenden**: Für Enums



#### 4. Memory Leaks

**Problem:** Speicher wird nicht freigegeben.

**Lösungen:**
- **Ownership-Regeln definieren**: Wer ist für die Freigabe verantwortlich?
- **Debug-Tools verwenden**: `valgrind`, AddressSanitizer

**Beispiel mit valgrind:**
```bash
valgrind ./programm
```



#### 5. Segmentationsfehler (Segmentation Fault)

**Problem:** Zugriff auf ungültigen Speicher.

**Lösungen:**
- **Null-Pointer prüfen**: `if (ptr == NULL) { ... }`
- **Speicher initialisieren**: Stelle sicher, dass Zeiger gültig sind
- **Bounds prüfen**: Bei Arrays und Puffern



#### 6. ABI-Inkompatibilität

**Problem:** Unterschiedliche Calling Conventions oder Strukturlayouts.

**Lösungen:**
- **`#[repr(C)]` verwenden**: Für Strukturen
- **`extern "C"` verwenden**: Für C++-Funktionen
- **Gleiche Compiler-Optionen**: Stelle sicher, dass beide Seiten die gleiche ABI verwenden



---



## 📚 Lernressourcen



### Bücher

- **[The Rust Programming Language](https://doc.rust-lang.org/book/)** – Offizielles Rust-Buch
- **[Rust for C++ Programmers](https://rust-lang.github.io/rust-clippy/master/index.html#/rust_for_c_programmers)** – Rust für C/C++-Entwickler
- **[C++ and Rust: Interoperability](https://www.packtpub.com/product/c-and-rust-interoperability/9781801075553)** – Buch über Sprachintegration
- **[Programming Rust](https://www.oreilly.com/library/view/programming-rust/9781491927274/)** – Fortgeschrittene Rust-Konzepte



### Online-Dokumentation

- **[Rust FFI Guide](https://doc.rust-lang.org/nomicon/ffi.html)** – Offizieller Rust-FFI-Leitfaden
- **[Rust by Example: FFI](https://doc.rust-lang.org/rust-by-example/ffi.html)** – Praktische Beispiele
- **[bindgen Documentation](https://docs.rs/bindgen/latest/bindgen/)** – bindgen-Anleitung
- **[cbindgen Documentation](https://docs.rs/cbindgen/latest/cbindgen/)** – cbindgen-Anleitung
- **[The Rustonomicon: FFI](https://doc.rust-lang.org/nomicon/ffi.html)** – Fortgeschrittene FFI-Themen



### Videos

- **[Rust FFI – David Calavera](https://www.youtube.com/watch?v=3C0JT7yB48k)** – Einführung in Rust FFI
- **[Interoperability Between Rust and C++ –GNUnify 2020](https://www.youtube.com/watch?v=3C0JT7yB48k)** – Sprachintegration
- **[bindgen Tutorial – RustFest 2018](https://www.youtube.com/watch?v=3C0JT7yB48k)** – Automatische Bindings



### Tools

- **[bindgen](https://github.com/rust-lang/rust-bindgen)** – Automatische Rust-Bindings aus C-Headern
- **[cbindgen](https://github.com/eqrion/cbindgen)** – Automatische C-Header aus Rust-Code
- **[Godbolt Compiler Explorer](https://godbolt.org/)** – Assembler-Output vergleichen
- **[Valgrind](https://valgrind.org/)** – Memory-Leak-Erkennung
- **[AddressSanitizer](https://github.com/google/sanitizers/wiki/AddressSanitizer)** – Speicherfehler erkennen



---



## 🔗 Verwandte Themen



- [Assembler](assembler.md) – Niedrigstufige Programmierung mit Inline-Assembler
- [Compiler](compiler.md) – Wie Code kompiliert wird
- [Linux-Systemprogrammierung](linux-systemprogrammierung.md) – System Calls und Kernel-Interaktion



---



*Letzte Aktualisierung: {{ git_revision_date_localized() }}*
