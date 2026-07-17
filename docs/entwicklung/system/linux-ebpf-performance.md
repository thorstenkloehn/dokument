# Praxis-Guide: Linux eBPF & Kernel Performance Profiling

**eBPF** (Extended Berkeley Packet Filter) ermöglicht das sichere Ausführen von Sandbox-Skripten im Linux-Kernel zur Echtzeit-Analyse von Systemaufrufen, I/O-Latenzen und Netzwerksignalen ohne Kernel-Module zu kompilieren.

---

## 🛠️ 1. BCC Tools (BPF Compiler Collection) installieren

```bash
sudo apt update && sudo apt install -y bpfcc-tools linux-headers-$(uname -r)
```

---

## ⚡ 2. Praxis-Tools für Systemanalysen

### Block I/O Latenz-Histogramm messen (`biolatency-bpfcc`)
Misst Festplatten-Lese/Schreiblatenzen im Kernel:

```bash
sudo biolatency-bpfcc 1 10
```

### Datei-Zugriffe in Echtzeit überwachen (`opensnoop-bpfcc`)
Zeigt alle `open()` Systemaufrufe von Prozessen:

```bash
sudo opensnoop-bpfcc
```

### Slow Disk Operations analysieren (`biosnoop-bpfcc`)
```bash
sudo biosnoop-bpfcc
```

---

## 🔗 Verwandte Themen
* [Linux-Systemprogrammierung](linux-systemprogrammierung.md) – Kernel & Systemrufe
* [Linux Cgroups v2 Limits](linux-cgroups-limits.md) – Cgroups
* [HTTP Server Benchmarking](../infrastruktur/http-server-benchmarking.md) – Benchmarking
