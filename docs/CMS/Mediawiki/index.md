## Postgres Datenbank erstellen
```bash
sudo -u postgres -i
createdb -E UTF8 -O thorsten mediawiki
psql -d mediawiki -c "GRANT ALL PRIVILEGES ON DATABASE mediawiki TO thorsten

exit
```
## PHP installieren
```bash
sudo apt install php-fpm php-pgsql php-xml php-curl php-gd php-mbstring php-xmlrpc php-xmlrpc php-zip php-intl -y
```



## Mediawiki installieren
```bash
cd /var/www
sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git mediawiki
sudo cd mediawiki
sudo git tag -l | sort -V
sudo git checkout 1.41.0
sudo git submodule update --init --recursive
sudo chown -R www-data:www-data /var/www/mediawiki
sudo chmod -R 755 /var/www/mediawiki

```
Hochladen der Konfiguration
```bash
sudo scp /home/thorsten/Downloads/LocalSettings.php thorsten@ahrensburg.city:/var/www/mediawiki/LocalSettings.php
```


## Lesbare URLs konfiguriern in mediawiki
```bash
sudo nano /var/www/mediawiki/LocalSettings.php
```




```php
$wgScriptPath = "";
$wgArticlePath = "/$1";
$wgUsePathInfo = true;

```
Erweiterung Registieren
```bash
sudo nano /var/www/mediawiki/LocalSettings.php
```

```

$wgScriptPath = "";
$wgArticlePath = "/$1";
$wgUsePathInfo = true;

wfLoadExtension( 'VisualEditor' );
# Cookie-Warnung aktivieren
wfLoadExtension( 'CookieWarning' );
wfLoadExtension( 'SyntaxHighlight_GeSHi' );
$wgCookieWarningEnabled=true;
$wgCookieWarningMoreUrl='';
$wgCookieWarningGeoIPServiceURL='';
$wgCookieWarningGeoIPLookup='none';
$wgCookieWarningForCountryCodes="EU";




define("NS_SCHWACHSTELLEN", 3006);
define("NS_SCHWACHSTELLEN_TALK", 3007);
$wgExtraNamespaces[NS_SCHWACHSTELLEN] = "Schwachstellen";
$wgExtraNamespaces[NS_SCHWACHSTELLEN_TALK] = "Schwachstellen Diskussion";
$wgNamespacesWithSubpages[NS_SCHWACHSTELLEN] = true;

// VisualEditor für Schwachstellen-Namensraum aktivieren
$wgVisualEditorAvailableNamespaces[NS_SCHWACHSTELLEN] = true;
$wgVisualEditorAvailableNamespaces[NS_SCHWACHSTELLEN_TALK] = true;
// Server-Namensraum
define("NS_SERVER", 3000);
define("NS_SERVER_TALK", 3001);
$wgExtraNamespaces[NS_SERVER] = "Server";
$wgExtraNamespaces[NS_SERVER_TALK] = "Server Diskussion";
$wgNamespacesWithSubpages[NS_SERVER] = true;

// Kurse-Namensraum
define("NS_KURSE", 3002);
define("NS_KURSE_TALK", 3003);
$wgExtraNamespaces[NS_KURSE] = "Kurse";
$wgExtraNamespaces[NS_KURSE_TALK] = "Kurse Diskussion";
$wgNamespacesWithSubpages[NS_KURSE] = true;


// AI-Namensraum
define("NS_AI", 3004);
define("NS_AI_TALK", 3005);
$wgExtraNamespaces[NS_AI] = "Ai";
$wgExtraNamespaces[NS_AI_TALK] = "Ai Diskussion";
$wgNamespacesWithSubpages[NS_AI] = true;

// VisualEditor für die neuen Namensräume aktivieren
$wgVisualEditorAvailableNamespaces[NS_SERVER] = true;
$wgVisualEditorAvailableNamespaces[NS_SERVER_TALK] = true;
$wgVisualEditorAvailableNamespaces[NS_KURSE] = true;
$wgVisualEditorAvailableNamespaces[NS_KURSE_TALK] = true;
$wgVisualEditorAvailableNamespaces[NS_AI] = true;
$wgVisualEditorAvailableNamespaces[NS_AI_TALK] = true;

define("NS_IDE", 3008);
define("NS_IDE_TALK", 3009);
$wgExtraNamespaces[NS_IDE] = "IDE";
$wgExtraNamespaces[NS_IDE_TALK] = "IDE Diskussion";
$wgNamespacesWithSubpages[NS_IDE] = true;
$wgVisualEditorAvailableNamespaces[NS_IDE] = true;
$wgVisualEditorAvailableNamespaces[NS_IDE_TALK] = true;
define("NS_BUILDER", 3010);
define("NS_BUILDER_TALK", 3011);

$wgExtraNamespaces[NS_BUILDER] = "Builder";
$wgExtraNamespaces[NS_BUILDER_TALK] = "Builder_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_BUILDER;
define("NS_BACKUP", 3012);
define("NS_BACKUP_TALK", 3013);

$wgExtraNamespaces[NS_BACKUP] = "Backup";
$wgExtraNamespaces[NS_BACKUP_TALK] = "Backup_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_BACKUP;

define("NS_Nachrichten", 3014);
define("NS_Nachrichten_TALK", 3015);
$wgExtraNamespaces[NS_Nachrichten] = "Nachrichten";
$wgExtraNamespaces[NS_Nachrichten_TALK] = "Nachrichten_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_Nachrichten;



php maintenance/rebuildLocalisationCache.php
php maintenance/update.php 
```


