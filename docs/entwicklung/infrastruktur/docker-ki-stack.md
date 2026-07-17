# Docker-Compose Vorlagen: Lokaler KI & Server-Stack

Dieses Dokument enthält produktionsnahe `docker-compose.yml` Konfigurationen zum schnellen Aufsetzen lokaler KI- und Server-Infrastrukturen.

---

## 🐳 1. Komplettes KI-Backend (PostgreSQL + pgvector, Ollama, Open-WebUI & Nginx)

Erstelle eine `docker-compose.yml`:

```yaml
version: '3.8'

services:
  # Reverse Proxy
  nginx:
    image: nginx:latest
    container_name: ki_nginx
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - ./nginx/conf.d:/etc/nginx/conf.d
      - ./nginx/ssl:/etc/nginx/ssl
    restart: always
    depends_on:
      - open-webui

  # Datenbank mit Vektor-Unterstützung
  postgres:
    image: pgvector/pgvector:pg16
    container_name: ki_postgres
    environment:
      POSTGRES_DB: ki_db
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:-geheim123}
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data
    restart: always

  # LLM Engine
  ollama:
    image: ollama/ollama:latest
    container_name: ki_ollama
    ports:
      - "11434:11434"
    volumes:
      - ollama_storage:/root/.ollama
    # Für GPU-Unterstützung (Nvidia) folgende Zeilen einkommentieren:
    # deploy:
    #   resources:
    #     reservations:
    #       devices:
    #         - driver: nvidia
    #           count: 1
    #           capabilities: [gpu]
    restart: always

  # Web-Oberfläche für Ollama
  open-webui:
    image: ghcr.io/open-webui/open-webui:main
    container_name: ki_webui
    ports:
      - "3000:8080"
    environment:
      - OLLAMA_BASE_URL=http://ollama:11434
    volumes:
      - webui_data:/app/backend/data
    restart: always
    depends_on:
      - ollama

volumes:
  postgres_data:
  ollama_storage:
  webui_data:
```

---

## ⚙️ 2. Befehle & Verwaltung

```bash
# Stack im Hintergrund starten
docker compose up -d

# Status überprüfen
docker compose ps

# Modell in Ollama herunterladen
docker exec -it ki_ollama ollama pull llama3.2

# Logs anzeigen
docker compose logs -f
```

---

## 🔗 Verwandte Themen
* [PostgreSQL + pgvector](../../wissen/daten/datenbanken/pgvector-anleitung.md) – Vektordatenbank-Guide
* [Nginx Konfiguration](nginx.md) – Webserver-Setup
* [Lokales RAG & LLM-Serving](../../künstliche-intelligenz/coding/lokales-rag-ollama.md) – RAG-Pipeline
