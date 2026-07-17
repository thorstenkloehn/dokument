# Praxis-Guide: Video- & Audio-Automatisierung mit FFmpeg & Whisper CLI

Dieser Guide zeigt die automatisierte Extraktion von Audio, die Erstellung präziser Untertitel mit OpenAI Whisper CLI sowie das Einbrennen der Untertitel in Videos.

---

```mermaid
graph LR
    Video["🎬 Video-Datei (.mp4)"] --> Extract["🔊 FFmpeg Audio-Extraktion"]
    Extract --> Audio["🎵 Audio-Datei (.wav)"]
    Audio --> Whisper["🤖 OpenAI Whisper CLI"]
    Whisper --> Subtitles["📝 Untertitel (".srt / .vtt")"]
    Subtitles --> Burn["🎬 FFmpeg Subtitle-Burn"]
    Burn --> FinalVideo["✨ Finales Video mit Untertiteln"]
```

---

## 🛠️ 1. Installation der CLI-Tools

```bash
# FFmpeg & Python venv installieren
sudo apt update && sudo apt install -y ffmpeg python3-pip

# OpenAI Whisper CLI & dependencies installieren
pip install -U openai-whisper
```

---

## ⚡ 2. Schritt-für-Schritt Automatisierungs-Skript

### Bash-Skript (`auto_subtitles.sh`)

```bash
#!/bin/bash
set -e

INPUT_VIDEO="$1"
FILENAME="${INPUT_VIDEO%.*}"
AUDIO_FILE="${FILENAME}_audio.wav"
SRT_FILE="${FILENAME}_audio.srt"
OUTPUT_VIDEO="${FILENAME}_subtitled.mp4"

if [ -z "$INPUT_VIDEO" ]; then
    echo "Verwendung: ./auto_subtitles.sh <video_datei.mp4>"
    exit 1
fi

echo "1. Audio extrahieren mit FFmpeg..."
ffmpeg -y -i "$INPUT_VIDEO" -vn -acodec pcm_s16le -ar 16000 -ac 1 "$AUDIO_FILE"

echo "2. Untertitel generieren mit Whisper (Sprache: Deutsch)..."
whisper "$AUDIO_FILE" --model small --language German --output_format srt

echo "3. Untertitel fest in Video einbrennen mit FFmpeg..."
ffmpeg -y -i "$INPUT_VIDEO" -vf "subtitles=$SRT_FILE:force_style='FontSize=18,PrimaryColour=&H00FFFFFF,OutlineColour=&H00000000,BorderStyle=3'" -c:a copy "$OUTPUT_VIDEO"

echo "✅ Fertig! Finales Video: $OUTPUT_VIDEO"
```

---

## 💡 3. Nützliche FFmpeg CLI-Tricks

### Video ohne Re-Encoding schneiden (von Minute 01:00 für 30 Sekunden)
```bash
ffmpeg -ss 00:01:00 -i input.mp4 -to 00:00:30 -c copy output_clip.mp4
```

### Video in ein schnelles GIF umwandeln
```bash
ffmpeg -i input.mp4 -vf "fps=10,scale=640:-1:flags=lanczos" output.gif
```

---

## 🔗 Verwandte Themen
* [KI in der Film- und Videoproduktion](ki-filmproduktion.md) – Übersicht KI-Videotools
* [KI und Audio](../audio/ki-audio.md) – Sprach- und Soundverarbeitung
* [Audacity mit KI](../audio/audacity-ki.md) – Manuelle Audiobearbeitung
