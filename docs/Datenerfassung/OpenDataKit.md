# OpenDataKit (ODK): Komplettanleitung

**OpenDataKit (ODK)** ist ein Open-Source-Toolkit zur effizienten Erhebung von Daten in Feldstudien. Das System ist speziell für den Einsatz in Entwicklungsländern und Ressourcen-begrenzten Umgebungen konzipiert und ermöglicht die Datenerfassung auf mobilen Geräten – auch offline. ODK wird von einer aktiven Community unterstützt und von Regierungen, NGOs, Forschungseinrichtungen und Unternehmen weltweit eingesetzt.

---

## 📋 Überblick

### Was ist ODK?

ODK ist eine Sammlung von Open-Source-Tools, die gemeinsam ein vollständiges System für die mobile Datenerfassung bieten:

| Komponente | Zweck | Plattform |
|------------|-------|-----------|
| **ODK Collect** | Mobile App zur Datenerfassung | Android |
| **ODK Central** | Server zur Formular- und Datenverwaltung | Web/Server |
| **ODK Aggregate** | Älterer Server (Vorgänger von Central) | Web/Server |
| **ODK Build** | Web-basierter Formular-Designer | Web |
| **ODK Validate** | CLI-Tool zur Formular-Validierung | Desktop |
| **ODK Briefcase** | Desktop-Tool für Daten-Synchronisation | Desktop |
| **XLSForm** | Excel-basiertes Formular-Design | Excel/Spreadsheet |

### Hauptmerkmale

✅ **Offline-Fähigkeit** – Volle Funktionalität ohne Internetverbindung
✅ **Open Source** – Kostenlos und frei anpassbar
✅ **Plattformunabhängig** – Laufend auf Android, mit Web-Alternativen
✅ **Skalierbar** – Geeignet für kleine Projekte bis zu großen Studien
✅ **Mehrsprachig** – Unterstützung für über 100 Sprachen
✅ **Erweiterbar** – Plugins und Customizations möglich

---

## 🚀 Schnellstart

### 1. Installation von ODK Collect (Android)

#### Methode A: Google Play Store
1. Öffne den **Google Play Store** auf deinem Android-Gerät
2. Suche nach **"ODK Collect"**
3. Installiere die App von **ODK** (Entwickler: ODK Team)
4. Starte die App nach der Installation

