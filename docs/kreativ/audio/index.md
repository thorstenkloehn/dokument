# Audio & Musik: Programmatische Audiogenerierung & -verarbeitung

Eine zentralisierte Übersicht über Werkzeuge, Frameworks und Bibliotheken zur programmatischen Erzeugung, Bearbeitung, Synthese und Analyse von Audiodaten und Musik mit KI-Unterstützung.

---

## Audio-Technologien im Überblick

Die programmatische Audioverarbeitung umfasst ein weites Spektrum von Anwendungen: von der einfachen Audiobearbeitung über komplexe Musiksynthese bis hin zur KI-gestützten Sprachverarbeitung und Musikgenerierung.

### Anwendungsbereiche

| Bereich | Beschreibung | Typische Tools & Bibliotheken |
|---------|--------------|-------------------------------|
| **Audiobearbeitung** | Schneiden, Mischen, Effekte | SoX, Audacity, PyDub |
| **Sprachsynthese (TTS)** | Text zu Sprache | Kokoro-ONNX, eSpeak, Festival |
| **Spracherkennung (STT)** | Sprache zu Text | Whisper, Vosk, Kaldi |
| **Musikgenerierung** | KI-basierte Musikkomposition | Magenta, MusicGen, Riffusion |
| **Audio-Analyse** | Feature-Extraktion, Klassifizierung | Librosa, PyAudioAnalysis |
| **Echtzeit-Verarbeitung** | Live-Audio-Manipulation | PortAudio, JUCE, Web Audio API |
| **MIDI-Programmierung** | Musiksteuerung über MIDI | Mido, Python-RTmidi, PortMidi |
| **Live-Coding** | Musik in Echtzeit programmieren | SuperCollider, Sonic Pi, TidalCycles |

---

## Hauptthemen

Einen vertiefenden Vergleich der aktuell stärksten quelloffenen KI-Modelle und -Werkzeuge (TTS, STT, Voice Cloning, Stem-Separation, Musikgenerierung) liefert die Seite [Beste KI-Audio-Tools (Open Source, Top 20)](ki-audio-tools-topliste.md).

### 1. [KI und Audio](ki-audio.md)
**Umfassende Übersicht zu KI-Anwendungen in der Audio-Verarbeitung** – Von Sprachsynthese bis Musikgenerierung.

* **Sprachverarbeitung**: Text-to-Speech (TTS) und Speech-to-Text (STT)
* **Musikgenerierung**: KI-basierte Komposition und Arrangierung
* **Audio-Enhancement**: Rauschunterdrückung, Hallentfernung, Upsampling
* **Stimmanalyse**: Pitch-Erkennung, Stimmungsanalyse, Sprecheridentifikation
* **Echtzeit-Anwendungen**: Live-Transkription, Echtzeit-Übersetzung

**KI-Modelle und Frameworks:**
- **Text-to-Speech**: Kokoro-ONNX, Coqui TTS, Tortoise-TTS
- **Speech-to-Text**: Whisper (OpenAI), Vosk, Mozilla DeepSpeech
- **Musikgenerierung**: MusicGen (Facebook), Riffusion, Stable Audio
- **Audio-Analyse**: Wav2Vec 2.0, HuBERT, CREPE

---

### 2. [Audacity mit KI](audacity-ki.md)
**Professionelle Audiobearbeitung mit KI-Plugins** – Wie KI die Audiobearbeitung in Audacity revolutioniert.

* **Rauschunterdrückung**: KI-basierte Entfernung von Hintergrundgeräuschen
* **Stem-Separation**: Trennung vonVocals, Bass, Drums und anderen Instrumenten
* **Automatische Transkription**: Sprache-zu-Text direkt in Audacity
* **Audio-Restauration**: Wiederherstellung alter oder beschädigter Aufnahmen
* **Effekt-Automatisierung**: KI-gestützte Effektvorschläge und -anpassung

