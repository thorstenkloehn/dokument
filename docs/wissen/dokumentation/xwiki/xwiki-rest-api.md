# Praxis-Guide: XWiki REST API & Python Integration

**XWiki** verfügt über eine mächtige REST-API zur programmatischen Erstellung, Abfrage und Aktualisierung von Wiki-Seiten, Objektmodellen und Anhängen.

---

## 🛠️ 1. Installation der Python Bibliothek

```bash
pip install requests
```

---

## 🐍 2. Python Skript (`xwiki_api.py`)

```python
import requests
from requests.auth import HTTPBasicAuth

XWIKI_URL = "http://localhost:8080/xwiki/rest"
AUTH = HTTPBasicAuth("admin", "admin_password")
HEADERS = {"Accept": "application/json", "Content-Type": "application/json"}

# 1. Alle Seiten in einem Space abfragen
def get_space_pages(wiki="xwiki", space="Main"):
    url = f"{XWIKI_URL}/wikis/{wiki}/spaces/{space}/pages"
    response = requests.get(url, auth=AUTH, headers=HEADERS)
    if response.status_code == 200:
        return response.json().get("pageSummaries", [])
    return []

# 2. Neue Seite in XWiki erstellen
def create_xwiki_page(wiki="xwiki", space="Main", page_title="NeueSeite", content="= Überschrift =\nInhalt..."):
    url = f"{XWIKI_URL}/wikis/{wiki}/spaces/{space}/pages/{page_title}"
    payload = {
        "title": page_title,
        "content": content,
        "syntax": "xwiki/2.1"
    }
    response = requests.put(url, json=payload, auth=AUTH, headers=HEADERS)
    if response.status_code in [200, 201]:
        print(f"✅ XWiki Seite '{page_title}' erfolgreich angelegt!")
    else:
        print(f"❌ Fehler: {response.status_code} - {response.text}")

if __name__ == "__main__":
    create_xwiki_page(page_title="API_Dokumentation", content="= Automatische Dokumentation =\nErstellt per REST-API.")
```

---

## 🔗 Verwandte Themen
* [XWiki Installieren](installieren.md) – XWiki Setup
* [MediaWiki Python Bot](../mediawiki/mediawiki-python-bot.md) – MediaWiki API
* [Dokumentenerstellung](../index.md) – Wissensmanagement
