# ydotool: Praktische Anleitung für Linux-Automatisierung

Eine umfassende Schritt-für-Schritt-Anleitung für **ydotool** – das mächtige CLI-Tool zur Low-Level-Automatisierung von Tastatur und Maus auf Linux (Wayland und X11).

---

## 🎯 Einführung: Was ist ydotool?

**ydotool** ist ein modernes, plattformunabhängiges CLI-Tool zur Simulation von Tastatur- und Mausereignissen auf Linux. Es kommuniziert direkt mit dem Kernel-Modul `uinput` und funktioniert sowohl unter **Wayland** als auch unter **X11**.

### Hauptmerkmale

| Funktion | Beschreibung | Vorteile |
|----------|--------------|----------|
| **Tastatursimulation** | Einzelne Tasten und Tastenkombinationen senden | Keine GUI erforderlich |
| **Maussteuerung** | Mausbewegungen, Klicks, Scrollen | Präzise Kontrolle |
| **Wayland-Kompatibel** | Funktioniert unter modernen Wayland-Compositors | Zukunftssicher |
| **X11-Kompatibel** | Funktioniert auch unter X11 | Rückwärtskompatibel |
| **Headless-Modus** | Funktioniert ohne grafische Oberfläche | Ideal für Server/Docker |
| **Skriptbar** | Einfache Integration in Shell-Skripte | Automatisierungsfreundlich |
| **Schnell** | Minimale Latenz | Echtzeitfähig |

### Vergleich: ydotool vs. xdotool vs. PyAutoGUI

| Tool | Wayland | X11 | CLI | Python | Multi-Plattform | Low-Level |
|------|--------|-----|-----|--------|----------------|-----------|
| **ydotool** | ✅ Ja | ✅ Ja | ✅ Ja | ❌ Nein | ❌ Linux nur | ✅ Ja |
| **xdotool** | ❌ Nein | ✅ Ja | ✅ Ja | ❌ Nein | ❌ Linux nur | ❌ Nein |
| **PyAutoGUI** | ⚠️ Eingeschränkt | ✅ Ja | ❌ Nein | ✅ Ja | ✅ Ja | ❌ Nein |
| **evdev** | ✅ Ja | ✅ Ja | ❌ Nein | ✅ Ja | ❌ Linux nur | ✅ Ja |

### Einsatzbereiche

| Anwendung | Beschreibung |
|-----------|--------------|
| **Server-Automatisierung** | Automatisierung in Headless-Umgebungen |
| **Docker-Container** | GUI-Automatisierung in Containern |
| **Wayland-Anwendungen** | Automatisierung moderner Linux-Apps |
| **Testautomatisierung** | Low-Level-Tests für Linux-Anwendungen |
| **CI/CD-Pipelines** | Automatisierung in Build-Prozessen |
| **Barrierefreiheit** | Alternative Eingabemethoden |
| **Remote-Administration** | Automatisierung auf Remote-Servern |

---

## 📥 Installation

### Ubuntu/Debian

```bash
# Abhängigkeiten installieren
sudo apt update
sudo apt install -y git cmake build-essential libevdev2 libevdev-dev \
    libudev-dev libinput-dev python3-pip

# Repository klonen
git clone https://github.com/ReimuNotMoe/ydotool.git
cd ydotool

# Kompilieren
mkdir build
cd build
cmake ..
make

# Installieren
sudo make install
sudo ldconfig

# ydotool sollte jetzt verfügbar sein
ydotool --version
```

### Arch Linux

```bash
# Aus AUR installieren
yay -S ydotool-git

# Oder manuell
git clone https://github.com/ReimuNotMoe/ydotool.git
cd ydotool
mkdir build && cd build
cmake ..
make
sudo make install
```

### Fedora/RHEL

```bash
sudo dnf install -y git cmake gcc-c++ make python3-devel \
    libevdev-devel libudev-devel libinput-devel

git clone https://github.com/ReimuNotMoe/ydotool.git
cd ydotool
mkdir build && cd build
cmake ..
make
sudo make install
```

### Docker

