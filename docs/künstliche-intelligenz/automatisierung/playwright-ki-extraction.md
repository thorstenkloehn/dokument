# Praxis-Guide: Playwright & KI-Web-Scraping

Kombiniere Playwright zur Automatisierung von dynamischen Webseiten (SPA/JavaScript) mit lokalen LLMs zur garantierten Extrahierung von strukturierten Daten (JSON).

---

```mermaid
graph LR
    URL["🌐 Ziel-Webseite"] --> Playwright["🎭 Playwright Headless Browser"]
    Playwright --> HTML["📜 Gereinigtes HTML / DOM"]
    HTML --> LLM["🤖 LLM ("Ollama / DeepSeek")"]
    LLM --> JSON["📊 Strukturiertes JSON Format"]
```

---

## 🛠️ 1. Installation

```bash
pip install playwright langchain-ollama pydantic
playwright install chromium
```

---

## 🐍 2. Python Skript (`scraper.py`)

```python
import asyncio
from playwright.async_api import async_playwright
from langchain_ollama import ChatOllama
from pydantic import BaseModel, Field

# 1. Gewünschte JSON-Struktur mit Pydantic definieren
class EventItem(BaseModel):
    titel: str = Field(description="Titel der Veranstaltung")
    datum: str = Field(description="Datum oder Zeitangabe")
    ort: str = Field(description="Veranstaltungsort")
    preis: str = Field(description="Eintrittspreis oder Kostenfrei")

class EventList(BaseModel):
    events: list[EventItem]

# 2. HTML von dynamischer Webseite laden
async def fetch_page_html(url: str) -> str:
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        await page.goto(url, wait_until="networkidle")
        
        # HTML extrahieren & vereinfachen (Skripte & Styles entfernen)
        content = await page.evaluate("""() => {
            const clone = document.body.cloneNode(true);
            clone.querySelectorAll('script, style, svg, path').forEach(el => el.remove());
            return clone.innerText;
        }""")
        
        await browser.close()
        return content

# 3. LLM-basiertes Parsing
def parse_events_with_llm(text_content: str) -> EventList:
    llm = ChatOllama(model="llama3.2", temperature=0.0)
    structured_llm = llm.with_structured_output(EventList)
    
    prompt = f"Extrahiere alle Veranstaltungen aus folgendem Text:\n\n{text_content[:4000]}"
    result = structured_llm.invoke(prompt)
    return result

# 4. Hauptausführung
async def main():
    url = "https://example.com/events"
    print(f"Lade Webseite: {url}...")
    raw_text = await fetch_page_html(url)
    
    print("Analysiere Daten mit KI...")
    extracted_data = parse_events_with_llm(raw_text)
    
    print("\nExtrahierte Events (JSON):")
    print(extracted_data.model_dump_json(indent=2))

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🔗 Verwandte Themen
* [Playwright Anleitung](playwright-anleitung.md) – Grundlagen der Web-Automatisierung
* [PyAutoGUI Anleitung](pyautogui-anleitung.md) – GUI-Automatisierung
* [Lokales RAG & LLM-Serving](../coding/lokales-rag-ollama.md) – Ollama Integration
