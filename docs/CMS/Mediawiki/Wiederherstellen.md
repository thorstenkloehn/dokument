```bash
# Repository klonen (ohne sudo, falls möglich)
git clone https://github.com/thorstenkloehn/Download.git ~/Download
cd ~/Download

```
sudo nano /var/www/mediawiki/LocalSettings.php
```
Geben Sie folgende Zeile am Ende der Datei ein, um den Import von Entitäten zu erlauben:

```php
$wgWBRepoSettings['allowEntityImport'] = true;
```


# MediaWiki-Dump importieren
```bash
php /var/www/mediawiki/maintenance/run.php importDump.php < pagedump.xml
php /var/www/mediawiki/maintenance/run.php rebuildrecentchanges.php
php /var/www/mediawiki/maintenance/run.php initSiteStats.php
```