**Beliebte KI-Plugins für Audacity:**
- **Noise Reduction**: RNNoise, Spectral Noise Reduction
- **Stem Separation**: Demucs, LTSM-Separator, Spleeter
- **Pitch & Tempo**: Rubber Band, SoundTouch mit KI-Optimierung
- **Mastering**: LANDR, iZotope Ozone (über Plugin-Bridges)

---

### 3. [DAW-Integration mit KI](daw-integration.md)
**KI in Digital Audio Workstations** – Integration von KI-Tools in professionelle Audio-Software.

* **Automatisierte Mixing-Unterstützung**: KI-gestützte EQ-, Kompressor- und Hall-Einstellungen
* **Intelligente Arrangierung**: Vorschläge für Song-Struktur und Instrumentierung
* **Stil-Transfer**: Übertragung des Klangcharakters eines Tracks auf einen anderen
* **Automatisierte Mastering**: KI-basierte Finalisierung von Tracks
* **Instrumenten-Erkennung**: Automatische Erkennung von Instrumenten in Audio-Dateien

**Unterstützte DAWs:**

| DAW | Plattform | KI-Integration |
|-----|-----------|----------------|
| **Ardour** | Linux, macOS, Windows | LADSPA-Plugins, Python-Skripte |
| **LMMS** | Linux, macOS, Windows | Native KI-Plugins |
| **Qtractor** | Linux | LADSPA, DSSI, LV2-Plugins |
| **REAPER** | Windows, macOS, Linux | ReaScript, Python, JS |
| **Bitwig Studio** | Windows, macOS, Linux | Modulator-System mit KI |

---

### 4. [MIDI-Programmierung mit KI](midi-programmierung.md)
**Intelligente Musiksteuerung durch KI-generierte und analysierte MIDI-Daten** – Programmierung von Musik mit KI-Unterstützung.

* **MIDI-Generierung**: KI erstellt Melodien, Harmonien und Rhythmen
* **Stil-Analyse**: KI analysiert bestehende MIDI-Dateien und schlägt ähnliche Patterns vor
* **Automatische Begleitung**: Generierung von Begleitparts basierend auf Melodie oder Akkordfolgen
* **MIDI-zu-Audio**: KI-gestützte Konvertierung von MIDI zu Audio mit hochwertigen Samples
* **Echtzeit-MIDI-Verarbeitung**: Live-Manipulation von MIDI-Daten

**MIDI-Bibliotheken und Tools:**
- **Python**: Mido, PrettyMIDI, Music21
- **C++**: RtMidi, PortMidi
- **Web**: Web MIDI API, Tone.js
- **Hardware**: MIDI-Controller, Synthesizer, Drum Machines

---

### 5. [Audio-Processing mit KI](audio-processing.md)
**Signalverarbeitung mit neuronalen Netzen** – Fortgeschrittene Audio-Manipulation mit KI.

* **Echtzeit-Effekte**: KI-basierte Hall-, Delay- und Modulationseffekte
* **Audio-Separation**: Trennung von Audioquellen (Source Separation)
* **Audio-Enhancement**: Qualitätsverbesserung von Aufnahmen
* **Stimmumwandlung**: Veränderung von Stimmeigenschaften (Pitch, Formant, Gender)
* **Audio-Inpainting**: Rekonstruktion fehlender Audiosegmente

**Anwendungsfälle:**
- **Podcast-Produktion**: Automatische Reinigung und Mastering
- **Musikproduktion**: KI-gestützte Mixing- und Mastering-Hilfe
- **Film & Video**: Dialog-Aufbereitung, Sound-Design
- **Gaming**: Dynamische Audio-Generierung
- **Barrierefreiheit**: Automatische Untertitelung und Audio-Beschreibung

---

## Programmiersprachen & Bibliotheken

### Python-Bibliotheken

Python bietet eine reiche Auswahl an Bibliotheken für Audioverarbeitung und -analyse.

#### Audioverarbeitung & Analyse

