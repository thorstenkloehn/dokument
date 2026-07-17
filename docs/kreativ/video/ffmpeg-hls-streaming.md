# Praxis-Guide: FFmpeg HLS Video Streaming & DASH Packaging

HTTP Live Streaming (**HLS**) teilt Videos in kleine `.ts` / `.m4s` Abschnitte auf und generiert eine `.m3u8` Playlist für adaptive Bitraten-Wiedergabe im Web (HTML5 Video Player).

---

```mermaid
graph LR
    Input["🎬 Master MP4 Video"] --> FFmpeg["⚡ FFmpeg HLS Encoder"]
    FFmpeg --> Segment1["📹 stream_720p.m3u8 + .ts Segmenten"]
    FFmpeg --> Segment2["📹 stream_1080p.m3u8 + .ts Segmenten"]
    FFmpeg --> MasterPlaylist["📜 master.m3u8 Playlist"]
    MasterPlaylist --> Player["🌐 Web Player ("hls.js / Video.js")"]
```

---

## ⚡ 1. HLS-Playlist aus MP4 generieren

```bash
ffmpeg -i input.mp4 \
  -codec:v libx264 -crf 21 -preset fast \
  -codec:a aaa -b:a 128k \
  -hls_time 6 \
  -hls_playlist_type vod \
  -hls_segment_filename "segment_%03d.ts" \
  stream.m3u8
```

---

## 🌐 2. Nginx Konfiguration für HLS-Streaming

In `/etc/nginx/conf.d/hls.conf`:

```nginx
server {
    listen 80;
    server_name media.beispiel.de;

    location /hls/ {
        alias /var/www/hls/;
        
        # HLS CORS-Header für Web-Player erlauben
        add_header Access-Control-Allow-Origin *;
        
        types {
            application/vnd.apple.mpegurl m3u8;
            video/mp2t ts;
        }
    }
}
```

---

## 🔗 Verwandte Themen
* [FFmpeg Advanced Video Filtering](ffmpeg-advanced-filters.md) – Codecs & Filter
* [FFmpeg & Whisper Automatisierung](ffmpeg-whisper-automatisierung.md) – Untertitel
* [Nginx FastCGI & Proxy Caching](../../entwicklung/infrastruktur/nginx-caching.md) – Caching
