
## Backup erstellen

```bash
cd /home/thorsten
gh repo clone thorstenkloehn/Download
sudo chmod 777 -R Download
cd /home/thorsten/Download
sudo rm /home/thorsten/Download/pagedump.xml
sudo rm /home/thorsten/Download/doc.xml
ssh thorsten@ahrensburg.city "php /var/www/mediawiki/maintenance/dumpBackup.php --full" > /home/thorsten/Download/pagedump.xml
ssh thorsten@ahrensburg.city "php /var/www/docs/maintenance/dumpBackup.php --full" > /home/thorsten/Download/doc.xml
git add pagedump.xml
git add doc.xml
git commit -m "Backup"
git push
```


