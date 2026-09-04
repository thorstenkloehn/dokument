# Praxis-Guide: Playwright Multi-Device & Geolocation Emulation

Emulation mobiler Geräte (iPhone, Pixel), Touch-Gesten, Geolocation (GPS-Koordinaten), Zeitzonen und Sprachen in Playwright für globale Web-Tests.

---

## 🐍 1. Python Skript (`device_emulation.py`)

```python
import asyncio
from playwright.async_api import async_playwright

async def run_mobile_geo_test():
    async with async_playwright() as p:
        # 1. Gerät-Profil wählen (z. B. iPhone 13 Pro)
        iphone = p.devices['iPhone 13 Pro']

        # 2. Browser-Kontext mit Emulation starten (Standort: Tokio, Japan)
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            **iphone,
            geolocation={"latitude": 35.6762, "longitude": 139.6503},
            permissions=["geolocation"],
            locale="ja-JP",
            timezone_id="Asia/Tokyo"
        )

        page = await context.new_page()
        await page.goto("https://maps.google.com")
        await page.screenshot(path="tokyo_mobile.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_mobile_geo_test())
```

---

## 🔗 Verwandte Themen
* [Playwright Trace Viewer](playwright-trace-viewer.md) – Test-Debugging
* [Playwright Visual Regression](playwright-visual-regression.md) – UI-Vergleich
* [Playwright Network Interception](playwright-network-mocking.md) – Network Mocking
