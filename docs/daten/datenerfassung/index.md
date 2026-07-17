# Datenerfassung: Tools, Methoden & Workflows

Eine umfassende Übersicht über Software, Technologien und Best Practices zur systematischen Erfassung, Validierung und Verarbeitung von Daten – insbesondere für Feldstudien, Forschung und betriebliche Anwendungen.

---

## 📊 Übersicht

Die Datenerfassung ist ein zentraler Bestandteil von Forschungsprojekten, Monitoring-Systemen und betrieblichen Prozessen. Moderne Tools ermöglichen die effiziente Erhebung von Daten unter verschiedenen Bedingungen – online und offline, auf mobilen Geräten oder stationären Systemen.

Diese Dokumentation konzentriert sich auf **Open-Source-Lösungen**, die lokal installiert und selbst gehostet werden können, um maximale Datenhoheit und Datenschutz zu gewährleisten.

---

## 🎯 Anwendungsbereiche

| Bereich | Typische Anwendungen | Empfohlene Tools |
|---------|---------------------|------------------|
| **Feldforschung** | Umfragen, Interviews, Beobachtungen | ODK, KoBoToolbox, SurveyCTO |
| **Medizinische Studien** | Patientendaten, klinische Erhebungen | OpenClinica, REDCap |
| **Bildung & Evaluation** | Lernfortschritt, Feedback | Moodle Umfragen, LimeSurvey |
| **Umweltmonitoring** | Sensoren, IoT-Geräte | QField, QGIS Mobile |
| **Betriebliche Datenerfassung** | Inventur, Qualitätskontrolle | Odoo, ERPNext |

---

## 🛠️ Hauptkategorien

### 1. [OpenDataKit (ODK)](OpenDataKit.md)
Ein Open-Source-Toolkit zur Erhebung von Daten in Feldstudien, speziell für den Einsatz in Entwicklungsländern und Ressourcen-begrenzten Umgebungen konzipiert.

* **Plattform**: Android (primär), Web-Formulare
* **Offline-Fähigkeit**: ✅ Volle Offline-Unterstützung mit späterer Synchronisation
* **Formular-Designer**: XLSForm (Excel-basiert) oder Online-Builder
* **Datenmanagement**: ODK Central, ODK Aggregate

### 2. Mobile Datenerfassung

#### Android-basierte Lösungen

* **[ODK Collect](OpenDataKit.md)** – Die Referenzimplementierung für ODK-Formulare auf Android
* **KoBoCollect** – Kompatible Alternative mit zusätzlichen Funktionen
* **QField** – Für GIS-basierte Datenerfassung mit QGIS
* **ODK Central** – Server-Komponente zum Verwalten von Formularen und Daten

#### iOS-basierte Lösungen

* **ODK Collect (iOS Beta)** – Offizielle iOS-Version
* **PyForm** – Alternative für iOS-Geräte

### 3. Web-basierte Datenerfassung

* **LimeSurvey** – Professionelles Online-Umfrage-Tool
* **REDCap** – Für klinische Studien und Gesundheitsdaten
* **Form.io** – Open-Source Formular-Builder mit API-Integration
* **Directus** – Headless CMS mit Formular-Frontend

### 4. Offline-First Lösungen

* **ODK** – Der Standard für Offline-Datenerfassung
* **SurveyCTO** – Kommerzielle Alternative mit Offline-Modus
* **CommCare** – Für Gesundheitsprogramme in entlegenen Gebieten
* **KoboToolbox** – Open-Source Alternative mit Cloud-Sync

---

## 🔄 Daten-Synchronisation

### Synchronisationsmethoden

| Methode | Beschreibung | Tools |
|---------|--------------|-------|
| **Direkte Sync** | Daten werden bei Internetverbindung automatisch hochgeladen | ODK Collect → ODK Central |
| **Batch-Sync** | Manuelle oder geplante Synchronisation | ODK Briefcase |
| **Cloud-Sync** | Synchronisation über Cloud-Dienste | Google Drive, Dropbox |
| **Lokales Netzwerk** | Sync über lokales WLAN/Server | ODK Aggregate |

### ODK Briefcase
Ein Desktop-Tool zur Verwaltung der Synchronisation zwischen Feldgeräten und Servern:

* Export/Import von Formularen
* Datenbereinigung und -transformation
* Unterstützung für mehrere Server

---

## 📈 Datenvalidierung & Qualitätssicherung

### Validierungsmethoden

1. **Formular-Constraints**
   - Pflichtfelder
   - Datentyp-Validierung
   - Bereichsprüfungen (Min/Max Werte)
   - Reguläre Ausdrücke für Textmuster

2. **Konditionelle Logik**
   - Dynamische Fragen basierend auf vorherigen Antworten
   - Skip-Logik (Überspringen irrelevanter Fragen)
   - Berechnete Felder

3. **Datenbereinigung**
   - Duplikaterkennung
   - Ausreißer-Detektion
   - Konsistenzprüfungen

### Tools für Validierung

* **ODK Validate** – CLI-Tool zur Formular-Validierung
* **XLSForm Validator** – Online-Tool zur Prüfung von XLSForm-Dateien
* **Python (Pandas, NumPy)** – Für programmatische Datenbereinigung
* **OpenRefine** – Für interaktive Datenbereinigung

