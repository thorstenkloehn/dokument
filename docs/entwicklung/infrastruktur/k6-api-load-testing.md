# Praxis-Guide: k6 API Load & Stress Testing

**k6** (von Grafana) ist ein modernes, skriptbasiertes Open-Source-Tool für Last- und Performance-Tests von REST-APIs, WebSockets und Webservern in JavaScript.

---

## 🛠️ 1. Installation

```bash
sudo gpg -k
sudo gpg --no-default-keyring --keyring /usr/share/keyrings/k6-archive-keyring.gpg --keyserver hkp://keyserver.ubuntu.com:80 --recv-keys C5AD17C747E3415A3642D57D77C6C491D6AC1D69
echo "deb [signed-by=/usr/share/keyrings/k6-archive-keyring.gpg] https://dl.k6.io/deb stable main" | sudo tee /etc/apt/sources.list.d/k6.list
sudo apt update && sudo apt install k6
```

---

## 💻 2. Lasttest-Skript in JavaScript (`load_test.js`)

```javascript
import http from 'k6/http';
import { check, sleep } from 'k6';

// 1. Test-Szenario Konfiguration (Ramping VUs)
export const options = {
  stages: [
    { duration: '30s', target: 50 },  # Ramp-Up auf 50 parallele Nutzer
    { duration: '1m',  target: 50 },  # 1 Minute halten
    { duration: '15s', target: 0 },   # Ramp-Down
  ],
  thresholds: {
    http_req_duration: ['p(95)<200'], # 95% aller Requests müssen < 200ms sein
    http_req_failed: ['rate<0.01'],    # Weniger als 1% Fehlerquote
  },
};

// 2. Testausführung pro virtuellem Nutzer (VU)
export default function () {
  const res = http.get('https://app.beispiel.de/api/status');
  
  check(res, {
    'Status ist 200': (r) => r.status === 200,
    'Antwortzeit ok': (r) => r.timings.duration < 200,
  });

  sleep(1);
}
```

---

## ⚡ 3. Test starten

```bash
k6 run load_test.js
```

---

## 🔗 Verwandte Themen
* [HTTP Server Benchmarking](http-server-benchmarking.md) – wrk & ab
* [Nginx Load Balancing](nginx-loadbalancing.md) – Lastausgleich
* [PostgreSQL Performance Tuning](postgresql-tuning.md) – Datenbank-Tuning
