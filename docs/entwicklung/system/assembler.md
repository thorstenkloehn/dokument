# Assembler (ASM) auf Linux

Assembler (ASM) ist die **niedrigste Abstraktionsebene** der Programmierung – hier schreibst du **direkt Maschinenbefehle** für die CPU. Linux unterstützt Assembler vollständig für alle gängigen Architekturen wie **x86-64, ARM, RISC-V** und mehr.



## 📌 Warum Assembler lernen?

| Vorteil | Beschreibung |
|---------|--------------|
| **Maximale Performance** | Keine Overheads durch Compiler-Optimierungen oder Abstraktionen. |
| **Hardware-Kontrolle** | Direkter Zugriff auf CPU-Features (SIMD, Cache, Register). |
| **Verständnis** | Lernen, wie Computer **wirklich** funktionieren. |
| **Debugging** | Binaries analysieren und Reverse Engineering betreiben. |
| **Kernel-Entwicklung** | Linux-Kernel und Treiber nutzen Assembler für kritische Pfade. |
| **Embedded Systems** | Mikrocontroller und Bare-Metal-Programmierung. |



---



## 🏗️ Grundlagen



### CPU-Register (x86-64)

| Register | Größe | Beschreibung |
|----------|-------|--------------|
| `rax`, `rbx`, `rcx`, `rdx` | 64 Bit | Allgemeine Register (A, B, C, D) |
| `rsi`, `rdi` | 64 Bit | Source/Destination Index (für syscalls) |
| `rbp`, `rsp` | 64 Bit | Base Pointer / Stack Pointer |
| `rip` | 64 Bit | Instruction Pointer (aktuelle Adresse) |
| `r8`–`r15` | 64 Bit | Zusätzliche Register (x86-64) |
| `eflags` | 32 Bit | Status-Flags (Zero, Carry, Overflow etc.) |

> **Hinweis**: In 32-Bit-Modus heißen die Register `eax`, `ebx` etc. (32 Bit), in 16-Bit-Modus `ax`, `bx` (16 Bit).



### Grundlegende Instruktionen

| Kategorie | Instruktion | Beispiel | Beschreibung |
|-----------|-------------|----------|--------------|
| **Datenübertragung** | `mov` | `mov $42, %rax` | Wert in Register laden |
| | | `mov %rbx, %rcx` | Register kopieren |
| **Arithmetik** | `add`, `sub`, `mul`, `div` | `add $10, %rax` | Addition |
| | | `inc %rax`, `dec %rax` | Inkrement/Dekrement |
| **Logik** | `and`, `or`, `xor`, `not` | `and $0xFF, %rax` | Bitweise AND |
| **Vergleiche** | `cmp` | `cmp %rax, %rbx` | Vergleicht zwei Werte |
| | | `test %rax, %rax` | Prüft auf Null |
| **Sprünge** | `jmp` | `jmp label` | Unbedingter Sprung |
| | `je`, `jne`, `jg`, `jl` | `je label` | Sprung wenn gleich (Equal) |
| **Funktionsaufrufe** | `call` | `call function` | Funktion aufrufen |
| | `ret` | `ret` | Aus Funktion zurückkehren |
| **Stack-Operationen** | `push`, `pop` | `push %rax` | Wert auf Stack pushen |
| | | `pop %rbx` | Wert vom Stack poppen |
| **System Calls** | `syscall` | `syscall` | Linux-Kernel aufrufen |



### Speicheradressierung

| Modus | Syntax | Beispiel | Beschreibung |
|-------|--------|----------|--------------|
| **Direkt** | `[adresse]` | `mov $42, (%rax)` | Speicherzelle an Adresse in `%rax` |
| **Indirekt mit Offset** | `[register + offset]` | `mov $42, 8(%rbp)` | 8 Bytes über `rbp` |
| **Indexiert** | `[base + index]` | `mov (%rax, %rbx, 4), %rcx` | `rax + rbx*4` |
| **Absolute Adresse** | `adresse` | `mov msg, %rsi` | Adresse von `msg` laden |



---



## 📝 Syntax-Varianten



### AT&T-Syntax (GNU Standard)

- **Format**: `instruktion quell, ziel`
- **Register**: Präfix `%` (z. B. `%rax`)
- **Immediate Werte**: Präfix `$` (z. B. `$42`)
- **Speicheradressen**: Klammern (z. B. `(%rax)`)
- **Kommentare**: `# Kommentar`

**Beispiel:**
```asm
mov $42, %rax    # Lade 42 in rax
mov %rax, %rbx   # Kopiere rax nach rbx
add $10, %rbx   # Addiere 10 zu rbx
```



