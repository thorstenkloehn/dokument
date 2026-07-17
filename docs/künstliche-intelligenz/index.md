# KI-Modelle & Frameworks: Übersicht

Eine zentralisierte Übersicht über künstliche Intelligenz-Modelle, Sprachmodelle (LLMs), Diffusionsmodelle, Frameworks und Bibliotheken für Entwicklung, Training und Deployment.

---

## 🤖 KI-Modell-Landschaft

Die Welt der KI-Modelle entwickelt sich rasant. Von kleinen, effizienten Modellen für lokale Ausführung bis hin zu großen, leistungsfähigen Modellen für Cloud-Deployment – diese Übersicht hilft dir, den Überblick zu behalten.

### Modell-Kategorien im Überblick

| Kategorie | Beschreibung | Typische Anwendungen | Beispiele |
|-----------|--------------|---------------------|-----------|
| **Sprachmodelle (LLMs)** | Modelle für Textverarbeitung, Code-Generierung, Dialoge | Chatbots, Code-Assistenten, Textgenerierung | Llama, Mistral, Phi, GPT |
| **Diffusionsmodelle** | Generative Modelle für Bilder, Audio, Video | Bildgenerierung, Inpainting, Stil-Transfer | Stable Diffusion, FLUX, Kandinsky |
| **Multimodale Modelle** | Modelle, die mehrere Modalitäten kombinieren | Bild+Text, Audio+Text, Video+Text | CLIP, BLIP, GPT-4 Vision |
| **Embedding-Modelle** | Modelle zur Vektordarstellung von Daten | Suche, Ähnlichkeitsvergleich, RAG | Sentence-Transformers, CLAP, BERT |
| **Bildklassifizierung** | Modelle zur Kategorisierung von Bildern | Objekterkennung, Bildanalyse | ResNet, ViT, EfficientNet |
| **Sprachverarbeitung** | Modelle für Audio und Sprache | TTS, STT, Übersetzungen | Whisper, Kokoro, Wav2Vec |
| **Empfehlungssysteme** | Modelle für personalisierte Empfehlungen | Produktempfehlungen, Content-Empfehlungen | Collaborative Filtering, Neural CF |
| **Zeitreihenmodelle** | Modelle für zeitliche Daten | Vorhersagen, Anomalie-Erkennung | LSTM, Transformer, Prophet |

---

## 📚 Hauptthemen

### 1. Sprachmodelle (Large Language Models - LLMs)

**Sprachmodelle für Textverarbeitung, Code-Generierung und Dialogsysteme.**

* **Anwendungsbereiche**:
  - Textgenerierung (Artikel, Code, Dokumentation)
  - Dialogsysteme (Chatbots, Virtuelle Assistenten)
  - Code-Generierung und -Vervollständigung
  - Übersetzungen zwischen Sprachen
  - Textklassifizierung und -analyse

* **Modell-Typen**:
  - **Base Models**: Grundmodelle für allgemeine Aufgaben (Llama, Mistral)
  - **Instruction-Tuned Models**: Feinabgestimmte Modelle für spezifische Aufgaben (Llama-3-Instruct, Mistral-Instruct)
  - **Chat-Optimized Models**: Spezialisierte Dialogmodelle (ChatML, Vicuna)
  - **Code-Specialized Models**: Für Programmieraufgaben optimiert (CodeLlama, DeepSeek-Coder)

* **Modell-Familien**:
  
| Modell | Entwickler | Größe | Lizenz | Besonderheiten |
|--------|------------|-------|--------|----------------|
| **Llama 3** | Meta | 8B - 70B | Open | Hochwertige Dialoge, Code-Fähigkeiten |
| **Mistral** | Mistral AI | 7B - 70B | Open | Effizient, mehrsprachig |
| **Phi-3** | Microsoft | 3.8B - 14B | Open | Kompakt, effizient |
| **GPT-4 / GPT-4o** | OpenAI | - | Closed | State-of-the-Art Performance |
| **Claude 3** | Anthropic | - | Closed | Hochwertige Dialoge, Vision |
| **Gemini** | Google | - | Closed | Multimodal, integriert |
| **DeepSeek** | DeepSeek | 7B - 67B | Open | Code-spezialisiert |
| **Qwen** | Alibaba | 7B - 72B | Open | Mehrsprachig, Code |