```dockerfile
# Dockerfile für ydotool
FROM ubuntu:22.04

RUN apt update && apt install -y git cmake build-essential \
    libevdev2 libevdev-dev libudev-dev libinput-dev && \
    rm -rf /var/lib/apt/lists/*

RUN git clone https://github.com/ReimuNotMoe/ydotool.git /tmp/ydotool && \
    cd /tmp/ydotool && \
    mkdir build && cd build && \
    cmake .. && \
    make && \
    make install && \
    rm -rf /tmp/ydotool

# Einfache Test-Befehle
CMD ["/bin/bash"]
```

### Installation überprüfen

```bash
# Version prüfen
ydotool --version

# Hilfe anzeigen
ydotool --help

# Alle Befehle auflisten
ydotool --help-commands
```

---

## 🎯 Grundlagen: Befehle und Syntax

### Befehlsstruktur

```
ydotool <command> [options] [arguments]
```

### Hauptbefehle

| Befehl | Beschreibung |
|--------|--------------|
| `key` | Taste drücken |
| `type` | Text eingeben |
| `click` | Maus klicken |
| `mousemove` | Maus bewegen |
| `scroll` | Mausrad scrollen |
| `delay` | Verzögerung einbauen |
| `mouse` | Maus-Status anzeigen |
| `exec` | Mehrere Befehle ausführen |
| `version` | Version anzeigen |

---

## ⌨️ Tastatursteuerung

### Einzelne Tasten drücken

#### Syntax
```
ydotool key [options] <keys>
```

#### Beispiele
```bash
# Einzelne Taste drücken (Taste wird gedrückt und losgelassen)
ydotool key a

# Mehrere Tasten gleichzeitig (Modifikator + Taste)
ydotool key ctrl+c

# Mehrere Tastenkombinationen
ydotool key alt+tab

# Funktionstasten
ydotool key F1
ydotool key F12

# Navigationstasten
ydotool key Up
ydotool key Down
ydotool key Left
ydotool key Right

# Sondertasten
ydotool key Enter
ydotool key Space
ydotool key BackSpace
ydotool key Delete
ydotool key Tab

# Zahlen
ydotool key 1
ydotool key 2
```

### Tasten gedrückt halten

```bash
# Taste drücken und halten (mit delay oder anderen Befehlen kombinieren)
ydotool key --key-press-delay 1000 a  # a für 1 Sekunde halten

# Besser: Mit separaten key-Befehlen
ydotool key --down a  # a drücken
ydotool delay 1000      # 1 Sekunde warten
ydotool key --up a     # a loslassen
```

### Text eingeben

#### Syntax
```
ydotool type [options] <text>
```

#### Beispiele
```bash
# Text eingeben (langsam, wie ein Mensch)
ydotool type "Hallo Welt"

# Text mit Verzögerung zwischen den Zeichen
ydotool type --delay 100 "Langsamer Text"  # 100ms zwischen Zeichen

# Text mit speziellen Zeichen
ydotool type "Benutzername: admin@beispiel.de"

# Mehrzeiliger Text
ydotool type "Erste Zeile\nZweite Zeile"
```

#### Optionen für `type`

| Option | Beschreibung | Standard |
|--------|--------------|----------|
| `--delay <ms>` | Verzögerung zwischen Zeichen in Millisekunden | 10 |
| `--key-press-delay <ms>` | Verzögerung beim Drücken einer Taste | 10 |
| `--key-release-delay <ms>` | Verzögerung beim Loslassen einer Taste | 10 |

### Unterstützte Tasten

| Kategorie | Beispiele |
|-----------|-----------|
| **Buchstaben** | `a`, `b`, `c`, ... `z`, `A`, `B`, ... `Z` |
| **Zahlen** | `1`, `2`, ... `0` |
| **Funktionstasten** | `F1`, `F2`, ... `F12` |
| **Navigation** | `Up`, `Down`, `Left`, `Right`, `PageUp`, `PageDown`, `Home`, `End` |
| **Sondertasten** | `Enter`, `Space`, `BackSpace`, `Delete`, `Tab`, `Escape` |
| **Modifikatoren** | `Shift`, `Ctrl`, `Alt`, `Super` (Windows-Taste) |
| **Numerisches Tastenfeld** | `KP_1`, `KP_2`, ... `KP_0`, `KP_Enter` |

