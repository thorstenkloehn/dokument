# Robot Framework: Praktische Anleitung für Testautomatisierung

Eine umfassende Schritt-für-Schritt-Anleitung für **Robot Framework** – das flexible Open-Source-Framework für Testautomatisierung, Akzeptanztests und Robotic Process Automation (RPA).

---

## 🎯 Einführung: Was ist Robot Framework?

**Robot Framework** ist ein generisches Open-Source-Framework für Testautomatisierung und Akzeptanztests. Es zeichnet sich durch:

| Merkmal | Beschreibung | Vorteil |
|---------|--------------|--------|
| **Keyword-basiert** | Tests werden in lesbarer Syntax geschrieben | Einfach zu lernen und zu warten |
| **Erweiterbar** | Unterstützt Bibliotheken und benutzerdefinierte Keywords | Maximale Flexibilität |
| **Plattformunabhängig** | Funktioniert auf Windows, macOS, Linux | Ein Framework für alle |
| **Modular** | Unterstützt verschiedene Test-Bibliotheken | Vielfältige Anwendungen |
| **Berichte & Logs** | Detaillierte HTML-Berichte und Logs | Gute Traceability |
| **IDE-Unterstützung** | RIDE, VS Code, PyCharm | Professionelle Entwicklung |

### Einsatzbereiche

| Bereich | Beschreibung | Beispiel |
|---------|--------------|----------|
| **Akzeptanztests** | End-to-End-Tests für Anwendungen | Web-Formular-Tests |
| **Web-Tests** | Browser-Automatisierung | Login-Tests, UI-Tests |
| **API-Tests** | REST/SOAP-API-Tests | RESTful API-Validierung |
| **Datenbank-Tests** | DB-Operationen testen | SQL-Queries validieren |
| **Mobile Tests** | Android/iOS-App-Tests | Appium-Integration |
| **RPA** | Robotic Process Automation | Desktop-Automatisierung |
| **CI/CD** | Kontinuierliche Integration | Jenkins, GitHub Actions |

### Vergleich: Robot Framework vs. Andere Testtools

| Tool | Syntax | Erweiterbarkeit | Web-Tests | API-Tests | RPA | Lernkurve |
|------|--------|----------------|-----------|-----------|-----|------------|
| **Robot Framework** | Keyword-basiert | ✅✅✅✅✅ | ✅✅✅✅ | ✅✅✅✅ | ✅✅✅ | ⭐⭐ |
| **Selenium** | Code-basiert | ✅✅✅ | ✅✅✅✅✅ | ❌ Nein | ❌ Nein | ⭐⭐⭐ |
| **Playwright** | Code-basiert | ✅✅✅✅ | ✅✅✅✅✅ | ❌ Nein | ❌ Nein | ⭐⭐⭐ |
| **Cypress** | Code-basiert | ✅✅✅ | ✅✅✅✅✅ | ❌ Nein | ❌ Nein | ⭐⭐⭐ |
| **Pytest** | Code-basiert | ✅✅✅✅✅ | ✅✅ | ✅✅ | ❌ Nein | ⭐⭐⭐⭐ |
| **PyAutoGUI** | Code-basiert | ✅✅ | ❌ Nein | ❌ Nein | ✅✅✅ | ⭐ |

---

## 📥 Installation

### Grundinstallation (Python)

```bash
# Robot Framework installieren
pip install robotframework

# Version überprüfen
robot --version
```

### Empfohlene Zusatzpakete

```bash
# Web-Testing mit Selenium
pip install robotframework-seleniumlibrary

# Browser-Driver (für Selenium)
# Chrome:
# - Download von https://sites.google.com/chromium.org/driver/
# - Oder: pip install webdriver-manager

# Firefox (GeckoDriver):
# - Download von https://github.com/mozilla/geckodriver/releases

# HTTP-Anfragen (REST API Testing)
pip install robotframework-requests

# Datenbank-Tests
pip install robotframework-databaselibrary

# SSH-Tests
pip install robotframework-sshlibrary

# Alle in einem
pip install robotframework robotframework-seleniumlibrary \
    robotframework-requests robotframework-databaselibrary \
    robotframework-sshlibrary
```

