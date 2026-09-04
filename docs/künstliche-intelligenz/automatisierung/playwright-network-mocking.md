# Praxis-Guide: Playwright Network Interception & API Mocking

Abfangen, Verändern und Simulieren von HTTP-Netzwerk-Requests und Backend-APIs in Playwright für schnelle, deterministische Frontend-Tests.

---

## 🐍 1. Python Skript (`mock_api.py`)

```python
import asyncio
from playwright.async_api import async_playwright, Route

async def handle_api_route(route: Route):
    # 1. Ersetze die echte Backend-Antwort durch ein Mock-JSON
    mock_json = {
        "status": "success",
        "user": {"name": "Test User", "role": "Administrator"}
    }
    
    # 2. Antwort injizieren (ohne echten Server-Request)
    await route.fulfill(
        status=200,
        content_type="application/json",
        body=str(mock_json).replace("'", '"')
    )

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        
        # Intercepting für alle /api/user Anfragen aktivieren
        await page.route("**/api/user", handle_api_route)
        
        # Seite aufrufen
        await page.goto("https://beispiel.de/dashboard")
        await page.screenshot(path="mocked_dashboard.png")
        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🔗 Verwandte Themen
* [Playwright Anleitung](playwright-anleitung.md) – Grundlagen der Automatisierung
* [Playwright & KI Web-Scraping](playwright-ki-extraction.md) – Scraping
* [Robot Framework API-Testing](robot-framework-api-testing.md) – API Testing
