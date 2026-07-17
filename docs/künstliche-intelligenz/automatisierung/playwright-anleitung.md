# Playwright: Praktische Anleitung für moderne Web-Automatisierung

Eine umfassende Schritt-für-Schritt-Anleitung für Playwright – das mächtige Framework für Web-Tests, Automatisierung und Scraping. Von der Installation über Grundlagen bis zu fortgeschrittenen Techniken.

---

## 🎯 Einführung: Was ist Playwright?

**Playwright** ist ein modernes, Open-Source-Framework von Microsoft für die Automatisierung von Web-Browsern. Es unterstützt:

| Funktion | Beschreibung | Unterstützte Browser |
|----------|--------------|---------------------|
| **Browser-Automatisierung** | Steuerung von Browsern programmatisch | Chromium, Firefox, WebKit |
| **Cross-Browser Testing** | Tests auf verschiedenen Browsern | ✅ Alle drei |
| **Cross-Plattform** | Funktioniert auf Windows, macOS, Linux | ✅ Alle |
| **Cross-Language** | API für Python, JavaScript, TypeScript, .NET | ✅ Alle |
| **Headless & Headed** | Ausführung ohne und mit GUI | ✅ Beide |
| **Mobile Emulation** | Simulation von Mobilgeräten | ✅ Ja |
| **Network Interception** | Abfangen und Modifizieren von HTTP-Anfragen | ✅ Ja |
| **Screenshot & Video** | Screenshots und Videoaufnahmen | ✅ Ja |
| **PDF-Generierung** | PDF aus Webseiten erstellen | ✅ Ja |

### Vorteile von Playwright

| Vorteil | Beschreibung |
|---------|--------------|
| **Schnell** | Deutlich schneller als Selenium |
| **Zuverlässig** | Automatische Warten und Retries |
| **Modern** | Asynchrone API, Promise-basiert |
| **Vollständig** | Keine externen Abhängigkeiten wie WebDriver |
| **Debugging** | Integrierte DevTools und Debugging |
| **Parallelisierung** | Einfache Parallelausführung von Tests |

### Vergleich: Playwright vs. Selenium vs. Puppeteer

| Feature | Playwright | Selenium | Puppeteer |
|---------|------------|----------|-----------|
| **Multi-Browser** | ✅ Chromium, Firefox, WebKit | ✅ Alle | ❌ Nur Chromium |
| **Multi-Language** | ✅ Python, JS, Java, .NET | ✅ Viele | ❌ Nur JS |
| **Speed** | ✅✅✅✅✅ Sehr schnell | ✅ Mittel | ✅✅✅✅ Schnell |
| **Reliability** | ✅✅✅✅✅ Automatische Warten | ✅✅ Manuell | ✅✅✅✅ Gut |
| **Headless** | ✅ Ja | ✅ Ja | ✅ Ja |
| **Mobile Emulation** | ✅ Ja | ✅ Ja | ✅ Ja |
| **Network Mocking** | ✅ Ja | ❌ Nein | ✅ Ja |
| **PDF Generation** | ✅ Ja | ❌ Nein | ✅ Ja |
| **Video Recording** | ✅ Ja | ❌ Nein | ❌ Nein |

---

## 📥 Installation

### Python-Installation

```bash
# Playwright für Python installieren
pip install playwright

# Browser Binaries herunterladen
playwright install

# Für zusätzliche Funktionen
pip install pytest pytest-playwright  # Für Testintegration
```

### Plattformspezifische Anforderungen

#### Windows
```bash
# Keine zusätzlichen Abhängigkeiten
pip install playwright
playwright install
```

#### macOS
```bash
# Keine zusätzlichen Abhängigkeiten
pip install playwright
playwright install
```

#### Linux (Ubuntu/Debian)
```bash
# Abhängigkeiten für Browser
sudo apt install -y libnss3 libnspr4 libatk1.0-0 libatk-bridge2.0-0 \
    libcups2 libdrm2 libdbus-1-3 libxkbcommon0 libxcomposite1 \
    libxdamage1 libxfixes3 libxrandr2 libgbm1 libasound2

# Playwright installieren
pip install playwright
playwright install
```

### Installation überprüfen

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Browser auflisten
    for browser_type in [p.chromium, p.firefox, p.webkit]:
        browser = browser_type.launch()
        print(f"{browser_type.name}: ✅ Installiert")
        browser.close()
