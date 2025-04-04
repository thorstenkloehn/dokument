## Wiedererstellen
```bash
sudo apt-get install gh
gh login
cd /home/thorsten
sudo gh repo clone thorstenkloehn/Download
sudo chmod 777 -R Download
cd /home/thorsten/Download
php /home/www/mediawiki/maintenance/run.php importDump.php < /home/thorsten/Download/pagedump.xml

```