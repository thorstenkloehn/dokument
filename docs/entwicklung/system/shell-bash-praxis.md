# Shell & Bash Scripting – Das Praxis-Handbuch

Die **Bash** (Bourne Again Shell) ist die Standard-Kommandozeile und Skriptsprache auf den meisten Linux- und Unix-Systemen. Sie dient als primäre Schnittstelle zur Automatisierung von Systemaufgaben, CI/CD-Pipelines, Server-Administration, Log-Analysen und Prozess-Orchestrierungen.

Dieses Handbuch bietet eine strukturierte Übersicht über Shell-Grundlagen, Ein- und Ausgabenumleitungen, Textverarbeitung mit `grep`/`awk`/`sed`, Datentypen, Arrays, Kontrollstrukturen, defensive Fehlerbehandlung (`set -euo pipefail`), `trap`-Signale, Cron-Jobs und `shellcheck`.

---

## 🚀 1. Shell-Grundlagen & Befehlsstruktur

### Was ist die Shell?
Die **Shell** ist ein Befehlszeilen-Interpreter, der Benutzereingaben entgegennimmt und als Betriebssystem-Befehle ausführt.

```mermaid
graph LR
    User(["Entwickler / CI Pipeline"]) -->|Befehl / Script| Shell["Bash Shell Interpreter"]
    Shell -->|1. Expansion & Parsing| Parser["Command Parser"]
    Parser -->|2. System Calls| Kernel["Linux Kernel"]
    Kernel -->|3. Output / Streams| Terminal["stdout / stderr"]
```

### Beliebte Shells im Vergleich
* **Bash (`/bin/bash`)**: Der weltweite De-facto Standard auf Linux-Servern.
* **Zsh (`/bin/zsh`)**: Standard-Shell auf macOS; bietet erweiterte Autovervollständigung und Themes (Oh My Zsh).
* **Dash (`/bin/dash`)**: Extrem schnelle, POSIX-konforme Shell (wird in Ubuntu für System-Skripte `/bin/sh` genutzt).
* **Fish (`/usr/bin/fish`)**: Benutzerfreundliche interaktive Shell mit nativer Auto-Suggestion.

---

## 🔀 2. I/O-Redirection, Streams & Pipelines

### Die 3 Standard-Streams
Jeder Linux-Prozess besitzt drei vorgegebene I/O-Kanäle:

| Stream | Dateideskriptor (FD) | Beschreibung | Standard-Ziel |
|---|---|---|---|
| `stdin` | `0` | Standard-Eingabe (Keyboard / Input) | Tastatur |
| `stdout` | `1` | Standard-Ausgabe (Normale Ergebnisse) | Terminal-Bildschirm |
| `stderr` | `2` | Standard-Fehlerausgabe (Fehlermeldungen) | Terminal-Bildschirm |

### Umleitungen & Piping (`|`)

```bash
# Output Umleitung (Überschreiben > vs. Anfügen >>)
echo "Zeile 1" > datei.txt
echo "Zeile 2" >> datei.txt

# Fehlerbehandlung: stderr separat umleiten oder mit stdout zusammenführen
command_with_error 2> error.log
command_with_error > output.log 2>&1  # stderr & stdout in selbe Datei
command_with_error &> output.log     # Moderne Bash-Kurzform

# Process Substitution: Erzeugt eine temporäre FIFO-Datei für Befehlsausgaben
diff -u <(ls /folder1) <(ls /folder2)
```

---

## ✍️ 3. Variablen, Datentypen & String-Manipulation

### Variablen & Gültigkeitsbereiche

```bash
#!/bin/bash

# Definition (KEINE Leerzeichen um das '=' erlaubt!)
NACHRICHT="Hello World"
declare -i ZAHLER=42         # Typsicheres Integer
declare -r KONSTANTE="FIXED" # Read-Only Variable

# Umgebungsvariable für Kindprozesse exportieren
export DB_HOST="localhost"

# Spezialvariablen
echo "Skriptname: $0"
echo "Anzahl Argumente: $#"
echo "Alle Argumente: $@"
echo "Exit-Code des letzten Befehls: $?"
echo "Prozess-ID (PID) des Skripts: $$"
```

### Arrays & Assoziative Arrays (Key-Value)

=== "Indizierte Arrays"
    ```bash
    # Indiziertes Array definieren
    FRUCHTE=("Apfel" "Banane" "Kirsche")

    # Elemente hinzufügen & auslesen
    FRUCHTE+=("Orange")
    echo "Erstes Element: ${FRUCHTE[0]}"
    echo "Alle Elemente: ${FRUCHTE[@]}"
    echo "Anzahl Elemente: ${#FRUCHTE[@]}"
    ```

=== "Assoziative Arrays (Hashes)"
    ```bash
    # Deklaration zwingend erforderlich!
    declare -A SERVERE_IPS

    SERVERE_IPS=(
        ["web01"]="192.168.1.10"
        ["db01"]="192.168.1.20"
    )

    echo "IP von db01: ${SERVERE_IPS["db01"]}"
    ```

### String-Manipulationen ohne externe Tools