### Tastenkombinationen

```bash
# Strg+C (Kopieren)
ydotool key ctrl+c

# Strg+V (Einfügen)
ydotool key ctrl+v

# Alt+Tab (Fenster wechseln)
ydotool key alt+tab

# Strg+Alt+T (Terminal öffnen)
ydotool key ctrl+alt+t

# Strg+Shift+Esc (Task-Manager)
ydotool key ctrl+shift+esc
```

---

## 🖱️ Maussteuerung

### Mausposition abfragen

```bash
# Aktuelle Mausposition anzeigen
ydotool mouse

# Ausgabe: x:100 y:200
```

### Maus bewegen

#### Syntax
```
ydotool mousemove [options] <coordinates>
```

#### Beispiele
```bash
# Maus zu absoluter Position bewegen
ydotool mousemove 100 200

# Maus relativ zur aktuellen Position bewegen
ydotool mousemove --relative 50 50

# Maus mit einer bestimmten Geschwindigkeit bewegen
ydotool mousemove --speed 100 100 200  # 100 Pixel pro Sekunde

# Maus mit Beschleunigung bewegen
ydotool mousemove --accel 2 --speed 200 100 200
```

#### Optionen für `mousemove`

| Option | Beschreibung | Standard |
|--------|--------------|----------|
| `--x <x>` | X-Koordinate | Erfordert |
| `--y <y>` | Y-Koordinate | Erfordert |
| `--relative` | Relative Bewegung | Absolute |
| `--speed <px/s>` | Geschwindigkeit in Pixel pro Sekunde | 1200 |
| `--accel <factor>` | Beschleunigungsfaktor | 1.0 |
| `--polar` | Polarkoordinaten verwenden | Kartesisch |

### Maus klicken

#### Syntax
```
ydotool click [options] <button>
```

#### Beispiele
```bash
# Links-Klick
ydotool click 0

# Rechts-Klick
ydotool click 2

# Mittlerer Mausknopf (Rad)
ydotool click 1

# Klick an bestimmter Position
ydotool mousemove 100 200
ydotool click 0

# Doppeltklick
ydotool click 0
ydotool delay 100
ydotool click 0

# Klick und halten (Drag & Drop)
ydotool mousemove 100 100
ydotool click --down 0
ydotool mousemove 200 200
ydotool delay 500
ydotool click --up 0
```

#### Mausknopf-Nummern

| Knopf | Nummer | Beschreibung |
|-------|--------|--------------|
| Left | 0 | Linker Mausknopf |
| Right | 2 | Rechter Mausknopf |
| Middle | 1 | Mittlerer Mausknopf (Rad) |
| Side | 3 | Seitlicher Mausknopf |
| Extra | 4 | Zusätzlicher Mausknopf |

#### Optionen für `click`

| Option | Beschreibung |
|--------|--------------|
| `--down` | Taste drücken (ohne Loslassen) |
| `--up` | Taste loslassen |
| `--button <n>` | Mausknopf (0=Links, 1=Mitte, 2=Rechts) |

### Mausrad scrollen

#### Syntax
```
ydotool scroll [options] <delta>
```

#### Beispiele
```bash
# Nach oben scrollen (positiv = hoch)
ydotool scroll 5

# Nach unten scrollen (negativ = runter)
ydotool scroll -5

# Eine Seite nach unten scrollen
ydotool scroll --page -1

# Eine Seite nach oben scrollen
ydotool scroll --page 1
```

---

## ⏱️ Zeitsteuerung

### Verzögerungen einbauen

```bash
# 1 Sekunde warten
ydotool delay 1000

# 500 Millisekunden warten
ydotool delay 500

# In Skripten
ydotool key a
ydotool delay 100
ydotool key b
```

---

## 🎬 Mehrere Befehle ausführen

