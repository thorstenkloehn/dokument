# XWiki über APT unter Debian und Ubuntu installieren

Mit den offiziellen DEB-Paketen lässt sich XWiki einschließlich Java-Laufzeit, Anwendungsserver und Datenbank installieren. Diese Anleitung führt durch eine stabile Standardinstallation auf einem Debian- oder Ubuntu-Server.

!!! note "Hinweis"
    Die verfügbaren Paketnamen und Java-Anforderungen hängen von der XWiki-Version und der verwendeten Distribution ab. Die Paketliste sollte deshalb vor der Installation immer mit `apt search xwiki` geprüft werden. Stand dieser Anleitung: August 2026.

## Voraussetzungen

- ein unterstütztes Debian- oder Ubuntu-System
- ein Benutzerkonto mit `sudo`-Rechten
- Internetzugang zum XWiki-Paketarchiv
- ausreichend Arbeitsspeicher für Java, XWiki und die Datenbank

!!! warning "Achtung"
    Vor einer Installation auf einem bereits genutzten Server sollten Datenbanken und Konfigurationsdateien gesichert werden. Außerdem darf nicht gleichzeitig eine andere Anwendung die vorgesehenen HTTP-Ports belegen.

## 1. XWiki-Paketquelle einrichten

Zuerst werden der Signaturschlüssel und die Paketquelle für stabile XWiki-Versionen eingetragen:

```bash
sudo wget https://maven.xwiki.org/xwiki-keyring.gpg \
  -O /usr/share/keyrings/xwiki-keyring.gpg

sudo wget https://maven.xwiki.org/stable/xwiki-stable.list \
  -O /etc/apt/sources.list.d/xwiki-stable.list

sudo apt update
```

Für produktive Systeme eignen sich in der Regel der Stable- oder der LTS-Zweig:

| Paketquelle | Zweck |
|---|---|
| `stable/xwiki-stable.list` | stabile Veröffentlichungen ohne Meilensteine und Release Candidates |
| `lts/xwiki-lts.list` | alle veröffentlichten Cycle-LTS-Versionen |
| `lts/xwiki-lts-latest.list` | jeweils neueste verfügbare LTS-Version |
| `releases/xwiki-releases.list` | alle Veröffentlichungen einschließlich Vorabversionen |

!!! tip "Tipp"
    Für einen Server mit möglichst seltenen Versionssprüngen ist die LTS-Paketquelle eine gute Wahl. Zum Wechseln muss im zweiten `wget`-Befehl lediglich die URL der gewünschten Paketquelle eingesetzt werden.

## 2. Verfügbare Pakete prüfen

```bash
apt search xwiki
```

Der Paketname kombiniert Anwendungsserver und Datenbank. Die Komplettpakete folgen normalerweise diesem Muster:

```text
xwiki-xjetty-mariadb
xwiki-xjetty-mysql
xwiki-xjetty-pgsql
xwiki-tomcat10-mariadb
xwiki-tomcat10-mysql
xwiki-tomcat10-pgsql
```

Neuere Distributionen können stattdessen Pakete für Tomcat 11 anbieten. Maßgeblich ist die Ausgabe von `apt search xwiki`.

### Anwendungsserver auswählen

| Variante | Geeignet für |
|---|---|
| **XJetty** | unkomplizierte Neuinstallation mit einem für XWiki vorbereiteten Jetty |
| **Tomcat** | Umgebungen, in denen Tomcat bereits administriert oder ausdrücklich vorausgesetzt wird |

### Datenbank auswählen

| Variante | Paketbestandteil |
|---|---|
| MariaDB | `mariadb` |
| MySQL | `mysql` |
| PostgreSQL | `pgsql` |

!!! warning "Achtung"
    Wird tatsächlich MariaDB eingesetzt, sollte auch das MariaDB-Paket gewählt werden. Das MySQL-Paket ist für einen echten MySQL-Server vorgesehen.

## 3. XWiki installieren

Für eine einfache Standardinstallation mit XJetty und MariaDB:

```bash
sudo apt install xwiki-xjetty-mariadb
```

Alternativ kann beispielsweise Tomcat mit PostgreSQL installiert werden:

```bash
sudo apt install xwiki-tomcat10-pgsql
```

APT installiert die benötigten Abhängigkeiten. Während der Einrichtung kann `dbconfig-common` nach der Datenbankkonfiguration und nach Kennwörtern fragen. Bei einer neuen Datenbankinstallation kann die automatische Konfiguration in der Regel übernommen werden.

!!! warning "Achtung"
    Datenbankkennwörter sicher aufbewahren. Bei älteren XWiki-Paketständen können Sonderzeichen im automatisch eingetragenen Datenbankkennwort Startprobleme verursachen. Tritt dieser Fehler auf, sollten die Zugangsdaten in `/etc/xwiki/hibernate.cfg.xml` geprüft werden.

