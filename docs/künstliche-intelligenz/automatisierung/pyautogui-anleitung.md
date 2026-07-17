# PyAutoGUI: Praktische Anleitung zur Desktop-Automatisierung

Eine umfassende Schritt-für-Schritt-Anleitung für die Automatisierung von Desktop-Aufgaben mit PyAutoGUI – von der Installation über Grundlagen bis zu fortgeschrittenen Techniken und Best Practices.

---

## 🎯 Einführung: Was ist PyAutoGUI?

**PyAutoGUI** ist eine plattformübergreifende Python-Bibliothek zur Automatisierung von GUI-Interaktionen. Sie ermöglicht:

| Funktion | Beschreibung | Anwendungsbeispiel |
|----------|--------------|-------------------|
| **Maussteuerung** | Bewegen, Klicken, Ziehen | Automatisierte Formularausfüllung |
| **Tastatursteuerung** | Tasten drücken, Text eingeben | Automatisierte Texteingabe |
| **Bilderkennung** | Screenshots analysieren, Muster finden | Navigation durch Bildschirmelemente |
| **Bildschirmausgabe** | Screenshots erstellen | Visuelle Dokumentation |
| **Plattformübergreifend** | Windows, macOS, Linux | Ein Skript für alle Systeme |

### Vorteile von PyAutoGUI

| Vorteil | Beschreibung |
|---------|--------------|
| **Einfache API** | Intuitive Funktionen wie `click()`, `write()`, `press()` |
| **Keine Abhängigkeiten** | Funktioniert mit Standard-Python (außer für Screenshot-Funktionen) |
| **Plattformunabhängig** | Ein Code läuft auf Windows, macOS und Linux |
| **Bilderkennung** | Findet und klickt auf Bildschirmelemente basierend auf Bildern |
| **Fail-Safe** | Automatische Abbruchmöglichkeit durch Maus in die Ecke bewegen |
| **Dokumentation** | Ausgezeichnete offizielle Dokumentation |

### Nachteile und Einschränkungen

| Einschränkung | Beschreibung | Lösung |
|--------------|--------------|--------|
| **Kein Zugriff auf GUI-Elemente** | Arbeitet mit Koordinaten, nicht mit semantischen Elementen | Kombiniere mit anderen Tools |
| **Langsame Bilderkennung** | `locateOnScreen()` kann langsam sein | Bildgröße reduzieren, Graustufen verwenden |
| **Skalierungsprobleme** | Funktioniert nicht gut mit unterschiedlichen Auflösungen | Referenzauflösung festlegen |
| **Kein direkter Zugriff auf Fenster** | Kann nicht direkt Fenster steuern | Kombiniere mit `pygetwindow` |
| **Wayland-Probleme auf Linux** | Unter Wayland funktioniert Maussteuerung nicht immer | X11 verwenden oder `ydotool` |

---

## 📥 Installation

### Grundinstallation

```bash
# PyAutoGUI installieren
pip install pyautogui

# Für Screenshot-Funktionen (erforderlich auf Linux)
pip install pillow

# Für zusätzliche Funktionen
pip install opencv-python  # Für bessere Bilderkennung
```

### Plattformspezifische Anforderungen

#### Windows
```bash
# Keine zusätzlichen Abhängigkeiten erforderlich
pip install pyautogui
```

#### macOS
```bash
# PyObjC für bessere Integration
pip install pyobjc

# Berechtigungen für Barrierefreiheit erteilen
# Systemeinstellungen → Sicherheit → Datenschutz → Barrierefreiheit
# Terminal und Python hinzufügen
```

#### Linux (X11)
```bash
# Abhängigkeiten für Screenshots
sudo apt install -y python3-tk scrot

# Für Wayland (experimentell)
sudo apt install -y python3-xlib  # Für XWayland
```

### Installation überprüfen

```python
import pyautogui

# Version prüfen
print(f"PyAutoGUI Version: {pyautogui.__version__}")

# Bildschirmauflösung prüfen
print(f"Bildschirmgröße: {pyautogui.size()}")

# Aktuelle Mausposition
print(f"Aktuelle Mausposition: {pyautogui.position()}")
```