| Operation | Syntax | Ergebnis (bei `STR="file.tar.gz"`) |
|---|---|---|
| String-Länge | `${#STR}` | `11` |
| Suffix entfernen | `${STR%.gz}` | `file.tar` |
| Gierig Suffix entfernen | `${STR%%.*}` | `file` |
| Prefix entfernen | `${STR#*.}` | `tar.gz` |
| Ersetzung (Erste) | `${STR/tar/zip}` | `file.zip.gz` |
| Großbuchstaben | `${STR^^}` | `FILE.TAR.GZ` |

---

## 🔀 4. Kontrollstrukturen & Operatoren

### Dateitests & Vergleiche

=== "Dateitests (`[ -f file ]`)"
    * `-f file`: Wahr, wenn die Datei existiert und eine **reguläre Datei** ist.
    * `-d dir`: Wahr, wenn das Verzeichnis existiert.
    * `-e path`: Wahr, wenn der Pfad existiert.
    * `-r` / `-w` / `-x`: Lesbar / Schreibbar / Ausführbar.

=== "Zahlen- & String-Vergleiche"
    ```bash
    NAME="Alice"
    AGE=25

    # String-Vergleich (doppelte eckige Klammern [[ ]] nutzen!)
    if [[ "$NAME" == "Alice" && -n "$NAME" ]]; then
        echo "Name passt und ist nicht leer."
    fi

    # Numerischer Vergleich (-eq, -ne, -lt, -gt, -le, -ge)
    if [[ "$AGE" -gt 18 ]]; then
        echo "Volljährig."
    fi
    ```

### Loops (Schleifen)

```bash
# For-Schleife über Elemente
for DATEI in *.log; do
    [[ -f "$DATEI" ]] || continue
    echo "Verarbeite $DATEI..."
done

# C-Style For-Schleife
for ((i=1; i<=5; i++)); do
    echo "Durchlauf $i"
done

# While-Schleife mit 'read' (Zeilenweises Einlesen einer Datei)
while IFS= read -r ZEILE; do
    echo "Zeile: $ZEILE"
done < config.txt
```

---

## 🛡️ 5. Defensives Scripting, Debugging & Signal Handling

!!! warning "Unbeabsichtigte Fehler verhindern"
    Standardmäßig läuft ein Bash-Skript weiter, selbst wenn ein Befehl fehlschlägt. Aktivieren Sie immer den **Strict Mode**!

### 1. Der Bash Strict Mode (`set -euo pipefail`)
Fügen Sie diesen Block am Anfang jedes Skripts ein:

```bash
#!/bin/bash
set -euo pipefail
IFS=$'\n\t'
```
* `set -e`: Bricht das Skript bei Fehler (Exit-Code != 0) sofort ab.
* `set -u`: Bricht ab, wenn eine undefinierte Variable aufgerufen wird.
* `set -o pipefail`: Der Exit-Code einer Pipeline entspricht dem letzten fehlerhaften Befehl.

### 2. Traps & Aufräumarbeiten bei Signalen (`trap`)
Mit `trap` können temporäre Dateien oder Sperren beim Abbrechen oder Beenden aufgeräumt werden:

```bash
TMP_DIR=$(mktemp -d)

# Aufräum-Funktion definieren
cleanup() {
    echo "Räume temporäre Dateien auf: $TMP_DIR"
    rm -rf "$TMP_DIR"
}

# Registrieren für EXIT, SIGINT (Ctrl+C) und SIGTERM
trap cleanup EXIT INT TERM
```

### 3. Debugging & Static Analysis
* `bash -n script.sh`: Prüft das Skript auf Syntax-Fehler ohne es auszuführen.
* `bash -x script.sh` / `set -x`: Gibt jede auszuführende Zeile mit aufgelösten Variablen im Terminal aus.
* **`shellcheck script.sh`**: Der Branchenstandard zur statischen Code-Analyse für Bash-Skripte.

---

## ⏰ 6. Automatisierung: Cron-Jobs & Systemd Timers

### Task-Scheduling mit `cron`

```bash
# Benutzer-Crontab bearbeiten
crontab -e

# Syntax: Minute Stunde Tag Monat Wochentag Befehl
# ┌───────────── Minute (0 - 59)
# │ ┌─────────── Stunde (0 - 23)
# │ │ ┌───────── Tag des Monats (1 - 31)
# │ │ │ ┌─────── Monat (1 - 12)
# │ │ │ │ ┌───── Wochentag (0 - 6) (Sonntag=0)
# * * * * * /path/to/script.sh

# Beispiel: Jeden Tag um 02:30 Uhr nachts ein Backup ausführen
30 2 * * * /usr/local/bin/backup.sh >> /var/log/backup.log 2>&1
```

---

## 🔗 7. Verwandte Themen & Weiterführende Links
* [Zurück zur Systemprogrammierungs-Übersicht](index.md)
* [Linux Praxis-Handbuch](linux-praxis.md)
* [Linux-Systemprogrammierung](linux-systemprogrammierung.md)
* [Systemd Service Creation](systemd-service-creation.md)