Nach der Installation laufen die Dienste normalerweise bereits und werden beim Systemstart automatisch aktiviert. Der Status lässt sich abhängig von der gewählten Variante prüfen:

=== "XJetty"

    ```bash
    sudo systemctl status xwiki
    ```

=== "Tomcat 10"

    ```bash
    sudo systemctl status tomcat10
    ```

## 4. Ersteinrichtung im Browser

XWiki ist standardmäßig unter folgender URL erreichbar:

```text
http://SERVER-IP:8080/xwiki
```

Beim ersten Aufruf startet der **Distribution Wizard**. Er installiert die Standardoberfläche und führt durch das Anlegen des Administratorkontos. Eine frisch installierte Instanz enthält vorher noch keine regulären Wiki-Seiten oder Benutzerkonten.

!!! tip "Tipp"
    Ist die Seite nicht erreichbar, zuerst den Dienststatus und anschließend die Protokolle prüfen. Zusätzlich müssen eine lokale Firewall oder eine vorgeschaltete Cloud-Firewall den verwendeten Port zulassen.

## 5. Java und Arbeitsspeicher prüfen

Aktuelle XWiki-Versionen benötigen eine unterstützte Java-Version. XWiki 16 benötigt mindestens Java 17; ab XWiki 18 ist Java 21 erforderlich. Die tatsächlich verwendete Version zeigt:

```bash
java -version
```

Bei Tomcat befindet sich die distributionsabhängige Startkonfiguration üblicherweise in `/etc/default/tomcat10` beziehungsweise `/etc/default/tomcat11`. Zu niedrige Java-Speichergrenzen können dazu führen, dass XWiki nicht vollständig startet oder unter Last instabil wird.

Nach einer Änderung muss der betreffende Dienst neu gestartet werden:

=== "XJetty"

    ```bash
    sudo systemctl restart xwiki
    ```

=== "Tomcat 10"

    ```bash
    sudo systemctl restart tomcat10
    ```

## 6. XWiki aktualisieren

Vor einer Aktualisierung sollten mindestens die Datenbank, `/etc/xwiki/` und `/var/lib/xwiki/data/` gesichert werden.

```bash
sudo apt update
sudo apt upgrade
```

Soll ausschließlich das installierte XWiki-Metapaket aktualisiert werden, wird dessen genauer Name angegeben, zum Beispiel:

```bash
sudo apt install xwiki-xjetty-mariadb
```

Nach einem Versionswechsel wird XWiki im Browser geöffnet. Der Distribution Wizard aktualisiert anschließend die installierte Oberfläche und Erweiterungen.

!!! warning "Achtung"
    Bei einem Wechsel der unterstützten Tomcat-Hauptversion kann sich auch der XWiki-Paketname ändern. In diesem Fall zuerst die aktuellen Pakete mit `apt search xwiki` ermitteln und die offiziellen Upgrade-Hinweise für die Zielversion lesen.

## 7. Fehler untersuchen

### Dienstprotokolle anzeigen

=== "XJetty"

    ```bash
    sudo journalctl -u xwiki -n 200 --no-pager
    sudo journalctl -u xwiki -f
    ```

    Zusätzliche XWiki-Protokolle können unter `/var/log/xwiki/` liegen.

=== "Tomcat 10"

    ```bash
    sudo journalctl -u tomcat10 -n 200 --no-pager
    sudo journalctl -u tomcat10 -f
    ```

    Je nach Distribution befinden sich weitere Protokolle unter `/var/log/tomcat10/`.

### Portbelegung prüfen

```bash
sudo ss -ltnp
```

### Paketinstallation reparieren

```bash
sudo dpkg --configure -a
sudo apt --fix-broken install
```

## Wichtige Verzeichnisse

| Pfad | Inhalt |
|---|---|
| `/etc/xwiki/` | zentrale XWiki-Konfiguration |
| `/var/lib/xwiki/data/` | dauerhafte XWiki-Daten, unter anderem Dateianhänge |
| `/usr/lib/xwiki/` | installierte Webanwendung |
| `/var/log/xwiki/` | XJetty-/XWiki-Protokolle, sofern dateibasiertes Logging aktiv ist |
| `/var/log/tomcat10/` | Tomcat-Protokolle bei einer Tomcat-10-Installation |

## Weiterführende Seiten

- [XWiki installieren und über Nginx bereitstellen](installieren.md)
- [XWiki REST API und Python](xwiki-rest-api.md)
- [XWiki-Agenten-Pipeline](xwiki-ki-agent.md)
- [Offizielle XWiki-Anleitung zur Installation über APT](https://www.xwiki.org/xwiki/bin/view/Documentation/AdminGuide/Installation/InstallationViaAPT/)