---

### 2. Diffusionsmodelle

**Generative Modelle für die Erstellung von Bildern, Audio und Video.**

* **Anwendungsbereiche**:
  - Text-zu-Bild Generierung (Text-to-Image)
  - Bild-zu-Bild Transformationen (Inpainting, Outpainting)
  - Stil-Transfer und Bildbearbeitung
  - Super-Resolution und Upscaling
  - Video-Generierung (Text-to-Video, Image-to-Video)

* **Modell-Typen**:
  - **Text-to-Image**: Generierung von Bildern aus Textbeschreibungen
  - **Image-to-Image**: Transformation bestehender Bilder
  - **Inpainting**: Rekonstruktion fehlender Bildbereiche
  - **ControlNet**: Steuerung der Generierung durch zusätzliche Eingaben (Kanten, Pose, etc.)
  - **Text-to-Video**: Generierung von Videos aus Text
  - **Image-to-Video**: Erstellung von Videos aus Bildern

* **Beliebte Diffusionsmodelle**:

| Modell | Typ | Entwickler | Besonderheiten |
|--------|-----|------------|----------------|
| **Stable Diffusion 3** | T2I | Stability AI | Offenes Ökosystem, viele Derivate |
| **FLUX** | T2I | Black Forest Labs | Hochwertige Ergebnisse |
| **Kandinsky 3** | T2I | Sberbank | Russian LLM + Diffusion |
| **Midjourney** | T2I | Midjourney | Closed, hochwertig |
| **DALL-E 3** | T2I | OpenAI | Closed, integriert mit ChatGPT |
| **Stable Video Diffusion** | T2V | Stability AI | Video-Generierung |
| **AnimateDiff** | Extension | - | Bewegungsverbesserung |
| **Deforum** | Toolkit | - | Automatisierte Video-Generierung |

---

### 3. Multimodale Modelle

**Modelle, die mehrere Modalitäten (Text, Bild, Audio, Video) kombinieren.**

* **Anwendungsbereiche**:
  - Bildbeschreibung (Image Captioning)
  - Visuelle Fragebeantwortung (VQA)
  - Text-zu-Bild mit Kontextverständnis
  - Audio-Text-Kombinationen
  - Video-Verständnis und -Generierung

* **Modell-Beispiele**:

| Modell | Modalitäten | Entwickler | Anwendungen |
|--------|-------------|------------|--------------|
| **GPT-4 Vision** | Text + Bild + Audio | OpenAI | Multimodale Dialoge |
| **Claude 3** | Text + Bild | Anthropic | Visuelles Verständnis |
| **Gemini 1.5** | Text + Bild + Audio + Video | Google | Multimodale Aufgaben |
| **LLaVA** | Text + Bild | Open Source | Visuelle Fragebeantwortung |
| **BLIP / BLIP-2** | Text + Bild | Salesforce | Bildbeschreibung, VQA |
| **Fuyu-8B** | Text + Bild | Adept AI | Interaktive Bildbearbeitung |
| **CLIP** | Text + Bild | OpenAI | Zero-Shot Klassifizierung |

---

### 4. Embedding-Modelle

**Modelle zur Erstellung von Vektordarstellungen (Embeddings) für Suche, Ähnlichkeit und Retrieval.**

* **Anwendungsbereiche**:
  - Semantische Suche
  - Ähnlichkeitsvergleich
  - Retrieval-Augmented Generation (RAG)
  - Clusteranalyse
  - Empfehlungssysteme

* **Modell-Beispiele**:

