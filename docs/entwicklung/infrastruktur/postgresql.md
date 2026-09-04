`postgresql-all` ist ein Metapaket, das alle verfügbaren PostgreSQL-Versionen und zugehörige Komponenten installiert. Es eignet sich, wenn Sie mehrere Versionen oder eine vollständige Entwicklungsumgebung benötigen. Für die meisten Anwendungsfälle reicht das Paket `postgresql`, das nur die aktuelle Standardversion installiert.
```
# Import the repository signing key:
sudo apt install curl ca-certificates
sudo install -d /usr/share/postgresql-common/pgdg
sudo curl -o /usr/share/postgresql-common/pgdg/apt.postgresql.org.asc --fail https://www.postgresql.org/media/keys/ACCC4CF8.asc

# Create the repository configuration file:
. /etc/os-release
sudo sh -c "echo 'deb [signed-by=/usr/share/postgresql-common/pgdg/apt.postgresql.org.asc] https://apt.postgresql.org/pub/repos/apt $VERSION_CODENAME-pgdg main' > /etc/apt/sources.list.d/pgdg.list"

# Update the package lists:
sudo apt update
sudo apt-get install postgresql-18
sudo -u postgres -i
createuser thorsten
createdb -E UTF8 -O thorsten thorsten
psql -c "\password thorsten"
psql -c "ALTER USER dein_benutzername CREATEDB;"
exit # Ausloggen

```