| Bibliothek | Hauptfunktion | Stärken | Installation |
|------------|---------------|---------|--------------|
| **pydub** | Einfache Audiobearbeitung | Benutzerfreundlich, FFmpeg-Backend | `pip install pydub` |
| **librosa** | Audio-Analyse | Feature-Extraktion, Musikanalyse | `pip install librosa` |
| **soundfile** | Audio I/O | Hochperformant, NumPy-Integration | `pip install soundfile` |
| **sounddevice** | Audio-Wiedergabe/Aufnahme | Echtzeit, PortAudio | `pip install sounddevice` |
| **scipy.io.wavfile** | WAV I/O | Wissenschaftliche Signalverarbeitung | `pip install scipy` |

#### MIDI-Programmierung

| Bibliothek | Hauptfunktion | Stärken |
|------------|---------------|---------|
| **mido** | MIDI-Dateien & Echtzeit-MIDI | Einfach zu bedienen, umfassend |
| **PrettyMIDI** | MIDI-Analyse & Generierung | Musiktheorie, Pattern-Erkennung |
| **Music21** | Musikanalyse | Musiktheorie, Notenblatt-Verarbeitung |
| **python-rtmidi** | Echtzeit-MIDI | Low-Latency, plattformübergreifend |

#### Sprachverarbeitung

| Bibliothek | Hauptfunktion | Modell |
|------------|---------------|--------|
| **Whisper** | Speech-to-Text | OpenAI Whisper |
| **Kokoro-ONNX** | Text-to-Speech | Kokoro TTS |
| **Vosk** | Offline Speech-to-Text | Kaldi-basiert |
| **transformers** | Sprachmodelle | Hugging Face |

### Systemnahe Programmierung (C++ & Rust)

Für maximale Performance und direkte Manipulation auf Sample-Ebene.

#### C++ Bibliotheken

| Bibliothek | Hauptfunktion | Stärken |
|------------|---------------|---------|
| **libsndfile** | Audio I/O | Viele Formate, robust |
| **JUCE** | Audioanwendungen & Plugins | VST, AU, AAX, GUI |
| **PortAudio** | Audio I/O | Cross-Platform, Echtzeit |
| **RtAudio** | Audio I/O | Low-Latency |

#### Rust Bibliotheken

| Bibliothek | Hauptfunktion | Stärken |
|------------|---------------|---------|
| **symphonia** | Audio-Dekodierung | Hochperformant, viele Formate |
| **hound** | WAV-Encoding/Decoding | Einfach, sicher |
| **cpal** | Audio I/O | Cross-Platform |
| **fundsp** | Audio-Synthese | Funktional, Echtzeit |

### FAUST (Functional Audio Stream)

**Funktionale Programmiersprache für Echtzeit-Audiosignalverarbeitung.**

- **Kompilierung**: FAUST-Code wird in C++, Rust, WebAssembly oder andere Sprachen kompiliert
- **Anwendungen**: Synthesizer, Effekte, Audio-Plugins
- **Vorteile**: Plattformunabhängig, hochoptimiert, mathematisch präzise
- **Integration**: VST, AU, LADSPA, WebAudio, etc.

---

## Web-Audio & Frontend-Frameworks

### Web Audio API

Die native JavaScript-Schnittstelle für Audiogenerierung und -verarbeitung im Browser.

**Hauptmerkmale:**
- Echtzeit-Synthese und -Verarbeitung
- Modulare Audio-Routing (AudioNodes)
- Räumliches Audio (Panning)
- Analyse-Funktionen (FFT, Frequenzanalyse)

### Web-Audio-Bibliotheken

| Bibliothek | Hauptfunktion | Stärken |
|------------|---------------|---------|
| **Tone.js** | Web-Audio-Framework | Synthesizer, Sampler, Effekte |
| **Howler.js** | Audio-Wiedergabe | Einfach, robust |
| **Pizzicato.js** | Musik-Generierung | Einfach zu lernen |
| **Wavesurfer.js** | Audio-Visualisierung | Waveform-Darstellung |
| **Peaks.js** | Audio-Editor | BBC Audio-Editor |

---

## Live-Coding & Algorithmische Komposition

### Live-Coding-Umgebungen

Werkzeuge zur Echtzeit-Erzeugung von Musik durch Programmcode.

#### SuperCollider

