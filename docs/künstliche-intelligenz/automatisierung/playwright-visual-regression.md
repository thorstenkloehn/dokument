# Praxis-Guide: Playwright Visual Regression Testing

Automatisierter Abgleich von Benutzeroberflächen durch Pixel-genauen Vergleich von Screenshots (**Visual Regression Testing**) zur Vermeidung unerwünschter Layout-Fehler.

---

## 🐍 1. Python Skript (`visual_test.py`)

```python
import pytest
from playwright.sync_api import Page, expect

def test_homepage_visual_regression(page: Page):
    # 1. Webseite aufrufen
    page.goto("https://beispiel.de")
    
    # 2. Warten bis alle Schriften & Bilder geladen sind
    page.wait_for_load_state("networkidle")
    
    # 3. Screenshot abgleichen mit Baseline-Referenzbild
    expect(page).to_have_screenshot("homepage_baseline.png", max_diff_pixels=100)
```

---

## ⚡ 2. Ausführung & Baseline-Erstellung

```bash
# Baseline-Screenshots beim ersten Mal erzeugen
pytest --update-snapshots visual_test.py

# Regelmäßigen visuellen Test ausführen
pytest visual_test.py
```

---

## 🔗 Verwandte Themen
* [Playwright Trace Viewer](playwright-trace-viewer.md) – Test-Debugging
* [Playwright Network Interception](playwright-network-mocking.md) – Mocking
* [Robot Framework API-Testing](robot-framework-api-testing.md) – Testing
