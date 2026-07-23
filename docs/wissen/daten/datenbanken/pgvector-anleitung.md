# Praxis-Guide: PostgreSQL + pgvector (Semantische Suche in der Praxis)

`pgvector` ist eine Open-Source-Erweiterung für PostgreSQL, die Vektoreinbettungen (Embeddings) direkt in deiner relationalen PostgreSQL-Datenbank speichert und hocheffizient durchsucht.

---

## 🛠️ 1. Installation & Aktivierung

### Extension in PostgreSQL aktivieren
```sql
CREATE EXTENSION IF NOT EXISTS vector;
```

---

## 📊 2. Tabellen-Setup & Vektor-Indizierung

### Tabelle mit Vektor-Spalte erstellen
```sql
CREATE TABLE dokumente (
    id BIGSERIAL PRIMARY KEY,
    titel TEXT NOT NULL,
    inhalt TEXT NOT NULL,
    embedding VECTOR(1536), -- 1536 Dimensionen (z. B. OpenAI text-embedding-3-small)
    erstellt_am TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);
```

### HNSW-Index für ultraschnelle Ähnlichkeitssuche anlegen
```sql
-- Hierarchical Navigable Small World (HNSW) Index für Kosinus-Ähnlichkeit
CREATE INDEX ON dokumente 
USING hnsw (embedding vector_cosine_ops)
WITH (m = 16, ef_construction = 64);
```

---

## 🔍 3. Daten einfügen & Semantische Suche

### Vektor-Daten einfügen
```sql
INSERT INTO dokumente (titel, inhalt, embedding)
VALUES (
    'Nginx SSL Anleitung',
    'So konfigurierst du Let''s Encrypt SSL-Zertifikate in Nginx.',
    '[-0.012, 0.045, 0.003, ...]' -- Array mit 1536 Zahlen
);
```

### K-Nearest-Neighbors (k-NN) Abfrage ausführen
```sql
-- Finde die 3 ähnlichsten Dokumente basierend auf der Kosinus-Distanz (<=>)
SELECT 
    id, 
    titel, 
    1 - (embedding <=> '[-0.010, 0.042, 0.001, ...]') AS aehnlichkeit
FROM dokumente
ORDER BY embedding <=> '[-0.010, 0.042, 0.001, ...]'
LIMIT 3;
```

---

## 🐍 4. Python-Integration mit Psycopg3

```python
import psycopg
from pgvector.psycopg import register_vector

# Verbindung aufbauen
conn = psycopg.connect("dbname=dokumente_db user=postgres password=geheim host=localhost")
register_vector(conn)

# Vektorsuche abfragen
query_embedding = [0.012, -0.034, ...] # 1536 Float-Werte

with conn.cursor() as cur:
    cur.execute("""
        SELECT titel, inhalt, 1 - (embedding <=> %s) AS score
        FROM dokumente
        ORDER BY embedding <=> %s
        LIMIT 5
    """, (query_embedding, query_embedding))
    
    for row in cur.fetchall():
        print(f"[{row[2]:.2f}] {row[0]}: {row[1][:50]}...")
```

---

## 🔗 Verwandte Themen
* [Datenbanken Übersicht](index.md) – Vektordatenbank-Überblick
* [Lokales RAG & LLM-Serving](../../../künstliche-intelligenz/coding/lokales-rag-ollama.md) – RAG mit Ollama
