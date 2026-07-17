# Praxis-Guide: MediaWiki Python Bot-Automatisierung

Skripting und Automatisierung von MediaWiki-Instanzen über die offizielle REST / Action API mit **mwclient**.

---

## 🛠️ 1. Installation

```bash
pip install mwclient
```

---

## 🐍 2. Python Skript (`wiki_bot.py`)

```python
import mwclient

# 1. Verbindung zu MediaWiki aufbauen
site = mwclient.Site('wiki.deine-domain.de', path='/')

# 2. Anmelden (Bot-Konto empfohlen)
site.login('BotUser', 'BotPassword123')

# 3. Seite lesen oder neu erstellen
page_name = 'Entwicklung/Python_Pipelines'
page = site.pages[page_name]

if page.exists:
    print(f"Seite '{page_name}' existiert bereits. Inhalt:")
    print(page.text()[:200])
else:
    # 4. Neue Seite erstellen
    content = """== Automatisch generierte Dokumentation ==
Diese Seite wurde automatisch per Python Bot erstellt.

=== Status ===
* API Status: Online
* Erstellt am: {{CURRENTTIMESTAMP}}
"""
    page.save(content, summary='Automatische Seitenerstellung per Python Bot')
    print(f"✅ Seite '{page_name}' erfolgreich angelegt!")
```

---

## 🔗 Verwandte Themen
* [MediaWiki Installieren](index.md) – Installation & Setup
* [Semantisches MediaWiki](../semantische-mediawiki/installieren.md) – Semantische Erweiterung
* [Pandoc Export-Pipeline](../../tools/pandoc-export-pipeline.md) – Dokumentenkonvertierung
