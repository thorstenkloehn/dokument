# XWiki: "Administration application is not installed" beheben

Nach einer frischen APT-/Debian-Paketinstallation zeigt XWiki auf der Import-Seite (`/xwiki/bin/import/XWiki/XWikiPreferences`) manchmal die Warnung *"The administration application is not installed"* — die Administrationsoberfläche fehlt komplett, es bleibt nur eine leere Import-Seite ohne Skin. Diese Seite erklärt die Ursache und zwei Lösungswege.

---

## Ursache

Administration und Extension Manager sind bei XWiki keine fest eingebauten Kernfunktionen, sondern eigene Erweiterungen (XARs), die laut [offizieller Dokumentation](https://extensions.xwiki.org/xwiki/bin/view/Extension/Administration%20Application) mit **„XWiki Standard"** gebündelt sind:

| Erweiterung | Extension-ID | Gebündelt mit |
|---|---|---|
| Administration Application | `org.xwiki.platform:xwiki-platform-administration-ui` | XWiki Standard |
| Extension Manager Application | `org.xwiki.platform:xwiki-platform-extension-ui` | XWiki Standard |

Ein reines `xwiki-tomcat10-pgsql`/`xwiki-xjetty-mariadb`-Paket (siehe [Installation über APT](installation-ueber-apt.md)) installiert zunächst nur die nackte Plattform. Erst der **Distribution Wizard** installiert beim ersten Aufruf das „Standard Flavor" mit allen Kernanwendungen. Läuft dieser Schritt nicht durch — z. B. weil beim ersten Start keine Internetverbindung zum Extension-Repository bestand, der Wizard abgebrochen wurde oder ein minimales Paket ohne Flavor genutzt wurde — bleibt die Instanz ohne Administration und ohne Extension Manager zurück. Die im Warnbanner selbst verlinkte Anleitung stammt noch aus XWiki Enterprise 1.5 und ist längst veraltet; die Import-Seite dahinter funktioniert aber weiterhin, weil sie zum XWiki-Kern gehört.

!!! note "Hinweis: Woran man das Problem erkennt"
    Fehlt nach der Ersteinrichtung das komplette Administrationsmenü und lässt sich `/xwiki/bin/admin/XWiki/XWikiPreferences` nicht normal öffnen, ist meist auch der Extension Manager selbst betroffen — denn auch er ist nur Teil von „XWiki Standard", nicht des Kerns.

---

## Weg 1: Fehlende XARs manuell importieren (funktioniert immer)

Da die Import-Seite selbst zum Kern gehört, lässt sie sich auch ohne Administration-App nutzen — genau der Screen aus der Warnmeldung. Laut den [offiziellen Installationshinweisen](https://extensions.xwiki.org/xwiki/bin/view/Extension/Extension%20Manager%20Application) ist das der vorgesehene manuelle Fallback, wenn eine Erweiterung nicht über den (noch fehlenden) Extension Manager installiert werden kann.

1. **Exakte XWiki-Version ermitteln** — steht im Seitenfuß der Instanz (z. B. „XWiki Debian 18.6.0").
2. **Extension Manager Application zuerst** als XAR in exakt passender Version herunterladen: `https://extensions.xwiki.org/xwiki/bin/download/Extension/Extension Manager Application/xwiki-platform-extension-ui-<VERSION>.xar` (Download-Link auf der [Extensionseite](https://extensions.xwiki.org/xwiki/bin/view/Extension/Extension%20Manager%20Application)).
3. Auf `https://DEINE-INSTANZ/xwiki/bin/import/XWiki/XWikiPreferences` unter **„Upload a new package"** die heruntergeladene `.xar`-Datei auswählen — sie erscheint danach unter **„Available packages"**.
4. Auf das Paket klicken und dem Import-Assistenten folgen (alle Seiten importieren).
5. Danach ist der Extension Manager erreichbar. Darüber lässt sich die **Administration Application** (und bei Bedarf gleich das komplette **„XWiki Standard"-Flavor**) bequem über die Suche installieren, statt jede Abhängigkeit einzeln als XAR herunterzuladen.

!!! warning "Achtung bei bereits genutzten Instanzen"
    Auf einer bereits mit Inhalten befüllten Wiki-Instanz warnt die offizielle Dokumentation ausdrücklich: Ein Import überschreibt u. a. `XWiki.XWikiPreferences` (wiki-weite Konfiguration), `XWiki.XWikiAllGroup`/`XWiki.AdminGroup` (Gruppenmitgliedschaften) und `XWiki.RegistrationConfig`. Bei einer frischen, noch leeren Installation ist das unkritisch — bei einer bereits konfigurierten Wiki vorher unbedingt sichern und Seiten beim Import selektiv auswählen.

!!! tip "Tipp: Direkter Zugriff ohne Administration Application"
    Manche Admin-Unterseiten sind auch ohne installierte Administration Application per URL-Parameter erreichbar, z. B. die Extension-History unter `?xpage=view&viewer=extensionHistory`. Praktisch für gezielte Zwischenschritte, bevor die volle Admin-Oberfläche wiederhergestellt ist.

---

## Weg 2: Distribution Wizard erneut anstoßen (sauberer, aber nicht immer möglich)

Der eigentlich vorgesehene Weg ist der **Distribution Wizard**, der beim ersten Login mit Administratorrechten automatisch startet und das komplette Standard-Flavor samt allen Abhängigkeiten in einem konsistenten Schritt installiert (inklusive automatischem Merge bei Konflikten). Ist der Wizard beim ersten Start fehlgeschlagen oder abgebrochen, hilft oft ein erneuter Login mit einem Administratorkonto oder ein Neustart des Anwendungsservers (`tomcat10`/`xwiki`, siehe [Installation über APT](installation-ueber-apt.md#7-fehler-untersuchen)) — danach prüft XWiki erneut, ob ein Flavor-Update ansteht.

Bleibt der Wizard weiterhin leer (kein Flavor zur Auswahl), fehlt meist die Internetverbindung zum Extension-Repository zum Zeitpunkt des Aufrufs — dann bleibt nur Weg 1 als Fallback.

---

## Verwandte Themen

- [XWiki installieren und über Nginx bereitstellen](installieren.md)
- [Installation über APT](installation-ueber-apt.md)
- [XWiki REST API und Python](xwiki-rest-api.md)
- [XWiki-Agenten-Pipeline](xwiki-ki-agent.md)
- [Administration Application (offizielle Doku)](https://extensions.xwiki.org/xwiki/bin/view/Extension/Administration%20Application)
- [Extension Manager Application (offizielle Doku)](https://extensions.xwiki.org/xwiki/bin/view/Extension/Extension%20Manager%20Application)
