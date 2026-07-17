# Praxis-Guide: Local LLM Fine-Tuning mit Unsloth & LoRA

**Unsloth** ermöglicht 2x schnelleres und 80% speichereffizienteres Feintuning von Open-Source LLMs (Llama 3, Mistral, Qwen) mittels LoRA (Low-Rank Adaptation) auf eigenen Daten.

---

```mermaid
graph LR
    BaseModel["🤖 Base LLM ("Llama 3.2 / Qwen 2.5")"] --> LoRA["⚡ LoRA Adapter (Fine-Tuning)"]
    Dataset["📊 Eigene Trainingsdaten (JSONL)"] --> Unsloth["🚀 Unsloth Trainer"]
    Unsloth --> LoRA
    LoRA --> GGUF["📦 GGUF Export ("für Ollama")"]
```

---

## 🛠️ 1. Installation

```bash
pip install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
pip install --no-deps "xformers<0.0.27" "trl<0.9.0" peft acceleration bitsandbytes
```

---

## 🐍 2. Python Fine-Tuning Skript (`train.py`)

```python
from unsloth import FastLanguageModel
import torch
from datasets import load_dataset
from trl import SFTTrainer
from transformers import TrainingArguments

max_seq_length = 2048
dtype = None # Auto-detect GPU precision
load_in_4bit = True # 4bit Quantisierung für geringen VRAM-Verbrauch

# 1. Modell & Tokenizer laden
model, tokenizer = FastLanguageModel.from_pretrained(
    model_name = "unsloth/Llama-3.2-3B-Instruct",
    max_seq_length = max_seq_length,
    dtype = dtype,
    load_in_4bit = load_in_4bit,
)

# 2. LoRA Adapter konfigurieren
model = FastLanguageModel.get_peft_model(
    model,
    r = 16, # LoRA Rank
    target_modules = ["q_proj", "k_proj", "v_proj", "o_proj", "gate_proj", "up_proj", "down_proj"],
    lora_alpha = 16,
    lora_dropout = 0,
    bias = "none",
)

# 3. Datensatz vorbereiten
dataset = load_dataset("json", data_files={"train": "train_data.jsonl"})

# 4. Trainer starten
trainer = SFTTrainer(
    model = model,
    tokenizer = tokenizer,
    train_dataset = dataset["train"],
    dataset_text_field = "text",
    max_seq_length = max_seq_length,
    args = TrainingArguments(
        per_device_train_batch_size = 2,
        gradient_accumulation_steps = 4,
        warmup_steps = 5,
        max_steps = 60,
        learning_rate = 2e-4,
        fp16 = not torch.cuda.is_bf16_supported(),
        bf16 = torch.cuda.is_bf16_supported(),
        logging_steps = 1,
        output_dir = "outputs",
    ),
)

trainer.train()

# 5. Export als GGUF für Ollama
model.save_pretrained_gguf("my_custom_model", tokenizer, quantization_method = "q4_k_m")
print("✅ Modell erfolgreich als GGUF für Ollama exportiert!")
```

---

## 🔗 Verwandte Themen
* [Lokales RAG & LLM-Serving](lokales-rag-ollama.md) – Einbinden in Ollama
* [KI Coding](ki-coding.md) – Grundkonzepte
* [Agentic Workflows](agentic-workflows-langgraph.md) – Multi-Agenten Nutzung
