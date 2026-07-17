# Praxis-Guide: Lokales RAG & LLM-Serving mit Ollama & ChromaDB

Dieser Leitfaden beschreibt den Aufbau einer vollständig lokalen, datenschutzkonformen RAG-Pipeline (Retrieval-Augmented Generation) zur Durchsuchung eigener Dokumente ohne externe Cloud-APIs.

---

```mermaid
graph LR
    Doc["📄 Eigene Dokumente ("PDF/MD/TXT")"] --> Embed["🔤 Embedding-Modell (nomic-embed-text)"]
    Embed --> VectorDB["📦 Vektordatenbank (ChromaDB)"]
    User["👤 Benutzer-Frage"] --> VectorDB
    VectorDB --> Context["🔍 Relevanter Kontext"]
    Context --> Ollama["🤖 Ollama LLM ("Llama 3 / DeepSeek")"]
    Ollama --> Answer["💬 Präzise Antwort mit Quellen"]
```

---

## 🚀 1. Voraussetzungen & Installation

### Ollama installieren
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### Benötigte Modelle herunterladen
```bash
# LLM für die Antwort-Generierung
ollama pull llama3.2

# Embedding-Modell für Vektorumwandlung
ollama pull nomic-embed-text
```

---

## 🐍 2. Python RAG-Pipeline mit LangChain

### Abhängigkeiten installieren
```bash
pip install langchain langchain-community langchain-ollama chromadb
```

### Python-Skript (`rag_pipeline.py`)
```python
from langchain_community.document_loaders import TextLoader, DirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, ChatOllama
from langchain_community.vectorstores import Chroma
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

# 1. Dokumente laden & aufteilen
loader = DirectoryLoader('./docs', glob="**/*.md", loader_cls=TextLoader)
docs = loader.load()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = text_splitter.split_documents(docs)

# 2. Embeddings & Vektorspeicher initialisieren
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = Chroma.from_documents(documents=chunks, embedding=embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 3})

# 3. LLM & Prompt-Template
llm = ChatOllama(model="llama3.2", temperature=0.2)

system_prompt = (
    "Du bist ein Assistent für Fragen-Antworten. "
    "Nutze den folgenden Kontext, um die Frage zu beantworten: \n\n"
    "{context}"
)
prompt = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{input}"),
])

# 4. Chain erstellen & ausführen
question_answer_chain = create_stuff_documents_chain(llm, prompt)
rag_chain = create_retrieval_chain(retriever, question_answer_chain)

response = rag_chain.invoke({"input": "Wie richte ich Nginx SSL ein?"})
print("Antwort:", response["answer"])
```

---

## 🌐 3. Web-UI mit Open-WebUI

Für eine ChatGPT-ähnliche Benutzeroberfläche kann **Open-WebUI** via Docker gestartet werden:

```bash
docker run -d -p 3000:8080 \
  --add-host=host.docker.internal:host-gateway \
  -v open-webui:/app/backend/data \
  --name open-webui \
  --restart always \
  ghcr.io/open-webui/open-webui:main
```

Unter `http://localhost:3000` steht nun ein lokales Web-Interface zur Verfügung.

---

## 🔗 Verwandte Themen
* [PostgreSQL + pgvector](../../wissen/daten/datenbanken/pgvector-anleitung.md) – Vektorspeicherung in PostgreSQL
* [Docker KI-Stack](../../entwicklung/infrastruktur/docker-ki-stack.md) – Fertiges Container-Setup
* [Lokale KI-Frontends](../../entwicklung/ide/lokale-ki-frontends.md) – Übersicht moderner KI-UIs
