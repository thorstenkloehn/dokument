# Linux-Systemprogrammierung

**Systemprogrammierung unter Linux** befasst sich mit der **niedrigstufigen Interaktion** zwischen Programmen und dem **Linux-Kernel**. Sie ermöglicht dir, **Systemaufrufe (Syscalls)**, **Prozessverwaltung**, **Dateisystemoperationen**, **Signale** und **Memory Management** direkt zu nutzen – alles auf der Grundlage von **C, Rust, C++ und Assembler**.



## 📌 Warum Linux-Systemprogrammierung?

| Anwendungsfall | Nutzen |
|--------------|--------|
| **Performance-Optimierung** | Direkter Systemzugriff ohne Overhead |
| **System-Tools entwickeln** | Eigene `ls`, `grep`, `cat`-ähnliche Programme |
| **Kernel-Module** | Treiber und Kernel-Erweiterungen schreiben |
| **Embedded Systems** | Linux auf eingeschränkten Geräten (Raspberry Pi, IoT) |
| **Sicherheitsforschung** | Systemverhalten analysieren und manipulieren |
| **Hochverfügbare Dienste** | Robuste Server- und Daemon-Prozesse |
| **Reverse Engineering** | Binaries analysieren und verstehen |



---



## 🏗️ Grundlagen der Linux-Architektur



### Linux-Kernel vs. User Space

```
┌─────────────────────────────────────────────────────────────┐
│                    USER SPACE (Anwendungen)                     │
├─────────────────────────────────────────────────────────────┤
│  Systembibliotheken (glibc)  │  Anwendungen  │  Shell  │  ...   │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                      KERNEL SPACE                                │
├─────────────────────────────────────────────────────────────┤
│  Systemaufrufe (Syscalls)  │  Treiber  │  Memory Mgmt  │  ...   │
└─────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────┐
│                        HARDWARE                                  │
├─────────────────────────────────────────────────────────────┤
│  CPU  │  RAM  │  Festplatte  │  Netzwerk  │  GPU  │  ...            │
└─────────────────────────────────────────────────────────────┘
```



### System Calls (Syscalls)

**Systemaufrufe** sind die **Schnittstelle zwischen User Space und Kernel**. Jeder Syscall:
- Hat eine **Nummer** (z. B. `1` für `write`)
- Wird über die **`syscall`**-Instruktion (x86-64) oder **`svc`** (ARM) aufgerufen
- Gibt einen **Rückgabewert** in `%rax` (x86-64) zurück
- Kann **Fehler** durch negativen Rückgabewert signalisieren (errno = `-rax`)



### glibc – Die C-Standardbibliothek

**glibc** (GNU C Library) ist die Standard-Implementierung der **C-Standardbibliothek** auf Linux. Sie bietet:
- **Wrapper für Syscalls** (z. B. `printf()` → `write()` Syscall)
- **Standard-Funktionen** (`malloc()`, `free()`, `strlen()`, etc.)
- **Thread-Unterstützung** (`pthread`)
- **Lokale und Zeitfunktionen** (`strftime()`, `localtime()`)

**Wichtig**: Die meisten Programme nutzen **glibc-Wrapper** statt direkte Syscalls. Für maximale Kontrolle kannst du aber **direkt Syscalls** aufrufen.



---



## 🔌 System Calls (Syscalls) im Detail



### Syscall-Nummern und Register (x86-64)