---

## 🖱️ Grundlagen: Maussteuerung

### Mausposition abfragen

```python
import pyautogui
import time

# Aktuelle Mausposition
x, y = pyautogui.position()
print(f"Aktuelle Position: X={x}, Y={y}")

# Mausposition für 5 Sekunden tracken
print("Bewege die Maus... (Strg+C zum Abbrechen)")
try:
    for _ in range(50):
        x, y = pyautogui.position()
        print(f"X={x}, Y={y}")
        time.sleep(0.1)
except KeyboardInterrupt:
    print("Abgebrochen")
```

### Maus bewegen

```python
import pyautogui
import time

# Maus zu absoluter Position bewegen (0,0 = obere linke Ecke)
pyautogui.moveTo(100, 100, duration=1.0)  # Bewegt sich in 1 Sekunde

# Maus relativ zur aktuellen Position bewegen
pyautogui.moveRel(50, 50, duration=0.5)  # 50px rechts, 50px runter

# Sofortige Bewegung (ohne Animation)
pyautogui.moveTo(200, 200, duration=0)  # Instantan
```

### Maus klicken

```python
import pyautogui
import time

# Einfacher Links-Klick
pyautogui.click(x=100, y=100)

# Rechtsklick
pyautogui.click(x=100, y=100, button='right')

# Doppeltklick
pyautogui.doubleClick(x=100, y=100)

# Klick und halten (Drag & Drop)
pyautogui.mouseDown(x=100, y=100, button='left')
time.sleep(0.5)  # Halten
pyautogui.mouseUp(x=200, y=200, button='left')  # Loslassen

# Klick an aktueller Mausposition
pyautogui.click()
```

### Mausklick-Optionen

| Parameter | Beschreibung | Standardwert |
|-----------|--------------|-------------|
| `x` | X-Koordinate | Erfordert |
| `y` | Y-Koordinate | Erfordert |
| `button` | Maustaste (`'left'`, `'right'`, `'middle'`) | `'left'` |
| `clicks` | Anzahl der Klicks | `1` |
| `interval` | Zeit zwischen Klicks (für `clicks > 1`) | `0.1` |
| `duration` | Dauer der Bewegung (Sekunden) | `0` (sofort) |

---

## ⌨️ Tastatursteuerung

### Einfache Texteingabe

```python
import pyautogui
import time

# Text eingeben (langsam, wie ein Mensch)
pyautogui.write('Hallo Welt!')

# Text mit Verzögerung
pyautogui.write('Langsamer Text', interval=0.25)  # 0.25s zwischen jedem Zeichen

# Text mit Tastenkombinationen
pyautogui.hotkey('ctrl', 'c')  # Strg+C kopieren
pyautogui.hotkey('ctrl', 'v')  # Strg+V einfügen
```

### Einzelne Tasten drücken

```python
import pyautogui

# Einzelne Taste drücken
pyautogui.press('enter')
pyautogui.press('space')
pyautogui.press('a')  # Buchstabe a

# Sondertasten
pyautogui.press('f1')
pyautogui.press('esc')
pyautogui.press('tab')
pyautogui.press('backspace')

# Tasten mit Modifikatoren
pyautogui.press('shift')
pyautogui.press('a')  # 'A' (Großbuchstabe)
```

### Unterstützte Tasten

| Tastenkategorie | Beispiele |
|----------------|-----------|
| **Buchstaben** | `'a'`, `'b'`, `'c'`, ... `'z'` |
| **Zahlen** | `'0'`, `'1'`, `'2'`, ... `'9'` |
| **Funktionstasten** | `'f1'`, `'f2'`, ... `'f12'` |
| **Navigation** | `'up'`, `'down'`, `'left'`, `'right'` |
| **Sondertasten** | `'enter'`, `'space'`, `'tab'`, `'backspace'`, `'delete'` |
| **Modifikatoren** | `'shift'`, `'ctrl'`, `'alt'`, `'win'`, `'command'` |
| **Numerisches Tastenfeld** | `'num0'`, `'num1'`, ... `'num9'`, `'numlock'` |

