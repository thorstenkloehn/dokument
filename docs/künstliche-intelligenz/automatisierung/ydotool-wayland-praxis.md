# Praxis-Guide: ydotool & Wayland Automatisierung

Unter Linux mit **Wayland** (Gnome/KDE) funktionieren herkömmliche X11-Tools wie `xdotool` nicht mehr. **ydotool** emuliert Tastatur-, Maus- und Touch-Eingaben direkt auf uinput-Kernel-Ebene.

---

## 🛠️ 1. Installation & Daemon-Setup

```bash
# ydotool & ydotoold Daemon installieren
sudo apt update && sudo apt install -y ydotool

# ydotoold Hintergrund-Dienst starten
sudo systemctl enable --now ydotoold
```

---

## ⚡ 2. CLI-Befehle für Tastatur & Maus

```bash
# Text eingeben
ydotool type "Hallo Welt!"

# Einzeltaste drücken (z. B. Enter -> Keycode 28)
ydotool key 28:1 28:0

# Maus bewegen (X: 500, Y: 400)
ydotool mousemove -x 500 -y 400

# Linksklick (Button 0x110)
ydotool click 0x110
```

---

## 🐍 3. Python Automatisierungs-Skript (`wayland_automation.py`)

```python
import subprocess
import time

def type_text(text: str):
    subprocess.run(["ydotool", "type", text])

def press_enter():
    subprocess.run(["ydotool", "key", "28:1", "28:0"])

if __name__ == "__main__":
    print("Starte Eingabe in 3 Sekunden...")
    time.sleep(3)
    type_text("echo 'Wayland Automatisierung funktioniert!'")
    press_enter()
```

---

## 🔗 Verwandte Themen
* [ydotool Anleitung](ydotool-anleitung.md) – Grundlegende Einführung
* [PyAutoGUI Anleitung](pyautogui-anleitung.md) – GUI-Automatisierung
* [Systemd Service Creation](../../entwicklung/system/systemd-service-creation.md) – Daemons