### Skript-Datei erstellen

```bash
# Skript-Datei erstellen (z.B. script.ydo)
cat > script.ydo << 'EOF'
# Kommentare mit #
# Jeder Befehl in einer neuen Zeile

# Text eingeben und Enter drücken
type "Hallo Welt"
delay 100
key Enter

# Maus bewegen und klicken
mousemove 100 200
click 0

# Warten
delay 500

# Tastenkombination
key ctrl+s
EOF

# Skript ausführen
ydotool exec script.ydo
```

### Inline-Skript ausführen

```bash
# Mehrere Befehle in einem Aufruf
ydotool exec -q "type 'Test'\nkey Enter\ndelay 200\nclick 0"

# Mit echo und Pipe
echo -e "type 'Hallo'\nkey Enter" | ydotool exec -
```

### Skript mit Variablen

```bash
#!/bin/bash

# Text aus Variable
TEXT="Hallo aus Bash"
X=100
Y=200

# Skript zusammenbauen
cat > /tmp/script.ydo << EOF
type "$TEXT"
delay 100
mousemove $X $Y
click 0
EOF

# Ausführen
ydotool exec /tmp/script.ydo

# Aufräumen
rm /tmp/script.ydo
```

---

## 🎯 Praktische Anwendungsbeispiele

### Beispiel 1: Automatisierte Formularausfüllung

```bash
#!/bin/bash

# Daten
type "Max Mustermann"
ydotool delay 100
ydotool key Tab

type "max@beispiel.de"
ydotool delay 100
ydotool key Tab

type "Meine Straße 123"
ydotool delay 100
ydotool key Tab

type "12345 Berlin"
ydotool delay 100
ydotool key Tab

# Submit-Button klicken (Position anpassen)
ydotool mousemove 500 300
ydotool click 0
```

### Beispiel 2: Terminal-Befehle ausführen

```bash
#!/bin/bash

# Terminal öffnen (Strg+Alt+T)
ydotool key ctrl+alt+t
ydotool delay 500

# Befehl eingeben
type "ls -la"
ydotool delay 100
ydotool key Enter

# Warten
ydotool delay 1000

# Terminal schließen (Strg+Shift+W)
ydotool key ctrl+shift+w
```

### Beispiel 3: Screenshot mit Skript

```bash
#!/bin/bash

# Fenster wechseln (Alt+Tab)
ydotool key alt+tab
ydotool delay 200

# Print Screen drücken
ydotool key Print

# Bild in Clipboard kopiert
# Mit xclip oder ähnlichem speichern
```

### Beispiel 4: Automatisierte Dateioperationen

```bash
#!/bin/bash

# Datei-Manager öffnen (Super+E = Windows-Taste+E)
ydotool key super+e
ydotool delay 1000

# Zu Verzeichnis navigieren
type "/home/benutzer/Dokumente"
ydotool delay 500
ydotool key Enter

ydotool delay 1000

# Neue Datei erstellen (F10 für Menü, dann N, T)
ydotool key F10
ydotool delay 300
ydotool key N
ydotool delay 300
ydotool key T
ydotool delay 300

# Dateiname eingeben
type "neue_datei.txt"
ydotool delay 100
ydotool key Enter
```

---

## 🔧 Fortgeschrittene Techniken

### Mauspositionen programmisch ermitteln

```bash
#!/bin/bash

# Aktuelle Mausposition speichern
ydotool mouse > /tmp/mouse_pos.txt

# Position auslesen
POSITION=$(cat /tmp/mouse_pos.txt)
X=$(echo $POSITION | grep -oP 'x:\K[0-9]+')
Y=$(echo $POSITION | grep -oP 'y:\K[0-9]+')

echo "Aktuelle Position: X=$X, Y=$Y"

# An dieser Position klicken
ydotool mousemove $X $Y
ydotool click 0

# Aufräumen
rm /tmp/mouse_pos.txt
```

### Tastenkombinationen mit Verzögerung