---

## 📷 Bilderkennung und Screenshots

### Screenshots erstellen

```python
import pyautogui

# Ganzer Bildschirm
screenshot = pyautogui.screenshot()
screenshot.save('ganzer_bildschirm.png')

# Region (x, y, breite, höhe)
region = pyautogui.screenshot(region=(100, 100, 300, 200))
region.save('region.png')

# Graustufen-Screenshot (schneller)
gray_screenshot = pyautogui.screenshot()
gray_screenshot = gray_screenshot.convert('L')
gray_screenshot.save('graustufen.png')
```

### Bilder auf dem Bildschirm finden

```python
import pyautogui

# Bild suchen und Position zurückgeben
button_location = pyautogui.locateOnScreen('button.png')
print(f"Button gefunden bei: {button_location}")

# Alle Vorkommen finden
all_locations = list(pyautogui.locateAllOnScreen('button.png'))
print(f"Gefunden {len(all_locations)} Vorkommen")

# Klick auf gefundenen Button
if button_location:
    button_center = pyautogui.center(button_location)
    pyautogui.click(button_center)
```

### Bilderkennung optimieren

```python
import pyautogui

# mit Toleranz (für ähnliche Farben)
location = pyautogui.locateOnScreen('button.png', confidence=0.8)
# confidence: 0.0 bis 1.0, wobei 1.0 exakte Übereinstimmung erfordert

# mit Graustufen (schneller)
gray_button = pyautogui.screenshot(region=(...))
gray_button = gray_button.convert('L')
gray_button.save('button_gray.png')
location = pyautogui.locateOnScreen('button_gray.png', grayscale=True)

# mit Region eingeschränkt (schneller)
location = pyautogui.locateOnScreen('button.png', region=(100, 100, 800, 600))
```

### Performance-Tipps für Bilderkennung

| Technik | Beschreibung | Geschwindigkeitsgewinn |
|---------|--------------|---------------------|
| **Kleinere Region** | Suche nur in relevantem Bereich | ✅✅✅✅ |
| **Graustufen** | Konvertiere zu Graustufen | ✅✅✅ |
| **Confidence anpassen** | niedrigere Genauigkeit | ✅✅ |
| **Bildgröße reduzieren** | Kleinere Referenzbilder | ✅✅ |
| **Vorverarbeitung** | Bilder vorverarbeiten | ✅ |

---

## 🎯 Praktische Anwendungsbeispiele

### Beispiel 1: Automatisierte Formularausfüllung

```python
import pyautogui
import time

# Warten bis das Formularfenster fokussiert ist
time.sleep(2)

# Namensfeld finden und ausfüllen
name_field = pyautogui.locateOnScreen('namensfeld.png')
if name_field:
    pyautogui.click(pyautogui.center(name_field))
    pyautogui.write('Max Mustermann')
    time.sleep(0.5)

# E-Mail-Feld
email_field = pyautogui.locateOnScreen('email_feld.png')
if email_field:
    pyautogui.click(pyautogui.center(email_field))
    pyautogui.write('max@beispiel.de')
    time.sleep(0.5)

# Submit-Button
submit_button = pyautogui.locateOnScreen('submit_button.png')
if submit_button:
    pyautogui.click(pyautogui.center(submit_button))
```

### Beispiel 2: Automatisierte Dateiübertragung

```python
import pyautogui
import time
import os

def datei_uebertragen(quelldatei, zieldatei):
    """Automatisierte Dateiübertragung mit Datei-Explorer."""
    
    # Datei-Explorer öffnen (Win+E)
    pyautogui.hotkey('win', 'e')
    time.sleep(2)
    
    # Zu Quellenverzeichnis navigieren
    pyautogui.write(os.path.dirname(quelldatei))
    pyautogui.press('enter')
    time.sleep(1)
    
    # Datei auswählen
    pyautogui.write(os.path.basename(quelldatei))
    time.sleep(0.5)
    
    # Kopieren (Strg+C)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(0.5)
    
    # Zu Zielverzeichnis navigieren
    pyautogui.write(os.path.dirname(zieldatei))
    pyautogui.press('enter')
    time.sleep(1)
    
    # Einfügen (Strg+V)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(2)

# Verwendung
datei_uebertragen('/Dokumente/test.txt', '/Backups/test.txt')
```

