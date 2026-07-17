# Praxis-Guide: Robot Framework Custom Python Keywords

Erweitere das Robot Framework durch eigene, in Python geschriebene Keyword-Bibliotheken für benutzerdefinierte Validierungen, Datenbankabfragen oder API-Interaktionen.

---

## 🐍 1. Python Keyword-Klasse schreiben (`CustomLibrary.py`)

```python
from robot.api.deco import keyword
from robot.api import logger

class CustomLibrary:
    ROBOT_LIBRARY_SCOPE = 'GLOBAL'

    @keyword("Validate Token Expiry")
    def validate_token_expiry(self, token_age_seconds: int, max_allowed: int = 3600):
        """Prüft ob ein Authentifizierungs-Token abgelaufen ist"""
        logger.info(f"Prüfe Token-Alter: {token_age_seconds}s (Max: {max_allowed}s)")
        if int(token_age_seconds) > int(max_allowed):
            raise AssertionError(f"Token ist abgelaufen! Alter: {token_age_seconds}s > {max_allowed}s")
        return True
```

---

## 🤖 2. In Robot Framework einbinden (`test_suite.robot`)

```robot
*** Settings ***
Documentation     Suite mit eigener Python-Bibliothek
Library           CustomLibrary.py

*** Test Cases ***
Test Token Validation Success
    [Documentation]    Testet ein gültiges Token
    Validate Token Expiry    1800    3600

Test Token Validation Failure
    [Documentation]    Erwartet einen Fehler bei abgelaufenem Token
    Run Keyword And Expect Error    Token ist abgelaufen!*    Validate Token Expiry    4000    3600
```

---

## 🔗 Verwandte Themen
* [Robot Framework API-Testing](robot-framework-api-testing.md) – REST API Testing
* [Robot Framework Anleitung](robot-framework-anleitung.md) – Grundlegende Einführung
* [Playwright Anleitung](playwright-anleitung.md) – Web Testing