---

## 🗄️ Datenbanken & Speicherung

### Lokale Speicheroptionen

* **SQLite** – Leichtgewichtige Datenbank für mobile Geräte
* **PostgreSQL** – Robuste Relation Datenbank für Server
* **MongoDB** – Dokumenten-basierte Speicherung für flexible Datenstrukturen

### Cloud-basierte Optionen

* **ODK Central** – Eigener Server für ODK-Daten
* **KoBoToolbox Server** – Gehostete Lösung
* **Self-hosted Lösungen** – Eigene Installation auf VPS

---

## 🔍 Datenanalyse & Visualisierung

### Analyse-Tools

* **R** – Statistische Analyse und Visualisierung
* **Python (Pandas, SciPy, Matplotlib)** – Datenanalyse mit Jupyter Notebooks
* **QGIS** – Räumliche Analyse für GIS-Daten
* **Tableau Public** – Visualisierung (nicht Open Source)
* **Metabase** – Open-Source Business Intelligence

### Automatisierte Berichte

* **Jupyter Notebooks** – Reproduzierbare Analysen
* **R Markdown** – Dynamische Berichte in R
* **Apache Superset** – Dashboards und Visualisierungen

---

## 🔐 Datenschutz & Sicherheit

### Best Practices

1. **Datenminimierung** – Nur notwendige Daten erheben
2. **Anonymisierung** – Persönliche Daten anonymisieren
3. **Verschlüsselung** – Daten auf Geräten und bei Übertragung verschlüsseln
4. **Zugriffskontrolle** – Rollenbasierte Berechtigungen
5. **Audit-Logs** – Protokollierung aller Zugriffe

### ODK-spezifische Sicherheitsmaßnahmen

* **Formular-Verschlüsselung** – Ende-zu-Ende-Verschlüsselung für sensible Daten
* **Geräte-PIN** – Schutz vor unerlaubtem Zugriff
* **SSL/TLS** – Verschlüsselte Kommunikation mit Servern
* **Datenlöschung** – Automatische Löschung nach Upload

---

## 📱 Geräteverwaltung

### Unterstützte Geräte

* **Android Smartphones/Tablets** – Primäre Plattform für ODK
* **iOS Geräte** – Eingeschränkte Unterstützung
* **Windows Tablets** – Über Android-Emulator oder Web-Formulare
* **Dedizierte Datenerfassungsgeräte** – Robuste Geräte für extreme Bedingungen

### Gerätekonfiguration

* **MDM (Mobile Device Management)** – Fernverwaltung von Feldgeräten
* **Kiosk-Modus** – Einschränkung auf Datenerfassungs-App
* **Batterie-Optimierung** – Energieeinstellungen für lange Feldissionen
* **Offline-Karten** – Vorab heruntergeladene Karten für GPS-Datenerfassung

---

## 🚀 Implementierungsroadmap

### Schritt 1: Anforderungen definieren
- [ ] Datentypen identifizieren (Text, Zahlen, Bilder, GPS, etc.)
- [ ] Offline-Anforderungen klären
- [ ] Anzahl der Datenerfasser schätzen
- [ ] Synchronisationsintervall festlegen

### Schritt 2: Tool-Auswahl
- [ ] Formular-Komplexität bewerten
- [ ] Plattform-Anforderungen (Android/iOS/Web) klären
- [ ] Server-Infrastruktur planen
- [ ] Budget festlegen

### Schritt 3: Formular-Design
- [ ] Fragen formulieren
- [ ] Validierungsregeln definieren
- [ ] Konditionelle Logik implementieren
- [ ] Testformular erstellen

### Schritt 4: Pilotphase
- [ ] Kleine Gruppe von Datenerfassern einbinden
- [ ] Feedback sammeln
- [ ] Probleme beheben
- [ ] Schulungsmaterial erstellen

### Schritt 5: Rollout
- [ ] Alle Geräte konfigurieren
- [ ] Datenerfasser schulen
- [ ] Synchronisationsprozess etablieren
- [ ] Monitoring einrichten

---

## 📚 Weiterführende Ressourcen

### Offizielle Dokumentation

* [ODK Dokumentation](https://docs.getodk.org/)
* [ODK Community Forum](https://forum.getodk.org/)
* [XLSForm Spezifikation](https://xlsform.org/)

### Tutorials & Guides

* [ODK Getting Started Guide](https://docs.getodk.org/getting-started/)
* [XLSForm Tutorial](https://xlsform.org/en/)
* [ODK Central Setup Guide](https://docs.getodk.org/central-intro/)

### Community & Support

* [ODK GitHub](https://github.com/getodk)
* [ODK Slack Community](https://slack.getodk.org/)
* [Stack Overflow (ODK Tag)](https://stackoverflow.com/questions/tagged/odk)

---

## 🔗 Verwandte Themen

* [Server/Kachelserver](../Server/Kachelserver/Server244.md) – Räumliche Datenverarbeitung
* [Server/Postgresql](../Server/Postgresql.md) – Datenbankspeicherung
* [Dokument_Erstellen](../Dokument_Erstellen/index.md) – Dokumentation der Datenerfassung
* [Tools/Analysetool](../Tools/Analysetool.md) – Datenanalyse-Tools