| Modell | Typ | Dimension | Entwickler | Anwendungen |
|--------|-----|-----------|------------|--------------|
| **all-MiniLM-L6-v2** | Text | 384 | Sentence-Transformers | Allround-Embeddings |
| **all-mpnet-base-v2** | Text | 768 | Sentence-Transformers | Hochwertige Embeddings |
| **text-embedding-3-small** | Text | 1536 | OpenAI | Optimiert für RAG |
| **text-embedding-3-large** | Text | 3072 | OpenAI | Hochgenau |
| **bge-base-en-v1.5** | Text | 768 | FlagEmbedding | BAAI Optimiert |
| **CLAP** | Bild + Text | 512 | LAION | Cross-Modal Retrieval |
| **ImageBind** | Bild + Text + Audio | 1024 | Meta | Multimodal Embeddings |

---

### 5. Bildverarbeitungsmodelle

**Modelle für Klassifizierung, Objekterkennung, Segmentierung und Bildanalyse.**

* **Klassifizierung**:
  - ResNet (50, 101, 152)
  - ViT (Vision Transformer)
  - EfficientNet (B0-B7)
  - ConvNeXt

* **Objekterkennung**:
  - YOLO (v8, v9, NAS)
  - Faster R-CNN
  - DETR (DEtection TRansformer)
  - Grounding DINO

* **Segmentierung**:
  - Segment Anything Model (SAM)
  - Mask R-CNN
  - U-Net
  - DeepLab

* **Pose-Estimation**:
  - MediaPipe Pose
  - OpenPose
  - HRNet
  - ViTPose

---

### 6. Sprachverarbeitungsmodelle

**Modelle für Text-to-Speech (TTS), Speech-to-Text (STT) und Übersetzungen.**

* **Speech-to-Text (STT)**:
  - Whisper (OpenAI) – Multilingual, Offline-fähig
  - Wav2Vec 2.0 (Facebook) – Selbstüberwachtes Lernen
  - Vosk – Offline, Open Source
  - DeepSpeech (Mozilla) – Einfach, effizient

* **Text-to-Speech (TTS)**:
  - Kokoro-ONNX – Hochwertig, offline
  - Coqui TTS – Open Source, mehrsprachig
  - Tortoise-TTS – Natürlich klingend
  - Piper – Leichtgewichtig, offline

* **Übersetzung**:
  - NLLB (Meta) – 200+ Sprachen
  - MarianMT – Open Source Transformers
  - OPUS-MT – Hochwertige Übersetzungen

---

## 🛠️ Frameworks & Bibliotheken

### Deep Learning Frameworks

| Framework | Sprache | Fokus | Besonderheiten |
|-----------|---------|-------|----------------|
| **PyTorch** | Python | Forschung, Produktion | Flexibel, große Community |
| **TensorFlow** | Python | Produktion, Deployment | TensorBoard, TF Serving |
| **JAX** | Python | Forschung, HPC | Autograd, VPU/Optimierung |
| **Keras** | Python | Einfachheit | Hochlevel API für TF |
| **ONNX** | - | Interoperabilität | Format für Modell-Austausch |

### Inference & Deployment Frameworks

| Framework | Sprache | Fokus | Besonderheiten |
|-----------|---------|-------|----------------|
| **vLLM** | Python | LLM Inference | PagedAttention, Hochperformant |
| **Text Generation WebUI** | Python | LLM UI | Oobabooga, viele Backends |
| **Ollama** | Go | Lokale Modelle | Einfach, cross-platform |
| **LM Studio** | - | GUI für LLMs | Lokale Ausführung |
| **Triton Inference Server** | Python/C++ | Enterprise | NVIDIA, Multi-Modell |
| **FastAPI + LangChain** | Python | API-Integration | Schnell, flexibel |

### Feinabstimmung & Training

| Framework | Sprache | Fokus | Besonderheiten |
|-----------|---------|-------|----------------|
| **Hugging Face Transformers** | Python | Feinabstimmung | 100.000+ vorgefertigte Modelle |
| **LoRA (Low-Rank Adaptation)** | Python | Effizientes Fine-Tuning | Speichereffizient |
| **QLoRA** | Python | Quantisiertes LoRA | 4-Bit Training möglich |
| **PEFT** | Python | Parameter-Effizientes FT | Viele Methoden |
| **BitsandBytes** | Python | 8-Bit/4-Bit Training | Speicheroptimierung |
| **Alpaca / LLaMA-Factory** | Python | Instruction-Tuning | Einfach zu bedienen |