#### Methode B: APK-Download
1. Lade die neueste APK von [ODK Downloads](https://github.com/getodk/collect/releases) herunter
2. Aktiviere auf deinem Gerät: **Einstellungen → Sicherheit → Unbekannte Quellen**
3. Installiere die APK-Datei
4. Starte ODK Collect

#### Methode C: F-Droid
1. Installiere **F-Droid** (Open-Source App-Store)
2. Suche nach **ODK Collect**
3. Installiere die App

### 2. Installation von ODK Central (Server)

#### Voraussetzungen
- Ubuntu 20.04/22.04/24.04 oder Docker
- Mindestens 2GB RAM, 2 CPU-Kerne
- Domain oder IP-Adresse mit SSL-Zertifikat

#### Docker-basierte Installation (empfohlen)

```bash
# Verzeichnis erstellen
mkdir odk-central && cd odk-central

# docker-compose.yml erstellen
cat > docker-compose.yml << 'EOF'
version: '3'
services:
  service:
    image: getodk/central:latest
    container_name: odk-central
    ports:
      - "8080:80"
      - "8443:443"
    volumes:
      - central-data:/srv
    environment:
      - ODK_CENTRAL_DEFAULT_ADMIN_PASSWORD=your-secure-password
      - ODK_CENTRAL_DEFAULT_ADMIN_EMAIL=admin@example.com
      - ODK_CENTRAL_PERIODIC_BACKUPS=true
    restart: unless-stopped

volumes:
  central-data:
EOF

# Container starten
docker compose up -d
```

Die Oberfläche ist danach unter `https://localhost:8443` erreichbar.

#### Manuelle Installation (ohne Docker)

Siehe [Offizielle ODK Central Installationsanleitung](https://docs.getodk.org/central-install/)

---

## 📝 Formular-Design mit XLSForm

### Was ist XLSForm?

XLSForm ist ein **Excel-basiertes Format** zur Definition von Formularen für ODK. Es ermöglicht:

- Einfache Erstellung von Formularen ohne Programmierung
- Verwendung von Excel oder Google Sheets
- Definition von Validierungen, Skip-Logik und Berechnungen

### XLSForm-Struktur

Ein XLSForm besteht aus mehreren **Tabs (Blättern)**:

| Tab | Zweck | Pflicht |
|-----|-------|---------|
| **survey** | Hauptfragen des Formulars | ✅ Ja |
| **choices** | Auswahlmöglichkeiten (z. B. für Multiple-Choice) | Nein |
| **settings** | Formular-Einstellungen | Nein |

### Grundlegende Syntax

| Spalte | Inhalt | Beispiel |
|--------|--------|----------|
| **type** | Fragetyp | `text`, `int`, `select_one`, `select_multiple` |
| **name** | Variable Name | `age`, `gender` |
| **label** | Frage-Text | `Wie alt sind Sie?` |
| **hint** | Hilfetext | `Geben Sie Ihr Alter in Jahren an` |
| **required** | Pflichtfeld | `yes`, `no` |
| **constraint** | Validierungsregel | `. > 0` (muss > 0 sein) |

### Fragetypen

| Typ | Beschreibung | Beispiel |
|-----|--------------|----------|
| `text` | Einzeiliger Text | Name, Adresse |
| `integer` | Ganzzahl | Alter, Anzahl |
| `decimal` | Dezimalzahl | Gewicht, Temperatur |
| `date` | Datum | Geburtsdatum |
| `time` | Uhrzeit | Beginnzeit |
| `datetime` | Datum + Uhrzeit | Zeitstempel |
| `select_one` | Single-Choice | Geschlecht, Status |
| `select_multiple` | Multiple-Choice | Interessen, Symptome |
| `yes_no` | Ja/Nein Frage | `Ja` oder `Nein` |
| `image` | Bildaufnahme | Foto hochladen |
| `audio` | Audioaufnahme | Sprachmemo |
| `video` | Videoaufnahme | Video aufnehmen |
| `geopoint` | GPS-Koordinaten | Standort erfassen |
| `geoshape` | Polygon/Area | Flächen erfassen |
| `calculate` | Berechnetes Feld | `sum(${var1}, ${var2})` |

---

## 📱 ODK Collect: Bedienungsanleitung

### Erste Schritte

1. **App starten** – ODK Collect öffnen
2. **Server konfigurieren**
   - URL des ODK Central/ Aggregate Servers eingeben
   - Benutzername und Passwort eingeben
   - Verbindung testen
3. **Formulare herunterladen**
   - Auf **"Formulare erhalten"** klicken
   - gewünschtes Formular auswählen
   - **Herunterladen** wählen
4. **Formular ausfüllen**
   - Heruntergeladenes Formular öffnen
   - Fragen beantworten
   - **Speichern** (Zwischenspeicherung) oder **Senden** (Upload)

### Wichtige Funktionen

| Funktion | Beschreibung |
|----------|--------------|
| **Entwurf speichern** | Speichert unvollständige Formulare für spätere Fortsetzung |
| **Senden** | Lädt ausgefüllte Formulare an den Server hoch |
| **Gesendete Formulare** | Zeigt bereits hochgeladene Formulare an |
| **Gespeicherte Formulare** | Zeigt unvollständige/gespeicherte Formulare an |

---

## 🖥️ ODK Central: Serververwaltung

### Dashboard-Übersicht

Nach dem Login sehen Sie:

- **Projects** – Ihre Projekte
- **Forms** – Formulare in jedem Projekt
- **Submissions** – Eingereichte Daten
- **Users** – Benutzerverwaltung

### Projekt erstellen

1. Auf **"New Project"** klicken
2. **Projektname** eingeben
3. **Beschreibung** hinzufügen (optional)
4. **Speichern**

### Formular hochladen

1. In das gewünschte Projekt navigieren
2. Auf **"Upload Form"** klicken
3. **XLSForm-Datei** oder **ZIP-Datei** auswählen
4. Formular-Details eingeben
5. **Upload**

---

## 📊 Datenanalyse & Export

### Daten exportieren

ODK Central unterstützt verschiedene Exportformate:
- **CSV** – Für Excel, Python, R
- **JSON** – Für API-Integration
- **OSM** – Für GIS-Anwendungen

### Beispiel: Python-Analyse

```python
import pandas as pd

# CSV einlesen
df = pd.read_csv('odk-export.csv')

# Grundlegende Statistik
print(df.describe())

# Nach Geschlecht gruppieren
print(df['gender'].value_counts())
```

---

## 🔗 Weiterführende Ressourcen

- [ODK Dokumentation](https://docs.getodk.org/)
- [ODK Collect Handbuch](https://docs.getodk.org/collect-intro/)
- [ODK Central Handbuch](https://docs.getodk.org/central-intro/)
- [XLSForm Dokumentation](https://xlsform.org/)
- [ODK Community Forum](https://forum.getodk.org/)
