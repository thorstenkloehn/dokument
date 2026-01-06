# Kurzform
```
cd /var/www
sudo git clone https://gerrit.wikimedia.org/r/mediawiki/core.git semanticmediawiki
cd semanticmediawiki
sudo git tag -l | sort -V
sudo git checkout 1.44.0
sudo git submodule update --init --recursive
composer install
composer require --no-update mediawiki/semantic-media-wiki
composer update
composer require --no-update mediawiki/maps:~12.0
composer update mediawiki/maps --no-dev
composer require --no-update mediawiki/cargo
composer update mediawiki/cargo --no-dev
composer require mediawiki/data-transfer
composer update
composer require mediawiki/page-forms
composer update
composer require mediawiki/semantic-result-formats
composer update
composer require mediawiki/semantic-compound-queries
composer update
composer require mediawiki/semantic-extra-special-properties
composer  update
composer require mediawiki/mermaid
composer  update

git clone https://gerrit.wikimedia.org/r/mediawiki/extensions/ExternalData /var/www/semanticmediawiki/extensions/ExternalData
cd /var/www/semanticmediawiki/extensions/ExternalData
composer install
npm install
mkdir /semanticmediawikidownload
cd /semanticmediawikidownload
wget https://extdist.wmflabs.org/dist/extensions/CookieWarning-REL1_44-00d6718.tar.gz
tar -xzf CookieWarning-REL1_44-00d6718.tar.gz -C /var/www/semanticmediawiki/extensions
sudo nano /etc/nginx/conf.d/semanticmediawiki.conf
```
Folgendes Eingeben Text
:

```
server {
    listen 443 ssl http2;
    listen [::]:443 ssl http2;
    server_name smw.ahrensburg.city;
    ssl_certificate /etc/letsencrypt/live/ahrensburg.city/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/ahrensburg.city/privkey.pem;
     root /var/www/mediawiki;
    index index.php index.html index.htm;
 
 location / {
        try_files $uri $uri/ /index.php?$args;
    }
    location ~ \.php$ {
        include snippets/fastcgi-php.conf;
        fastcgi_pass unix:/var/run/php/php8.3-fpm.sock;
    }

    location ~ /\.ht {

           deny all;
    }

}
```
Weiter geht es im Terminal

```
sudo -u postgres -i
createdb -E UTF8 -O thorsten smw
exit
```
* Jetzt den Browser starten

* Weiter geht es im Terminal
```
sudo scp /home/thorsten/Downloads/LocalSettings.php thorsten@ahrensburg.city:/var/www/semanticmediawiki/LocalSettings.php
```