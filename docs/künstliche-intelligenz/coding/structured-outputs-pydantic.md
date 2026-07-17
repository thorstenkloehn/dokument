# Praxis-Guide: Structured LLM Outputs mit Pydantic & Instructor

Für produktive Anwendungen müssen KI-Modelle Daten in einem strikt definierten JSON-Format ohne Syntax-Fehler oder Halluzinationen zurückgeben. Mit **Instructor** und **Pydantic** erzwingst du valide Datenstrukturen.

---

```mermaid
graph LR
    Prompt["📝 User Prompt / Eingabe"] --> Instructor["🛡️ Instructor + Pydantic Validator"]
    Instructor --> LLM["🤖 LLM ("Ollama / OpenAI")"]
    LLM -->|Validierung fehlgeschlagen| ReTry["🔄 Auto-Retry Prompt mit Pydantic Fehler"]
    ReTry --> LLM
    LLM -->|Erfolgreich| VerifiedJSON["📊 Valides Pydantic Objekt / JSON"]
```

---

## 🛠️ 1. Installation

```bash
pip install instructor pydantic langchain-ollama
```

---

## 🐍 2. Python Skript (`structured_extraction.py`)

```python
import instructor
from pydantic import BaseModel, Field
from openai import OpenAI

# 1. Pydantic-Schema definieren
class SoftwareFeature(BaseModel):
    feature_name: str = Field(description="Name des Software-Features")
    aufwand_stunden: int = Field(description="Geschätzter Entwicklungsaufwand in Stunden")
    prioritaet: str = Field(description="Priorität: Hoch, Mittel oder Niedrig")

class ProjectEstimation(BaseModel):
    projekt_titel: str
    features: list[SoftwareFeature]
    gesamt_aufwand_stunden: int

# 2. Client initialisieren (Ollama via OpenAI API-Format)
client = instructor.from_openai(
    OpenAI(
        base_url="http://localhost:11434/v1",
        api_key="ollama"
    ),
    mode=instructor.Mode.JSON
)

# 3. Strukturierte Extraktion ausführen
def estimate_project(requirements_text: str) -> ProjectEstimation:
    resp = client.chat.completions.create(
        model="llama3.2",
        response_model=ProjectEstimation,
        messages=[
            {"role": "system", "content": "Du bist ein erfahrener IT-Projektleiter."},
            {"role": "user", "content": f"Schätze folgendes Projekt ab:\n{requirements_text}"}
        ]
    )
    return resp

# Ausführen
if __name__ == "__main__":
    requirements = """
    Wir benötigen eine Nginx SSL-Konfiguration für einen Kachelserver sowie ein 
    PostgreSQL Datenbank-Backup-Skript mit E-Mail Benachrichtigung.
    """
    estimation = estimate_project(requirements)
    print(estimation.model_dump_json(indent=2))
```

---

## 🔗 Verwandte Themen
* [Lokales RAG & LLM-Serving](lokales-rag-ollama.md) – RAG mit Ollama
* [Playwright & KI Web-Scraping](../automatisierung/playwright-ki-extraction.md) – Datenextraktion
* [Agentic Workflows](agentic-workflows-langgraph.md) – Multi-Agenten Systeme