### Intel-Syntax (NASM/YASM Standard)

- **Format**: `instruktion ziel, quell` (umgekehrt zu AT&T!)
- **Register**: Kein Präfix (z. B. `rax`)
- **Immediate Werte**: Kein Präfix (z. B. `42`)
- **Speicheradressen**: Klammern (z. B. `[rax]`)
- **Kommentare**: `; Kommentar`

**Beispiel:**
```asm
mov rax, 42    ; Lade 42 in rax
mov rbx, rax   ; Kopiere rax nach rbx
add rbx, 10    ; Addiere 10 zu rbx
```



### Vergleich: AT&T vs. Intel

| Operation | AT&T | Intel |
|-----------|------|-------|
| Lade 42 in rax | `mov $42, %rax` | `mov rax, 42` |
| Kopiere rax nach rbx | `mov %rax, %rbx` | `mov rbx, rax` |
| Addiere 10 zu rbx | `add $10, %rbx` | `add rbx, 10` |
| Speicherzugriff | `mov (%rax), %rbx` | `mov rbx, [rax]` |



---



## 🔌 System Calls auf Linux



### Grundlagen

Linux verwendet **Software-Interrupts** (oder `syscall`-Instruktion auf x86-64) für Systemaufrufe. Jeder Syscall hat:
- Eine **Nummer** (z. B. `1` für `write`)
- **Argumente** in speziellen Registern
- Ein **Rückgabewert** in `%rax`



### Syscall-Nummern finden

Die Syscall-Nummern sind in den Kernel-Headern definiert:

```bash
# x86-64 Syscall-Nummern anzeigen
cat /usr/include/asm/unistd_64.h

# oder online:
# https://filippo.io/linux-syscall-table/
```

| Syscall | Nummer (x86-64) | Description | Argumente |
|---------|------------------|-------------|-----------|
| `read` | 0 | Lesen aus Datei | `rax=0`, `rdi=fd`, `rsi=buffer`, `rdx=count` |
| `write` | 1 | Schreiben in Datei | `rax=1`, `rdi=fd`, `rsi=buffer`, `rdx=count` |
| `open` | 2 | Datei öffnen | `rax=2`, `rdi=path`, `rsi=flags`, `rdx=mode` |
| `close` | 3 | Datei schließen | `rax=3`, `rdi=fd` |
| `exit` | 60 | Prozess beenden | `rax=60`, `rdi=status` |
| `fork` | 57 | Prozess erzeugen | `rax=57` |
| `execve` | 59 | Programm ausführen | `rax=59`, `rdi=path`, `rsi=argv`, `rdx=envp` |



### Syscall-Register (x86-64)

| Register | Argument |
|----------|----------|
| `rax` | Syscall-Nummer |
| `rdi` | 1. Argument |
| `rsi` | 2. Argument |
| `rdx` | 3. Argument |
| `r10` | 4. Argument |
| `r8` | 5. Argument |
| `r9` | 6. Argument |
| `rax` | Rückgabewert |

> **Hinweis**: Bei 32-Bit (x86) werden die Register `eax`, `ebx`, `ecx`, `edx`, `esi`, `edi`, `ebp` verwendet.



---



## 🛠️ Tools für Assembler auf Linux



### GNU Assembler (`as`)

Der Standard-Assembler unter Linux (Teil von **Binutils**).

**Installation:**
```bash
# Auf Debian/Ubuntu
sudo apt install binutils

# Auf Fedora/RHEL
sudo dnf install binutils
```



**Grundlegende Befehle:**

| Befehl | Beschreibung |
|--------|--------------|
| `as [--64] file.s -o file.o` | Assemblieren ( `--64` für x86-64) |
| `ld file.o -o file` | Linken |
| `as --64 hello.s && ld hello.o -o hello` | Komplett: Assemblieren + Linken |



### Linker (`ld`)

Kombiniert Objektdateien (`*.o`) zu ausführbaren Programmen.

**Beispiel:**
```bash
# Einfaches Programm linken
ld hello.o -o hello

# Mit Startcode (für _start anstatt main)
ld -e _start hello.o -o hello
```



### Disassembler (`objdump`)

Zeigt den **Maschinencode** als lesbaren Assembler-Code an.

**Beispiele:**
```bash
# Disassemblieren einer Objektdatei
objdump -d hello.o

# Disassemblieren eines Executables
objdump -d ./hello

# Nur die .text-Sektion anzeigen
objdump -d -j .text ./hello
```



### Debugger (`gdb`)

Interaktives Debugging mit Assembler-Ansicht.

