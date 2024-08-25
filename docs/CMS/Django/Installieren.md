## Django Insstallieren Entwicklungsumgebung
### 
```bash
sudo apt install python3 python3-pip python3-venv python-is-python3
```
### Virtuelle Umgebung erstellen
```bash
cd $HOME
    mkdir meindjango
    cd meindjango
    python3 -m venv .venv
    source .venv/bin/activate
```
### Django CMS:

```bash

pip install django
pip install django-cms
python manage.py runserver
```