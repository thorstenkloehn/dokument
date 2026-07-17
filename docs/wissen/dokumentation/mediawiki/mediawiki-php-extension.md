# Praxis-Guide: MediaWiki PHP Extension Entwicklung

Entwicklung eigener **MediaWiki Extensions** in PHP zur Registrierung benutzerdefinierter Parser-Tags (z. B. `<infobox>`) und Event-Hooks.

---

## 💻 1. Extension-Struktur (`extensions/MeinCustomTag/`)

Ordnerstruktur:
* `extensions/MeinCustomTag/extension.json`
* `extensions/MeinCustomTag/src/Hooks.php`

### `extension.json` (Manifest)
```json
{
    "name": "MeinCustomTag",
    "version": "1.0.0",
    "author": "Thorsten",
    "description": "Erweitert MediaWiki um das Tag <customtag>",
    "type": "other",
    "AutoloadNamespaces": {
        "MediaWiki\\Extension\\MeinCustomTag\\": "src/"
    },
    "Hooks": {
        "ParserFirstCallInit": "MediaWiki\\Extension\\MeinCustomTag\\Hooks::onParserFirstCallInit"
    },
    "manifest_version": 2
}
```

### `src/Hooks.php` (PHP Logik)
```php
<?php
namespace MediaWiki\Extension\MeinCustomTag;

use Parser;

class Hooks {
    public static function onParserFirstCallInit(Parser $parser) {
        $parser->setHook('customtag', [self::class, 'renderCustomTag']);
    }

    public static function renderCustomTag($input, array $args, Parser $parser, $frame) {
        $output = htmlspecialchars($input);
        return "<div class='my-custom-box'><strong>Hinweis:</strong> {$output}</div>";
    }
}
```

---

## ⚡ 2. Aktivieren in `LocalSettings.php`

```php
wfLoadExtension( 'MeinCustomTag' );
```

---

## 🔗 Verwandte Themen
* [MediaWiki Python Bot](mediawiki-python-bot.md) – Python Botting
* [MediaWiki Backup Skripte](mediawiki-backup-skripte.md) – Backup-Skripte
* [XWiki REST API & Python](../xwiki/xwiki-rest-api.md) – XWiki API