**Beispiele:**
```bash
# Programm starten
gdb ./hello

# Disassemblieren der main-Funktion
(gdb) disassemble main

# Schrittweise Ausführung (Assembler-Ebene)
(gdb) layout asm
(gdb) stepi  # Single instruction
(gdb) nexti  # Next instruction

# Register anzeigen
(gdb) info registers
(gdb) print $rax

# Speicher anzeigen
(gdb) x/10x $rsp  # 10 Hex-Werte ab Stack-Pointer
```



### NASM (Netwide Assembler)

Unterstützt **Intel-Syntax** und ist populär für Cross-Platform-Assembler.

**Installation:**
```bash
sudo apt install nasm  # Debian/Ubuntu
sudo dnf install nasm  # Fedora/RHEL
```



**Beispiel (Intel-Syntax):**
```asm
; hello.asm
section .data
    msg db 'Hello, NASM!', 0xA
    len equ $ - msg

section .text
    global _start

_start:
    mov rax, 1      ; sys_write
    mov rdi, 1      ; stdout
    mov rsi, msg    ; buffer
    mov rdx, len    ; length
    syscall
    
    mov rax, 60     ; sys_exit
    xor rdi, rdi    ; status 0
    syscall
```

**Kompilieren & Linken:**
```bash
nasm -f elf64 hello.asm -o hello.o
ld hello.o -o hello
./hello
```



---



## 💻 Praktische Beispiele



### 1. Hello World in x86-64 Assembler (AT&T-Syntax)

```asm
# hello.s
.section .data
msg: .ascii "Hello, Linux ASM!\n"
len = . - msg

.section .text
.global _start
_start:
    # write(1, msg, len)
    mov $1, %rax          # sys_write (1)
    mov $1, %rdi          # fd (stdout = 1)
    lea msg, %rsi        # buffer address
    mov $len, %rdx        # length
    syscall

    # exit(0)
    mov $60, %rax         # sys_exit (60)
    xor %rdi, %rdi        # status = 0
    syscall
```

**Kompilieren & Ausführen:**
```bash
as --64 hello.s -o hello.o
ld hello.o -o hello
./hello
```



### 2. Addition von zwei Zahlen

```asm
# add.s
.section .text
.global _start
_start:
    mov $10, %rax   # a = 10
    mov $20, %rbx   # b = 20
    add %rbx, %rax  # rax = rax + rbx (30)
    
    # exit(30)
    mov $60, %rax   # sys_exit
    mov %rax, %rdi  # status = 30
    syscall
```

**Testen:**
```bash
as --64 add.s -o add.o
ld add.o -o add
./add
echo $?  # Gibt 30 aus (Exit-Status)
```



### 3. Schleife (Zählen von 1 bis 10)

```asm
# loop.s
.section .text
.global _start
_start:
    mov $1, %rcx   # Zähler = 1
loop_start:
    # Hier könnte man %rcx ausgeben (für Einfachheit weggelassen)
    inc %rcx       # Zähler++
    cmp $10, %rcx  # Vergleiche mit 10
    jle loop_start # Springe zurück, wenn <= 10
    
    # exit(0)
    mov $60, %rax
    xor %rdi, %rdi
    syscall
```



### 4. Inline-Assembler in C

```c
// inline_asm.c
#include <stdio.h>

int main() {
    int a = 10, b = 20, result;
    
    __asm__ volatile (
        "addl %1, %0"   // %0 = %0 + %1
        : "=r" (result) // Ausgabe: result
        : "r" (a), "0" (b) // Eingabe: a, b (b in %0 vorinitialisieren)
    );
    
    printf("Result: %d\n", result); // 30
    return 0;
}
```

**Kompilieren:**
```bash
gcc inline_asm.c -o inline_asm
./inline_asm
```



### 5. Inline-Assembler in Rust (Nightly)

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

**Kompilieren (benötigt Nightly Rust):**
```bash
rustup default nightly
rustc inline_asm.rs -o inline_asm
./inline_asm
```



### 6. Datei lesen mit Syscalls

