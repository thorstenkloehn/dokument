## Postgres Datenbank erstellen
```bash
sudo -u postgres -i
createdb -E UTF8 -O thorsten mediawiki
exit
```
## PHP installieren
```bash
sudo apt install php-fpm php-pgsql php-xml php-curl php-gd php-mbstring php-xmlrpc php-xmlrpc php-zip php-intl -y
```
## Composer installieren
```bash
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
php -r "if (hash_file('sha384', 'composer-setup.php') === 'dac665fdc30fdd8ec78b38b9800061b4150413ff2e3b6f88543c636f7cd84f6db9189d43a81e5503cda447da73c7e5b6') { echo 'Installer verified'; } else { echo 'Installer corrupt'; unlink('composer-setup.php'); } echo PHP_EOL;"
php composer-setup.php
php -r "unlink('composer-setup.php');"

sudo mv composer.phar /usr/local/bin/composer
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
## mediawiki extensions installieren
```bash
sudo nano /var/www/mediawiki/LocalSettings.php
```
```php
wfLoadExtension( 'CookieWarning' );
wfLoadExtension( 'SemanticMediaWiki' );
enableSemantics( 'ahrensburg.city' );
wfLoadExtension( 'Gadgets' );
$wgCookieWarningEnabled=true;
$wgCookieWarningMoreUrl='';
$wgCookieWarningGeoIPServiceURL='';
$wgCookieWarningGeoIPLookup='none';
$wgCookieWarningForCountryCodes="EU";
$wgGroupPermissions['user']['move'] = false;
wfLoadExtension( 'Maps' );
$egMapsDefaultService = 'leaflet';
```
## Semantik Web
```bash
cd /var/wiki/mediawiki
sudo COMPOSER=composer.local.json  composer require --no-update mediawiki/semantic-media-wiki
 sudo composer update --no-dev
 php maintenance/update.php
```

## Maps
```bash
cd /var/wiki/mediawiki
COMPOSER=composer.local.json composer require --no-update mediawiki/maps:~10.1
composer update mediawiki/maps --no-dev -o
```
## Git clone extensions
```bash
cd /var/wiki/mediawiki/extensions
git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/CookieWarning.git
```
## Weblinks
* [Git clone](https://www.mediawiki.org/wiki/Download_from_Git)