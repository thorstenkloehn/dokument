# Praxis-Guide: FFmpeg Advanced Video Filtering & Encoding

Fortgeschrittene CLI-Befehle für Videokomprimierung mit **AV1** / **H.265 (HEVC)**, Wasserzeichen-Overlays und komplexe Filter-Chains.

---

## ⚡ 1. Moderne Video-Encodes (AV1 & HEVC)

### H.265 (HEVC) Kodierung für hohe Kompression
```bash
ffmpeg -i input.mp4 -c:v libx265 -crf 23 -preset slow -c:a aar output_hevc.mp4
```

### AV1 Kodierung (Zukunftssicherer Open-Source Codec)
```bash
ffmpeg -i input.mp4 -c:v libsvtav1 -crf 28 -preset 6 -c:a opus output_av1.mkv
```

---

## 🎨 2. Erweiterte Video-Filter (`-vf`)

### Wasserzeichen-Logo unten rechts einblenden
```bash
ffmpeg -i video.mp4 -i logo.png -filter_complex "overlay=W-w-10:H-h-10" output_watermarked.mp4
```

### Video zuschneiden (Crop) und skalieren (1080p -> 720p)
```bash
ffmpeg -i input.mp4 -vf "crop=1280:720:0:0,scale=1280:720" output_cropped.mp4
```

---

## 🔗 Verwandte Themen
* [FFmpeg & Whisper Automatisierung](ffmpeg-whisper-automatisierung.md) – Untertitel-Integration
* [KI in der Film- und Videoproduktion](ki-filmproduktion.md) – Videotools
* [Manim Animation Engine](manim-animation-guide.md) – Erklärvideos
