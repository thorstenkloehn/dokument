# Praxis-Guide: Linux Cgroups v2 & CPU/RAM Limits per CLI

Mit **cgroups v2** (Control Groups) lassen sich Prozessen unter Linux harte Limits für Arbeitsspeicher (RAM) und Rechenleistung (CPU) zuweisen, um Systemüberlastungen durch rechenintensive Hintergrundprozesse zu verhindern.

---

## ⚡ 1. Ad-hoc Prozess-Limits mit `systemd-run`

Starte ein rechenintensives Skript direkt mit 500 MB RAM-Limit und maximal 1 CPU-Kern:

```bash
systemd-run --scope -p MemoryMax=500M -p CPUQuota=100% /home/thorsten/app/skript.sh
```

---

## 🛠️ 2. Cgroups v2 manuell in `/sys/fs/cgroup` steuern

```bash
# 1. Eigenen Control Group Ordner anlegen
sudo mkdir /sys/fs/cgroup/meine_gruppe

# 2. Arbeitsspeicher auf 1 GB begrenzen
echo "1G" | sudo tee /sys/fs/cgroup/meine_gruppe/memory.max

# 3. CPU-Quota auf 50% eines Kerns begrenzen (50000 / 100000)
echo "50000 100000" | sudo tee /sys/fs/cgroup/meine_gruppe/cpu.max

# 4. Aktuellen Shell-Prozess in die Cgroup verschieben
echo $$ | sudo tee /sys/fs/cgroup/meine_gruppe/cgroup.procs
```

---

## 🔗 Verwandte Themen
* [Systemd Service Creation](systemd-service-creation.md) – Service Units mit Cgroups
* [Linux-Systemprogrammierung](linux-systemprogrammierung.md) – Prozessverwaltung
