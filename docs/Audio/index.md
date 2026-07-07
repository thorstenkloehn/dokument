# Programmatische Audiogenerierung & -verarbeitung

Diese Übersicht listet Werkzeuge, Frameworks und Bibliotheken auf, die zur programmatischen Generierung, Bearbeitung, Synthese und Analyse von Audiodaten und Musik verwendet werden können.

## 1. Python-Bibliotheken für Audioverarbeitung & Analyse

Werkzeuge für die Manipulation, Transformation und wissenschaftliche Auswertung von Audiodaten in Python.

* **pydub**: Eine einfache, leicht verständliche Python-Bibliothek zum Schneiden, Zusammenfügen, Konvertieren und grundlegenden Bearbeiten von Audiodateien (basiert im Hintergrund auf FFmpeg).
* **librosa**: Das Standard-Python-Paket für Musik- und Audio-Analyse. Es bietet Werkzeuge zur Feature-Extraktion (wie Spektrogramme, Mel-Frequenz-Cepstrum-Koeffizienten (MFCCs), Tonart- und BPM-Erkennung).
* **scipy (scipy.io.wavfile)**: Ermöglicht das direkte Einlesen und Schreiben von WAV-Dateien als NumPy-Arrays für die wissenschaftliche Signalverarbeitung (z. B. Filterung, Fouriertransformationen).
* **sounddevice / soundfile**: 
    * **soundfile** ermöglicht das performante Einlesen und Schreiben von Audiodateien als NumPy-Arrays über `libsndfile`.
    * **sounddevice** erlaubt die direkte und latenzfreie Wiedergabe und Aufnahme von NumPy-Audio-Arrays über PortAudio.
* **mido**: Eine benutzerfreundliche Python-Bibliothek zum Erstellen, Einlesen, Schreiben und Senden von MIDI-Dateien und Echtzeit-MIDI-Signalen.

## 2. Text-to-Speech (TTS) & Sprachsynthese

Systeme zur Umwandlung von Text in gesprochene Sprache (Sprachsynthese).

* **Kokoro-ONNX**: Ein extrem schnelles, ressourcenschonendes und qualitativ hochwertiges Open-Source-Modell für Text-to-Speech, das lokal über die ONNX Runtime ausgeführt werden kann und sich ideal für die Offline-Sprachgenerierung eignet.

## 3. Systemnahe Audio-Programmierung (C++ & Rust)

Low-Level-Werkzeuge für höchste Performance, direkte Manipulation auf Sample-Ebene und die Entwicklung von Audio-Plugins.

* **Rust (symphonia / hound)**:
    * **symphonia**: Eine reine Rust-Bibliothek für das performante Dekodieren und Demuxen gängiger Audioformate.
    * **hound**: Ein einfacher WAV-Encoder und -Decoder in Rust, ideal für die direkte und sichere Manipulation von Audiodaten auf Sample-Ebene.
* **C++ (libsndfile / JUCE)**:
    * **libsndfile**: Eine ausgereifte C-Bibliothek zum Lesen und Schreiben von Audiodateien in einer Vielzahl von Formaten.
    * **JUCE**: Das führende plattformübergreifende C++-Framework für die Entwicklung von Audioanwendungen und -plugins (z. B. VST, AU, AAX), das den Industriestandard für die direkte Manipulation von Sample-Arrays (Float-Points zwischen -1.0 und 1.0) darstellt.
* **FAUST (Functional Audio Stream)**: Eine funktionale Programmiersprache für Echtzeit-Audiosignalverarbeitung. FAUST-Code wird in hocheffizienten C++-, Rust- oder WebAssembly-Code kompiliert, um daraus Synthesizer, Effekte oder Audio-Plugins zu generieren.

## 4. Web-Audio & Frontend-Frameworks

Schnittstellen und Bibliotheken zur Audiogenerierung und -bearbeitung direkt im Webbrowser.

* **Web Audio API**: Die native JavaScript-Schnittstelle im Browser für präzise Echtzeit-Synthese, Analyse, Filterung und räumliche Audio-Positionierung (Panning) direkt in Webanwendungen.
* **Tone.js**: Ein mächtiges, interaktives Web-Audio-Framework, das auf der Web Audio API aufsetzt. Es bietet gebrauchsfertige Synthesizer, Sampler, Effekte und eine extrem präzise Zeitsteuerung (Sequencer/Timeline) für komplexe Musikarrangements im Browser.
* **Howler.js**: Eine schlanke und robuste JavaScript-Audiobibliothek, die die Wiedergabe von Audio-Dateien über mehrere Plattformen hinweg vereinfacht (mit automatischer Fallback-Steuerung).