```

---

## 🚀 Grundlagen: Erste Schritte

### Einfaches Browser-Skript

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Browser starten
    browser = p.chromium.launch(headless=False)  # headless=True für unsichtbaren Modus
    
    # Neue Seite öffnen
    page = browser.new_page()
    
    # URL aufrufen
    page.goto("https://www.beispiel.de")
    
    # Titel der Seite
    print(f"Seitentitel: {page.title()}")
    
    # URL
    print(f"URL: {page.url}")
    
    # Browser schließen
    browser.close()
```

### Asynchrone API (empfohlen)

```python
import asyncio
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        # Browser starten
        browser = await p.chromium.launch(headless=False)
        
        # Neue Seite öffnen
        page = await browser.new_page()
        
        # URL aufrufen
        await page.goto("https://www.beispiel.de")
        
        # Titel der Seite
        print(f"Seitentitel: {await page.title()}")
        
        # Browser schließen
        await browser.close()

# Ausführen
asyncio.run(main())
```

---

## 🔍 Navigation und Interaktion

### Seiten navigation

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Seite öffnen
    page.goto("https://www.beispiel.de")
    
    # Zurück navigieren
    page.go_back()
    
    # Vorwärts navigieren
    page.go_forward()
    
    # Seite neu laden
    page.reload()
    
    # Zu neuer URL navigieren
    page.goto("https://www.beispiel.de/seite2")
    
    # Warten bis Seite geladen ist (automatisch in den meisten Fällen)
    page.wait_for_load_state()
    
    browser.close()
```

### Elementauswahl (Selectors)

Playwright unterstützt CSS- und XPath-Selectors sowie Text-basierte Auswahl:

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de")
    
    # CSS-Selector
    element = page.locator("#login-button")
    
    # XPath-Selector
    element = page.locator("//button[@id='login-button']")
    
    # Text-basierte Auswahl
    element = page.locator("text=Login")
    
    # Platzhalter-Text
    element = page.locator("input[placeholder='Benutzername']")
    
    # Mehrere Elemente
    links = page.locator("a")  # Alle <a>-Tags
    
    # N-tes Element
    second_link = page.locator("a").nth(1)  # Zweiter Link
    
    browser.close()
```

### Interaktion mit Elementen

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de/login")
    
    # Text eingeben
    page.locator("#username").fill("mein_benutzername")
    page.locator("#password").fill("mein_passwort")
    
    # Klick auf Button
    page.locator("#login-button").click()
    
    # Checkbox aktivieren
    page.locator("#remember-me").check()
    
    # Radio-Button auswählen
    page.locator("#gender-male").check()
    
    # Dropdown auswählen
    page.locator("#country").select_option("Deutschland")
    page.locator("#country").select_option(value="DE")
    page.locator("#country").select_option(index=2)
    
    # Dateieingabe
    page.locator("#profile-picture").set_input_files("profilbild.jpg")
    
    # Mehrfachauswahl
    page.locator("#hobbies").select_option(["Lesen", "Sport"])
    
    browser.close()
```

---

## 📊 Warten und Synchronisation

Playwright hat ein intelligentes Auto-Waiting-System:

### Automatisches Warten

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Playwright wartet automatisch auf Elemente
    page.goto("https://www.beispiel.de")
    
    # Klick wartet automatisch bis Element sichtbar und klickbar ist
    page.locator("#login-button").click()
    
    # fill() wartet bis Element sichtbar und editierbar ist
    page.locator("#username").fill("test")
    
    browser.close()
```

### Explizites Warten

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de")
    
    # Warten auf Sichtbarkeit
    page.locator("#loading-spinner").wait_for(timeout=5000)
    
    # Warten bis Element verschwunden ist
    page.locator("#loading-spinner").wait_for(state="hidden")
    
    # Warten auf Text
    page.wait_for_selector("text=Willkommen")
    
    # Warten auf URL-Änderung
    page.wait_for_url("https://www.beispiel.de/dashboard")
    
    # Warten auf Navigation
    with page.expect_navigation():
        page.locator("#submit").click()
    
    # Warten auf neue Seite
    new_page = page.wait_for_event("popup")
    
    # Warten auf Netzwerk-Idle (keine Anfragen mehr)
    page.wait_for_load_state("networkidle")
    
    browser.close()