### Installation überprüfen

```bash
# Version prüfen
robot --version

# Hilfe anzeigen
robot --help

# Einfaches Testbeispiel
robot --version && echo "Robot Framework ist installiert!"
```

---

## 🚀 Grundlagen: Erste Schritte

### Einfaches Testbeispiel

Erstelle eine Datei `erster_test.robot`:

```robotframework
*** Settings ***
Documentation    Mein erster Robot Framework Test

*** Test Cases ***
Beispiel Test
    Log    Dies ist ein Testschritt
    Log    weiteres Log
    Pass    Test erfolgreich
```

Führe den Test aus:
```bash
robot erster_test.robot
```

### Teststruktur

```robotframework
*** Settings ***
# Globale Einstellungen
Documentation    Beschreibung des Tests
Library          SeleniumLibrary

*** Variables ***
# Variablen definieren
${URL}          https://www.beispiel.de
${BROWSER}      chrome

*** Test Cases ***
# Testfälle
Öffne Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    Beispiel
    Close Browser

*** Keywords ***
# Benutzerdefinierte Keywords
Meine Anmeldung
    Input Text    id=username    testuser
    Input Text    id=password    testpass
    Click Button    id=login
```

### Ausführung

```bash
# Single Test
robot test.robot

# Mehrere Tests
robot test1.robot test2.robot

# Directory ausführen
robot tests/

# Mit Optionen
robot --outputdir results/ tests/
```

---

## 🧩 Bibliotheken (Libraries)

### Übersicht der wichtigsten Bibliotheken

| Bibliothek | Beschreibung | Install | Typ |
|-------------|--------------|---------|-----|
| **BuiltIn** | Grundfunktionen (Log, Should, Run) | Standard | Core |
| **SeleniumLibrary** | Web-Testing mit Selenium | `pip install robotframework-seleniumlibrary` | Web |
| **RequestsLibrary** | HTTP-Requests für API-Tests | `pip install robotframework-requests` | API |
| **DatabaseLibrary** | Datenbank-Tests (SQL) | `pip install robotframework-databaselibrary` | DB |
| **SSHLibrary** | SSH-Verbindungen testen | `pip install robotframework-sshlibrary` | SSH |
| **ProcessLibrary** | Prozess-Steuerung | `pip install robotframework-processlibrary` | OS |
| **DateTime** | Datum/Zeit-Funktionen | Standard | Core |
| **Collections** | Listen/Dict-Funktionen | Standard | Core |
| **String** | String-Operationen | Standard | Core |

---

## 🌐 Web-Testing mit SeleniumLibrary

### Grundlagen

#### Installation

```bash
pip install robotframework-seleniumlibrary

# Browser-Driver installieren
# Für Chrome:
pip install webdriver-manager

# Oder manuell:
# 1. Download ChromeDriver von https://sites.google.com/chromium.org/driver/
# 2. In PATH platzieren oder Pfad in Test angeben
```

#### Einfaches Web-Testbeispiel

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.beispiel.de
${BROWSER}    chrome

*** Test Cases ***
Öffne und prüfe Website
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Title Should Be    Beispiel
    Page Should Contain    Willkommen
    Close Browser
```

### Element-Lokatoren

| Locator-Typ | Syntax | Beispiel |
|-------------|--------|----------|
| **id** | `id=<value>` | `id=login-button` |
| **name** | `name=<value>` | `name=username` |
| **css** | `css=<selector>` | `css=button.primary` |
| **xpath** | `xpath=<path>` | `xpath=//button[@id='login']` |
| **link** | `link=<text>` | `link=Hier klicken` |
| **partial link** | `partial link=<text>` | `partial link=Login` |
| **tag** | `tag=<name>` | `tag=div` |
| **class** | `class=<name>` | `class=btn` |

### Interaktion mit Elementen

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Formular Test
    Open Browser    https://www.beispiel.de/login    chrome
    
    # Text eingeben
    Input Text    id=username    testuser
    Input Text    id=password    test123
    
    # Dropdown auswählen
    Select From List By Value    id=country    DE
    # oder
    Select From List By Label    id=country    Deutschland
    # oder
    Select From List By Index    id=country    2
    
    # Checkbox aktivieren
    Checkbox Should Be Selected    id=remember-me
    
    # Radio-Button auswählen
    Click Element    id=gender-male
    
    # Button klicken
    Click Button    id=login
    
    # Warten auf Element
    Wait Until Page Contains    Willkommen
    Wait Until Element Is Visible    id=dashboard
    
    Close Browser
