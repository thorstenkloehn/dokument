## Tools für Backup und Restore von MediaWiki
### Git installieren
```bash
sudo apt-get update 
sudo apt-get upgrade

sudo apt-get install git

git config --global user.email "you@example.com"
git config --global user.name "Your Name"
```

### GitHub CLI installieren
```bash
(type -p wget >/dev/null || (sudo apt update && sudo apt-get install wget -y)) \
&& sudo mkdir -p -m 755 /etc/apt/keyrings \
&& wget -qO- https://cli.github.com/packages/githubcli-archive-keyring.gpg | sudo tee /etc/apt/keyrings/githubcli-archive-keyring.gpg > /dev/null \
&& sudo chmod go+r /etc/apt/keyrings/githubcli-archive-keyring.gpg \
&& echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/githubcli-archive-keyring.gpg] https://cli.github.com/packages stable main" | sudo tee /etc/apt/sources.list.d/github-cli.list > /dev/null \
&& sudo apt update \
&& sudo apt install gh -y
```

### GitHub CLI anmelden
```bash
gh auth login

```

### Backup für MediaWiki erstellen
```bash
cd /home/thorsten
gh repo clone thorstenkloehn/Download
sudo chmod 777 -R Download
cd /home/thorsten/Download
sudo rm /home/thorsten/Download/pagedump.xml
php /home/thorsten/mediawiki/maintenance/dumpBackup.php --full > /home/thorsten/Download/pagedump.xml
git add .
git commit -m "Backup"
git push
```


