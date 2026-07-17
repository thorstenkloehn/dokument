# Praxis-Guide: Audacity Macro Automatisierung & Batch-Processing

Mit **Audacity Makros** (ehemals Ketten/Chains) lassen sich wiederkehrende Audio-Bearbeitungsschritte (Rauschunterdrückung, Normalisierung, Kompression, Export) automatisieren.

---

## 🛠️ 1. Makro in Audacity erstellen

1. Öffne Audacity → **Werkzeuge** → **Makros...**
2. Klicke auf **Neu** und benenne das Makro (z. B. `Podcast_Mastering`).
3. Füge folgende Befehle in der richtigen Reihenfolge hinzu:

```text
1. High-Pass Filter (Frequency: 80Hz)
2. Noise Reduction (Rauschabstand: 12dB)
3. Compressor (Threshold: -18dB, Ratio: 3:1)
4. Loudness Normalization (Target: -16 LUFS)
5. Export MP3 (Bitrate: 192 kbps)
```

---

## 🐍 2. Python Audacity Scripting (via Pipe)

Audacity unterstützt die Steuerung via Named Pipes (`mod-script-pipe`).

```python
import os
import sys

# Name Pipes für Kommunikation
if sys.platform == 'win32':
    TONAME = '\\\\.\\pipe\\ToSrvPipe'
    FROMNAME = '\\\\.\\pipe\\FromSrvPipe'
else:
    TONAME = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
    FROMNAME = '/tmp/audacity_script_pipe.from.' + str(os.getuid())

def send_command(command):
    to_pipe = open(TONAME, 'w')
    to_pipe.write(command + '\n')
    to_pipe.flush()

# Beispiel: Audacity Makro per Python starten
if __name__ == "__main__":
    send_command('Macro: Podcast_Mastering')
    print("✅ Audacity Makro per Skript ausgeführt!")
```

---

## 🔗 Verwandte Themen
* [Audacity mit KI](audacity-ki.md) – Audacity KI-Plugins
* [DAW-Integration mit KI](daw-integration.md) – DAW Einbindung
* [MIDI-Generierung mit Python](midi-python-automation.md) – MIDI-Skripte