**Mächtige Programmiersprache und Sound-Engine für Echtzeit-Audiosynthese.**

- **Sprache**: Spezialisierte Syntax für Audiosynthese
- **Funktionen**: Synthesizer, Effekte, Pattern-Generierung
- **Performance**: Echtzeit, Low-Latency
- **Integration**: Externe Steuerung über OSC

#### Sonic Pi

**Auf Ruby basierende Live-Coding-Umgebung für Musikproduktion.**

- **Zielgruppe**: Bildung, Anfänger, Performance
- **Funktionen**: Synthesizer, Sampler, Effekte
- **Backend**: SuperCollider als Audio-Engine
- **Vorteile**: Einfach zu lernen, pädagogisch wertvoll

#### TidalCycles

**Haskell-basierte Live-Coding-Umgebung für algorithmische Musik.**

- **Paradigma**: Funkionale Programmierung
- **Fokus**: Rhythmische Patterns und Strukturen
- **Backend**: SuperDirt (SuperCollider)
- **Vorteile**: Mächtig für komplexe rhythmische Muster

#### Pure Data (Pd)

**Grafische, datenflussorientierte Programmiersprache für Echtzeit-Audio.**

- **Konzept**: Patches mit Objekten und Verbindungen
- **Anwendungen**: Synthesizer, Effekte, Video, Interaktion
- **Vorteile**: Visuell, flexibel, Open Source
- **Alternativen**: Max/MSP (kommerziell)

#### Hydra

**JavaScript-basierter Live-Coding-Videosynthesizer für den Browser.**

- **Primärfokus**: Visuelle Effekte
- **Audio-Integration**: Synchronisation mit Audio-Sources
- **Vorteile**: Web-basiert, einfach zu teilen

---

## Kommandozeilen-Tools

### SoX (Sound eXchange)

**Das Schweizer Taschenmesser der Audio-Verarbeitung auf der Kommandozeile.**

**Hauptfunktionen:**
- Format-Konvertierung
- Audio schneiden und zusammenfügen
- Effekte anwenden (Hall, Pitch, Tempo, etc.)
- Batch-Verarbeitung

**Beispielbefehle:**
```bash
# Format konvertieren
sox input.wav output.mp3

# Audio schneiden (von 10s bis 20s)
sox input.wav output.wav trim 10 10

# Pitch ändern (+2 Halbtöne)
sox input.wav output.wav pitch 200

# Hall hinzufügen
sox input.wav output.wav reverb 50
```

### FFmpeg

**Multimediale Framework für Audio- und Video-Verarbeitung.**

**Audio-spezifische Funktionen:**
- Format-Konvertierung
- Audio-Extraktion aus Videos
- Bitrate-Anpassung
- Metadaten-Bearbeitung

**Beispielbefehle:**
```bash
# Audio aus Video extrahieren
ffmpeg -i video.mp4 -vn -acodec copy audio.mp3

# Audio in mehrere Formate konvertieren
ffmpeg -i input.wav -codec:a libmp3lame -q:a 2 output.mp3

# Audio normalisieren
ffmpeg -i input.wav -af "loudnorm=I=-16:TP=-1.5" output.wav
```

---

## KI-Agenten-Tauglichkeit

Empfehlung, welche Tools sich am besten für die Automatisierung durch KI-Agenten eignen:

| Tool | Kategorie | Eignung | Grund |
|------|----------|---------|-------|
| **SoX** | CLI-Tool | ⭐⭐⭐⭐⭐ | Einfache Befehle, deterministisch |
| **Kokoro-ONNX** | TTS | ⭐⭐⭐⭐⭐ | Python-Skript, lokale Ausführung |
| **pydub / scipy** | Audio-Bearbeitung | ⭐⭐⭐⭐⭐ | Klare Python-API |
| **Tone.js** | Web-Audio | ⭐⭐⭐⭐ | Deklarative Struktur, JavaScript |
| **Sonic Pi** | Live-Coding | ⭐⭐⭐⭐ | Ruby-Syntax, kompakt |
| **Rust (symphonia)** | Audio-Processing | ⭐⭐⭐ | Leistungsfähig, aber komplex |
| **C++ (JUCE)** | Audio-Entwicklung | ⭐⭐ | Komplexe Speicherverwaltung |