```

### Warten auf Bedingungen

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de")
    
    # Warten bis Funktion True zurückgibt
    page.wait_for_function("""
        () => {
            const element = document.querySelector('#dynamic-element');
            return element && element.textContent.includes('Fertig');
        }
    """)
    
    # Warten bis Element bestimmte CSS-Eigenschaft hat
    page.locator("#element").wait_for_function("""
        el => getComputedStyle(el).display !== 'none'
    """)
    
    browser.close()
```

---

## 🌐 Netzwerk-Handhabung

### Anfragen abfangen und modifizieren

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Anfragen abfangen
    def handle_request(request):
        print(f"Anfrage: {request.method} {request.url}")
    
    def handle_response(response):
        print(f"Antwort: {response.status} {response.url}")
    
    page.on("request", handle_request)
    page.on("response", handle_response)
    
    page.goto("https://www.beispiel.de")
    
    browser.close()
```

### Anfragen blockieren

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # Werbung blockieren
    page.route("**/*.{png,jpg,jpeg,webp}", lambda route: route.abort())
    
    # Bestimmte URL blockieren
    page.route("https://www.beispiel.de/tracking*", lambda route: route.abort())
    
    # Anfragen umleiten
    page.route("https://api.beispiel.de/*", lambda route: route.fulfill(
        status=200,
        content_type="application/json",
        body=json.dumps({"mocked": True})
    ))
    
    page.goto("https://www.beispiel.de")
    
    browser.close()
```

### Mock API-Anfragen

```python
from playwright.sync_api import sync_playwright
import json

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    
    # API-Aufruf mocken
    def handle_api_route(route):
        if route.request.url.endswith("/api/users"):
            # Mock-Antwort
            mock_data = {
                "users": [
                    {"id": 1, "name": "Max Mustermann"},
                    {"id": 2, "name": "Anna Schmidt"}
                ]
            }
            route.fulfill(
                status=200,
                content_type="application/json",
                body=json.dumps(mock_data)
            )
        else:
            route.continue_()
    
    page.route("**", handle_api_route)
    
    page.goto("https://www.beispiel.de")
    
    # Mock-API aufrufen
    response = page.evaluate("""
        async () => {
            const response = await fetch('/api/users');
            return await response.json();
        }
    """)
    
    print(f"Mock-Antwort: {response}")
    
    browser.close()
```

---

## 📸 Screenshots und PDF

### Screenshots erstellen

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de")
    
    # Ganze Seite
    page.screenshot(path="ganze_seite.png")
    
    # Element
    page.locator("#header").screenshot(path="header.png")
    
    # Bereich (x, y, breite, höhe)
    page.screenshot(path="bereich.png", clip={"x": 0, "y": 0, "width": 400, "height": 200})
    
    # Voller Bildschirm (inkl. Scrollbereich)
    page.screenshot(path="voller_bildschirm.png", full_page=True)
    
    # Mit Optionen
    page.screenshot(
        path="custom.png",
        type="jpeg",  # oder "png"
        quality=80,  # 0-100
        omit_background=True  # Transparenter Hintergrund
    )
    
    browser.close()
```

### PDF generieren

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de")
    
    # PDF der ganzen Seite
    page.pdf(path="seite.pdf")
    
    # PDF mit Optionen
    page.pdf(
        path="custom.pdf",
        format="A4",  # oder "Letter"
        orientation="portrait",  # oder "landscape"
        scale=0.8,  # 0.1-1.0
        margin={"top": "20mm", "right": "20mm", "bottom": "20mm", "left": "20mm"},
        print_background=True
    )
    
    browser.close()
```

### Videoaufnahme

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Browser mit Videoaufnahme starten
    browser = p.chromium.launch()
    context = browser.new_context(
        record_video_dir="videos/"
    )
    
    page = context.new_page()
    page.goto("https://www.beispiel.de")
    
    # Aktionen durchführen
    page.locator("#login").click()
    page.locator("#username").fill("test")
    
    # Browser schließen
    context.close()
    browser.close()
    
    # Video ist jetzt in videos/ gespeichert
```

---

## 📱 Mobile Emulation

### Geräte emulieren

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # iPhone 12 emulieren
    iphone_12 = p.devices["iPhone 12"]
    
    browser = p.chromium.launch()
    context = browser.new_context(**iphone_12)
    
    page = context.new_page()
    page.goto("https://www.beispiel.de")
    
    # User Agent prüfen
    user_agent = page.evaluate("() => navigator.userAgent")
    print(f"User Agent: {user_agent}")
    
    # Viewport abfragen
    viewport = page.evaluate("() => {
        return {
            width: window.innerWidth,
            height: window.innerHeight,
            deviceScaleFactor: window.devicePixelRatio
        }
    }")
    print(f"Viewport: {viewport}")
    
    context.close()
    browser.close()
```