### Beispiel 3: Automatisiertes Screenshot-Tool

```python
import pyautogui
import time
from datetime import datetime

def screenshot_area(region, output_dir='screenshots'):
    """Erstellt einen Screenshot eines bestimmten Bereichs."""
    os.makedirs(output_dir, exist_ok=True)
    
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = f"{output_dir}/screenshot_{timestamp}.png"
    
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(filename)
    print(f"Screenshot gespeichert: {filename}")

# Verwendung: Bereich (x, y, breite, höhe)
screenshot_area(region=(100, 100, 800, 600))
```

### Beispiel 4: Automatisiertes Testskript

```python
import pyautogui
import time
import unittest

class TestWebApplication(unittest.TestCase):
    """Automatisierte GUI-Tests mit PyAutoGUI."""
    
    def setUp(self):
        """Vor jedem Test."""
        time.sleep(1)
        
    def test_login(self):
        """Testet den Login-Prozess."""
        # Benutzername-Feld finden
        username_field = pyautogui.locateOnScreen('username_field.png')
        self.assertIsNotNone(username_field, "Benutzername-Feld nicht gefunden")
        
        # Benutzername eingeben
        pyautogui.click(pyautogui.center(username_field))
        pyautogui.write('testuser')
        
        # Passwort-Feld
        password_field = pyautogui.locateOnScreen('password_field.png')
        self.assertIsNotNone(password_field, "Passwort-Feld nicht gefunden")
        pyautogui.click(pyautogui.center(password_field))
        pyautogui.write('testpass')
        
        # Login-Button
        login_button = pyautogui.locateOnScreen('login_button.png')
        self.assertIsNotNone(login_button, "Login-Button nicht gefunden")
        pyautogui.click(pyautogui.center(login_button))
        
        # Warten auf erfolgreichen Login
        time.sleep(3)
        success_indicator = pyautogui.locateOnScreen('login_success.png')
        self.assertIsNotNone(success_indicator, "Login fehlgeschlagen")
    
    def test_navigation(self):
        """Testet die Navigation."""
        # Menü öffnen
        menu_button = pyautogui.locateOnScreen('menu_button.png')
        self.assertIsNotNone(menu_button, "Menü-Button nicht gefunden")
        pyautogui.click(pyautogui.center(menu_button))
        
        # Auf Einstellungen klicken
        settings_item = pyautogui.locateOnScreen('settings_item.png')
        self.assertIsNotNone(settings_item, "Einstellungen nicht gefunden")
        pyautogui.click(pyautogui.center(settings_item))
        
        # Überprüfen, ob Einstellungen geöffnet sind
        time.sleep(2)
        settings_title = pyautogui.locateOnScreen('settings_title.png')
        self.assertIsNotNone(settings_title, "Einstellungen wurden nicht geöffnet")

# Tests ausführen
if __name__ == '__main__':
    unittest.main()
```

---

## 🛡️ Fehlerbehandlung und Best Practices

### Fail-Safe Mechanismus

PyAutoGUI hat einen eingebauten Fail-Safe: Wenn die Maus schnell in eine Ecke des Bildschirms bewegt wird, wird eine `FailSafeException` ausgelöst.

```python
import pyautogui

# Fail-Safe aktivieren (Standardmäßig aktiviert)
pyautogui.FAILSAFE = True

# Fail-Safe deaktivieren (nicht empfohlen!)
# pyautogui.FAILSAFE = False

try:
    # Dein Code
    pyautogui.click(100, 100)
    
except pyautogui.FailSafeException:
    print("Fail-Safe ausgelöst! Maus wurde in die Ecke bewegt.")
```

