## Wiedererstellen
```bash
sudo apt-get install gh
gh auth login
cd /home/thorsten
sudo gh repo clone thorstenkloehn/Download
sudo chmod 777 -R Download
cd /home/thorsten/Download
php /var/www/mediawiki/maintenance/run.php importDump.php < /home/thorsten/Download/pagedump.xml

```