# Praxis-Guide: Semantisches MediaWiki (SMW) SPARQL Endpoint

**SMW** kann RDF-Trippel in einen Graph-Store (z. B. Apache Jena / Blazegraph) exportieren. Über den **SPARQL-Endpoint** lassen sich komplexe semantische Graph-Abfragen über den gesamten Dokumentenbestand ausführen.

---

## 🔍 1. SPARQL Graph Query Beispielsyntax

```sparql
PREFIX wiki: <http://wiki.beispiel.de/id/>
PREFIX property: <http://wiki.beispiel.de/property/>

SELECT ?server ?ip ?os WHERE {
  ?server property:Hat_Servertyp "Webserver" .
  ?server property:Hat_IP ?ip .
  ?server property:Hat_OS ?os .
}
ORDER BY ?server
```

---

## 🐍 2. SPARQL Abfrage per Python (`sparql_query.py`)

```python
from SPARQLWrapper import SPARQLWrapper, JSON

sparql = SPARQLWrapper("http://wiki.beispiel.de/sparql")
sparql.setQuery("""
    PREFIX property: <http://wiki.beispiel.de/property/>
    SELECT ?server ?ip WHERE {
        ?server property:Hat_Servertyp "Webserver" .
        ?server property:Hat_IP ?ip .
    }
""")
sparql.setReturnFormat(JSON)
results = sparql.query().convert()

for result in results["results"]["bindings"]:
    print(f"Server: {result['server']['value']} | IP: {result['ip']['value']}")
```

---

## 🔗 Verwandte Themen
* [SMW Inline Queries](smw-inline-queries.md) – Inline Queries
* [MediaWiki Python Bot](../mediawiki/mediawiki-python-bot.md) – Wiki Botting
* [Semantisches MediaWiki Installieren](installieren.md) – SMW Setup