```bash
#!/bin/bash

# Strg+Alt+Del mit Verzögerung
ydotool key --down ctrl
ydotool key --down alt
ydotool key --down del
ydotool delay 100
ydotool key --up del
ydotool key --up alt
ydotool key --up ctrl
```

### Schleifen und Bedingungen

```bash
#!/bin/bash

# 10 Mal die Leertaste drücken
for i in {1..10}; do
    ydotool key Space
    ydotool delay 100
done

# Bis eine Bedingung erfüllt ist (vereinfacht)
COUNT=0
while [ $COUNT -lt 5 ]; do
    ydotool key F5  # Seite neu laden
    ydotool delay 2000
    ((COUNT++))
done
```

### Kombination mit anderen Tools

#### Mit xdotool (X11)

```bash
#!/bin/bash

# Fenster-ID finden
WINDOW_ID=$(xdotool search --name "Terminal" | head -1)

# Fenster fokussieren
xdotool windowactivate $WINDOW_ID

# ydotool-Befehle ausführen
ydotool type "Hallo von ydotool"
ydotool key Enter
```

#### Mit xprop (Fenster-Informationen)

```bash
#!/bin/bash

# Aktives Fenster finden
ACTIVE_WINDOW=$(xdotool getactivewindow)

# Fensterinformationen abfragen
WINDOW_NAME=$(xprop -id $ACTIVE_WINDOW WM_NAME | cut -d'"' -f2)

if [ "$WINDOW_NAME" = "Terminal" ]; then
    ydotool type "Im Terminal"
else
    ydotool type "Nicht im Terminal"
fi

ydotool key Enter
```

### Logdateien erstellen

```bash
#!/bin/bash

# Logdatei
LOG_FILE="/tmp/ydotool.log"

# Funktion zum Loggen
log() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1" >> $LOG_FILE
}

log "Starte Automatisierung"

# Befehle ausführen
ydotool type "Test"
log "Text eingegeben"

ydotool key Enter
log "Enter gedrückt"

ydotool mousemove 100 200
log "Maus bewegt"

ydotool click 0
log "Geklickt"

log "Automatisierung abgeschlossen"
```

---

## 🛡️ Fehlerbehandlung

### Häufige Probleme und Lösungen

#### Problem: Berechtigungen

```bash
# Fehler: "Could not open uinput device"
# Lösung: Benutzer zur uinput-Gruppe hinzufügen

sudo usermod -aG input $USER
sudo usermod -aG uinput $USER

# Abmelden und neu anmelden oder Reboot
# Alternativ:
sudo su - $USER -c "ydotool key a"
```

#### Problem: Wayland-Probleme

```bash
# Unter Wayland funktioniert ydotool normalerweise
# Falls nicht:

# Prüfen ob Wayland verwendet wird
echo $XDG_SESSION_TYPE

# Falls X11 erzwingen
# In ~/.xprofile oder ~/.xinitrc
# export XDG_SESSION_TYPE=x11

# Oder bei Login Wayland deaktivieren
```

#### Problem: Keine Reaktion

```bash
# Mögliche Ursachen:
# 1. Falsche Tastencodes (Groß-/Kleinschreibung beachten)
# 2. Zu schnelle Ausführung (delay hinzufügen)
# 3. Fokus nicht auf dem richtigen Fenster

# Lösung: Fokus prüfen
ydotool mouse
# Manuell testen
ydotool key a
ydotool delay 1000
ydotool key b
```

#### Problem: Tastatur-Layout

```bash
# ydotool verwendet das US-Tastaturlayout
# Für andere Layouts müssen die Tastencodes angepasst werden

# Beispiel: Auf DE-Layout ist 'z' und 'y' vertauscht
# US 'z' = DE 'y'
# US 'y' = DE 'z'

# Lösung: Tastatur-Layout in Systemeinstellungen prüfen
# Oder Tastencodes manuell anpassen
```

---

## 📊 Performance-Optimierung

### Tipps für effiziente Skripte

1. **Minimale Verzögerungen verwenden**
   ```bash
   # Statt festen Verzögerungen
   ydotool delay 1000  # 1 Sekunde
   
   # Besser: Nur dort warten, wo nötig
   ydotool type "Text"  # Standardmäßig 10ms zwischen Zeichen
   ydotool key Enter
   ydotool delay 200    # Nur nach kritischen Aktionen
   ```