```

### Warten (Waiting)

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Warten Beispiele
    Open Browser    https://www.beispiel.de    chrome
    
    # Warten auf Sichtbarkeit
    Wait Until Element Is Visible    id=loading-spinner    timeout=10s
    
    # Warten auf Text
    Wait Until Page Contains    Daten geladen    timeout=5s
    
    # Warten auf URL
    Wait Until Page Contains    /dashboard    timeout=5s
    
    # Warten auf Element verschwindet
    Wait Until Element Is Not Visible    id=loading    timeout=10s
    
    # Warten mit Bedingung
    Wait Until Keyword Succeeds    5 min    5 sec    Element Should Contain    id=status    Fertig
    
    Close Browser
```

### Alerts und Popups

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Alert Handling
    Open Browser    https://www.beispiel.de    chrome
    
    # Alert akzeptieren
    Click Button    id=delete
    Handle Alert    action=accept    text=Sind Sie sicher?
    
    # Alert ablehnen
    Click Button    id=cancel
    Handle Alert    action=dismiss
    
    # Text aus Alert prüfen
    ${alert_text}=    Get Alert Message
    Should Be Equal As Strings    ${alert_text}    Warnung!
    Handle Alert    action=accept
    
    Close Browser
```

### Frames und Windows

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Frames und Windows
    Open Browser    https://www.beispiel.de    chrome
    
    # Zu Frame wechseln
    Select Frame    id=iframe-content
    Click Element    id=frame-button
    
    # Zurück zum Hauptfenster
    Select Frame    relative=parent
    
    # Neues Fenster/Tab öffnen
    Click Element    id=new-window
    
    # Zu neuem Fenster wechseln
    Select Window    title=Neues Fenster
    Page Should Contain    Neuer Inhalt
    
    # Zurück zum ersten Fenster
    Select Window    index=0
    
    Close Browser
```

---

## 📡 API-Testing mit RequestsLibrary

### Installation

```bash
pip install robotframework-requests
```

### Grundlagen

```robotframework
*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://api.beispiel.de

*** Test Cases ***
GET Request Test
    &{headers}=    Create Dictionary    Content-Type=application/json
    ${response}=    GET On Session    ${BASE_URL}/users    headers=${headers}
    
    # Status-Code prüfen
    Should Be Equal As Integers    ${response.status_code}    200
    
    # Response-Body prüfen
    ${body}=    Convert String To Dictionary    ${response.text}
    Should Be Equal As Strings    ${body['status']}    success
    
    # Header prüfen
    Should Be Equal As Strings    ${response.headers['Content-Type']}    application/json
```

### POST-Request

```robotframework
*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://api.beispiel.de

*** Test Cases ***
POST Request Test
    # Session erstellen
    Create Session    ${BASE_URL}
    
    # Request-Body erstellen
    &{data}=    Create Dictionary    username=testuser    password=test123
    ${json_data}=    Convert Dictionary To String    ${data}
    
    # POST-Request senden
    &{headers}=    Create Dictionary    Content-Type=application/json
    ${response}=    POST On Session    /login    json=${json_data}    headers=${headers}
    
    # Antwort prüfen
    Should Be Equal As Integers    ${response.status_code}    200
    ${body}=    Convert String To Dictionary    ${response.text}
    Should Be Equal As Strings    ${body['token']}    abc123xyz
    
    # Session schließen
    Delete All Sessions
```

### Authentication

```robotframework
*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://api.beispiel.de

*** Test Cases ***
Basic Auth Test
    &{auth}=    Create Dictionary    username=admin    password=secret
    ${response}=    GET On Session    ${BASE_URL}/secure    auth=${auth}
    Should Be Equal As Integers    ${response.status_code}    200
    Delete All Sessions

Bearer Token Auth Test
    Create Session    ${BASE_URL}
    &{headers}=    Create Dictionary    Authorization=Bearer abc123xyz
    ${response}=    GET On Session    /secure    headers=${headers}
    Should Be Equal As Integers    ${response.status_code}    200
    Delete All Sessions
```

