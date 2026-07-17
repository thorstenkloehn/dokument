# Praxis-Guide: FFmpeg Video Contact Sheets & Thumbnail Grids

Automatisches Extrahieren periodischer Einzelbilder aus einem Video und Zusammenfügen zu einer Vorschau-Grafik (**Contact Sheet / Thumbnail Grid**) per FFmpeg CLI.

---

## ⚡ 1. Thumbnail Grid erzeugen (4x4 Raster)

```bash
ffmpeg -i input.mp4 -vf "select='not(mod(n\,100))',scale=320:180,tile=4x4" -frames:v 1 contact_sheet.png
```

---

## ⚡ 2. Zeitbasiertes Contact Sheet (Bilder alle 10 Sekunden)

```bash
ffmpeg -i input.mp4 -vf "fps=1/10,scale=320:180,tile=5x5" -frames:v 1 preview_grid.jpg
```

### Parameter-Erklärung:
* `fps=1/10`: Extrahiert 1 Bild alle 10 Sekunden
* `scale=320:180`: Skaliert jedes Thumbnail auf 16:9 Format
* `tile=5x5`: Platziert 25 Kacheln in einem 5 Spalten x 5 Zeilen Raster
* `-frames:v 1`: Erzeugt genau 1 finales Ausgabebild

---

## 🔗 Verwandte Themen
* [FFmpeg Advanced Filtering](ffmpeg-advanced-filters.md) – Codecs & Filter
* [FFmpeg HLS Video Streaming](ffmpeg-hls-streaming.md) – Video Streaming
* [FFmpeg & Whisper Automatisierung](ffmpeg-whisper-automatisierung.md) – Transkription
