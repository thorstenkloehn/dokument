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



## Mediawiki installieren auf Entwicklungs Rechner
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





php maintenance/rebuildLocalisationCache.php
php maintenance/update.php 
```

## Auf den Server übertragen

```bash


# Oder nur bestimmte Dateien/Verzeichnisse synchronisieren
rsync -avz --delete \
  --exclude='LocalSettings.php' \
  --exclude='.git' \
  --exclude='cache/*' \
  --exclude='images/temp/*' \
  --exclude='images/thumb/*' \
  /var/www/mediawiki/ user@server:/var/www/mediawiki/
```

