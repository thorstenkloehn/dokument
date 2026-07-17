# Praxis-Guide: Microsoft Semantic Kernel in Python

**Semantic Kernel** ist ein Enterprise AI SDK von Microsoft zur einfachen Integration von LLMs mit nativen Python-Funktionen (Native Plugins), Prompts (Semantic Functions) und externen Vektorspeichern.

---

## 🛠️ 1. Installation

```bash
pip install semantic-kernel
```

---

## 🐍 2. Python Skript (`kernel_demo.py`)

```python
import asyncio
import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

# 1. Kernel initialisieren
kernel = sk.Kernel()

# 2. LLM Service konfigurieren (Ollama oder OpenAI)
kernel.add_service(
    OpenAIChatCompletion(
        service_id="local-llm",
        ai_model_id="llama3.1",
        api_key="ollama",
        endpoint="http://localhost:11434/v1"
    )
)

# 3. Nativ-Plugin definieren
class CalculatorPlugin:
    @sk.kernel_function(description="Berechnet die Summe zweier Zahlen", name="Add")
    def add(self, a: float, b: float) -> float:
        return float(a) + float(b)

kernel.add_plugin(CalculatorPlugin(), plugin_name="MathPlugin")

# 4. Ausführung
async def main():
    result = await kernel.invoke(
        plugin_name="MathPlugin",
        function_name="Add",
        a=15.5,
        b=4.5
    )
    print(f"Ergebnis aus Nativ-Plugin: {result}")

if __name__ == "__main__":
    asyncio.run(main())
```

---

## 🔗 Verwandte Themen
* [AutoGen Multi-Agent Framework](autogen-multiagent-framework.md) – AutoGen Agenten
* [Agentic Workflows (LangGraph)](agentic-workflows-langgraph.md) – LangGraph
* [Structured LLM Outputs (Pydantic)](structured-outputs-pydantic.md) – Pydantic Schemas
