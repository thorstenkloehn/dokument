# Praxis-Guide: PostgreSQL JSONB & GIN-Indizes

PostgreSQL bietet mit dem Datentyp `JSONB` vollwertige NoSQL-Dokumentenspeicherung mit binärer Komprimierung, Feldindizierung via **GIN-Indizes** und komplexen JSON-Operatoren (`@>`, `->>`).

---

## 📊 1. Tabelle mit JSONB-Spalte & GIN-Index erstellen

```sql
CREATE TABLE nutzer_profile (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    einstellungen JSONB NOT NULL DEFAULT '{}'::jsonb,
    erstellt_am TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- GIN-Index (Generalized Inverted Index) für ultraschnelle JSON-Suche anlegen
CREATE INDEX idx_nutzer_einstellungen ON nutzer_profile USING gin (einstellungen);
```

---

## 🔍 2. JSONB Daten einfügen & Abfragen

### Daten einfügen
```sql
INSERT INTO nutzer_profile (username, einstellungen)
VALUES (
    'thorsten',
    '{"theme": "dark", "notifications": {"email": true, "sms": false}, "tags": ["admin", "dev"]}'
);
```

### Abfrage 1: JSON-Verschachtelung abfragen (`->>`)
```sql
SELECT username 
FROM nutzer_profile 
WHERE einstellungen->'notifications'->>'email' = 'true';
```

### Abfrage 2: Enthält-Operator (`@>`) mit GIN-Index Nutzung
```sql
-- Prüft ob das JSON den Schlüssel/Wert-Paar enthält (nutzt den GIN-Index!)
SELECT username 
FROM nutzer_profile 
WHERE einstellungen @> '{"theme": "dark"}';
```

---

## 🔗 Verwandte Themen
* [PostgreSQL Performance Tuning](postgresql-tuning.md) – Tuning
* [PostgreSQL + pgvector](../../wissen/daten/datenbanken/pgvector-anleitung.md) – Vektordatenbanken
* [PostgreSQL Table Partitioning](postgresql-table-partitioning.md) – Partitionierung