### Geolocation setzen

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
        geolocation={"longitude": 13.404954, "latitude": 52.520008},  # Berlin
        permissions=["geolocation"]
    )
    
    page = context.new_page()
    page.goto("https://maps.google.com")
    
    # Standort auf Karte prüfen
    location = page.evaluate("() => {
        return new Promise(resolve => {
            navigator.geolocation.getCurrentPosition(
                position => resolve(position.coords),
                error => resolve(null)
            );
        });
    }")
    print(f"Standort: {location}")
    
    context.close()
    browser.close()
```

### Permissions setzen

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context(
        permissions=["geolocation", "camera", "microphone", "notifications"]
    )
    
    page = context.new_page()
    page.goto("https://www.beispiel.de")
    
    context.close()
    browser.close()
```

---

## 🧪 Testing mit Playwright

### Einfaches Testbeispiel

```python
from playwright.sync_api import sync_playwright, expect

def test_login():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("https://www.beispiel.de/login")
        
        # Formular ausfüllen
        page.locator("#username").fill("testuser")
        page.locator("#password").fill("testpass")
        page.locator("#login-button").click()
        
        # Erwartetes Ergebnis prüfen
        expect(page).to_have_url("https://www.beispiel.de/dashboard")
        expect(page.locator("#welcome-message")).to_have_text("Willkommen, testuser!")
        
        browser.close()

# Test ausführen
test_login()
```

### Test mit Pytest

```python
# test_login.py
import pytest
from playwright.sync_api import sync_playwright, expect

@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

@pytest.fixture
def page(browser):
    page = browser.new_page()
    yield page
    page.close()

def test_successful_login(page):
    page.goto("https://www.beispiel.de/login")
    
    page.locator("#username").fill("testuser")
    page.locator("#password").fill("testpass")
    page.locator("#login-button").click()
    
    expect(page).to_have_url("https://www.beispiel.de/dashboard")
    expect(page.locator("#welcome")).to_be_visible()

def test_invalid_login(page):
    page.goto("https://www.beispiel.de/login")
    
    page.locator("#username").fill("wronguser")
    page.locator("#password").fill("wrongpass")
    page.locator("#login-button").click()
    
    expect(page.locator("#error-message")).to_have_text("Ungültige Anmeldedaten")
```

### Test-Konfiguration

Erstelle eine `pytest.ini` Datei:

```ini
[pytest]
testpaths = tests
python_files = test_*.py
python_functions = test_*
addopts = -v --tb=short
```

Erstelle eine `playwright.config.py` Datei:

```python
from playwright.test import TestConfig

config = TestConfig(
    use=[
        {
            "browser_name": "chromium",
            "headless": True,
            "viewport": {"width": 1920, "height": 1080},
            "screenshot": "only-on-failure",
            "video": "retain-on-failure",
            "trace": "on-first-retry",
        }
    ]
)
```

---

## 📊 Daten extrahieren (Web Scraping)

### Einfaches Scraping

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de/produkte")
    
    # Alle Produktnamen extrahieren
    produkte = page.locator(".produkt-name").all_text_contents()
    
    # Alle Preise extrahieren
    preise = page.locator(".produkt-preis").all_text_contents()
    
    # Als Liste kombinieren
    produkte_data = list(zip(produkte, preise))
    
    for produkt, preis in produkte_data:
        print(f"{produkt}: {preis}")
    
    browser.close()
```

### Tabellen extrahieren

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de/tabelle")
    
    # Tabellenzeilen extrahieren
    zeilen = page.locator("table tr")
    
    data = []
    for zeile in zeilen.all():
        zellen = zeile.locator("td").all_text_contents()
        data.append(zellen)
    
    # Als CSV speichern
    import csv
    with open('tabelle.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    
    browser.close()
```

### Infinite Scrolling handhaben

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://www.beispiel.de/infinite-scroll")
    
    items = []
    last_count = 0
    
    while True:
        # Aktuelle Items sammeln
        current_items = page.locator(".item").all_text_contents()
        
        # Wenn sich nichts mehr ändert, abbrechen
        if len(current_items) == last_count:
            break
        
        last_count = len(current_items)
        items.extend(current_items)
        
        # Nach unten scrollen
        page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
        
        # Kurz warten
        page.wait_for_timeout(2000)
    
    print(f"Gesamt {len(items)} Items geladen")
    
    browser.close()