---

## 🎯 Praxisbeispiele

### Beispiel 1: Lokale KI-Chat-Anwendung

**Anforderungen:**
- Lokale Ausführung ohne Cloud
- Gute Performance auf Consumer-Hardware
- Unterstützung für RAG

**Lösung:**
```python
# 1. Modell laden mit Ollama
from langchain_community.llms import Ollama
llm = Ollama(model="llama3:8b-instruct")

# 2. Embeddings für RAG
from langchain.embeddings import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

# 3. Vektordatenbank
from langchain.vectorstores import Chroma
vectorstore = Chroma.from_documents(documents, embeddings)

# 4. RAG-Kette erstellen
from langchain.chains import RetrievalQA
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# 5. Frage beantworten
result = qa.run("Was steht im Dokument über KI-Modelle?")
```

**Empfohlene Modelle:** Llama 3 8B, Mistral 7B, Phi-3 14B

---

### Beispiel 2: Bildgenerierung mit Stable Diffusion

**Anforderungen:**
- Text-zu-Bild Generierung
- Lokale Ausführung
- Kontrolle über den Generierungsprozess

**Lösung:**
```python
from diffusers import StableDiffusionPipeline
import torch

# 1. Pipeline laden
pipe = StableDiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-3-medium",
    torch_dtype=torch.float16
).to("cuda")

# 2. Bild generieren
prompt = "A futuristic city at night, cyberpunk style, neon lights"
image = pipe(prompt).images[0]

# 3. Bild speichern
image.save("futuristic_city.png")
```

**Empfohlene Modelle:** Stable Diffusion 3, FLUX, Kandinsky 3

---

### Beispiel 3: Multimodale Anwendung (Bild + Text)

**Anforderungen:**
- Bildbeschreibung
- Visuelle Fragebeantwortung
- Kombinierte Text+Bild-Analyse

**Lösung:**
```python
from transformers import pipeline

# 1. Bildbeschreibung (Image Captioning)
captioner = pipeline("image-to-text", model="Salesforce/blip-image-captioning-large")
result = captioner("photo.jpg")
print(result[0]['generated_text'])

# 2. Visuelle Fragebeantwortung (VQA)
vqa = pipeline("visual-question-answering", model="dandelin/vilt-b32-finetuned-vqav2")
result = vqa({"image": "photo.jpg", "question": "What color is the car?"})
print(result[0]['answer'])
```

**Empfohlene Modelle:** LLaVA, BLIP-2, GPT-4 Vision

---

### Beispiel 4: Embeddings für Suche & RAG

**Anforderungen:**
- Semantische Suche in Dokumenten
- Ähnlichkeitsvergleich
- Retrieval-Augmented Generation

**Lösung:**
```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

# 1. Modell laden
model = SentenceTransformer('all-MiniLM-L6-v2')

# 2. Texte einbetten
sentences = ["KI-Modelle", "Machine Learning", "Deep Learning"]
embeddings = model.encode(sentences)

# 3. Ähnlichkeit berechnen
query = "Künstliche Intelligenz"
query_embedding = model.encode([query])
similarities = cosine_similarity(query_embedding, embeddings)
print(similarities)
```

**Empfohlene Modelle:** all-MiniLM-L6-v2, all-mpnet-base-v2, text-embedding-3-small

---

## 🤖 KI-Agenten-Tauglichkeit

Empfehlung, welche Modelle und Frameworks sich am besten für die Automatisierung durch KI-Agenten eignen:

