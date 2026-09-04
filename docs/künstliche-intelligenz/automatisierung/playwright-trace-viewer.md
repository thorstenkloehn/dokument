# Praxis-Guide: Playwright Trace Viewer & CI Debugging

Der **Playwright Trace Viewer** ist ein visuelles GUI-Tool zur schrittweisen Analyse fehlgeschlagener automatisierter Web-Tests, inklusive Netzwerk-Interaktionen, Screenshots, DOM-Snapshots und Konsolen-Logs.

---

## 🛠️ 1. Tracing im Python-Skript aktivieren

```python
import asyncio
from playwright.async_api import async_playwright

async def run_test_with_trace():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        context = await browser.new_context()

        # 1. Tracing vor den Testaktionen starten
        await context.tracing.start(screenshots=True, snapshots=True, sources=True)

        page = await context.new_page()
        await page.goto("https://beispiel.de/login")
        
        # Testaktionen
        await page.fill("#username", "admin")
        await page.fill("#password", "wrongpassword")
        await page.click("#login-btn")

        # 2. Trace-Datei im Fehlerfall oder am Ende speichern
        await context.tracing.stop(path="trace.zip")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(run_test_with_trace())
```

---

## 🔍 2. Trace-Datei im CLI Viewer öffnen

```bash
# Öffnet den interaktiven Playwright Trace Viewer im Browser
playwright show-trace trace.zip
```

Im Trace Viewer kann man durch jede einzelne Aktion wie in einem Film vor- und zurückspulen, um den exakten Fehlerursprung zu analysieren.

---

## 🔗 Verwandte Themen
* [Playwright Network Interception](playwright-network-mocking.md) – Mocking
* [Playwright & KI Web-Scraping](playwright-ki-extraction.md) – Extraktion
* [Robot Framework API-Testing](robot-framework-api-testing.md) – Test-Automatisierung