| Syscall | Nummer | Beschreibung | Argumente |
|---------|--------|--------------|-----------|
| `read` | 0 | Lesen aus Datei | `rax=0`, `rdi=fd`, `rsi=buffer`, `rdx=count` |
| `write` | 1 | Schreiben in Datei | `rax=1`, `rdi=fd`, `rsi=buffer`, `rdx=count` |
| `open` | 2 | Datei öffnen | `rax=2`, `rdi=path`, `rsi=flags`, `rdx=mode` |
| `close` | 3 | Datei schließen | `rax=3`, `rdi=fd` |
| `stat` | 4 | Datei-Status abfragen | `rax=4`, `rdi=path`, `rsi=statbuf` |
| `fstat` | 5 | Datei-Status (über fd) | `rax=5`, `rdi=fd`, `rsi=statbuf` |
| `lstat` | 6 | Symbolischer Link-Status | `rax=6`, `rdi=path`, `rsi=statbuf` |
| `lseek` | 8 | Dateizeiger bewegen | `rax=8`, `rdi=fd`, `rsi=offset`, `rdx=whence` |
| `mmap` | 9 | Speicher abbilden | `rax=9`, `rdi=addr`, `rsi=length`, `rdx=prot`, `r10=flags`, `r8=fd`, `r9=offset` |
| `munmap` | 11 | Speicherabbildung aufheben | `rax=11`, `rdi=addr`, `rsi=length` |
| `brk` | 12 | Heap-Größe ändern | `rax=12`, `rdi=addr` |
| `exit` | 60 | Prozess beenden | `rax=60`, `rdi=status` |
| `exit_group` | 231 | Alle Threads beenden | `rax=231`, `rdi=status` |
| `fork` | 57 | Prozess erzeugen | `rax=57` |
| `clone` | 56 | Thread erzeugen | `rax=56`, `rdi=flags`, `rsi=stack`, `rdx=parent_tid`, `r10=child_tid`, `r8=tls` |
| `execve` | 59 | Programm ausführen | `rax=59`, `rdi=path`, `rsi=argv`, `rdx=envp` |
| `wait4` | 61 | Auf Kindprozess warten | `rax=61`, `rdi=pid`, `rsi=status`, `rdx=options`, `r10=rusage` |
| `kill` | 62 | Signal senden | `rax=62`, `rdi=pid`, `rsi=signal` |
| `sigaction` | 13 | Signal-Handler setzen | `rax=13`, `rdi=sig`, `rsi=act`, `rdx=oldact` |
| `sigreturn` | 15 | Von Signal-Handler zurückkehren | `rax=15`, `rdi=unused` |
| `rt_sigprocmask` | 14 | Signal-Maske setzen | `rax=14`, `rdi=how`, `rsi=set`, `rdx=oldset`, `r10=sigsetsize` |



### Syscall-Register (x86-64)

| Register | Argument | Beschreibung |
|----------|----------|--------------|
| `rax` | Syscall-Nummer | Gibt auch den Rückgabewert zurück |
| `rdi` | 1. Argument | - |
| `rsi` | 2. Argument | - |
| `rdx` | 3. Argument | - |
| `r10` | 4. Argument | - |
| `r8` | 5. Argument | - |
| `r9` | 6. Argument | - |
| Stack | 7.+ Argument | Von rechts nach links |



### Fehlerbehandlung

- **Erfolg**: Rückgabewert ≥ 0
- **Fehler**: Rückgabewert < 0, **errno = -Rückgabewert**

**Beispiel (Fehler prüfen):**
```c
long ret = syscall(SYS_open, "file.txt", O_RDONLY);
if (ret < 0) {
    errno = -ret;
    perror("open failed");
}
```



### Syscall-Nummern finden

```bash
# x86-64 Syscall-Nummern anzeigen
cat /usr/include/asm/unistd_64.h

# ARM64 Syscall-Nummern
cat /usr/include/asm/unistd.h

# Online-Tabelle
# https://filippo.io/linux-syscall-table/
# https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/
```



---



## 💻 System Calls in der Praxis



### 1. Dateioperationen



#### `open()` – Datei öffnen

**C-Code:**
```c
#include <fcntl.h>      // O_RDONLY, O_WRONLY, O_CREAT, etc.
#include <unistd.h>     // syscall, open
#include <errno.h>     // errno
#include <stdio.h>      // perror

int main() {
    int fd = open("test.txt", O_RDONLY);
    if (fd < 0) {
        perror("open failed");
        return 1;
    }
    
    // Datei verwenden...
    
    close(fd);
    return 0;
}
```



**Rust-Code (mit `nix`-Crate):**
```rust
use nix::fcntl::{open, OFlag};
use nix::unistd::close;
use std::path::Path;

fn main() -> Result<(), nix::Error> {
    let fd = open(Path::new("test.txt"), OFlag::O_RDONLY, nix::sys::stat::Mode::empty())?;
    
    // Datei verwenden...
    
    close(fd)?;
    Ok(())
}
```



#### `read()` – Aus Datei lesen

**C-Code:**
```c
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

int main() {
    int fd = open("test.txt", O_RDONLY);
    if (fd < 0) {
        perror("open failed");
        return 1;
    }
    
    char buffer[1024];
    ssize_t bytes_read = read(fd, buffer, sizeof(buffer));
    if (bytes_read < 0) {
        perror("read failed");
        close(fd);
        return 1;
    }
    
    printf("Read %zd bytes: %.*s\n", bytes_read, (int)bytes_read, buffer);
    
    close(fd);
    return 0;
}
```



**Rust-Code:**
```rust
use std::fs::File;
use std::io::Read;

fn main() -> std::io::Result<()> {
    let mut file = File::open("test.txt")?;
    let mut buffer = [0; 1024];
    let bytes_read = file.read(&mut buffer)?;
    
    let content = String::from_utf8_lossy(&buffer[..bytes_read]);
    println!("Read {} bytes: {}", bytes_read, content);
    
    Ok(())
}
```



