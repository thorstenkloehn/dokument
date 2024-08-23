## Wiedererstellen
```bash
cd /home/thorsten
sudo gh repo clone thorstenkloehn/Download
sudo chmod 777 -R Download
cd /home/thorsten/Download
php /home/thorsten/mediawiki/maintenance/importDump.php < /home/thorsten/Download/pagedump.xml

```