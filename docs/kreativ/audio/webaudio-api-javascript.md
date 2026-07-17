# Praxis-Guide: WebAudio API in JavaScript

Die **Web Audio API** ermöglicht die direkte Synthese, Manipulation und Echtzeit-Verarbeitung von Audiosignalen im Webbrowser ohne externe Bibliotheken.

---

## 💻 1. Minimaler Synthesizer in JavaScript (`synth.js`)

```javascript
// 1. AudioContext initialisieren
const audioCtx = new (window.AudioContext || window.webkitAudioContext)();

function playTone(frequency = 440, duration = 1.0) {
    // 2. Oszillator (Klangerzeuger) & GainNode (Lautstärke) erstellen
    const osc = audioCtx.createOscillator();
    const gain = audioCtx.createGain();

    osc.type = 'sine'; // Wellenform: sine, square, sawtooth, triangle
    osc.frequency.value = frequency; // A4 = 440Hz

    // 3. Hüllkurve (Envelope / Fade-Out) definieren
    gain.gain.setValueAtTime(0.5, audioCtx.currentTime);
    gain.gain.exponentialRampToValueAtTime(0.0001, audioCtx.currentTime + duration);

    // 4. Verbinden: Oszillator -> Gain -> Lautsprecher
    osc.connect(gain);
    gain.connect(audioCtx.destination);

    // 5. Tone abspielen & stoppen
    osc.start();
    osc.stop(audioCtx.currentTime + duration);
}

// Beispiel: Sinuston A4 (440Hz) abspielen
document.getElementById('play-btn').addEventListener('click', () => {
    if (audioCtx.state === 'suspended') {
        audioCtx.resume();
    }
    playTone(440, 1.5);
});
```

---

## 🔗 Verwandte Themen
* [MIDI-Generierung mit Python](midi-python-automation.md) – MIDI-Skripte
* [DAW-Integration mit KI](daw-integration.md) – DAW-Pipelines
* [Audio-Processing mit KI](audio-processing.md) – Audioverarbeitung