#### `write()` – In Datei schreiben

**C-Code (direkter Syscall):**
```c
#include <unistd.h>
#include <fcntl.h>

int main() {
    int fd = open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644);
    if (fd < 0) {
        return 1;
    }
    
    const char* msg = "Hello, Linux Syscalls!\n";
    size_t len = strlen(msg);
    
    ssize_t bytes_written = write(fd, msg, len);
    if (bytes_written < 0) {
        return 1;
    }
    
    close(fd);
    return 0;
}
```



**Assembler (x86-64, direkter Syscall):**
```asm
# write.asm
.section .data
msg: .ascii "Hello, Linux Syscalls!\n"
len = . - msg

.section .text
.global _start
_start:
    # open("output.txt", O_WRONLY | O_CREAT | O_TRUNC, 0644)
    mov $2, %rax          # sys_open
    lea filename, %rdi   # filename
    mov $0x241, %rsi      # O_WRONLY | O_CREAT | O_TRUNC
    mov $0644, %rdx       # mode (rw-r--r--)
    syscall
    
    mov %rax, %r8         # fd in r8 speichern
    
    # write(fd, msg, len)
    mov $1, %rax          # sys_write
    mov %r8, %rdi         # fd
    lea msg, %rsi         # buffer
    mov $len, %rdx        # length
    syscall
    
    # close(fd)
    mov $3, %rax          # sys_close
    mov %r8, %rdi         # fd
    syscall
    
    # exit(0)
    mov $60, %rax
    xor %rdi, %rdi
    syscall

.section .data
filename: .ascii "output.txt\0"
```



### 2. Prozessverwaltung



#### `fork()` – Prozess erzeugen

**C-Code:**
```c
#include <unistd.h>
#include <stdio.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        // Kindprozess
        printf("Child process: PID = %d\n", getpid());
    } else {
        // Elternprozess
        printf("Parent process: PID = %d, Child PID = %d\n", getpid(), pid);
    }
    
    return 0;
}
```



**Rust-Code:**
```rust
use nix::unistd::{fork, ForkResult, getpid};
use std::process;

fn main() {
    match unsafe { fork() } {
        Ok(ForkResult::Parent { child, .. }) => {
            println!("Parent process: PID = {}, Child PID = {}", 
                     getpid().unwrap(), child);
        }
        Ok(ForkResult::Child) => {
            println!("Child process: PID = {}", getpid().unwrap());
        }
        Err(e) => {
            eprintln!("fork failed: {}", e);
            process::exit(1);
        }
    }
}
```



#### `execve()` – Programm ausführen

**C-Code:**
```c
#include <unistd.h>
#include <stdio.h>

int main() {
    char* argv[] = {"ls", "-l", NULL};
    char* envp[] = {NULL};
    
    execve("/bin/ls", argv, envp);
    
    // Nur erreicht, wenn execve fehlt
    perror("execve failed");
    return 1;
}
```



**Rust-Code:**
```rust
use nix::unistd::execve;
use std::ffi::CString;
use std::path::Path;

fn main() {
    let path = CString::new("/bin/ls").unwrap();
    let arg0 = CString::new("ls").unwrap();
    let arg1 = CString::new("-l").unwrap();
    let args = vec![arg0, arg1];
    
    // NULL-terminierte Argumentliste
    let argv: Vec<_> = args.iter().map(|s| s.as_ptr()).chain(std::iter::once(std::ptr::null())).collect();
    
    // execve aufrufen
    if let Err(e) = execve(&path, &argv, &[std::ptr::null()]) {
        eprintln!("execve failed: {}", e);
        std::process::exit(1);
    }
}
```



#### `wait()` – Auf Kindprozess warten

**C-Code:**
```c
#include <unistd.h>
#include <sys/wait.h>
#include <stdio.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        // Kindprozess
        printf("Child: PID = %d\n", getpid());
        _exit(42);  // Exit-Status 42
    } else {
        // Elternprozess
        int status;
        waitpid(pid, &status, 0);
        
        if (WIFEXITED(status)) {
            printf("Child exited with status: %d\n", WEXITSTATUS(status));
        }
    }
    
    return 0;
}
```



### 3. Speicherverwaltung



#### `mmap()` – Speicher abbilden

