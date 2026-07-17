# Praxis-Guide: Lokaler AI Code-Assistant mit Continue.dev & Ollama

**Continue.dev** ist ein Open-Source AI-Coding Assistant für VS Code und JetBrains, der vollständig lokal mit **Ollama** betrieben werden kann – ohne Daten an externe Cloud-Dienste zu senden.

---

```mermaid
graph LR
    IDE["💻 VS Code / JetBrains"] --> Continue["🔌 Continue.dev Extension"]
    Continue -->|Autocompletion (StarCoder)| Ollama1["🤖 Ollama (qwen2.5-coder:1.5b)"]
    Continue -->|Chat & Edit (DeepSeek)| Ollama2["🤖 Ollama (qwen2.5-coder:7b / deepseek-r1)"]
```

---

## 🛠️ 1. Vorbereitung & Ollama Modelle laden

```bash
# Modell für Tab-Autovervollständigung (schnell)
ollama pull qwen2.5-coder:1.5b

# Modell für Chat & Refactoring (leistungsstark)
ollama pull qwen2.5-coder:7b
```

---

## ⚙️ 2. Continue.dev Konfiguration (`~/.continue/config.json`)

```json
{
  "models": [
    {
      "title": "Local Qwen 7B (Chat & Edit)",
      "provider": "ollama",
      "model": "qwen2.5-coder:7b"
    }
  ],
  "tabAutocompleteModel": {
    "title": "Local Qwen 1.5B (Autocomplete)",
    "provider": "ollama",
    "model": "qwen2.5-coder:1.5b"
  },
  "customCommands": [
    {
      "name": "test",
      "prompt": "Schreibe Unit Tests für den markierten Code mit Pytest.",
      "description": "Erstelle automatische Unit Tests"
    }
  ]
}
```

---

## 💡 3. Nützliche Tastenkombinationen

* `Ctrl + L` / `Cmd + L`: Öffnet den Continue-Chat im Seitenfenster.
* `Ctrl + I` / `Cmd + I`: Markierten Code im Editor direkt bearbeiten (Inline Edit).
* `Tab`: Autovervollständigung akzeptieren.

---

## 🔗 Verwandte Themen
* [Programmieren mit KI](programmieren-mit-ki.md) – Entwicklungs-Workflow
* [Lokales RAG & LLM-Serving](lokales-rag-ollama.md) – Ollama Serving
* [Lokale KI-Frontends](../../entwicklung/ide/lokale-ki-frontends.md) – Übersicht lokaler Frontends