### Warten und Timeouts

```python
import pyautogui
import time

def wait_for_image(image, timeout=10, interval=0.5):
    """Wartet auf das Erscheinen eines Bildes."""
    start_time = time.time()
    
    while time.time() - start_time < timeout:
        location = pyautogui.locateOnScreen(image)
        if location:
            return location
        time.sleep(interval)
    
    raise TimeoutError(f"Bild {image} nicht innerhalb von {timeout} Sekunden gefunden")

# Verwendung
try:
    location = wait_for_image('loading_complete.png', timeout=30)
    print(f"Bild gefunden bei: {location}")
except TimeoutError:
    print("Timeout erreicht")
```

### Bildschirmauflösung und Skalierung

```python
import pyautogui

# Bildschirmgröße abfragen
width, height = pyautogui.size()
print(f"Bildschirm: {width}x{height}")

# Für Multi-Monitor-Setup
import pyautogui
print(f"Primärer Monitor: {pyautogui.size()}")

# Alle Monitore
import screeninfo
monitors = screeninfo.get_monitors()
for i, monitor in enumerate(monitors):
    print(f"Monitor {i}: {monitor.width}x{monitor.height} bei ({monitor.x}, {monitor.y})")
```

### Logging und Debugging

```python
import pyautogui
import time
import logging

# Logging einrichten
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename='automation.log'
)

# Mausbewegungen loggen
class LoggingPyAutoGUI:
    @staticmethod
    def moveTo(x, y, duration=0, **kwargs):
        logging.info(f"Maus bewegt zu: ({x}, {y}), Dauer: {duration}s")
        pyautogui.moveTo(x, y, duration, **kwargs)
    
    @staticmethod
    def click(x=None, y=None, button='left', **kwargs):
        pos = pyautogui.position() if x is None or y is None else (x, y)
        logging.info(f"Klick bei: {pos}, Taste: {button}")
        pyautogui.click(x, y, button, **kwargs)
    
    @staticmethod
    def write(text, **kwargs):
        logging.info(f"Text eingegeben: {text}")
        pyautogui.write(text, **kwargs)

# Verwendung
log_gui = LoggingPyAutoGUI()
log_gui.moveTo(100, 100, duration=1)
log_gui.click(100, 100)
log_gui.write('Hallo Welt')
```

---

## 🚀 Fortgeschrittene Techniken

### OpenCV für bessere Bilderkennung

```python
import pyautogui
import cv2
import numpy as np

def find_template_cv2(template_path, threshold=0.8):
    """Findet ein Template mit OpenCV (präziser als PyAutoGUI)."""
    # Screenshot machen
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # Template laden
    template = cv2.imread(template_path, cv2.IMREAD_COLOR)
    
    # Template Matching
    result = cv2.matchTemplate(screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    
    # Schwellenwert prüfen
    if max_val >= threshold:
        # Koordinaten berechnen
        h, w = template.shape[:2]
        top_left = max_loc
        bottom_right = (top_left[0] + w, top_left[1] + h)
        center = ((top_left[0] + bottom_right[0]) // 2, 
                  (top_left[1] + bottom_right[1]) // 2)
        return center
    
    return None

# Verwendung
center = find_template_cv2('button.png', threshold=0.8)
if center:
    pyautogui.click(center)
```

### OCR mit Tesseract

```python
import pyautogui
import pytesseract
from PIL import Image

# Tesseract installieren (Ubuntu)
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev
# pip install pytesseract

# Text aus Bildschirmregion extrahieren
def extract_text_from_screen(region=None):
    """Extrahiert Text aus einer Bildschirmregion."""
    screenshot = pyautogui.screenshot(region=region)
    text = pytesseract.image_to_string(screenshot, lang='deu')
    return text.strip()

# Verwendung
text = extract_text_from_screen(region=(100, 100, 400, 200))
print(f"Erkannter Text: {text}")
```

### Parallelisierung

