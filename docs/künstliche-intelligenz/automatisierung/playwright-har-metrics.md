# Praxis-Guide: Playwright HAR Export & Performance Metriken

Aufzeichnen von HTTP-Archivdateien (**HAR** - HTTP Archive) und exakte Messung von Web-Performance Metriken (Ladezeit, TTFB, DOMContentLoaded) in Playwright.

---

## 🐍 1. Python Skript (`har_performance.py`)

```python
import asyncio
import json
from playwright.async_api import async_playwright

async def measure_performance():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        
        # 1. Konfigurieren: HAR-Datei automatisch exportieren
        context = await browser.new_context(
            record_har_path="network_trace.har",
            record_har_content="embed"
        )

        page = await context.new_page()
        
        # 2. Seite laden & Navigation abwarten
        response = await page.goto("https://beispiel.de")
        
        # 3. Performance Navigation Timings über Browser-API abrufen
        performance_timing = await page.evaluate("() => JSON.stringify(window.performance.timing)")
        timing_data = json.loads(performance_timing)

        load_time = timing_data['loadEventEnd'] - timing_data['navigationStart']
        ttfb = timing_data['responseStart'] - timing_data['requestStart']

        print(f"📊 Gesamte Ladezeit: {load_time} ms")
        print(f"⚡ Time to First Byte (TTFB): {ttfb} ms")
        print("✅ HAR-Datei gespeichert in: network_trace.har")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(measure_performance())
```

---

## 🔗 Verwandte Themen
* [Playwright Trace Viewer](playwright-trace-viewer.md) – Tracing
* [Playwright Network Interception](playwright-network-mocking.md) – Network Mocking
* [k6 API Load Testing](../../entwicklung/infrastruktur/k6-api-load-testing.md) – Lasttests