```asm
# read_file.s
.section .data
filename: .ascii "test.txt\0"
buffer: .space 1024

.section .text
.global _start
_start:
    # open(filename, O_RDONLY)
    mov $2, %rax          # sys_open
    lea filename, %rdi   # filename
    xor %rsi, %rsi        # flags = 0 (O_RDONLY)
    xor %rdx, %rdx        # mode = 0
    syscall
    
    mov %rax, %r8         # fd in r8 speichern
    
    # read(fd, buffer, 1024)
    mov $0, %rax          # sys_read
    mov %r8, %rdi         # fd
    lea buffer, %rsi      # buffer
    mov $1024, %rdx       # count
    syscall
    
    # write(1, buffer, rax)  # rax = gelesene Bytes
    mov $1, %rax          # sys_write
    mov $1, %rdi          # stdout
    lea buffer, %rsi      # buffer
    mov %rax, %rdx        # count (aus read)
    syscall
    
    # close(fd)
    mov $3, %rax          # sys_close
    mov %r8, %rdi         # fd
    syscall
    
    # exit(0)
    mov $60, %rax
    xor %rdi, %rdi
    syscall
```



---



## 🎯 Architektspezifische Hinweise



### x86-64

- **Standard** auf modernen Linux-Systemen
- **Register**: 16 allgemeine Register (`rax`–`r15`)
- **Syscall**: `syscall`-Instruktion
- **ABI**: [System V AMD64 ABI](https://refspecs.linuxfoundation.org/elf/x86_64-SysV-psABI.pdf)



### ARM (AArch64)

- **Register**: `x0`–`x30` (64 Bit), `w0`–`w30` (32 Bit)
- **Syscall**: `svc #0`
- **Syscall-Nummern**: `x8`
- **Argumente**: `x0`–`x5`

**Beispiel (ARM64):**
```asm
// hello-arm.s
.data
msg: .ascii "Hello, ARM64!\n"
len = . - msg

.text
.global _start
_start:
    mov x0, #1          // fd (stdout)
    ldr x1, =msg       // buffer
    ldr x2, =len       // length
    mov x8, #64        // sys_write (64)
    svc #0             // syscall
    
    mov x0, #0         // status
    mov x8, #93        // sys_exit (93)
    svc #0
```

**Kompilieren (Cross-Compiling):**
```bash
aarch64-linux-gnu-as hello-arm.s -o hello-arm.o
aarch64-linux-gnu-ld hello-arm.o -o hello-arm
qemu-aarch64 ./hello-arm
```



### RISC-V

- **Register**: `x0`–`x31` (64 Bit bei RV64)
- **Syscall**: `ecall`
- **Syscall-Nummern**: `a7`
- **Argumente**: `a0`–`a5`

**Beispiel (RISC-V):**
```asm
# hello-riscv.s
.data
msg: .ascii "Hello, RISC-V!\n"
len = . - msg

.text
.global _start
_start:
    li a7, 64          # sys_write (64)
    li a0, 1           # fd (stdout)
    la a1, msg         # buffer
    li a2, len         # length
    ecall
    
    li a7, 93          # sys_exit (93)
    li a0, 0           # status
    ecall
```

**Kompilieren:**
```bash
riscv64-linux-gnu-as hello-riscv.s -o hello-riscv.o
riscv64-linux-gnu-ld hello-riscv.o -o hello-riscv
qemu-riscv64 ./hello-riscv
```



---



## 🔍 Debugging & Analyse



### Disassemblieren mit objdump

```bash
# Vollständiges Disassemblieren
objdump -d ./programm

# Nur eine Funktion anzeigen
objdump -d -j .text ./programm

# Mit Adressen und Symbolen
objdump -d -S ./programm

# ELF-Header anzeigen
objdump -f ./programm

# Alle Sections anzeigen
objdump -h ./programm
```



### GDB für Assembler-Debugging

```bash
# Programm starten
gdb ./programm

# Breakpoint bei _start setzen
(gdb) break _start

# Programm starten
(gdb) run

# Assembler-Ansicht aktivieren
(gdb) layout asm

# Register anzeigen
(gdb) info registers
(gdb) info all-registers

# Speicher anzeigen
(gdb) x/10i $rip  # 10 Instruktionen ab Instruction Pointer
(gdb) x/10x $rsp  # 10 Hex-Werte ab Stack-Pointer

# Schrittweise ausführen
(gdb) stepi   # Einzelschritt (in Funktion)
(gdb) nexti   # Nächste Instruktion (ohne in Funktion)
(gdb) continue # Weiter bis zum nächsten Breakpoint
```



### Radare2 (Alternative zu GDB)

```bash
# Installieren
sudo apt install radare2

# Programm analysieren
r2 -A ./programm

# Assembler anzeigen
[0x00000000]> pd 20  # 20 Instruktionen anzeigen

# Breakpoint setzen und ausführen
[0x00000000]> db _start
[0x00000000]> dc
```



### strace – System Calls beobachten

```bash
# Alle System Calls eines Programms anzeigen
strace ./programm

# Nur bestimmte Syscalls anzeigen
strace -e write ./programm

# Statistik über Syscalls
strace -c ./programm
```



---



## 📚 Lernressourcen



### Bücher

- **[Programming from the Ground Up](https://savannah.gnu.org/projects/pgubook/)** – Kostenloses x86-Assembler-Buch
- **[Assembly Language for x86 Processors](https://www.amazon.com/Assembly-Language-x86-Processors-7th/dp/013407226X)** – Kip R. Irvine
- **[The Art of Assembly Language](https://www.amazon.com/Art-Assembly-Language-Randy-Hyde/dp/1886411972)** – Randy Hyde



### Online-Tutorials

- **[OSDev Wiki – x86 Assembly](https://wiki.osdev.org/x86_Assembly)** – OS-Entwicklung mit ASM
- **[ASM Tutorial (TutorialsPoint)](https://www.tutorialspoint.com/assembly_programming/)** – Grundlagen
- **[NASM Documentation](https://www.nasm.us/docs.php)** – Offizielle NASM-Doks
- **[Linux Syscall Reference](https://filippo.io/linux-syscall-table/)** – Syscall-Tabelle



### Videos

- **[LiveOverflow – x86 Assembly](https://www.youtube.com/playlist?list=PLHMOxMJQYUDy0xQ6YY7XZV78hc0xq7ZQZ)** – Security & ASM
- **[MIT 6.004: Computation Structures](https://computationstructures.org/)** – Computer-Architektur
- **[The Primeagen – Learning Assembly](https://www.youtube.com/watch?v=75gBxQdYjYI)** – Praktische Einführung



### Tools

- **[Godbolt Compiler Explorer](https://godbolt.org/)** – C/C++/Rust in ASM umwandeln
- **[Compiler Explorer (ARM/RISC-V)](https://godbolt.org/)** – Mehrere Architekturen
- **[Online Assembler (Jbeale)](http://www.jbeale.com/asm/)** – Einfacher Online-Assembler



---



## 🎯 Best Practices



### 1. Register richtig nutzen

- **`rax`**: Rückgabewert von Funktionen/Syscalls
- **`rsp`**: Stack-Pointer (nie direkt manipulieren, außer in Prolog/Epilog)
- **`rbp`**: Base-Pointer (für Stack-Frames)
- **`rdi`, `rsi`, `rdx`, `rcx`, `r8`, `r9`**: Funktionsargumente (x86-64 ABI)
- **Kalibrieren**: Nach Funktionsaufrufen Register sichern, die ändert werden



### 2. Stack-Frames

Ein typischer **Funktionsprolog** (x86-64):
```asm
push %rbp        # Alten Base-Pointer sichern
mov %rsp, %rbp   # Neuen Base-Pointer setzen
sub $16, %rsp    # Platz für lokale Variablen
```

**Funktionsepilog:**
```asm
mov %rbp, %rsp   # Base-Pointer wiederherstellen
pop %rbp        # Alten Base-Pointer laden
ret             # Zurückspringen
```



### 3. Syscalls sicher aufrufen

- Immer **Register vor Syscalls sichern**, die verändert werden
- **`rax`**, **`rdi`**, **`rsi`**, **`rdx`** werden oft überschrieben
- Beispiel für sicheres Syscall:
```asm
mov %rax, %r10   # rax sichern
mov $1, %rax     # sys_write
mov $1, %rdi     # stdout
mov %r10, %rsi   # buffer (aus rax)
mov $10, %rdx    # length
syscall
mov %r10, %rax   # rax wiederherstellen
```



### 4. Fehlerbehandlung

- **Syscall-Fehler**: Negativer Rückgabewert in `rax` (errno in `-rax`)
- **Fehler prüfen:**
```asm
syscall
cmp $0, %rax
jl error_handler  # Springe wenn rax < 0 (Fehler)
```



### 5. Performance-Tipps

- **SIMD nutzen**: `mm0`–`mm7` (MMX), `xmm0`–`xmm15` (SSE), `ymm0`–`ymm15` (AVX)
- **Cache-optimieren**: Daten nah beieinander speichern
- **Branch Prediction**: `cmov` (conditional move) statt `jmp` für einfache Bedingungen
- **Inline**: Kritische Code-Pfade in ASM schreiben



---



## 🔗 Verwandte Themen



- [Compiler](compiler.md) – Wie Assembler-Code generiert wird
- [Rust, C++ & C Integration](rust-c-cpp-integration.md) – Inline-Assembler in Hochsprachen
- [Linux-Systemprogrammierung](linux-systemprogrammierung.md) – Syscalls und Kernel-Interaktion



---



*Letzte Aktualisierung: {{ git_revision_date_localized() }}*