```python
import pyautogui
import threading
import time

def task1():
    """Aufgabe 1: Formular ausfüllen."""
    pyautogui.click(100, 100)
    pyautogui.write('Task 1')
    time.sleep(1)

def task2():
    """Aufgabe 2: Screenshot machen."""
    time.sleep(0.5)
    screenshot = pyautogui.screenshot(region=(200, 200, 300, 200))
    screenshot.save('task2.png')

# Threads starten
thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Alle Aufgaben abgeschlossen")
```

### Multi-Monitor-Unterstützung

```python
import pyautogui
import screeninfo

def get_monitor_dimensions():
    """Gibt die Abmessungen aller Monitore zurück."""
    monitors = screeninfo.get_monitors()
    return [(m.x, m.y, m.width, m.height) for m in monitors]

def click_on_monitor(monitor_index, x, y):
    """Klickt auf einen bestimmten Monitor."""
    monitors = get_monitor_dimensions()
    if monitor_index < len(monitors):
        m_x, m_y, m_w, m_h = monitors[monitor_index]
        abs_x = m_x + x
        abs_y = m_y + y
        pyautogui.click(abs_x, abs_y)
    else:
        print(f"Monitor {monitor_index} nicht gefunden")

# Beispiel: Auf zweiten Monitor bei (100, 100) klicken
click_on_monitor(1, 100, 100)
```

---

## 🎯 Praxisprojekte

### Projekt 1: Automatisiertes Daten-Eingabe-System

**Ziel:** Automatisierte Eingabe von Daten aus einer CSV-Datei in ein Webformular.

```python
import pyautogui
import csv
import time

def fill_form_from_csv(csv_file):
    """Füllt ein Formular mit Daten aus einer CSV-Datei."""
    
    # Formular öffnen
    pyautogui.hotkey('alt', 'tab')  # Zum Formular wechseln
    time.sleep(1)
    
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        
        for row in reader:
            # Vorname
            pyautogui.click(100, 100)  # Vorname-Feld
            pyautogui.write(row['vorname'])
            time.sleep(0.3)
            
            # Nachname
            pyautogui.click(100, 150)  # Nachname-Feld
            pyautogui.write(row['nachname'])
            time.sleep(0.3)
            
            # E-Mail
            pyautogui.click(100, 200)  # E-Mail-Feld
            pyautogui.write(row['email'])
            time.sleep(0.3)
            
            # Submit
            pyautogui.click(100, 300)  # Submit-Button
            time.sleep(2)  # Warten auf Bestätigung
            
            # Zurücksetzen für nächsten Datensatz
            pyautogui.click(200, 300)  # Zurücksetzen-Button
            time.sleep(1)

# Verwendung
fill_form_from_csv('daten.csv')
```

### Projekt 2: Automatisiertes Testskript für Webanwendung

```python
import pyautogui
import time
import json

def run_website_test(test_config):
    """Führt einen automatisierten Test einer Website durch."""
    
    # Browser öffnen
    pyautogui.hotkey('win', 'r')
    pyautogui.write('chrome')
    pyautogui.press('enter')
    time.sleep(3)
    
    # URL eingeben
    pyautogui.write(test_config['url'])
    pyautogui.press('enter')
    time.sleep(5)
    
    # Testschritte durchführen
    for step in test_config['steps']:
        if step['type'] == 'click':
            # Klick auf Bildschirmposition
            pyautogui.click(step['x'], step['y'])
            time.sleep(step.get('wait', 1))
            
        elif step['type'] == 'write':
            # Text eingeben
            pyautogui.write(step['text'])
            time.sleep(0.5)
            
        elif step['type'] == 'screenshot':
            # Screenshot machen
            screenshot = pyautogui.screenshot(region=tuple(step['region']))
            screenshot.save(f"{step['filename']}.png")
            
        elif step['type'] == 'hotkey':
            # Tastenkombination
            pyautogui.hotkey(*step['keys'])
            time.sleep(1)
    
    # Browser schließen
    pyautogui.hotkey('ctrl', 'w')

# Testkonfiguration
test_config = {
    'url': 'https://beispiel.de',
    'steps': [
        {'type': 'click', 'x': 500, 'y': 300, 'wait': 2},
        {'type': 'write', 'text': 'Testuser'},
        {'type': 'click', 'x': 500, 'y': 350, 'wait': 2},
        {'type': 'write', 'text': 'test123'},
        {'type': 'click', 'x': 500, 'y': 400, 'wait': 3},
        {'type': 'screenshot', 'region': [0, 0, 800, 600], 'filename': 'test_result'}
    ]
}

# Test ausführen
run_website_test(test_config)
```

