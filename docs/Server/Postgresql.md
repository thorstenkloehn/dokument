`postgresql-all` ist ein Metapaket, das alle verfügbaren PostgreSQL-Versionen und zugehörige Komponenten installiert. Es eignet sich, wenn Sie mehrere Versionen oder eine vollständige Entwicklungsumgebung benötigen. Für die meisten Anwendungsfälle reicht das Paket `postgresql`, das nur die aktuelle Standardversion installiert.
```
sudo apt-get install postgresql-all
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql -c "\password thorsten"
psql -c "ALTER USER dein_benutzername CREATEDB;"
exit # Ausloggen

```