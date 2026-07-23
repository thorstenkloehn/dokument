# Praxis-Guide: Systemd Service Creation & Linux Prozessverwaltung

Eine Schritt-für-Schritt-Anleitung zur Erstellung von eigenen **Systemd Service Units** unter Linux für automatischen Systemstart, Prozessüberwachung, Logging via `journalctl` und Auto-Restart im Fehlerfall.

---

## ⚙️ 1. Systemd Service Unit erstellen

Erstelle die Datei `/etc/systemd/system/mein_dienst.service`:

```ini
[Unit]
Description=Mein eigener Python Hintergrund-Dienst
After=network.target postgresql.service
Wants=postgresql.service

[Service]
Type=simple
User=thorsten
WorkingDirectory=/home/thorsten/app
ExecStart=/home/thorsten/app/.venv/bin/python main.py

# Neustart-Verhalten im Fehlerfall
Restart=always
RestartSec=5s

# Ressourcen-Beschränkungen (Cgroups)
MemoryMax=1G
CPUWeight=100

# Security Hardening
NoNewPrivileges=true
ProtectSystem=full

[Install]
WantedBy=multi-user.target
```

---

## 🚀 2. Dienst aktivieren & verwalten

```bash
# Systemd-Konfiguration neu laden
sudo systemctl daemon-reload

# Dienst beim Systemstart aktivieren & sofort starten
sudo systemctl enable --now mein_dienst.service

# Status prüfen
sudo systemctl status mein_dienst.service

# Logs in Echtzeit verfolgen
journalctl -u mein_dienst.service -f
```

---

## 🔗 Verwandte Themen
* [Linux-Systemprogrammierung](linux-systemprogrammierung.md) – Prozesse & Signale
* [Nginx Hardening](../infrastruktur/nginx-hardening.md) – Server-Sicherheit