## 5. Live-Coding & Algorithmische Komposition

Werkzeuge, mit denen Musik live oder algorithmisch durch das Schreiben und Ausführen von Programmcode in Echtzeit erzeugt wird.

* **SuperCollider**: Eine mächtige Programmiersprache und Sound-Engine für Echtzeit-Audiosynthese und algorithmische Komposition. Sie dient auch als technischer Unterbau (Audio-Server) für Sonic Pi und TidalCycles.
* **Sonic Pi**: Eine auf Ruby basierende Live-Coding-Umgebung zur Synthesizer- und Sample-basierten Musikproduktion. Sie wurde für Schule, Lehre und Performance entwickelt und nutzt SuperCollider als Synthesizer-Backend.
* **TidalCycles**: Eine Haskell-basierte Live-Coding-Umgebung für das algorithmische Erzeugen von komplexen rhythmischen und musikalischen Mustern (Patterns). Die Audio-Ausgabe erfolgt über den SuperCollider-Synthesizer *SuperDirt*.
* **Pure Data (Pd)**: Eine grafische, datenflussorientierte Programmiersprache zur Echtzeit-Erzeugung und -Verarbeitung von Audio, MIDI und Video (die Open-Source-Alternative zu Max/MSP).
* **Hydra**: Ein JavaScript-basierter Live-Coding-Videosynthesizer für den Webbrowser. Obwohl primär ein visuelles Werkzeug, wird Hydra in der Audio-Live-Coding-Szene häufig zur Generierung von Echtzeit-Visualisierungen verwendet, die mit Live-Audioquellen (wie Sonic Pi oder TidalCycles) synchronisiert sind.

## 6. Kommandozeilen-Tools & Audio-Verarbeitung

Software für schnelles Batch-Processing auf Dateiebene und automatisierte Audio-Operationen.

* **SoX (Sound eXchange)**: Das „Schweizer Taschenmesser“ der Audio-Verarbeitung auf der Kommandozeile. Perfekt geeignet, um Audiodateien per Terminalbefehl schnell zu schneiden, zu konvertieren, zu mischen oder mit Effekten (z. B. Hall, Pitch) zu versehen.

## KI-Agenten-Tauglichkeit (Automatisierte Audioerstellung)

Empfehlung, welche der oben gelisteten Tools sich am besten eignen, um von KI-Agenten gesteuert zu werden, um eigenständig Audioinhalte, Sprache oder Musik zu erzeugen:

* **SoX** (Kategorie 6) – **Hervorragend geeignet:** Da es sich um ein reines CLI-Tool handelt, können KI-Agenten grundlegende Audio-Manipulationsschritte (Schneiden, Zusammenfügen, Konvertieren, Effekte) extrem schnell und ohne Overhead direkt über Terminalbefehle ausführen.
* **Kokoro-ONNX** (Kategorie 2) – **Hervorragend geeignet:** Da es einfach als Python-Skript geladen werden kann, können KI-Agenten problemlos Text übergeben und hochqualitative Audio-Dateien im Hintergrund generieren lassen.
* **pydub / scipy** (Kategorie 1) – **Hervorragend geeignet:** Die klaren Programmierschnittstellen erlauben es KI-Agenten, klassische Audio-Manipulationsschritte deterministisch über Python-Skripte auszuführen.
* **Tone.js** (Kategorie 4) – **Sehr gut geeignet:** Durch die klare deklarative Struktur von Tone.js können LLMs leicht Synthesizer-Konfigurationen und Notensequenzen in JavaScript generieren, die direkt im Browser abgespielt werden.
* **Sonic Pi** (Kategorie 5) – **Sehr gut geeignet:** Die Ruby-Syntax von Sonic Pi ist deklarativ und kompakt. KI-Agenten können sehr einfach Melodielinien oder Rhythmuspatterns in Code schreiben, der dann über eine OSC-Schnittstelle (Open Sound Control) an Sonic Pi übertragen werden kann.
* **Rust (symphonia) / C++ (JUCE)** (Kategorie 3) – **Bedingt geeignet:** Extrem leistungsfähig für professionelle DSP-Entwicklung (Digital Signal Processing), jedoch sind die komplexen Speicherverwaltungs- und Kompilierungsschritte für KI-Agenten in der autonomen Ausführung oft zu fehleranfällig.