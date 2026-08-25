# Claude Cowork in Ihrem Browser nutzen (+ Chrome-Erweiterung)

Neben Desktop-App und Mobile-App läuft Claude Cowork inzwischen auch **direkt im Browser** – auf zwei Wegen: über `claude.ai` selbst und über die **Claude-in-Chrome-Erweiterung**, deren Seitenleiste seit dem 12. August 2026 eine vollwertige Cowork-Sitzung ist.

---

## 🌐 Cowork auf claude.ai (Web)

Seit dem 7. Juli 2026 läuft Cowork als Beta auch direkt im Browser unter `claude.ai` – für Pro-, Max- und Team-Pläne, bei Enterprise nach Freischaltung durch Admins. Aufgaben starten, verfolgen und lenken funktioniert identisch zur Desktop-App.

!!! warning "Lokale Aktionen brauchen weiterhin die Desktop-App"
    Reine Cloud-Aufgaben (Recherche, Textentwürfe, Datenanalyse aus verbundenen Connectors) laufen im Web vollständig eigenständig. Lokaler Dateizugriff, lokale Browser-Steuerung und Computer-Aktionen setzen weiterhin voraus, dass die **Claude-Desktop-App auf dem betreffenden Rechner geöffnet und verbunden bleibt**.

---

## 🧩 Die Claude-in-Chrome-Erweiterung

**Claude in Chrome** ist eine Browser-Erweiterung, die Claude die aktuell geöffnete Seite „sehen" und darauf handeln lässt: Links klicken, Formulare ausfüllen, Text eingeben, zwischen Seiten navigieren – unter Nutzung der bereits bestehenden Logins.

### Installation

1. Erweiterung über den **Chrome Web Store** installieren.
2. Mit dem Claude-Account anmelden.
3. Seitenleiste (Side Panel) öffnen.

### Verfügbarkeit (Stand 08/2026)

| Plan | Zugriff |
|---|---|
| **Max, Team** | Sofort verfügbar |
| **Pro** | Rollout läuft, folgt in den kommenden Wochen |
| **Enterprise** | Standardmäßig deaktiviert; Admins können freischalten und auf bestimmte Domains beschränken |

### Was sie zusätzlich ermöglicht

Seit dem Update vom 12. August 2026 ist die Seitenleiste keine isolierte Mini-Funktion mehr, sondern eine vollständige Cowork-Sitzung:

- **Gespeicherte Historie:** Unterhaltungen werden wie jede andere Cowork-Sitzung gespeichert.
- **Skills & Connectors:** Funktionieren auch im Browser-Kontext.
- **Geräteübergreifende Fortsetzung:** Eine im Browser-Tab begonnene Aufgabe lässt sich auf Desktop, Web oder Mobile fortsetzen.

!!! tip "Praxisbeispiel"
    Rechnungsdaten aus mehreren Lieferantenportalen (interne Dashboards, Legacy-Systeme, Vendor-Portale ohne eigene Claude-Anbindung) einsammeln und direkt im Browser zu einer Budget-Tabelle zusammenführen – anschließend die Sitzung zur Feinbearbeitung an die Desktop-App übergeben.

### Grenzen der Erweiterung

- Funktioniert **nur in Chrome**, nicht in anderen Chromium-Browsern (Edge, Brave, Arc) und nicht auf Mobilgeräten.
- Ersetzt nicht die Desktop-App für Dateiarbeit oder Anbindung von Drittanwendungen außerhalb des Browsers.
- **Sicherheitshinweis:** Wie jeder Browser-Agent ist die Erweiterung grundsätzlich anfällig für Prompt-Injection über manipulierte Webseiteninhalte. Cowork verifiziert deshalb folgenreiche Aktionen (Formular-Absenden, Käufe) zusätzlich, bevor sie ausgeführt werden – ersetzt aber nicht die eigene Wachsamkeit bei unbekannten Seiten.

---

## 🔗 Verwandte Themen

- [Ihr erstes Projekt mit Claude Cowork](claude-cowork-erstes-projekt.md)
- [Claude Cowork in der Praxis anwenden](claude-cowork-praxis.md)
- [Empfohlene Tools und kostenlose Ressourcen](claude-cowork-tools-ressourcen.md)
- [Claude Cowork von Ihrem Smartphone aus nutzen](claude-cowork-smartphone.md)
- [Claude Cowork unter Linux](claude-cowork-linux.md)
- [Claude Cowork vs. Claude Code vs. Antigravity](claude-cowork-code-antigravity-vergleich.md)
