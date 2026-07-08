## Datei herunterladen
```
Repository klonen (ohne sudo, falls möglich)
git clone https://github.com/thorstenkloehn/Download.git ~/Download
cd ~/Download
```

## MediaWiki-Dump auf MediaWiki-Instanzen importieren

```
php /var/www/mediawiki/maintenance/run.php importDump.php < pagedump.xml
php /var/www/mediawiki/maintenance/run.php rebuildrecentchanges.php
php /var/www/mediawiki/maintenance/run.php initSiteStats.php
php /var/www/mediawiki/maintenance/run.php importDump.php < docs.xml
php /var/www/mediawiki/maintenance/run.php rebuildrecentchanges.php
php /var/www/mediawiki/maintenance/run.php initSiteStats.php
```
## Namensräume in der LocalSettings.php auf https://ahrensburg.city anlegen

```
define("NS_Nachrichten", 3000);
define("NS_Nachrichten_TALK", 3001);

$wgExtraNamespaces[NS_Nachrichten] = "Nachrichten";
$wgExtraNamespaces[NS_Nachrichten_TALK] = "Nachrichten_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_Nachrichten;
define("NS_BLOG", 3002);
define("NS_BLOG_TALK", 3003);

$wgExtraNamespaces[NS_BLOG] = "Blog";
$wgExtraNamespaces[NS_BLOG_TALK] = "Blog_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_BLOG;
$wgVisualEditorAvailableNamespaces[NS_BLOG] = true;
```
## Namensräume in der LocalSettings.php auf https://docs.ahrensburg.city anlegen

```
$wgNamespacesWithSubpages[NS_MAIN] = true;
# End of automatically generated settings.
# Add more configuration options below.

define("NS_BLOG", 4000);
define("NS_BLOG_TALK", 4001);

$wgExtraNamespaces[NS_BLOG] = "Blog";
$wgExtraNamespaces[NS_BLOG_TALK] = "Blog_Diskussion";
$wgVisualEditorAvailableNamespaces[] = NS_BLOG;
$wgVisualEditorAvailableNamespaces[NS_BLOG] = true;

```






