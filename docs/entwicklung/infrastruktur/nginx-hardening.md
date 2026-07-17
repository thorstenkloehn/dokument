# Praxis-Guide: Nginx Hardening & Server-Sicherheit

Eine produktionsreife Nginx-Konfiguration erfordert robuste Sicherheitsmaßnahmen zum Schutz vor DDoS-Angriffen, Brute-Force, Bad Bots und Information Disclosure.

---

## 🔒 1. Sicherheits-Header (Security Headers)

Füge folgende Direktiven in deine Nginx-Konfiguration (`/etc/nginx/conf.d/security.conf`) ein:

```nginx
# Verhindere Clickjacking
add_header X-Frame-Options "SAMEORIGIN" always;

# Verhindere MIME-Type-Sniffing
add_header X-Content-Type-Options "nosniff" always;

# XSS-Schutz für ältere Browser
add_header X-XSS-Protection "1; mode=block" always;

# Referrer Policy für Datenschutz
add_header Referrer-Policy "strict-origin-when-cross-origin" always;

# HTTP Strict Transport Security (HSTS) - 2 Jahre
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;

# Content Security Policy (CSP) Grundgerüst
add_header Content-Security-Policy "default-src 'self' http: https: data: blob: 'unsafe-inline'" always;
```

---

## ⚡ 2. Rate Limiting (Schutz vor DoS & Brute Force)

In `/etc/nginx/nginx.conf` im `http`-Block definieren:

```nginx
# Maximal 10 Anfragen pro Sekunde pro IP-Adresse erlauben
limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s;

# Maximal 20 parallele Verbindungen pro IP
limit_conn_zone $binary_remote_addr zone=addr:10m;
```

Im jeweiligen `server`- oder `location`-Block anwenden:

```nginx
location /login/ {
    limit_req zone=one burst=5 nodelay;
    limit_conn addr 5;
    proxy_pass http://backend_upstream;
}
```

---

## 🛡️ 3. Information Disclosure reduzieren

In `/etc/nginx/nginx.conf`:

```nginx
# Nginx Versionsnummer in Fehlermeldungen verbergen
server_tokens off;
```

---

## 🚨 4. Fail2ban Integration gegen Brute Force

### Fail2ban Filter erstellen (`/etc/fail2ban/filter.d/nginx-req-limit.conf`)
```ini
[Definition]
failregex = limiting requests, excess:.* by zone.*client: <HOST>
ignoregex =
```

### Jail konfigurieren (`/etc/fail2ban/jail.local`)
```ini
[nginx-req-limit]
enabled = true
filter = nginx-req-limit
logpath = /var/log/nginx/error.log
findtime = 600
maxretry = 10
bantime = 3600
```

```bash
sudo systemctl restart fail2ban
```

---

## 🔗 Verwandte Themen
* [Nginx & SSL](nginx-ssl.md) – SSL/TLS Verschlüsselung
* [Sicherheit Übersicht](sicherheit/index.md) – Server-Sicherheit
* [Docker KI-Stack](docker-ki-stack.md) – Nginx im Docker Container