```

---

## 🔐 Authentifizierung und Sessions

### Einfache Authentifizierung

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    
    page = context.new_page()
    page.goto("https://www.beispiel.de/login")
    
    # Login durchführen
    page.locator("#username").fill("mein_benutzername")
    page.locator("#password").fill("mein_passwort")
    page.locator("#login-button").click()
    
    # Warten auf erfolgreichen Login
    page.wait_for_url("https://www.beispiel.de/dashboard")
    
    # Authentifizierten Context speichern
    context.storage_state(path="auth_state.json")
    
    browser.close()
```

### Gespeicherte Session wiederverwenden

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    
    # Session laden
    context = browser.new_context(storage_state="auth_state.json")
    page = context.new_page()
    
    # Direkt zur geschützten Seite navigieren
    page.goto("https://www.beispiel.de/dashboard")
    
    # Seite sollte direkt zugänglich sein
    print(f"Titelseite: {page.title()}")
    
    context.close()
    browser.close()
```

### Cookies setzen

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    context = browser.new_context()
    page = context.new_page()
    
    # Cookies manuell setzen
    context.add_cookies([
        {
            "name": "session_id",
            "value": "abc123",
            "domain": ".beispiel.de",
            "path": "/",
            "expires": 1717027200,  # Unix Timestamp
            "httpOnly": False,
            "secure": True,
            "sameSite": "Lax"
        }
    ])
    
    page.goto("https://www.beispiel.de/dashboard")
    
    # Cookies abfragen
    cookies = context.cookies()
    for cookie in cookies:
        print(f"{cookie['name']}: {cookie['value']}")
    
    context.close()
    browser.close()
```

---

## 🎯 Praxisprojekte

### Projekt 1: Automatisiertes Login-Testsystem

**Ziel:** Automatisierte Tests für einen Login-Prozess mit verschiedenen Benutzertypen.

```python
from playwright.sync_api import sync_playwright, expect
import csv

def test_login_with_csv(user_file):
    """Testet Login mit Benutzerdaten aus CSV."""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        with open(user_file, 'r') as f:
            reader = csv.DictReader(f)
            
            for row in reader:
                page.goto("https://www.beispiel.de/login")
                
                # Login durchführen
                page.locator("#username").fill(row['username'])
                page.locator("#password").fill(row['password'])
                page.locator("#login-button").click()
                
                # Ergebnis prüfen
                if row['expected'] == 'success':
                    expect(page).to_have_url("https://www.beispiel.de/dashboard")
                    print(f"✅ {row['username']}: Login erfolgreich")
                else:
                    expect(page.locator("#error")).to_be_visible()
                    print(f"✅ {row['username']}: Login fehlgeschlagen (erwartet)")
                
                # Screenshot bei Fehler
                if page.locator("#error").is_visible() and row['expected'] == 'success':
                    page.screenshot(path=f"failed_{row['username']}.png")
        
        browser.close()

# CSV-Datei: users.csv
# username,password,expected
# testuser,testpass,success
# lockeduser,pass,error
# admin,admin123,success

test_login_with_csv('users.csv')
```

### Projekt 2: Web Scraper für Produktdaten

```python
from playwright.sync_api import sync_playwright
import csv
import json

def scrape_products(url, output_file='products.csv'):
    """Scraped Produktdaten von einer E-Commerce-Seite."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto(url)
        
        # Auf Produkte laden warten
        page.wait_for_selector(".produkt")
        
        products = []
        
        # Alle Produkte durchgehen
        product_cards = page.locator(".produkt").all()
        
        for card in product_cards:
            product = {
                'name': card.locator(".name").text_content().strip(),
                'price': card.locator(".preis").text_content().strip(),
                'description': card.locator(".beschreibung").text_content().strip(),
                'rating': card.locator(".bewertung").text_content().strip(),
                'url': card.locator("a").get_attribute("href")
            }
            products.append(product)
        
        # Als CSV speichern
        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=products[0].keys())
            writer.writeheader()
            writer.writerows(products)
        
        print(f"✅ {len(products)} Produkte gescraped und in {output_file} gespeichert")
        
        browser.close()
    
    return products

# Verwendung
scrape_products("https://www.beispiel.de/produkte")
```

