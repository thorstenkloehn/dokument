## Postgres Datenbank erstellen
```bash
sudo -u postgres -i
createdb -E UTF8 -O thorsten django
exit

```
## Django Insstallieren Entwicklungsumgebung
### Virtuelle Umgebung erstellen
```bash
cd $HOME
   sudo mkdir Django
    sudo cd Django
    sudo python3.12 -m venv .venv
    sudo source .venv/bin/activate
```
### Django datei erstellen .env
```bash
sudo nano .env
```
### .env Text einfügen
```bash
SECRET_KEY=django-insecure
DATABASE_NAME=your_database_name
DATABASE_USER=your_database_user
DATABASE_PASSWORD=your_database_password
DATABASE_HOST=your_database_host
DATABASE_PORT=your_database_port
```
## setting.py bei Django
```python
# settings.py
import os
import environ

# Initialisieren Sie die Umgebung
env = environ.Env()

# BASE_DIR definieren
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# .env-Datei laden
environ.Env.read_env(os.path.join(BASE_DIR, '.env'))

# Geheimschlüssel
SECRET_KEY = env('SECRET_KEY')

# Datenbankkonfiguration
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': env('DATABASE_NAME'),
        'USER': env('DATABASE_USER'),
        'PASSWORD': env('DATABASE_PASSWORD'),
        'HOST': env('DATABASE_HOST'),
        'PORT': env('DATABASE_PORT'),
    }
}
```
## Django Superuser erstellen
```bash
python manage.py createsuperuser
```
