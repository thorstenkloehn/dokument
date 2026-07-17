# Praxis-Guide: Nginx Rate Limiting & DDoS-Schutz

Schütze Server und APIs vor Brute-Force-Angriffen und DDoS-Überlastung durch **Rate Limiting** (`limit_req_zone`) und Begrenzung paralleler Verbindungen (`limit_conn_zone`).

---

## ⚙️ 1. Rate-Limit Zonen definieren (`nginx.conf`)

Im `http`-Block von `/etc/nginx/nginx.conf`:

```nginx
# 1. Zone für API Rate-Limiting (Maximal 10 Anfragen pro Sekunde pro IP)
limit_req_zone $binary_remote_addr zone=api_limit:10m rate=10r/s;

# 2. Zone für Verbindungslimits (Maximal 20 parallele Verbindungen pro IP)
limit_conn_zone $binary_remote_addr zone=conn_limit:10m;
```

---

## ⚡ 2. Rate-Limiting im Server-Block anwenden

```nginx
server {
    listen 80;
    server_name api.beispiel.de;

    # Verbindungen pro IP begrenzen
    limit_conn conn_limit 20;

    location /api/ {
        # Rate Limit mit Puffer (burst=20) anwenden (nodelay verhindert künstliche Verzögerung)
        limit_req zone=api_limit burst=20 nodelay;
        
        # HTTP Statuscode bei Limit-Überschreitung (Standard ist 530, hier 429 Too Many Requests)
        limit_req_status 429;

        proxy_pass http://localhost:8000;
    }
}
```

---

## 🔗 Verwandte Themen
* [Nginx GeoIP Blocking](nginx-geoip-blocking.md) – GeoIP & Bot-Abwehr
* [Nginx Hardening & Sicherheit](nginx-hardening.md) – Sicherheitseinstellungen
* [Nginx Load Balancing](nginx-loadbalancing.md) – Lastausgleich