### Projekt 3: Automatisiertes Monitoring-System

```python
import pyautogui
import time
import smtplib
from email.mime.text import MIMEText

def monitor_and_alert(check_interval=300, alert_email=None):
    """Überwacht ein System und sendet Benachrichtigungen bei Problemen."""
    
    def check_status():
        """Überprüft den Status des Systems."""
        # Screenshot machen
        screenshot = pyautogui.screenshot()
        
        # Nach Error-Meldungen suchen
        error_indicator = pyautogui.locateOnScreen('error.png')
        if error_indicator:
            return False
        
        # Nach OK-Meldungen suchen
        ok_indicator = pyautogui.locateOnScreen('ok.png')
        if ok_indicator:
            return True
        
        return None  # Unbekannter Status
    
    def send_alert(subject, message):
        """Sendet eine E-Mail-Benachrichtigung."""
        if not alert_email:
            return
            
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'monitor@beispiel.de'
        msg['To'] = alert_email
        
        with smtplib.SMTP('smtp.beispiel.de', 587) as server:
            server.starttls()
            server.login('user', 'password')
            server.send_message(msg)
    
    # Hauptschleife
    while True:
        status = check_status()
        
        if status is False:
            # Fehler erkannt
            screenshot = pyautogui.screenshot()
            screenshot.save('error_screenshot.png')
            send_alert(
                'Systemfehler erkannt',
                'Ein Fehler wurde auf dem überwachten System erkannt. Siehe Anhänge.'
            )
        
        time.sleep(check_interval)

# Monitoring starten
# monitor_and_alert(alert_email='admin@beispiel.de')
```

---

## 📚 Ressourcen und weiterführende Links

### Offizielle Dokumentation
- [PyAutoGUI Documentation](https://pyautogui.readthedocs.io/en/latest/)
- [PyAutoGUI GitHub](https://github.com/asweigart/pyautogui)
- [Installationsanleitung](https://pyautogui.readthedocs.io/en/latest/install.html)

### Tutorials und Guides
- [PyAutoGUI Tutorial (Real Python)](https://realpython.com/pyautogui-python-automation/)
- [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/)
- [PyAutoGUI Examples](https://pyautogui.readthedocs.io/en/latest/examples.html)

### Alternativen
| Tool | Plattform | Sprache | Spezialisierung |
|------|-----------|---------|----------------|
| **PyAutoGUI** | Win/macOS/Linux | Python | Allgemeine GUI-Automatisierung |
| **pywinauto** | Windows | Python | Windows-GUI-Automatisierung |
| **Selenium** | Win/macOS/Linux | Python/JS/Java | Web-Automatisierung |
| **Playwright** | Win/macOS/Linux | Python/JS/Java | Moderne Web-Automatisierung |
| **xdotool** | Linux (X11) | CLI | X11-Automatisierung |
| **ydotool** | Linux (Wayland/X11) | CLI | Low-Level-Automatisierung |

---

## 🔗 Verwandte Themen

* [Desktop Automation/Übersicht](index.md) – Umfassende Übersicht über Desktop-Automatisierungstools
* [Desktop Automation mit Robot Framework](robot-framework-anleitung.md) – Testautomatisierung mit Robot Framework
* [Desktop Automation mit ydotool](ydotool-anleitung.md) – Low-Level-Automatisierung auf Linux
* [Webautomatisierung mit Playwright](playwright-anleitung.md) – Moderne Web-Tests und Automatisierung

---

*Letzte Aktualisierung: Juli 2026*