| Modell/Framework | Kategorie | Eignung | Grund |
|-----------------|----------|---------|-------|
| **Ollama** | LLM Inference | ⭐⭐⭐⭐⭐ | Einfache CLI, lokale Ausführung, viele Modelle |
| **Hugging Face Transformers** | Feinabstimmung | ⭐⭐⭐⭐⭐ | Python-API, klare Struktur, viele Beispiele |
| **LangChain** | LLM-Anwendungen | ⭐⭐⭐⭐⭐ | Modular, gut dokumentiert, Python-basiert |
| **Sentence-Transformers** | Embeddings | ⭐⭐⭐⭐⭐ | Einfache API, viele vorgefertigte Modelle |
| **Stable Diffusion (via Diffusers)** | T2I | ⭐⭐⭐⭐ | Python-API, gute Kontrolle |
| **Whisper** | STT | ⭐⭐⭐⭐⭐ | Einfache Python-API, offline-fähig |
| **vLLM** | LLM Inference | ⭐⭐⭐⭐ | Hochperformant, aber komplexere Setup |
| **PyTorch** | Training | ⭐⭐⭐ | Mächtig, aber komplex für KI-Agenten |
| **TensorFlow** | Training | ⭐⭐ | Sehr komplex für autonome Ausführung |
| **Text Generation WebUI** | GUI | ⭐⭐⭐⭐ | GUI-basiert, aber gute API |

---

## 🔗 Verwandte Themen

* [Server/KI/ML-Infrastrukturen](../Server/ki-ml-infrastrukturen.md) – Infrastruktur für KI-Modelle
* [IDE/Lokale KI-Frontends](../IDE/lokale-ki-frontends.md) – Web-UIs für lokale Modelle
* [Tools & Hilfswerkzeuge](../Tools/index.md) – Entwicklungs- und Analyse-Tools
* [Webentwicklung/KI Webentwicklung](../Webentwicklung/ki-webentwicklung.md) – KI in der Webentwicklung
* [Audio/KI und Audio](../Audio/index.md) – Sprach- und Audiomodelle
* [Video/KI-gestützte Videogenerierung](../Video/index.md) – Diffusionsmodelle für Video

---

## 📖 Weiterführende Ressourcen

### Offizielle Dokumentationen
- [Hugging Face Docs](https://huggingface.co/docs) – Transformers, Diffusers, etc.
- [PyTorch Docs](https://pytorch.org/docs/stable/index.html) – PyTorch Framework
- [TensorFlow Docs](https://www.tensorflow.org/api_docs) – TensorFlow Framework
- [ONNX Docs](https://onnx.ai/onnx/api/) – Modell-Interoperabilität
- [Ollama Docs](https://github.com/jmorganca/ollama) – Lokale Modell-Ausführung
- [vLLM Docs](https://docs.vllm.ai/) – Hochperformante LLM-Inference

### Modell-Repositories
- [Hugging Face Model Hub](https://huggingface.co/models) – 100.000+ KI-Modelle
- [Civital](https://civitai.com/) – Stable Diffusion Modelle & LoRAs
- [OpenRouter](https://openrouter.ai/) – Modell-Marketplace mit API-Zugriff
- [Replicate](https://replicate.com/) – Cloud-Hosting für Open-Source-Modelle

### Frameworks & Bibliotheken
- [LangChain](https://python.langchain.com/) – LLM-Anwendungsframework
- [LlamaIndex](https://www.llamaindex.ai/) – Datenintegration für LLMs
- [Diffusers](https://huggingface.co/docs/diffusers/index) – Diffusionsmodelle
- [Sentence-Transformers](https://www.sbert.net/) – Embedding-Modelle
- [Transformers](https://huggingface.co/docs/transformers/index) – NLP-Modelle

### Communities & Blogs
- [r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/) – Lokale LLMs
- [r/StableDiffusion](https://www.reddit.com/r/StableDiffusion/) – Bildgenerierung
- [r/LargeLanguageModels](https://www.reddit.com/r/LargeLanguageModels/) – LLMs
- [Hugging Face Blog](https://huggingface.co/blog) – Neue Modelle & Techniken
- [Towards Data Science](https://towardsdatascience.com/) – KI-Artikel

---

*Letzte Aktualisierung: Juli 2026*
