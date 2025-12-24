```bash
# Repository klonen (ohne sudo, falls möglich)
git clone https://github.com/thorstenkloehn/Download.git ~/Download
cd ~/Download

# MediaWiki-Dump importieren
php /var/www/mediawiki/maintenance/run.php importDump.php < pagedump.xml
```