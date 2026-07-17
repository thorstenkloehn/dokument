# Praxis-Guide: Nginx FastCGI & Proxy Caching

Nginx In-Memory Proxy-Caching reduziert die Serverlast und Datenbankabfragen um bis zu 95%, indem dynamische Antworten im RAM oder auf der SSD zwischengespeichert werden.

---

```mermaid
graph LR
    Client["🌐 Client Request"] --> Nginx["⚡ Nginx Caching Layer"]
    Nginx -->|HIT (Cache vorhanden)| ReturnCache["⚡ In-Memory Response (<2ms)"]
    Nginx -->|MISS (Kein Cache)| Backend["🐘 PHP-FPM / Python / Node.js Backend"]
    Backend --> StoreCache["💾 Cache speichern & ausliefern"]
```

---

## ⚙️ 1. Cache-Zone in `nginx.conf` einrichten

Im `http`-Block von `/etc/nginx/nginx.conf`:

```nginx
# Cache-Pfad und Speichergröße definieren (keys_zone=my_cache:10m -> 10MB für Cache-Keys, max 1GB Daten)
proxy_cache_path /var/cache/nginx levels=1:2 keys_zone=my_cache:10m max_size=1g inactive=60m use_temp_path=off;
```

---

## ⚡ 2. Proxy Cache im `server`-Block aktivieren

```nginx
server {
    listen 80;
    server_name app.beispiel.de;

    location / {
        proxy_pass http://localhost:8080;
        
        # Cache aktivieren
        proxy_cache my_cache;
        proxy_cache_valid 200 302 10m;
        proxy_cache_valid 404 1m;
        
        # Cache Bypass für angemeldete Benutzer (Cookie / Header)
        proxy_cache_bypass $cookie_nocache $arg_nocache;
        
        # Cache Status in HTTP-Header ausgeben (HIT, MISS, BYPASS)
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

```bash
sudo mkdir -p /var/cache/nginx
sudo nginx -t && sudo systemctl reload nginx
```

---

## 🔗 Verwandte Themen
* [Nginx Load Balancing](nginx-loadbalancing.md) – Lastausgleich
* [Nginx Hardening & Sicherheit](nginx-hardening.md) – Rate Limiting
* [HTTP Server Benchmarking](http-server-benchmarking.md) – Benchmarking
