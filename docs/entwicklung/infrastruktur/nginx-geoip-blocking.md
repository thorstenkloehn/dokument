# Praxis-Guide: Nginx GeoIP Blocking & Bot-Abwehr

Schütze Server und Web-Anwendungen durch geografische IP-Sperren (**GeoIP2**) und automatisierte Erkennung böswilliger Bots und Crawler.

---

## 🔒 1. GeoIP2 Modul & Datenbank installieren

```bash
sudo apt update && sudo apt install -y libmaxminddb0 libmaxminddb-dev mmdb-bin nginx-module-geoip2
```

---

## ⚙️ 2. Nginx GeoIP2 Konfiguration (`nginx.conf`)

Im `http`-Block von `/etc/nginx/nginx.conf`:

```nginx
geoip2 /var/lib/GeoIP/GeoLite2-Country.mmdb {
    $geoip2_data_country_code country iso_code;
}

# Erlaube nur Zugriffe aus Deutschland, Österreich und der Schweiz (DE, AT, CH)
map $geoip2_data_country_code $allowed_country {
    default no;
    DE yes;
    AT yes;
    CH yes;
}

# Bad Bot Blocking via User-Agent Match
map $http_user_agent $bad_bot {
    default 0;
    ~*(bytespider|gptbot|claudebot|semrushbot) 1;
}
```

---

## ⚡ 3. Sperre im Server-Block durchsetzen

```nginx
server {
    listen 80;
    server_name app.beispiel.de;

    # 1. Bad Bots blockieren
    if ($bad_bot = 1) {
        return 403;
    }

    # 2. Zugriffe außerhalb erlaubter Länder blockieren
    if ($allowed_country = no) {
        return 403 "Zugriff aus Ihrem Land ist nicht gestattet.";
    }

    location / {
        proxy_pass http://localhost:8080;
    }
}
```

---

## 🔗 Verwandte Themen
* [Nginx Hardening & Sicherheit](nginx-hardening.md) – Rate Limiting & HSTS
* [Nginx Load Balancing](nginx-loadbalancing.md) – Lastausgleich
* [Docker KI-Stack](docker-ki-stack.md) – Nginx im Container