---

## 🗄️ Datenbank-Testing mit DatabaseLibrary

### Installation

```bash
pip install robotframework-databaselibrary

# Datenbank-Treiber
# PostgreSQL: pip install psycopg2-binary
# MySQL: pip install mysql-connector-python
# SQLite: Standard
```

### Grundlagen

```robotframework
*** Settings ***
Library    DatabaseLibrary

*** Variables ***
${DB_NAME}    testdb
${DB_USER}    admin
${DB_PASS}    password
${DB_HOST}    localhost

*** Test Cases ***
PostgreSQL Test
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}
    
    # Query ausführen
    ${rows}=    Query    SELECT * FROM users WHERE active = True
    
    # Anzahl Zeilen prüfen
    Should Be Equal As Integers    ${rows}    5
    
    # Einzelne Zeile prüfen
    ${first_row}=    Query    SELECT * FROM users LIMIT 1
    Should Be Equal As Strings    ${first_row}[0][1]    Max Mustermann
    
    Disconnect From Database
```

### SQLite-Beispiel

```robotframework
*** Settings ***
Library    DatabaseLibrary

*** Test Cases ***
SQLite Test
    Connect To Database    sqlite3    database.db
    
    # Tabelle erstellen
    Execute SQL    CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)
    
    # Daten einfügen
    Execute SQL    INSERT INTO users (name) VALUES ('Max Mustermann')
    Execute SQL    INSERT INTO users (name) VALUES ('Anna Schmidt')
    
    # Daten prüfen
    ${count}=    Query    SELECT COUNT(*) FROM users
    Should Be Equal As Integers    ${count}    2
    
    # Daten löschen
    Execute SQL    DELETE FROM users
    
    Disconnect From Database
```

---

## 🏗️ Benutzerdefinierte Keywords

### Einfache Keywords

```robotframework
*** Settings ***

*** Keywords ***
Anmelden
    [Arguments]    ${benutzername}    ${passwort}
    Input Text    id=username    ${benutzername}
    Input Text    id=password    ${passwort}
    Click Button    id=login
    Wait Until Page Contains    Willkommen

Ausloggen
    Click Element    id=logout
    Wait Until Page Contains    Auf Wiedersehen

*** Test Cases ***
Login Logout Test
    Open Browser    https://www.beispiel.de    chrome
    Anmelden    testuser    test123
    Ausloggen
    Close Browser
```

### Keywords mit Rückgabewerten

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Get Element Count
    [Arguments]    ${locator}
    ${count}=    Get Element Count    ${locator}
    [Return]    ${count}

Get Element Text
    [Arguments]    ${locator}
    ${text}=    Get Text    ${locator}
    [Return]    ${text}

*** Test Cases ***
Element Count Test
    Open Browser    https://www.beispiel.de    chrome
    ${count}=    Get Element Count    css=.menu-item
    Should Be Greater Than As Integers    ${count}    0
    Close Browser
```

### Keywords mit Standardwerten

```robotframework
*** Settings ***

*** Keywords ***
Suche Element
    [Arguments]    ${locator}    ${timeout}=10s    ${error}=Element nicht gefunden
    Wait Until Element Is Visible    ${locator}    timeout=${timeout}
    ...    error=${error}
    Log    Element ${locator} gefunden

*** Test Cases ***
Suche Test
    Open Browser    https://www.beispiel.de    chrome
    Suche Element    id=main-content
    Suche Element    css=.sidebar    timeout=5s    error=Sidebar nicht sichtbar
    Close Browser
```

---

## 📊 Variablen und Datensteuerung

### Variablen-Typen

```robotframework
*** Variables ***
# Skalar
${STRING}    Hallo Welt
${NUMBER}    42
${BOOLEAN}    ${TRUE}

# Liste
@{LISTE}    Item1    Item2    Item3

# Dictionary
&{DICT}    key1=wert1    key2=wert2