**C-Code:**
```c
#include <sys/mman.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    // Datei öffnen
    int fd = open("test.txt", O_RDONLY);
    if (fd < 0) {
        perror("open failed");
        return 1;
    }
    
    // Dateigröße bestimmen
    off_t size = lseek(fd, 0, SEEK_END);
    
    // Speicher abbilden
    void* addr = mmap(NULL, size, PROT_READ, MAP_PRIVATE, fd, 0);
    if (addr == MAP_FAILED) {
        perror("mmap failed");
        close(fd);
        return 1;
    }
    
    // Speicherinhalt lesen
    char* content = (char*)addr;
    printf("File content: %.*s\n", (int)size, content);
    
    // Speicherabbildung aufheben
    munmap(addr, size);
    close(fd);
    
    return 0;
}
```



**Rust-Code:**
```rust
use nix::sys::mman::{mmap, munmap, MapFlags, ProtFlags};
use nix::fcntl::{open, OFlag};
use nix::unistd::{close, lseek, Whence};
use std::path::Path;

fn main() -> Result<(), nix::Error> {
    // Datei öffnen
    let fd = open(Path::new("test.txt"), OFlag::O_RDONLY, nix::sys::stat::Mode::empty())?;
    
    // Dateigröße bestimmen
    let size = lseek(fd, 0, Whence::SeekEnd)? as usize;
    
    // Speicher abbilden
    let addr = unsafe {
        mmap(
            None,
            size,
            ProtFlags::PROT_READ,
            MapFlags::MAP_PRIVATE,
            fd,
            0,
        )
    }?;
    
    // Speicherinhalt als String lesen
    let content = unsafe {
        let slice = std::slice::from_raw_parts(addr as *const u8, size);
        String::from_utf8_lossy(slice)
    };
    
    println!("File content: {}", content);
    
    // Speicherabbildung aufheben
    unsafe { munmap(addr, size)? };
    close(fd)?;
    
    Ok(())
}
```



#### `brk()` / `sbrk()` – Heap-Größe ändern

**C-Code:**
```c
#include <unistd.h>
#include <stdio.h>

int main() {
    // Aktuellen Heap-Endpunkt speichern
    void* current_break = sbrk(0);
    printf("Current break: %p\n", current_break);
    
    // Heap um 1MB erweitern
    void* new_break = sbrk(1024 * 1024);
    if (new_break == (void*)-1) {
        perror("sbrk failed");
        return 1;
    }
    
    printf("New break: %p\n", new_break);
    
    // Heap zurücksetzen
    brk(current_break);
    
    return 0;
}
```



### 4. Signale



#### `signal()` – Signal-Handler setzen

**C-Code:**
```c
#include <signal.h>
#include <stdio.h>
#include <unistd.h>

void sigint_handler(int signum) {
    printf("\nReceived SIGINT (Ctrl+C)\n");
    _exit(1);
}

int main() {
    signal(SIGINT, sigint_handler);
    
    printf("Press Ctrl+C to trigger SIGINT...\n");
    
    while (1) {
        sleep(1);
    }
    
    return 0;
}
```



#### `sigaction()` – Erweitertes Signal-Handling

**C-Code:**
```c
#include <signal.h>
#include <stdio.h>
#include <unistd.h>

void sigint_handler(int signum, siginfo_t* si, void* unused) {
    printf("\nReceived signal %d\n", signum);
    printf("Sender PID: %d\n", si->si_pid);
    _exit(1);
}

int main() {
    struct sigaction sa;
    sa.sa_sigaction = sigint_handler;
    sa.sa_flags = SA_SIGINFO;
    sigemptyset(&sa.sa_mask);
    
    if (sigaction(SIGINT, &sa, NULL) < 0) {
        perror("sigaction failed");
        return 1;
    }
    
    printf("Press Ctrl+C to trigger SIGINT...\n");
    
    while (1) {
        sleep(1);
    }
    
    return 0;
}
```



**Rust-Code (mit `signal-hook`-Crate):**
```rust
use signal_hook::{consts::SIGINT, iterator::Signals};
use std::io;

fn main() -> io::Result<()> {
    let mut signals = Signals::new(&[SIGINT])?;
    
    println!("Press Ctrl+C to trigger SIGINT...");
    
    for signal in signals.forever() {
        match signal {
            SIGINT => {
                println!("\nReceived SIGINT (Ctrl+C)");
                std::process::exit(1);
            }
            _ => unreachable!(),
        }
    }
    
    Ok(())
}
```



#### `kill()` – Signal senden

**C-Code:**
```c
#include <signal.h>
#include <unistd.h>
#include <stdio.h>

int main() {
    pid_t pid = fork();
    
    if (pid < 0) {
        perror("fork failed");
        return 1;
    } else if (pid == 0) {
        // Kindprozess: Wartet auf Signal
        printf("Child (PID=%d) waiting for signal...\n", getpid());
        pause();  // Wartet auf Signal
        printf("Child received signal!\n");
    } else {
        // Elternprozess: Sendet Signal nach 2 Sekunden
        sleep(2);
        printf("Parent sending SIGUSR1 to child (PID=%d)...\n", pid);
        kill(pid, SIGUSR1);
        wait(NULL);  // Wartet auf Kind
    }
    
    return 0;
}
```



