# Praxis-Guide: Semantisches MediaWiki (SMW) Inline Queries

**Semantisches MediaWiki (SMW)** verwandelt ein Standard-MediaWiki in eine kollaborative Datenbank. Mit **Inline Queries** (`{{#ask:...}}`) lassen sich dynamische Tabellen, Abfragen und Berichte direkt in Wiki-Seiten einbetten.

---

## 📊 1. Semantische Attribute definieren

Auf beliebigen Wiki-Seiten Attribute festlegen:

```mediawiki
[[Hat Status::Produktion]]
[[Hat Servertyp::Nginx]]
[[Hat IP::10.0.0.10]]
```

---

## 🔍 2. Dynamische Inline Query (`{{#ask:...}}`)

Erstelle eine dynamische Tabelle aller Produktionsserver:

```mediawiki
{{#ask:
 [[Hat Status::Produktion]]
 |?Hat Servertyp = Webserver Typ
 |?Hat IP = IP-Adresse
 |format=table
 |limit=20
 |sort=Hat IP
 |order=ascending
}}
```

---

## 🔗 Verwandte Themen
* [Semantisches MediaWiki Installieren](installieren.md) – SMW Setup
* [Evolution und Architekturen von Semantisches MediaWiki](evolution-digitaler-semantisches-mediawiki.md) – Vertiefung zu Generation 2
* [MediaWiki Python Bot](../mediawiki/mediawiki-python-bot.md) – Bot-Automatisierung
* [Dokumentenerstellung](../index.md) – Übersicht