# Liste aus Dictionary
@{LIST_OF_DICTS}    &{item1}    &{item2}
...    &{item1}=    name=Max    age=30
...    &{item2}=    name=Anna    age=25
```

### Variablen in Tests verwenden

```robotframework
*** Settings ***

*** Variables ***
${URL}    https://www.beispiel.de
@{USERS}    user1    user2    user3

*** Test Cases ***
Variablen Beispiel
    Log    URL: ${URL}
    
    # Liste durchgehen
    FOR    ${user}    IN    @{USERS}
        Log    Benutzer: ${user}
    END
    
    # Dictionary
    &{user}=    Create Dictionary    name=Max    age=30
    Log    Name: ${user.name}, Alter: ${user.age}
```

### Externe Variablen-Dateien

Erstelle `variables.py`:
```python
BROWSER = "chrome"
URL = "https://www.beispiel.de"
USERS = ["user1", "user2", "user3"]
```

Verwende in Robot:
```robotframework
*** Settings ***
Variables    variables.py

*** Test Cases ***
Externe Variablen
    Log    Browser: ${BROWSER}
    Log    URL: ${URL}
    FOR    ${user}    IN    @{USERS}
        Log    ${user}
    END
```

---

## 🎯 Praxisprojekte

### Projekt 1: Kompletter Web-Test für E-Commerce

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${URL}    https://www.shop.beispiel.de
${BROWSER}    chrome

*** Keywords ***
Öffne Shop
    Open Browser    ${URL}    ${BROWSER}
    Maximize Browser Window
    Wait Until Page Contains    Willkommen im Shop

Suche Produkt
    [Arguments]    ${suchbegriff}
    Input Text    id=search    ${suchbegriff}
    Press Keys    id=search    RETURN
    Wait Until Page Contains    Suchergebnisse

Füge Zum Warenkorb hinzu
    [Arguments]    ${index}=0
    Click Element    xpath=(//button[contains(text(),'Zum Warenkorb')])[${index}+1]
    Wait Until Page Contains    hinzugefügt

Zur Kasse Gehen
    Click Element    id=checkout
    Wait Until Page Contains    Kasse

*** Test Cases ***
Einkaufsprozess Test
    Öffne Shop
    Suche Produkt    Laptop
    Füge Zum Warenkorb hinzu    0
    Füge Zum Warenkorb hinzu    1
    Zur Kasse Gehen
    Page Should Contain    2 Artikel
    Close Browser
```

### Projekt 2: API-Test-Suite

```robotframework
*** Settings ***
Library    RequestsLibrary

*** Variables ***
${BASE_URL}    https://api.beispiel.de

*** Keywords ***
Create Auth Session
    [Arguments]    ${username}    ${password}
    Create Session    ${BASE_URL}
    &{auth}=    Create Dictionary    username=${username}    password=${password}
    ${response}=    POST On Session    /auth/login    json=${auth}
    [Return]    ${response}

Get With Auth
    [Arguments]    ${endpoint}    ${response}
    &{headers}=    Create Dictionary    Authorization=Bearer ${response.json()['token']}
    ${result}=    GET On Session    ${endpoint}    headers=${headers}
    [Return]    ${result}

*** Test Cases ***
API Authentication Test
    ${auth_response}=    Create Auth Session    testuser    test123
    Should Be Equal As Integers    ${auth_response.status_code}    200
    
    ${user_response}=    Get With Auth    /api/user    ${auth_response}
    Should Be Equal As Integers    ${user_response.status_code}    200
    
    Delete All Sessions

API Data Validation Test
    Create Session    ${BASE_URL}
    
    ${response}=    GET On Session    /api/users
    Should Be Equal As Integers    ${response.status_code}    200
    
    ${users}=    Convert String To Dictionary    ${response.text}
    Length Should Be    ${users}    10
    
    # Prüfen dass alle User aktive E-Mails haben
    FOR    ${user}    IN    ${users}
        Should Contain    ${user['email']}    @
    END
    
    Delete All Sessions
```

### Projekt 3: Datenbank-Integrations-Test