2. **Befehle gruppieren**
   ```bash
   # Schlecht: Einzelne Befehle
   ydotool mousemove 100 200
   ydotool delay 100
   ydotool click 0
   
   # Besser: In einem Skript
   ydotool exec -q "mousemove 100 200\nclick 0"
   ```

3. **Relative Bewegungen verwenden**
   ```bash
   # Absolute Positionen sind auflösungsabhängig
   ydotool mousemove 1920 1080
   
   # Relative Bewegungen sind portabler
   ydotool mousemove --relative 0 100  # 100px nach unten
   ```

4. **Skripte vorab testen**
   ```bash
   # Einzelne Befehle testen
ydotool key a
   ydotool mousemove 100 100
   
   # Erst dann komplexe Skripte erstellen
   ```

---

## 🎯 Praxisprojekte

### Projekt 1: Automatisiertes Login-Skript

**Ziel:** Automatisches Einloggen in ein Terminal oder eine Anwendung.

```bash
#!/bin/bash

# Benutzerdaten
USERNAME="mein_benutzername"
PASSWORD="mein_passwort"

# Terminal öffnen (falls noch nicht offen)
ydotool key ctrl+alt+t
ydotool delay 500

# Benutzername eingeben
type "$USERNAME"
ydotool delay 100
ydotool key Enter

# Warten auf Passwort-Prompt
ydotool delay 500

# Passwort eingeben (wird nicht angezeigt)
type "$PASSWORD"
ydotool delay 100
ydotool key Enter

# Warten auf erfolgreichen Login
ydotool delay 2000

echo "Login abgeschlossen"
```

### Projekt 2: Automatisierte Bildschirmaufnahme

```bash
#!/bin/bash

# Abhängigkeiten: ffmpeg, xdotool (für Fokus)

# Fokus auf Fenster setzen
WINDOW_ID=$(xdotool getactivewindow)

# Zeitstempel für Dateiname
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
OUTPUT="recording_$TIMESTAMP.mp4"

# Aufnahme starten (mit ffmpeg)
# Tastendruck registrieren
echo "Aufnahme gestartet. Drücke q zum Beenden."

# Fenster fokussieren
xdotool windowactivate $WINDOW_ID

# ydotool für Tastendruck verwenden
# q drücken um Aufnahme zu beenden
# Dies erfordert ein separater Prozess oder Hotkey

# Einfacher: Zeitgesteuerte Aufnahme
DURATION=10  # Sekunden
ffmpeg -video_size 1920x1080 -framerate 30 -f x11grab -i :0.0 \
    -t $DURATION -c:v libx264 -pix_fmt yuv420p \
    $OUTPUT &

PID=$!

# Warten auf q-Taste
while true; do
    # Prüfen ob q gedrückt wurde (vereinfacht)
    # In einer echten Implementierung würde man hier ein Key-Listener verwenden
    sleep 0.1
    
    # Nach DURATION Sekunden beenden
    if [ $(echo "$(date +%s) - $START_TIME" | bc) -ge $DURATION ]; then
        break
    fi
done

# ffmpeg beenden
kill $PID

# Datei verschieben
mv output.mp4 $OUTPUT
echo "Aufnahme gespeichert: $OUTPUT"
```

### Projekt 3: Automatisiertes Testskript für GUI-Anwendung

