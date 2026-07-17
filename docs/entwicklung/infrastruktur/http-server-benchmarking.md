# Praxis-Guide: HTTP-Server Benchmarking mit wrk & Apache Benchmark

Methoden zur Messung von Durchsatz (Requests/sec), Latenz und Stabilität von Nginx, Apache und Backend-APIs unter hoher Last.

---

## 🛠️ 1. Werkzeuge installieren

```bash
# Apache Benchmark (ab) installieren
sudo apt update && sudo apt install -y apache2-utils

# wrk (modernes Multi-Threaded Benchmarking Tool) installieren
sudo apt install -y wrk
```

---

## ⚡ 2. Benchmarks durchführen

### Apache Benchmark (`ab`)

```bash
# Sendet 10.000 Requests mit 100 parallelen Verbindungen
ab -n 10000 -c 100 https://app.beispiel.de/
```

### wrk (High-Performance Multi-Threaded Benchmark)

```bash
# Führt einen 30-Sekunden Test mit 4 Threads und 400 parallelen Verbindungen durch
wrk -t4 -c400 -d30s https://app.beispiel.de/
```

Beispiel-Ausgabe von `wrk`:
```text
Running 30s test @ https://app.beispiel.de/
  4 threads and 400 connections
  Thread Stats   Avg      Stdev     Max   +/- Stdev
    Latency    12.45ms    3.12ms  45.10ms   89.12%
    Req/Sec     8.12k     1.20k   10.50k    72.00%
  972410 requests in 30.00s, 1.25GB read
Requests/sec:  32413.67
Transfer/sec:     42.66MB
```

---

## 📊 3. Latenz-Analyse & Auswertung

* **Requests/sec**: Zielwert für statischen Nginx-Content > 20.000 Req/sec.
* **Latency P99**: 99% aller Anfragen sollten in unter 50ms beantwortet werden.

---

## 🔗 Verwandte Themen
* [Nginx Load Balancing](nginx-loadbalancing.md) – Lastausgleich
* [Nginx Hardening & Sicherheit](nginx-hardening.md) – Rate Limiting
* [Benchmark](../../wissen/tools/benchmark.md) – Allgemeine Benchmarks
