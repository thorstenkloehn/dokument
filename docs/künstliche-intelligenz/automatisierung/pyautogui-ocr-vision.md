# Praxis-Guide: PyAutoGUI mit OpenCV & OCR

Erweitere PyAutoGUI um Computer Vision (**OpenCV**) und optische Zeichenerkennung (**Tesseract OCR**), um Oberflächenelemente bild- und textbasiert dynamisch zu erkennen und anzuklicken.

---

## 🛠️ 1. Installation

```bash
sudo apt update && sudo apt install -y tesseract-ocr tesseract-ocr-deu
pip install pyautogui opencv-python pytesseract pillow
```

---

## 🐍 2. Python Skript (`vision_automation.py`)

```python
import pyautogui
import pytesseract
import cv2
import numpy as np

# 1. Bildschirmausschnitt aufnehmen & OCR anwenden
def find_text_on_screen(target_text: str):
    screenshot = pyautogui.screenshot()
    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    
    # OCR Zeichenerkennung
    data = pytesseract.image_to_data(img, lang='deu+eng', output_type=pytesseract.Output.DICT)
    
    for i in range(len(data['text'])):
        if target_text.lower() in data['text'][i].lower():
            x = data['left'][i] + data['width'][i] // 2
            y = data['top'][i] + data['height'][i] // 2
            print(f"✅ Text '{target_text}' gefunden bei X:{x}, Y:{y}")
            return x, y
            
    print(f"❌ Text '{target_text}' nicht auf dem Bildschirm gefunden.")
    return None

# 2. Automatisch auf Button mit bestimmtem Text klicken
if __name__ == "__main__":
    pos = find_text_on_screen("Speichern")
    if pos:
        pyautogui.click(pos[0], pos[1])
```

---

## 🔗 Verwandte Themen
* [PyAutoGUI Anleitung](pyautogui-anleitung.md) – Grundlagen der GUI-Automatisierung
* [Playwright & KI Web-Scraping](playwright-ki-extraction.md) – Web-Extraktion
* [ydotool Anleitung](ydotool-anleitung.md) – Wayland Automatisierung
* [Beste lokale Computer-KI-Agenten (Allgemein, Top 20)](lokale-ki-agenten-topliste.md) – vollständige Vision-Grounding-Agenten im Vergleich
