## WordPress-Themen in WordPress erstellen

Um ein neues Thema in Wordpress zu erstellen, müssen Sie die folgenden Schritte ausführen:

1. **Erstellen Sie ein neues Verzeichnis**: Zuerst müssen Sie ein neues Verzeichnis für Ihr Thema erstellen. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
cd /var/www/html/wp-content/themes
sudo mkdir ahrensburg 
```

2. **Erstellen Sie eine `style.css`-Datei**: Als nächstes müssen Sie eine `style.css`-Datei in Ihrem neuen Thema-Verzeichnis erstellen. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
cd ahrensburg
sudo nano style.css
```

Fügen Sie den folgenden Inhalt hinzu:

```css
/*
Theme Name: Ahrensburg
Author: Thorsten Klöhn
Description: Ein einfaches Wordpress-Thema
Version: 1.0
*/

```

3. **Erstellen Sie eine `index.php`-Datei**: Als nächstes müssen Sie eine `index.php`-Datei in Ihrem neuen Thema-Verzeichnis erstellen. Sie können dies tun, indem Sie das folgende Kommando ausführen:

```bash
sudo nano index.php
```

Fügen Sie den folgenden Inhalt hinzu:

```php
<?php
// Silence is golden.
```

4. **Aktivieren Sie das Thema**: Gehen Sie zu Ihrem Wordpress-Dashboard und navigieren Sie zu `Design` > `Themes`. Dort sollten Sie Ihr neues Thema sehen. Klicken Sie auf `Aktivieren`, um Ihr neues Thema zu aktivieren.

Nachdem Sie diese Schritte ausgeführt haben, haben Sie erfolgreich ein neues Thema in Wordpress erstellt und aktiviert.

## Fazit

Das Erstellen eines neuen Wordpress-Themas ist ein einfacher Prozess, der nur wenige Schritte erfordert. Indem Sie die oben genannten Schritte befolgen, können Sie Ihr eigenes benutzerdefiniertes Thema erstellen und es in Wordpress aktivieren. Viel Spaß beim Erstellen Ihres eigenen Themas!


### Wordpress eine Menü hinzufügen

Erstellen eine Datei `functions.php` im Verzeichnis des Themas und fügen Sie den folgenden Code hinzu:

```php
<?php

function register_my_menus() {
  register_nav_menus(
    array(
      'header-menu' => __( 'Header Menu' ),
      'extra-menu' => __( 'Extra Menu' )
     )
   );
 }
 add_action( 'init', 'register_my_menus' );

?>
```
Hinzufügen Sie den folgenden Code in die `index.php`-Datei:

```php
wp_nav_menu( array( 'theme_location' => 'header-menu' ) );
```

## Titel hinzufügen index.php

```php
<title> <?php the_title(); ?> </title>
```

## Inhalt hinzufügen index.php

```php
<?php the_content(); ?>
```






