# Praxis-Guide: Robot Framework API-Testing

Das **Robot Framework** ist ein plattformunabhängiges, keyword-basiertes Test-Automation-Framework für Akzeptanztests und robotergestützte Prozessautomatisierung (RPA).

---

## 🛠️ 1. Installation

```bash
pip install robotframework robotframework-requests
```

---

## 🤖 2. Test-Suite erstellen (`api_tests.robot`)

```robot
*** Settings ***
Documentation     End-to-End REST API Test Suite
Library           RequestsLibrary
Library           Collections

*** Variables ***
${BASE_URL}       https://jsonplaceholder.typicode.com

*** Test Cases ***
GET User Details And Validate JSON
    [Documentation]    Prüft ob der User-Endpunkt Status 200 und korrekte Daten liefert
    Create Session    api_session    ${BASE_URL}    verify=True
    ${response}=      GET On Session    api_session    /users/1
    
    # Statuscode prüfen
    Status Should Be    200    ${response}
    
    # JSON-Daten verifizieren
    ${json}=          Set Variable    ${response.json()}
    Should Be Equal As Strings    ${json['name']}    Leanne Graham
    Should Be Equal As Strings    ${json['username']}    Bret

POST New Item And Verify Creation
    [Documentation]    Erstellt ein neues Item via POST-Request
    Create Session    api_session    ${BASE_URL}
    &{headers}=       Create Dictionary    Content-Type=application/json
    &{payload}=       Create Dictionary    title=Robot Test    body=Automatisierter Text    userId=1
    
    ${response}=      POST On Session    api_session    /posts    json=${payload}    headers=${headers}
    
    Status Should Be    201    ${response}
    ${json}=          Set Variable    ${response.json()}
    Should Be Equal As Strings    ${json['title']}    Robot Test
```

---

## ⚡ 3. Testausführung

```bash
# Tests ausführen und HTML-Berichte generieren
robot --outputdir results api_tests.robot
```

Nach der Ausführung stehen interaktive Testergebnisse unter `results/report.html` zur Verfügung.

---

## 🔗 Verwandte Themen
* [Robot Framework Anleitung](robot-framework-anleitung.md) – Grundlegende Einführung
* [Playwright Anleitung](playwright-anleitung.md) – Web UI Testing
* [Playwright & KI Web-Scraping](playwright-ki-extraction.md) – Scraping & Extraktion