### 5. Threads



#### `pthread` – POSIX Threads (C)

**C-Code:**
```c
#include <pthread.h>
#include <stdio.h>

void* thread_function(void* arg) {
    int thread_num = *(int*)arg;
    printf("Thread %d: Hello from thread!\n", thread_num);
    return NULL;
}

int main() {
    pthread_t threads[3];
    int thread_args[3] = {0, 1, 2};
    
    for (int i = 0; i < 3; i++) {
        pthread_create(&threads[i], NULL, thread_function, &thread_args[i]);
    }
    
    for (int i = 0; i < 3; i++) {
        pthread_join(threads[i], NULL);
    }
    
    return 0;
}
```



**Rust-Code:**
```rust
use std::thread;
use std::time::Duration;

fn main() {
    let handles: Vec<_> = (0..3).map(|i| {
        thread::spawn(move || {
            println!("Thread {}: Hello from thread!", i);
        })
    }).collect();
    
    for handle in handles {
        handle.join().unwrap();
    }
}
```



#### `clone()` – Thread-Erzeugung (Syscall)

**C-Code:**
```c
#include <sched.h>
#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int thread_function(void* arg) {
    printf("Thread: Hello from thread! (arg=%d)\n", *(int*)arg);
    return 0;
}

int main() {
    const int STACK_SIZE = 4096 * 4096;  // 16 MB Stack
    char* stack = malloc(STACK_SIZE);
    char* stack_top = stack + STACK_SIZE;
    
    int arg = 42;
    
    pid_t pid = clone(
        thread_function,
        stack_top,
        CLONE_VM | CLONE_FS | CLONE_FILES | CLONE_SIGHAND,
        &arg
    );
    
    if (pid < 0) {
        perror("clone failed");
        free(stack);
        return 1;
    }
    
    if (pid == 0) {
        // Thread
        _exit(0);
    } else {
        // Haupt-Thread
        waitpid(pid, NULL, 0);
        free(stack);
    }
    
    return 0;
}
```



---



## 📁 Dateisystem-Operationen



### Datei-Attribute (`stat`)

**C-Code:**
```c
#include <sys/stat.h>
#include <unistd.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    if (argc < 2) {
        printf("Usage: %s <file>\n", argv[0]);
        return 1;
    }
    
    struct stat st;
    if (stat(argv[1], &st) < 0) {
        perror("stat failed");
        return 1;
    }
    
    printf("File: %s\n", argv[1]);
    printf("Size: %ld bytes\n", st.st_size);
    printf("Mode: %o\n", st.st_mode);
    printf("UID: %d\n", st.st_uid);
    printf("GID: %d\n", st.st_gid);
    printf("Last access: %ld\n", st.st_atime);
    printf("Last modification: %ld\n", st.st_mtime);
    
    return 0;
}
```



### Verzeichnisse lesen (`opendir`/`readdir`)

**C-Code:**
```c
#include <dirent.h>
#include <stdio.h>

int main(int argc, char* argv[]) {
    char* path = argc > 1 ? argv[1] : ".";
    
    DIR* dir = opendir(path);
    if (!dir) {
        perror("opendir failed");
        return 1;
    }
    
    struct dirent* entry;
    while ((entry = readdir(dir)) != NULL) {
        printf("%s\n", entry->d_name);
    }
    
    closedir(dir);
    return 0;
}
```



**Rust-Code:**
```rust
use std::fs;

fn main() -> std::io::Result<()> {
    let path = std::env::args().nth(1).unwrap_or_else(|| ".".to_string());
    
    for entry in fs::read_dir(path)? {
        let entry = entry?;
        println!("{}", entry.file_name().to_string_lossy());
    }
    
    Ok(())
}
```



### Datei-Deskriptoren

| Deskriptor | Beschreibung |
|------------|--------------|
| `0` | Standard Input (stdin) |
| `1` | Standard Output (stdout) |
| `2` | Standard Error (stderr) |



**C-Code (stdin lesen):**
```c
#include <unistd.h>
#include <stdio.h>

int main() {
    char buffer[1024];
    ssize_t bytes_read = read(STDIN_FILENO, buffer, sizeof(buffer));
    if (bytes_read < 0) {
        perror("read failed");
        return 1;
    }
    
    write(STDOUT_FILENO, buffer, bytes_read);
    return 0;
}
```



---



## 🔧 Prozessumgebung