```robotframework
*** Settings ***
Library    SeleniumLibrary
Library    DatabaseLibrary

*** Variables ***
${URL}    https://www.beispiel.de
${DB_HOST}    localhost
${DB_NAME}    testdb
${DB_USER}    admin
${DB_PASS}    password

*** Keywords ***
Connect To DB
    Connect To Database    psycopg2    ${DB_NAME}    ${DB_USER}    ${DB_PASS}    ${DB_HOST}

Get User Count From DB
    ${count}=    Query    SELECT COUNT(*) FROM users
    [Return]    ${count}

Get User Count From UI
    Go To    ${URL}/users
    ${count}=    Get Element Count    css=.user-item
    [Return]    ${count}

*** Test Cases ***
DB-UI Synchronisation Test
    Connect To DB
    
    ${db_count}=    Get User Count From DB
    Open Browser    ${URL}    chrome
    
    ${ui_count}=    Get User Count From UI
    
    Should Be Equal As Integers    ${db_count}    ${ui_count}
    
    Close Browser
    Disconnect From Database
```

### Projekt 4: Komplexes RPA-Skript

```robotframework
*** Settings ***
Library    SeleniumLibrary
Library    OperatingSystem

*** Variables ***
${DOWNLOAD_DIR}    /tmp/downloads

*** Keywords ***
Download File
    [Arguments]    ${url}    ${filename}
    Create Directory    ${DOWNLOAD_DIR}
    ${filepath}=    Set Variable    ${DOWNLOAD_DIR}/${filename}
    
    # Datei herunterladen
    Go To    ${url}
    Click Element    id=download-button
    Wait Until Page Contains    Download gestartet
    
    # Warten bis Datei heruntergeladen
    Wait Until Keyword Succeeds    1 min    5 sec    File Should Exist    ${filepath}
    
    [Return]    ${filepath}

Process File
    [Arguments]    ${filepath}
    # Datei verarbeiten (Beispiel: CSV lesen)
    ${content}=    Get File    ${filepath}
    ${lines}=    Split String To Lines    ${content}
    
    FOR    ${line}    IN    ${lines}
        Log    ${line}
    END
    
    [Return]    ${lines}

*** Test Cases ***
RPA Workflow Test
    Open Browser    https://www.beispiel.de/reports    chrome
    
    ${filepath}=    Download File    https://www.beispiel.de/reports/monthly.csv    report.csv
    ${data}=    Process File    ${filepath}
    
    Should Be Greater Than    ${data}    0
    
    Close Browser
    Remove Directory    ${DOWNLOAD_DIR}    recursive=True
```

---

## 📊 Test-Ausführung und Berichte

### Test-Ausführung

```bash
# Einzelner Test
robot test.robot

# Mehrere Tests
robot test1.robot test2.robot

# Directory
robot tests/

# Mit Tags (nur bestimmte Tests ausführen)
robot --include login tests/
robot --exclude smoke tests/

# Parallelisierung
robot --processes 4 tests/
```

### Berichte und Logs

```bash
# Standard-Ausgabe (erstellt output.xml, report.html, log.html)
robot tests/

# Benutzerdefiniertes Ausgabeverzeichnis
robot --outputdir results/ tests/

# Keine Berichte
robot --log NONE --report NONE --xunit NONE tests/

# Log-Level
robot --loglevel TRACE tests/
```

### Berichte interpretieren

- **report.html**: Übersicht über alle Testfälle mit Statistiken
- **log.html**: Detailliertes Log mit allen Schritten
- **output.xml**: Maschinenlesbares Ergebnis (JUnit-kompatibel)

### CI/CD-Integration

#### GitHub Actions

```yaml
name: Robot Framework Tests

on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v4
    
    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'
    
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install robotframework robotframework-seleniumlibrary
    
    - name: Run tests
      run: robot --outputdir results/ tests/
    
    - name: Upload results
      uses: actions/upload-artifact@v3
      with:
        name: test-results
        path: results/
```

#### Jenkins

```groovy
pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
                sh 'pip install robotframework robotframework-seleniumlibrary'
                sh 'robot --outputdir results/ tests/'
            }
        }
        
        stage('Report') {
            steps {
                publishHTML(target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: 'results',
                    reportFiles: 'report.html',
                    reportName: 'Robot Framework Report'
                ])
            }
        }
    }
    
    post {
        always {
            junit '**/results/output.xml'
        }
    }
}
```

