# Praxis-Guide: PostgreSQL Volltextsuche mit tsvector & GIN

PostgreSQL bietet eine leistungsfähige, integrierte **Volltextsuche** mit Stammformenreduktion (Stemming), Stoppwort-Filterung und Relevanz-Ranking (`ts_rank`), die externe Suchmaschinen wie Elasticsearch für viele Anwendungsfälle überflüssig macht.

---

## 📊 1. Tabelle mit Volltextsuche-Spalte & GIN-Index erstellen

```sql
CREATE TABLE artikel (
    id BIGSERIAL PRIMARY KEY,
    titel TEXT NOT NULL,
    inhalt TEXT NOT NULL,
    -- Generierte Spalte für Volltextsuche (auf Deutsch)
    such_vector TSVECTOR GENERATED ALWAYS AS (
        to_tsvector('german', coalesce(titel, '') || ' ' || coalesce(inhalt, ''))
    ) STORED
);

-- GIN-Index für extrem schnelle Volltextsuche anlegen
CREATE INDEX idx_artikel_suche ON artikel USING gin (such_vector);
```

---

## 🔍 2. Abfragen mit Stemming & Ranking (`tsquery`)

```sql
-- Suche nach Artikeln mit den Begriffen "Datenbank" UND "Sicherheit"
SELECT 
    titel, 
    ts_rank(such_vector, to_tsquery('german', 'datenbank & sicherheit')) AS rank
FROM artikel
WHERE such_vector @@ to_tsquery('german', 'datenbank & sicherheit')
ORDER BY rank DESC;
```

---

## 🔗 Verwandte Themen
* [PostgreSQL JSONB & GIN-Indizes](postgresql-jsonb-gin-indexes.md) – NoSQL & JSON
* [PostgreSQL + pgvector](../../wissen/daten/datenbanken/pgvector-anleitung.md) – Vektorsuche
* [PostgreSQL Performance Tuning](postgresql-tuning.md) – Datenbank-Tuning