### Umgebungsvariablen

**C-Code:**
```c
#include <stdio.h>

int main() {
    extern char** environ;
    
    for (char** env = environ; *env != NULL; env++) {
        printf("%s\n", *env);
    }
    
    return 0;
}
```



**Rust-Code:**
```rust
use std::env;

fn main() {
    for (key, value) in env::vars() {
        println!("{}={}", key, value);
    }
}
```



### Argumentparsing

**C-Code:**
```c
#include <stdio.h>

int main(int argc, char* argv[]) {
    printf("Program name: %s\n", argv[0]);
    
    for (int i = 1; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }
    
    return 0;
}
```



**Rust-Code:**
```rust
use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    
    println!("Program name: {}", args[0]);
    
    for (i, arg) in args.iter().skip(1).enumerate() {
        println!("Argument {}: {}", i + 1, arg);
    }
}
```



---



## 📊 Prozess- und Systeminformationen



### Prozess-ID und Elternprozess

**C-Code:**
```c
#include <unistd.h>
#include <stdio.h>

int main() {
    printf("PID: %d\n", getpid());
    printf("PPID: %d\n", getppid());
    printf("UID: %d\n", getuid());
    printf("GID: %d\n", getgid());
    return 0;
}
```



**Rust-Code:**
```rust
use nix::unistd::{getpid, getppid, getuid, getgid};

fn main() {
    println!("PID: {}", getpid().unwrap());
    println!("PPID: {}", getppid().unwrap());
    println!("UID: {}", getuid().unwrap());
    println!("GID: {}", getgid().unwrap());
}
```



### Systeminformationen (`uname`)

**C-Code:**
```c
#include <sys/utsname.h>
#include <stdio.h>

int main() {
    struct utsname sys_info;
    if (uname(&sys_info) < 0) {
        perror("uname failed");
        return 1;
    }
    
    printf("System: %s\n", sys_info.sysname);
    printf("Hostname: %s\n", sys_info.nodename);
    printf("Release: %s\n", sys_info.release);
    printf("Version: %s\n", sys_info.version);
    printf("Machine: %s\n", sys_info.machine);
    
    return 0;
}
```



### CPU-Informationen

**Bash:**
```bash
# CPU-Info anzeigen
cat /proc/cpuinfo

# Anzahl der CPUs
nproc

# CPU-Typ
lscpu
```



**C-Code:**
```c
#include <stdio.h>
#include <unistd.h>

int main() {
    long nprocs = sysconf(_SC_NPROCESSORS_ONLN);
    printf("Number of CPUs: %ld\n", nprocs);
    
    long pagesize = sysconf(_SC_PAGESIZE);
    printf("Page size: %ld bytes\n", pagesize);
    
    return 0;
}
```



---



## 🛠️ Nützliche System-Tools



### `strace` – Systemaufrufe beobachten

```bash
# Alle Syscalls eines Programms anzeigen
strace ls

# Nur bestimmte Syscalls anzeigen
strace -e trace=open,read,write ls

# Statistik über Syscalls
strace -c ls

# Syscalls mit Zeitstempeln
strace -t ls

# Syscalls in eine Datei umleiten
strace -o output.txt ls
```



### `ltrace` – Bibliotheksaufrufe beobachten

```bash
# Bibliotheksaufrufe anzeigen
ltrace ls

# Nur bestimmte Funktionen anzeigen
ltrace -e malloc,free ls
```



### `lsof` – Geöffnete Dateien anzeigen

```bash
# Alle geöffneten Dateien anzeigen
lsof

# Geöffnete Dateien eines Prozesses
lsof -p <PID>

# Netzwerkverbindungen
lsof -i
```



### `ps` – Prozessliste

```bash
# Alle Prozesse anzeigen
ps aux

# Prozesse nach Name filtern
ps aux | grep nginx

# Prozessbaum
pstree
```



### `top` / `htop` – Systemmonitor

```bash
# Echtzeit-Prozessmonitor
top

# Verbesserte Version
htop
```



### `vmstat` – Virtueller Speicher

```bash
# Speichernutzung anzeigen
vmstat

# Mit Intervall
vmstat 1
```



### `dmesg` – Kernel-Meldungen

```bash
# Kernel-Meldungen anzeigen
dmesg

# Nur letzte Meldungen
dmesg | tail

# Echtzeit-Meldungen
dmesg -w
```



---



## 🎯 Best Practices



### 1. Fehlerbehandlung

- **Immer Rückgabewerte prüfen** (Syscalls können fehlschlagen)
- **errno nutzen** für detaillierte Fehlinformationen
- **`perror()`** für einfache Fehlermeldungen