---

## 🛡️ Fehlerbehandlung

### Try-Except (Error Handling)

```robotframework
*** Settings ***

*** Keywords ***
Safe Click
    [Arguments]    ${locator}
    TRY
        Click Element    ${locator}
    EXCEPT    *
        Log    Fehler beim Klicken auf ${locator}    level=WARN
        Capture Page Screenshot
    END

*** Test Cases ***
Fehlerbehandlung Test
    Open Browser    https://www.beispiel.de    chrome
    Safe Click    id=non-existent-element
    Close Browser
```

### Conditional Execution

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Conditional Test
    Open Browser    https://www.beispiel.de    chrome
    
    # Nur ausführen wenn Element sichtbar
    Run Keyword If    ${True}    Log    Dies wird ausgeführt
    Run Keyword If    ${False}    Log    Dies wird NICHT ausgeführt
    
    # Bedingte Ausführung
    ${visible}=    Run Keyword And Return Status    Page Should Contain Element    id=login
    Run Keyword If    ${visible}    Click Element    id=login
    
    Close Browser
```

### Retry-Mechanismus

```robotframework
*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
Retry Until Success
    [Arguments]    ${keyword}    ${max_attempts}=5    ${delay}=1s    @{args}
    FOR    ${i}    IN RANGE    ${max_attempts}
        TRY
            Run Keyword    ${keyword}    @{args}
            [Return]    ${True}
        EXCEPT    *
            Sleep    ${delay}
        END
    END
    Fail    Maximum attempts (${max_attempts}) exceeded

*** Test Cases ***
Retry Test
    Open Browser    https://www.beispiel.de    chrome
    
    ${success}=    Retry Until Success    Click Element    id=dynamic-element    max_attempts=10    delay=2s
    Should Be Equal As Booleans    ${success}    ${True}
    
    Close Browser
```

---

## 📚 Ressourcen und weiterführende Links

### Offizielle Dokumentation
- [Robot Framework User Guide](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Quick Start Guide](https://robotframework.org/robotframework/latest/QuickStart.html)
- [API Documentation](https://robotframework.org/robotframework/latest/RobotFrameworkAPI.html)
- [GitHub Repository](https://github.com/robotframework/robotframework)

### Tutorials und Kurse
- [Robot Framework Tutorial (Official)](https://robotframework.org/#tutorials)
- [Robot Framework Academy](https://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Udemy: Robot Framework Test Automation](https://www.udemy.com/topic/robot-framework/)

### Community Ressourcen
- [Robot Framework Forum](https://forum.robotframework.org/)
- [Stack Overflow - Robot Framework](https://stackoverflow.com/questions/tagged/robotframework)
- [Robot Framework Slack](https://robotframework.slack.com/)

### Bücher
- [Robot Framework Test Automation](https://www.amazon.com/Robot-Framework-Test-Automation-Second/dp/1788835858)
- [Acceptance Test Driven Development with Robot Framework](https://www.amazon.com/Acceptance-Test-Driven-Development-Robot-Framework/dp/1785286339)

### Alternativen
| Tool | Type | Syntax | Lernkurve |
|------|------|--------|------------|
| **Robot Framework** | Keyword-Driven | Keyword-basiert | ⭐⭐ |
| **Selenium** | Code-Driven | Python/Java/etc. | ⭐⭐⭐ |
| **Cypress** | Code-Driven | JavaScript | ⭐⭐ |
| **Playwright** | Code-Driven | JavaScript/Python | ⭐⭐ |
| **Pytest** | Code-Driven | Python | ⭐⭐⭐ |

---

## 🔗 Verwandte Themen

* [Desktop Automation/Übersicht](index.md) – Umfassende Übersicht über Desktop-Automatisierungstools
* [Desktop Automation mit PyAutoGUI](pyautogui-anleitung.md) – GUI-Automatisierung mit Python
* [Desktop Automation mit Playwright](playwright-anleitung.md) – Moderne Web-Automatisierung
* [Desktop Automation mit ydotool](ydotool-anleitung.md) – Low-Level-Automatisierung auf Linux

---

*Letzte Aktualisierung: Juli 2026*
