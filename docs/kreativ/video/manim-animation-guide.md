# Praxis-Guide: Manim Mathematical Animation Engine

**Manim** (entwickelt von Grant Sanderson / 3Blue1Brown) ist ein mächtiges Python-Framework zum programmatischen Erstellen von mathematischen und technischen 2D-Animationen.

---

```mermaid
graph LR
    Code["🐍 Python Code (Manim Scene)"] --> Render["⚡ Manim Rendering Engine"]
    Render --> Output["🎬 Hochauflösendes MP4 Video"]
```

---

## 🛠️ 1. Installation

```bash
# FFmpeg & LaTeX / Cairo Abhängigkeiten installieren
sudo apt update && sudo apt install -y ffmpeg libcairo2-dev libpango1.0-dev

# Manim Community Edition installieren
pip install manim
```

---

## 🐍 2. Erste Animation programmieren (`scene.py`)

```python
from manim import *

class SquareToCircle(Scene):
    def construct(self):
        # 1. Objekte erzeugen
        circle = Circle()  # Erzeuge einen Kreis
        circle.set_fill(PINK, opacity=0.5)  # Farbe und Transparenz setzen

        square = Square()  # Erzeuge ein Quadrat
        square.rotate(PI / 4)  # 45 Grad rotieren

        # 2. Animationen durchführen
        self.play(Create(square))  # Zeichne Quadrat
        self.play(Transform(square, circle))  # Transformiere Quadrat zu Kreis
        self.play(FadeOut(square))  # Ausblenden
```

---

## 🎬 3. Video Rendern

```bash
# Vorschau in 480p Qualität rendern (schnell)
manim -pql scene.py SquareToCircle

# In hoher Qualität (1080p60) rendern
manim -pqh scene.py SquareToCircle
```

---

## 🔗 Verwandte Themen
* [FFmpeg & Whisper Automatisierung](ffmpeg-whisper-automatisierung.md) – Automatische Untertitelung
* [KI in der Film- und Videoproduktion](ki-filmproduktion.md) – KI-Videoproduktion
* [Ideenfindung mit KI](../design/ideenfindung-ki.md) – Storyboarding
