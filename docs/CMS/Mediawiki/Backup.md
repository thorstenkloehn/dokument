
## Backup erstellen

```bash
cd /home/thorsten
gh repo clone thorstenkloehn/Download
sudo chmod 777 -R Download
cd /home/thorsten/Download
sudo rm /home/thorsten/Download/pagedump.xml
ssh root@ahrensburg.city "php /var/www/mediawiki/mediawiki/maintenance/dumpBackup.php --full" > /home/thorsten/Download/pagedump.xml
git add pagedump.xml
git commit -m "Backup"
git push
```


