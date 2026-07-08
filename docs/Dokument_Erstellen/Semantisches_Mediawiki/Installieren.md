## Semantic MediaWiki mit Composer installieren

### Voraussetzungen

- Eine funktionierende MediaWiki-Installation
- Composer ist installiert
- Zugriff auf die Kommandozeile des Servers

### Schritt 1: Semantic MediaWiki mit Composer hinzufügen

Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:

```bash
composer require --no-update mediawiki/semantic-media-wiki
```

Danach installiere die Abhängigkeiten mit:

```bash
composer update
```

### Schritt 2: Extension in MediaWiki aktivieren

Öffne die Datei `LocalSettings.php` im Hauptverzeichnis deiner MediaWiki-Installation und füge folgende Zeilen hinzu:

```php
wfLoadExtension( 'SemanticMediaWiki' );
enableSemantics( 'localhost' ); # Ersetze localhost durch deine Domain
```

### Schritt 3: Datenbank aktualisieren

Führe das MediaWiki-Wartungsskript aus, um die Datenbank zu aktualisieren:

```bash
php maintenance/update.php
```

### Schritt 4: Überprüfung

- Rufe deine Wiki-Seite im Browser auf.
- Gehe zu „Spezial:Version“ und prüfe, ob „Semantic MediaWiki“ in der Liste der installierten Erweiterungen erscheint.

### Hinweise

- Passe die Domain in `enableSemantics()` an deine eigene Domain an.
- Weitere Konfigurationsmöglichkeiten findest du in der offiziellen Dokumentation:  
    https://www.semantic-mediawiki.org/wiki/Help:Installation/de

---

## Maps

Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:

```bash
composer require --no-update mediawiki/maps:~12.0
composer update mediawiki/maps --no-dev
```

Öffne die Datei `LocalSettings.php` im Hauptverzeichnis deiner MediaWiki-Installation und füge folgende Zeilen hinzu:

```php
wfLoadExtension( 'Maps' );
$egMapsDefaultService = 'leaflet';
```

Führe das MediaWiki-Wartungsskript aus, um die Datenbank zu aktualisieren:

```bash
php maintenance/update.php
```

## Cargo mit Composer installieren

### Voraussetzungen

- MediaWiki ist installiert und funktionsfähig
- Composer ist installiert
- Zugriff auf die Kommandozeile des Servers

### Schritt 1: Cargo mit Composer hinzufügen

Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:

```bash
composer require --no-update mediawiki/cargo
composer update mediawiki/cargo --no-dev
```

### Schritt 2: Extension in MediaWiki aktivieren

Öffne die Datei `LocalSettings.php` und füge folgende Zeile hinzu:

```php
wfLoadExtension( 'Cargo' );
```

### Schritt 3: Datenbanktabellen anlegen

Führe das MediaWiki-Wartungsskript aus, um die Cargo-Datenbanktabellen zu erstellen:

```bash
php maintenance/update.php
```

### Schritt 4: Überprüfung

- Rufe deine Wiki-Seite im Browser auf.
- Gehe zu „Spezial:Version“ und prüfe, ob „Cargo“ in der Liste der installierten Erweiterungen erscheint.

### Hinweise

- Weitere Informationen und Konfigurationsmöglichkeiten findest du in der offiziellen Dokumentation:  
    https://www.mediawiki.org/wiki/Extension:Cargo/de

---

## External Data

Führe im gewünschten Verzeichnis folgenden Befehl aus:

```bash
git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/ExternalData /var/www/mediawiki/extensions/ExternalData
cd /var/www/mediawiki/extensions/ExternalData
composer install
npm install
```

Öffne die Datei `LocalSettings.php` und füge folgende Zeile hinzu:

```php
wfLoadExtension( 'ExternalData' );
```

Führe das MediaWiki-Wartungsskript aus:

```bash
php maintenance/update.php
```

---

## Data Transfer

Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:

```bash
composer require mediawiki/data-transfer
composer update
```

Öffne die Datei `LocalSettings.php` und füge folgende Zeile hinzu:

```php
wfLoadExtension( 'DataTransfer' );
```

---

## Page Forms

Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:

```bash
composer require mediawiki/page-forms
composer update
```

Öffne die Datei `LocalSettings.php` und füge folgende Zeile hinzu:

```php
wfLoadExtension( 'PageForms' );
```

---

## Semantic Result Formats

Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:

```bash
composer require mediawiki/semantic-result-formats
composer update
```
Öffne die Datei `LocalSettings.php` und füge folgende Zeile hinzu:
```
wfLoadExtension( 'SemanticResultFormats' );
```
## Semantic Compound Queries

Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:
```
composer require mediawiki/semantic-compound-queries
composer update
```
Öffne die Datei `LocalSettings.php` und füge folgende Zeile hinzu:
```
wfLoadExtension( 'SemanticCompoundQueries' );
```

## Semantic Extra Special Properties 
Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:
```
composer require mediawiki/semantic-extra-special-properties
composer composer update
```
 Öffne die Datei `LocalSettings.php` und füge folgende Zeile hinzu:
 ```
 wfLoadExtension( 'SemanticExtraSpecialProperties' );
 ```

## Mermaid

Führe im Hauptverzeichnis deiner MediaWiki-Installation folgenden Befehl aus:
```
composer require mediawiki/mermaid
composer composer update
```
Öffne die Datei `LocalSettings.php` und füge folgende Zeile hinzu:
```
wfLoadExtension( 'Mermaid' );  
$mermaidgDefaultTheme = 'neutral';
```