---

## Praxisbeispiele

### Beispiel 1: Automatisierte Podcast-Produktion

**Workflows:**
1. Audio aufnehmen (Audacity oder CLI-Tool)
2. Rauschunterdrückung mit KI (RNNoise, Adobe Podcast Enhance)
3. Automatisches Schneiden von Pausen (Silence Detection)
4. Lautstärke normalisieren
5. Intro/Outro hinzufügen
6. In verschiedene Formate exportieren
7. Automatische Transkription (Whisper)

**Tools:** SoX, FFmpeg, Whisper, Audacity mit KI-Plugins

### Beispiel 2: KI-gestützte Musikproduktion

**Workflows:**
1. Melodie-Idee in MIDI programmieren (Mido)
2. KI-gestützte Harmonie-Generierung (Music21, Magenta)
3. Instrumentierung mit KI (Orchestration Models)
4. MIDI zu Audio rendern (FluidSynth, Synthesizer)
5. Mixing mit KI-Unterstützung (iZotope, LANDR)
6. Mastering mit KI (LANDR, eMastered)

**Tools:** Mido, Magenta, FluidSynth, iZotope Ozone

### Beispiel 3: Echtzeit-Audio-Effekte

**Workflows:**
1. Audio-Stream erfassen (PortAudio, Web Audio API)
2. Echtzeit-Analyse (FFT, Pitch-Detection)
3. Effekte anwenden (Hall, Delay, Distortion)
4. KI-gestützte Parameteranpassung
5. Audio ausgeben

**Tools:** Web Audio API, Tone.js, PortAudio, Python mit SoundDevice

---

## Verwandte Themen

* [Content/KI-gestützte Inhalte](../../künstliche-intelligenz/content/index.md) – KI für Content-Erstellung
* [Webentwicklung/Frontend mit KI](../../entwicklung/webentwicklung/frontend-ki.md) – KI in der Webentwicklung
* [Tools/Analysetool](../../wissen/tools/analysetool.md) – Audio-Analyse-Tools
* [Desktop Automation](../../künstliche-intelligenz/automatisierung/index.md) – Automatisierung von Audio-Workflows
* [IDE/Lokale KI-Frontends](../../entwicklung/ide/lokale-ki-frontends.md) – KI-Oberflächen für Audio-Anwendungen

---

## Weiterführende Ressourcen

### Offizielle Dokumentationen
- [Librosa Documentation](https://librosa.org/doc/latest/) – Python Audio Analysis
- [PortAudio](http://www.portaudio.com/) – Cross-Platform Audio I/O
- [JUCE Framework](https://juce.com/) – C++ Audio Application Framework
- [Web Audio API](https://developer.mozilla.org/en-US/docs/Web/API/Web_Audio_API) – Browser Audio
- [FAUST Language](https://faust.grame.fr/) – Functional Audio Programming

### KI-Tools für Audio
- [Kokoro-ONNX](https://github.com/Plachtaa/kokoro-onnx) – Hochwertige TTS
- [Whisper](https://github.com/openai/whisper) – Speech-to-Text
- [Magenta](https://magenta.tensorflow.org/) – Musik mit KI
- [MusicGen](https://github.com/facebookresearch/audiocraft) – Musikgenerierung
- [Riffusion](https://github.com/riffusion/riffusion) – Audio-Generierung

### Communities & Blogs
- [r/AudioEngineering](https://www.reddit.com/r/AudioEngineering/) – Audio-Technik
- [r/WeAreTheMusicMakers](https://www.reddit.com/r/WeAreTheMusicMakers/) – Musikproduktion
- [r/synthrecipes](https://www.reddit.com/r/synthrecipes/) – Synthesizer-Programmierung
- [Audio Programmer](https://theaudioprogrammer.com/) – Blog
- [Librosa Blog](https://librosa.org/doc/latest/) – Audio-Analyse

---

*Letzte Aktualisierung: Juli 2026*
