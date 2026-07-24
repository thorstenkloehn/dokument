# Praxis-Guide: Agentic Workflows mit LangGraph & CrewAI

Multi-Agenten-Systeme ermöglichen die Aufteilung komplexer Aufgaben (z. B. Recherche, Code-Generierung, Code-Review) auf spezialisierte autonome Agenten.

---

```mermaid
graph TD
    User["👤 Benutzer-Auftrag"] --> Router["🧠 Supervisor / Router Agent"]
    Router --> Researcher["🔍 Research Agent ("Web & Doku")"]
    Router --> Coder["💻 Coding Agent (Code-Erstellung)"]
    Researcher --> Reviewer["📋 Review Agent ("Qualitätsprüfung")"]
    Coder --> Reviewer
    Reviewer -->|Korrektur nötig| Coder
    Reviewer -->|Bestanden| FinalOutput["✨ Finales Ergebnis"]
```

---

## 🛠️ 1. Installation

```bash
pip install langgraph langchain-ollama crewai
```

---

## 🐍 2. Python Skript mit LangGraph (`agent_graph.py`)

```python
from typing import Annotated, TypedDict
from langchain_ollama import ChatOllama
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages

# State-Definition
class State(TypedDict):
    messages: Annotated[list, add_messages]

# LLM initialisieren
llm = ChatOllama(model="llama3.2", temperature=0.2)

# Agenten-Knoten definieren
def researcher(state: State):
    prompt = f"Recherchiere die wichtigsten Punkte zu: {state['messages'][-1].content}"
    response = llm.invoke(prompt)
    return {"messages": [response]}

def writer(state: State):
    prompt = f"Schreibe eine zusammenfassende Dokumentation basierend auf: {state['messages'][-1].content}"
    response = llm.invoke(prompt)
    return {"messages": [response]}

# Graph aufbauen
graph_builder = StateGraph(State)
graph_builder.add_node("researcher", researcher)
graph_builder.add_node("writer", writer)

graph_builder.add_edge(START, "researcher")
graph_builder.add_edge("researcher", "writer")
graph_builder.add_edge("writer", END)

graph = graph_builder.compile()

# Ausführen
if __name__ == "__main__":
    result = graph.invoke({"messages": [("user", "Erstelle eine Zusammenfassung über Rust vs Go für Backend-Services")]})
    print("Ergebnis:", result["messages"][-1].content)
```

---

## 🔗 Verwandte Themen
* [Vibe Coding & Engineering](vibe-coding-engineering.md) – Entwickeln mit KI-Assistenten
* [Lokales RAG & LLM-Serving](lokales-rag-ollama.md) – Lokales Serving
* [Playwright & KI Web-Scraping](../automatisierung/playwright-ki-extraction.md) – Datenbeschaffung
* [Beste Self-Hosting-KI-Agenten (Allgemein, Top 20)](selbsthosting-ki-agenten-topliste.md) – LangGraph im Vergleich zu anderen Frameworks
* [Beste Cloud-KI-Agenten (Allgemein, Top 20)](cloud-ki-agenten-topliste.md) – gehostete Alternative (LangGraph Platform)