**Beispiel:**
```c
int fd = open("file.txt", O_RDONLY);
if (fd < 0) {
    perror("open failed");  // Zeigt: "open failed: No such file or directory"
    return 1;
}
```



### 2. Ressourcen freigeben

- **Immer Datei-Deskriptoren schließen** (`close()`)
- **Speicher freigeben** (`free()`, `munmap()`)
- **Kindprozesse warten** (`wait()` / `waitpid()`)

**Beispiel:**
```c
int fd = open("file.txt", O_RDONLY);
if (fd < 0) { /* error */ }

// Datei verwenden...

close(fd);  // WICHTIG: Immer schließen!
```



### 3. Buffer-Overflows vermeiden

- **Immer Puffergrößen prüfen**
- **`strncpy()` statt `strcpy()`** verwenden
- **`snprintf()` statt `sprintf()`** verwenden

**Beispiel:**
```c
char buffer[1024];
// SICHER
snprintf(buffer, sizeof(buffer), "Hello, %s!", name);

// UNSICHER
sprintf(buffer, "Hello, %s!", name);  // Buffer Overflow möglich!
```



### 4. Thread-Safety

- **Globale Variablen vermeiden** in Mehrthread-Umgebungen
- **Mutexes nutzen** für geteilte Ressourcen
- **`pthread`-Funktionen** sind thread-sicher (z. B. `pthread_mutex_lock()`)



### 5. Portabilität

- **Nicht alle Syscalls sind auf allen Systemen verfügbar**
- **Architektur-spezifische Register** beachten (x86-64 vs. ARM vs. RISC-V)
- **Feature-Tests nutzen** (`#ifdef`)

**Beispiel:**
```c
#ifdef __linux__
    // Linux-spezifischer Code
    syscall(SYS_...);
#elif __APPLE__
    // macOS-spezifischer Code
    syscall(...);
#endif
```



---



## 📚 Lernressourcen



### Bücher