### Projekt 3: PDF-Generierung für Berichte

```python
from playwright.sync_api import sync_playwright
import glob
import os

def generate_report_pdf(report_url, output_dir='reports'):
    """Generiert PDF-Berichte aus Webseiten."""
    os.makedirs(output_dir, exist_ok=True)
    
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        # Mehrere Berichte generieren
        report_files = glob.glob('report_links.txt')
        
        with open('report_links.txt', 'r') as f:
            for line in f:
                url = line.strip()
                if url:
                    page.goto(url)
                    
                    # Auf Inhalte warten
                    page.wait_for_load_state("networkidle")
                    
                    # PDF generieren
                    filename = url.split('/')[-1] or "report"
                    pdf_path = f"{output_dir}/{filename}.pdf"
                    page.pdf(path=pdf_path, format="A4")
                    print(f"✅ PDF generiert: {pdf_path}")
        
        browser.close()

# report_links.txt enthalten URLs, eine pro Zeile
generate_report_pdf("https://www.beispiel.de/berichte")
```

### Projekt 4: Formular-Test mit Datenvalidierung

```python
from playwright.sync_api import sync_playwright, expect
import pytest

def test_form_validation():
    """Testet Formularvalidierung."""
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        
        page.goto("https://www.beispiel.de/registrierung")
        
        # Test: Leeres Formular abschicken
        page.locator("#submit").click()
        expect(page.locator(".error")).to_have_text("Bitte geben Sie Ihren Namen ein")
        
        # Test: Ungültige E-Mail
        page.locator("#name").fill("Max Mustermann")
        page.locator("#email").fill("ungueltig")
        page.locator("#submit").click()
        expect(page.locator(".error")).to_have_text("Bitte geben Sie eine gültige E-Mail-Adresse ein")
        
        # Test: Erfolgreiche Registrierung
        page.locator("#email").fill("max@beispiel.de")
        page.locator("#password").fill("sicheresPasswort123")
        page.locator("#submit").click()
        expect(page).to_have_url("https://www.beispiel.de/danke")
        
        browser.close()

# Test ausführen
test_form_validation()
```

---

## 📚 Ressourcen und weiterführende Links

### Offizielle Dokumentation
- [Playwright Documentation](https://playwright.dev/)
- [Playwright Python Documentation](https://playwright.dev/python/docs/intro)
- [Playwright GitHub](https://github.com/microsoft/playwright)
- [API Reference](https://playwright.dev/python/docs/api)

### Tutorials und Guides
- [Playwright Python Tutorial](https://playwright.dev/python/docs/tutorial)
- [Playwright Test Documentation](https://playwright.dev/python/docs/test-basics)
- [Web Scraping with Playwright](https://playwright.dev/python/docs/web-scraping)
- [Playwright vs Selenium](https://playwright.dev/python/docs/comparison)

### Community Ressourcen
- [Playwright Discord](https://discord.gg/playwright)
- [Playwright GitHub Discussions](https://github.com/microsoft/playwright/discussions)
- [Stack Overflow - Playwright](https://stackoverflow.com/questions/tagged/playwright)

### Alternativen
| Tool | Sprache | Multi-Browser | Speed | Test-Fokus |
|------|---------|---------------|-------|-----------|
| **Playwright** | Python/JS/Java/.NET | ✅ Ja | ✅✅✅✅✅ | ✅✅✅ |
| **Selenium** | Python/JS/Java/C# | ✅ Ja | ✅✅ | ✅✅ |
| **Puppeteer** | JavaScript | ❌ Nein | ✅✅✅✅ | ✅✅ |
| **Cypress** | JavaScript | ❌ Nein | ✅✅✅ | ✅✅✅ |
| **Robot Framework** | Python/Robot | ✅ Ja | ✅✅ | ✅✅✅ |

---

## 🔗 Verwandte Themen

* [Desktop Automation/Übersicht](index.md) – Umfassende Übersicht über Desktop-Automatisierungstools
* [Desktop Automation mit PyAutoGUI](pyautogui-anleitung.md) – GUI-Automatisierung mit Python
* [Desktop Automation mit ydotool](ydotool-anleitung.md) – Low-Level-Automatisierung auf Linux
* [Desktop Automation mit Robot Framework](robot-framework-anleitung.md) – Testautomatisierung mit Robot Framework

---

*Letzte Aktualisierung: Juli 2026*
