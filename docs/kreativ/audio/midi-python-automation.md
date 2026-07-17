# Praxis-Guide: MIDI-Generierung & DAW-Automatisierung mit Python

Generiere prozedurale Akkordfolgen, Melodien und MIDI-Dateien vollautomatisiert mit Python und lade sie direkt in deine Digital Audio Workstation (DAW).

---

## 🛠️ 1. Installation

```bash
pip install mido python-rtmidi
```

---

## 🐍 2. Python Skript: MIDI-Datei generieren (`generate_midi.py`)

```python
from mido import Message, MidiFile, MidiTrack

def create_chord_progression():
    mid = MidiFile()
    track = MidiTrack()
    mid.tracks.append(track)

    # C-Dur, G-Dur, a-Moll, F-Dur Akkordfolge (C - G - Am - F)
    chords = [
        [60, 64, 67], # C-Dur
        [55, 59, 62], # G-Dur
        [57, 60, 64], # a-Moll
        [53, 57, 60]  # F-Dur
    ]

    tempo = 480 # Ticks pro Beat

    for chord in chords:
        # Akkord-Noten anschlagen (Note On)
        for note in chord:
            track.append(Message('note_on', note=note, velocity=80, time=0))
        
        # 1 Takt halten (Note Off nach 4 Beats)
        first = True
        for note in chord:
            delay = tempo * 4 if first else 0
            track.append(Message('note_off', note=note, velocity=64, time=delay))
            first = False

    output_file = "progression.mid"
    mid.save(output_file)
    print(f"✅ MIDI-Datei erfolgreich gespeichert unter '{output_file}'!")

if __name__ == "__main__":
    create_chord_progression()
```

---

## 🔗 Verwandte Themen
* [MIDI-Programmierung mit KI](midi-programmierung.md) – KI MIDI-Erzeugung
* [DAW-Integration mit KI](daw-integration.md) – Einbindung in DAWs
* [Audio-Processing mit KI](audio-processing.md) – Audioverarbeitung