- **[Linux System Programming](https://www.amazon.com/Linux-System-Programming-Robert-Love/dp/1449339530)** – Robert Love
- **[The Linux Programming Interface](https://www.amazon.com/Linux-Programming-Interface-System-Handbook/dp/1593272200)** – Michael Kerrisk (DER Klassiker!)
- **[Linux Kernel Development](https://www.amazon.com/Linux-Kernel-Development-Robert-Love/dp/0672329468)** – Robert Love
- **[Understanding the Linux Kernel](https://www.amazon.com/Understanding-Linux-Kernel-Third-Daniel/dp/0596005652)** – Daniel P. Bovet, Marco Cesati



### Online-Dokumentation

- **[Linux man-pages](https://man7.org/linux/man-pages/)** – Offizielle Manual Pages
- **[Linux Syscall Reference](https://filippo.io/linux-syscall-table/)** – Syscall-Tabelle
- **[Linux Kernel Documentation](https://www.kernel.org/doc/html/latest/)** – Kernel-Doks
- **[POSIX Standard](https://pubs.opengroup.org/onlinepubs/9699919799/)** – POSIX-Spezifikation



### Videos

- **[Linux System Programming – LiveOverflow](https://www.youtube.com/c/LiveOverflow)** – Syscalls & Systemprogrammierung
- **[The Linux Kernel – Linux Foundation](https://www.youtube.com/watch?v=0CpSxQWt7W0)** – Kernel-Interna
- **[Writing a Simple OS from Scratch](https://www.youtube.com/watch?v=26QPDBe-NB8)** – OS-Entwicklung



### Online-Kurse

- **[Linux System Programming (Udemy)](https://www.udemy.com/course/linux-system-programming/)** – Praktische Einführung
- **[Operating Systems: Three Easy Pieces](https://pages.cs.wisc.edu/~remzi/OSTEP/)** – Kostenloses Online-Buch



### Tools

- **[strace](https://strace.io/)** – Syscall-Tracing
- **[ltrace](http://www.ltrace.org/)** – Bibliotheksaufruf-Tracing
- **[gdb](https://www.gnu.org/software/gdb/)** – Debugger
- **[Valgrind](https://valgrind.org/)** – Memory-Error-Detection
- **[perf](https://perf.wiki.kernel.org/)** – Performance-Analyse



---



## 🔗 Verwandte Themen



- [Assembler](assembler.md) – Direkte CPU-Steuerung mit Syscalls
- [Compiler](compiler.md) – Wie Systemprogramme kompiliert werden
- [Rust, C++ & C Integration](rust-c-cpp-integration.md) – Sprachübergreifende Systemprogrammierung



---



## 🚀 Praxisprojekte



### 1. Einfacher HTTP-Server

**Ziel**: Ein minimaler HTTP-Server, der auf Port 8080 lauscht.

**C-Code:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netinet/in.h>

int main() {
    int server_fd = socket(AF_INET, SOCK_STREAM, 0);
    if (server_fd < 0) {
        perror("socket failed");
        exit(1);
    }
    
    struct sockaddr_in address;
    address.sin_family = AF_INET;
    address.sin_addr.s_addr = INADDR_ANY;
    address.sin_port = htons(8080);
    
    if (bind(server_fd, (struct sockaddr*)&address, sizeof(address)) < 0) {
        perror("bind failed");
        exit(1);
    }
    
    if (listen(server_fd, 3) < 0) {
        perror("listen failed");
        exit(1);
    }
    
    printf("Server listening on port 8080...\n");
    
    while (1) {
        int client_fd = accept(server_fd, NULL, NULL);
        if (client_fd < 0) {
            perror("accept failed");
            continue;
        }
        
        char* response = "HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\nHello, World!";
        write(client_fd, response, strlen(response));
        close(client_fd);
    }
    
    return 0;
}
```



### 2. Mini-Shell

**Ziel**: Eine einfache Shell, die Befehle ausführt.

**C-Code:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/wait.h>

#define MAX_LINE 1024

int main() {
    char line[MAX_LINE];
    
    while (1) {
        printf("$ ");
        fflush(stdout);
        
        if (!fgets(line, MAX_LINE, stdin)) {
            break;
        }
        
        // Newline entfernen
        line[strcspn(line, "\n")] = 0;
        
        if (strcmp(line, "exit") == 0) {
            break;
        }
        
        pid_t pid = fork();
        if (pid < 0) {
            perror("fork failed");
        } else if (pid == 0) {
            // Kindprozess: Befehl ausführen
            execlp("/bin/sh", "sh", "-c", line, NULL);
            perror("exec failed");
            exit(1);
        } else {
            // Elternprozess: Auf Kind warten
            wait(NULL);
        }
    }
    
    return 0;
}
```



### 3. Datei-Kopierprogramm

**Ziel**: Ein einfaches `cp`-Klon.

**C-Code:**
```c
#include <stdio.h>
#include <fcntl.h>
#include <unistd.h>
#include <sys/stat.h>

#define BUFFER_SIZE 4096

int main(int argc, char* argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <source> <destination>\n", argv[0]);
        return 1;
    }
    
    int src_fd = open(argv[1], O_RDONLY);
    if (src_fd < 0) {
        perror("open source failed");
        return 1;
    }
    
    struct stat st;
    if (fstat(src_fd, &st) < 0) {
        perror("fstat failed");
        close(src_fd);
        return 1;
    }
    
    int dst_fd = open(argv[2], O_WRONLY | O_CREAT | O_TRUNC, st.st_mode);
    if (dst_fd < 0) {
        perror("open destination failed");
        close(src_fd);
        return 1;
    }
    
    char buffer[BUFFER_SIZE];
    ssize_t bytes_read;
    
    while ((bytes_read = read(src_fd, buffer, BUFFER_SIZE)) > 0) {
        if (write(dst_fd, buffer, bytes_read) != bytes_read) {
            perror("write failed");
            close(src_fd);
            close(dst_fd);
            return 1;
        }
    }
    
    if (bytes_read < 0) {
        perror("read failed");
    }
    
    close(src_fd);
    close(dst_fd);
    return 0;
}
```



### 4. Netzwerk-Ping-Tool

**Ziel**: Ein einfaches Tool, das prüft, ob ein Host erreichbar ist.

**C-Code:**
```c
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/socket.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <netinet/in.h>

int main(int argc, char* argv[]) {
    if (argc != 3) {
        fprintf(stderr, "Usage: %s <host> <port>\n", argv[0]);
        return 1;
    }
    
    const char* host = argv[1];
    int port = atoi(argv[2]);
    
    struct sockaddr_in addr;
    memset(&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_port = htons(port);
    
    struct hostent* host_entry = gethostbyname(host);
    if (!host_entry) {
        herror("gethostbyname failed");
        return 1;
    }
    
    memcpy(&addr.sin_addr, host_entry->h_addr_list[0], host_entry->h_length);
    
    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd < 0) {
        perror("socket failed");
        return 1;
    }
    
    if (connect(sockfd, (struct sockaddr*)&addr, sizeof(addr)) < 0) {
        perror("connect failed");
        close(sockfd);
        return 1;
    }
    
    printf("Connected to %s:%d\n", host, port);
    close(sockfd);
    return 0;
}
```



---



*Letzte Aktualisierung: {{ git_revision_date_localized() }}*