```bash
#!/bin/bash

# Testskript für eine GUI-Anwendung
LOG_FILE="/tmp/test.log"

echo "Test gestartet: $(date)" > $LOG_FILE

# Anwendung starten (Annahme: bereits offen)
# Fenster fokussieren
ydotool key alt+tab
ydotool delay 500

# Test 1: Menü öffnen
echo "Test 1: Menü öffnen" >> $LOG_FILE
ydotool key F10
ydotool delay 300

# Test 2: Überprüfen ob Menü geöffnet
# (Visuelle Prüfung - in echten Tests mit anderen Tools kombinieren)
ydotool key Escape
ydotool delay 200

# Test 3: Tastenkombination testen
echo "Test 2: Tastenkombination" >> $LOG_FILE
ydotool key ctrl+n
ydotool delay 500
ydotool key ctrl+w
ydotool delay 200

# Test 4: Texteingabe
echo "Test 3: Texteingabe" >> $LOG_FILE
type "Testtext 123"
ydotool delay 100
ydotool key BackSpace
ydotool key BackSpace
ydotool key BackSpace
ydotool delay 100

# Test 5: Mausoperationen
echo "Test 4: Mausoperationen" >> $LOG_FILE
ydotool mousemove 100 100
ydotool delay 100
ydotool click 0
ydotool delay 100
ydotool mousemove 200 200
ydotool click 2  # Rechtsklick

# Test abgeschlossen
echo "Alle Tests abgeschlossen: $(date)" >> $LOG_FILE
echo "Ergebnisse in $LOG_FILE gespeichert"
```

### Projekt 4: Automatisierte Datenverarbeitung

```bash
#!/bin/bash

# Automatisierte Verarbeitung von Dateien
INPUT_DIR="/home/benutzer/Input"
OUTPUT_DIR="/home/benutzer/Output"

echo "Starte Datenverarbeitung..."

# Datei-Manager öffnen
ydotool key super+e
ydotool delay 1000

# Zu Input-Verzeichnis navigieren
type "$INPUT_DIR"
ydotool delay 500
ydotool key Enter
ydotool delay 1000

# Alle Dateien auswählen
ydotool key ctrl+a
ydotool delay 300

# Kopieren
ydotool key ctrl+c
ydotool delay 300

# Zu Output-Verzeichnis navigieren
ydotool key ctrl+l
ydotool delay 200
type "$OUTPUT_DIR"
ydotool delay 500
ydotool key Enter
ydotool delay 1000

# Einfügen
ydotool key ctrl+v
ydotool delay 500

# Bestätigen (je nach Datei-Manager)
ydotool key Enter

echo "Datenverarbeitung abgeschlossen"
```

---

## 📚 Ressourcen und weiterführende Links

### Offizielle Dokumentation
- [ydotool GitHub](https://github.com/ReimuNotMoe/ydotool)
- [README & Documentation](https://github.com/ReimuNotMoe/ydotool/blob/master/README.md)
- [Releases](https://github.com/ReimuNotMoe/ydotool/releases)

### Ähnliche Tools
| Tool | Beschreibung | Wayland | X11 |
|------|--------------|--------|-----|
| **ydotool** | Modernes CLI-Tool für Tastatur/Maus | ✅ Ja | ✅ Ja |
| **xdotool** | Klassisches X11-Tool | ❌ Nein | ✅ Ja |
| **evdev** | Low-Level Input-Device Handling | ✅ Ja | ✅ Ja |
| **uinput** | Kernel-Level Input | ✅ Ja | ✅ Ja |
| **input-leap** | Tastatur/Maus über Netzwerk teilen | ✅ Ja | ✅ Ja |

### Community Ressourcen
- [Arch Linux Wiki - ydotool](https://wiki.archlinux.org/title/ydotool)
- [GitHub Issues](https://github.com/ReimuNotMoe/ydotool/issues)

---

## 🔗 Verwandte Themen

* [Desktop Automation/Übersicht](index.md) – Umfassende Übersicht über Desktop-Automatisierungstools
* [Desktop Automation mit PyAutoGUI](pyautogui-anleitung.md) – GUI-Automatisierung mit Python
* [Desktop Automation mit Playwright](playwright-anleitung.md) – Moderne Web-Automatisierung
* [Desktop Automation mit Robot Framework](robot-framework-anleitung.md) – Testautomatisierung mit Robot Framework
* [Beste lokale Computer-KI-Agenten (Allgemein, Top 20)](lokale-ki-agenten-topliste.md) – fertige Vision-Agenten als Alternative zum Eigenbau

---

*Letzte Aktualisierung: Juli 2026*
