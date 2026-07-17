# Alternative Kachelserver für OpenStreetMap-Daten

Diese Seite bietet einen Überblick über verschiedene Kachelserver-Lösungen, die als Alternative oder Ergänzung zum klassischen mod_tile/renderd-Stack verwendet werden können. Jede Lösung hat spezifische Vor- und Nachteile in Bezug auf Performance, Skalierbarkeit und Einfachheit der Installation.

## Übersicht der Kachelserver-Alternativen

### 1. **TileServer-GL**

**Beschreibung:** Ein moderner, auf Node.js basierender Kachelserver, der Mapnik-Stile oder Mapbox GL Styles rendert. Ideal für Vektor- und Rasterkacheln.

**Vorteile:**
- Unterstützt sowohl Raster- als auch Vektorkacheln (MVT)
- Einfache Installation und Konfiguration
- Gute Integration mit PostGIS
- Unterstützt Mapbox GL Styles direkt

**Nachteile:**
- Erfordert Node.js
- Für sehr hohe Lasten möglicherweise weniger performant als mod_tile

**Installation auf Ubuntu:**

```bash
# Node.js installieren (empfohlen: Node 18+)
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# TileServer-GL installieren
sudo npm install -g tileserver-gl

# Configuration Datei erstellen
nano ~/tileserver-config.json
```

Beispiel-Konfiguration (`~/tileserver-config.json`):

```json
{
  "options": {
    "paths": {
      "root": "/var/www/tiles",
      "fonts": "/usr/share/fonts",
      "styles": "/usr/local/share/mapbox-gl-styles"
    }
  },
  "sources": {
    "osm": {
      "type": "postgis",
      "dbconn": "postgresql://renderaccount:password@localhost:5432/gis"
    }
  },
  "styles": {
    "osm-bright": {
      "style": "osm-bright.json",
      "serve": true
    }
  }
}
```

**Datenbank einrichten:**

```bash
# PostGIS-Datenbank für OSM-Daten vorbereiten
sudo -u postgres psql -d gis -c "CREATE EXTENSION IF NOT EXISTS postgis;"
sudo -u postgres psql -d gis -c "CREATE EXTENSION IF NOT EXISTS hstore;"

# OSM-Daten importieren mit osm2pgsql
osm2pgsql --create --database gis --user renderaccount \
  --style openstreetmap-carto.style \
  --host localhost \
  germany-latest.osm.pbf
```

**TileServer-GL starten:**

```bash
tileserver-gl ~/tileserver-config.json
```

Für Produktion als Systemd-Service einrichten:

```bash
sudo nano /etc/systemd/system/tileserver-gl.service
```

```ini
[Unit]
Description=TileServer-GL
After=network.target

[Service]
ExecStart=/usr/local/bin/tileserver-gl /home/renderaccount/tileserver-config.json
User=renderaccount
Restart=always

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable tileserver-gl
sudo systemctl start tileserver-gl
```

---

### 2. **renderd + mod_tile (klassische Lösung)**

**Beschreibung:** Der traditionelle OSM-Kachelserver-Stack, der auf den offiziellen OpenStreetMap-Servern verwendet wird.

**Vorteile:**
- Bewährte, stabile Lösung
- Optimiert für hohe Last
- Gute Dokumentation verfügbar
- Unterstützt verschiedene Rendering-Backends

**Nachteile:**
- Komplexere Installation
- Erfordert Apache-Webserver
- Weniger flexibel für moderne Stile

 Siehe die bestehenden Anleitungen:
- [Ubuntu 20.04](Server204.md)
- [Ubuntu 22.04](Server224.md)
- [Ubuntu 24.04](Server244.md)

---

### 3. **MapProxy**

**Beschreibung:** Ein Open-Source-Proxy für Geodaten, der Kacheln zwischenspeichern und transformieren kann.

**Vorteile:**
- Sehr flexibel (unterstützt verschiedene Quellen)
- Gute Caching-Funktionen
- Kann als Gateway zu anderen Kachelservern dienen
- Unterstützt WMS, TMS, WMTS

**Nachteile:**
- Kein direktes Rendern von OSM-Daten
- Benötigt eine separate Rendering-Lösung

**Installation auf Ubuntu:**

```bash
# Python und pip installieren
sudo apt install -y python3 python3-pip python3-venv

# Virtuelle Umgebung erstellen
python3 -m venv ~/mapproxy-venv
source ~/mapproxy-venv/bin/activate
pip install MapProxy

# Konfiguration erstellen
mkdir ~/mapproxy-config
nano ~/mapproxy-config/mapproxy.yaml
```

Beispiel-Konfiguration für OSM-ähnliche Daten:

```yaml
services:
  demo:
  tms:
    use_grid_names: true
    # origin: 'nw'
  kmldemo:
    use_grid_names: true
  wmts:
  wms:
    srs: ['EPSG:4326', 'EPSG:3857']
    image_formats: ['image/png', 'image/jpeg']
    versions: ['1.1.1', '1.3.0']

layers:
  - name: osm_cache
    title: OSM Cache Layer
    sources: [osm_cache_source]

sources:
  osm_cache_source:
    type: tile
    url: http://localhost/osm_tiles/%(z)s/%(x)s/%(y)s.png
    transparent: true

caches:
  osm_cache:
    grids: [GLOBAL_MERCATOR]
    sources: [osm_cache_source]
    cache:
      type: filesystem
      directory: /var/cache/mapproxy/osm
      directory_layout: tc
      base_url: http://yourserver/tms
```

**MapProxy starten:**

```bash
# Testen
mapproxy-util serve-devel ~/mapproxy-config/mapproxy.yaml

# Für Produktion
mapproxy-util create -f ~/mapproxy-config/mapproxy.yaml ~/mapproxy-config/mapproxy.wsgi
```

---

### 4. **OSRM (Open Source Routing Machine)**

**Beschreibung:** Ein hochperformanter Routing-Engine, der auch Kacheln für Visualisierungen bereitstellen kann.

**Vorteile:**
- Sehr schnell
- Spezialisiert auf Routing und Navigation
- Kann auch für Kachelgenerierung verwendet werden

**Nachteile:**
- Kein direktes Kartendarstellung-Rendering
- Komplexere Einrichtung

**Installation auf Ubuntu:**

```bash
# Abhängigkeiten installieren
sudo apt install -y build-essential cmake pkg-config git \
  libbz2-dev libstxxl-dev libstxxl1v5 libxml2-dev libzip-dev \
  libboost-all-dev lua5.2 liblua5.2-dev libtbb-dev

# OSRM klonen und kompilieren
git clone https://github.com/Project-OSRM/osrm-backend.git
cd osrm-backend
mkdir build && cd build
cmake ..
make
sudo make install

# Daten herunterladen und verarbeiten
wget https://download.geofabrik.de/europe/germany-latest.osm.pbf
osrm-extract germany-latest.osm.pbf -p profiles/car.lua
osrm-partition germany-latest.osm.pbf
osrm-customize germany-latest.osm.pbf

# Server starten
osrm-routed germany-latest.osrm &
```

---

### 5. **Mapnik + Python (custom rendering)**

**Beschreibung:** Direkte Nutzung von Mapnik über Python-Skripte für maximale Flexibilität.

**Vorteile:**
- Volle Kontrolle über das Rendering
- Kann an spezifische Anforderungen angepasst werden
- Gute für Prototyping

**Nachteile:**
- Kein integriertes Caching
- Erfordert mehr manuellen Code
- Weniger performant für hohe Last

**Installation auf Ubuntu:**

```bash
# Python und Mapnik installieren
sudo apt install -y python3 python3-pip python3-dev
pip install mapnik

# PostgreSQL-Adapter
pip install psycopg2-binary

# Beispiel-Skript für Kachelgenerierung
nano ~/render_tile.py
```

```python
#!/usr/bin/env python3
import mapnik
import psycopg2
import sys

# Datenbankverbindung
db_conn = psycopg2.connect("dbname=gis user=renderaccount host=localhost")

# Mapnik-Stil laden
m = mapnik.Map(256, 256, '+proj=merc +a=6378137 +b=6378137 +lat_ts=0.0 +lon_0=0.0 +x_0=0.0 +y_0=0 +k=1.0 +units=m +nadgrids=@null +wktext +no_defs')
mapnik.load_map(m, 'osm-bright.xml')

# PostGIS als Datenquelle
layer = mapnik.Layer('osm')
layer.datasource = mapnik.PostGIS(
    dbname='gis',
    user='renderaccount',
    password='yourpassword',
    host='localhost',
    table='planet_osm_polygon'
)
layer.styles.append('osm-polygon')
m.layers.append(layer)

# Kachel rendern
def render_tile(z, x, y):
    # Mercator-Koordinaten berechnen
    # ... (Koordinatentransformation hier)
    
    m.zoom_to_box(minx, miny, maxx, maxy)
    img = mapnik.Image(256, 256)
    mapnik.render(m, img)
    img.save('tile_{}_{}_{}.png'.format(z, x, y))

if __name__ == '__main__':
    render_tile(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
```

---

### 6. **TileMill (historisch, aber immer noch relevant)**

**Beschreibung:** Ein Desktop-Tool von Mapbox zur Erstellung von Kartendesigns, das auch als Server betrieben werden kann.

**Vorteile:**
- Benutzerfreundliche GUI
- Gute für Kartendesign
- Kann Designs exportieren

**Nachteile:**
- Nicht mehr aktiv entwickelt
- Erfordert manuelle Einrichtung

**Installation:**
TileMill ist nicht mehr als Open-Source verfügbar, aber die Designs können mit anderen Tools verwendet werden.

---

## Vergleich der Kachelserver-Lösungen

| Lösung | Typ | Performance | Komplexität | PostGIS-Integration | Vektorkacheln |
|--------|-----|-------------|-------------|---------------------|---------------|
| mod_tile/renderd | Raster | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ |
| TileServer-GL | Raster/Vektor | ⭐⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ |
| MapProxy | Proxy/Cache | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ❌ |
| OSRM | Routing | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐ | ❌ |
| Mapnik+Python | Raster | ⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ |

---

## OpenStreetMap-Daten in PostGIS importieren

Unabhängig von der gewählten Kachelserver-Lösung ist der Import von OSM-Daten in PostGIS ein wichtiger Schritt. Hier ist der allgemeine Prozess:

### 1. Datenbank vorbereiten

```bash
# PostgreSQL mit PostGIS installieren
sudo apt install -y postgresql postgresql-contrib postgis postgresql-16-postgis-3

# Datenbank und Benutzer erstellen
sudo -u postgres createuser renderaccount
sudo -u postgres createdb -O renderaccount gis
sudo -u postgres psql -d gis -c "CREATE EXTENSION postgis;"
sudo -u postgres psql -d gis -c "CREATE EXTENSION hstore;"
sudo -u postgres psql -d gis -c "ALTER TABLE geometry_columns OWNER TO renderaccount;"
sudo -u postgres psql -d gis -c "ALTER TABLE spatial_ref_sys OWNER TO renderaccount;"
```

### 2. OSM-Daten herunterladen

```bash
# Deutschland herunterladen
wget https://download.geofabrik.de/europe/germany-latest.osm.pbf

# Oder spezifische Region (z.B. Schleswig-Holstein)
wget https://download.geofabrik.de/europe/germany/schleswig-holstein-latest.osm.pbf

# Oder Ausschnitt mit osmosis erstellen
osmosis --read-pbf file=germany-latest.osm.pbf \
  --bounding-box left=10.1141 right=10.3716 top=53.7136 bottom=53.6249 \
  --write-pbf file=ahrensburg.pbf
```

### 3. Daten importieren mit osm2pgsql

```bash
# Grundinstallation
sudo apt install -y osm2pgsql

# Import mit Standard-Stil
osm2pgsql --create \
  --database gis \
  --user renderaccount \
  --host localhost \
  --style openstreetmap-carto.style \
  --tag-transform-script openstreetmap-carto.lua \
  --hstore \
  --latlon \
  --projection 3857 \
  --number-processes 4 \
  --cache 2000 \
  germany-latest.osm.pbf

# Für Updates (ohne --create)
osm2pgsql --append \
  --database gis \
  --user renderaccount \
  --host localhost \
  --style openstreetmap-carto.style \
  --tag-transform-script openstreetmap-carto.lua \
  germany-latest.osm.pbf
```

### 4. Indizes erstellen (für Performance)

```bash
# Verbinden mit der Datenbank
psql -U renderaccount -d gis

# Indizes für häufig abgefragte Spalten
CREATE INDEX idx_planet_osm_point_geom ON planet_osm_point USING GIST(way);
CREATE INDEX idx_planet_osm_line_geom ON planet_osm_line USING GIST(way);
CREATE INDEX idx_planet_osm_polygon_geom ON planet_osm_polygon USING GIST(way);
CREATE INDEX idx_planet_osm_roads_geom ON planet_osm_roads USING GIST(way);

-- Für bessere Abfrageperformance
CREATE INDEX idx_planet_osm_roads_type ON planet_osm_roads(highway);
CREATE INDEX idx_planet_osm_roads_name ON planet_osm_roads(name);
```

### 5. OpenStreetMap Carto-Stil einrichten

```bash
# CartoCSS-Stil klonen
git clone https://github.com/gravitystorm/openstreetmap-carto.git
cd openstreetmap-carto

# Abhängigkeiten installieren
sudo apt install -y nodejs npm
sudo npm install -g carto

# Stil anpassen (optional)
nano project.mml

# Stil kompilieren
carto project.mml > mapnik.xml

# Shapefiles für niedrige Zoomstufen herunterladen
scripts/get-external-data.py

# Schriftarten herunterladen
scripts/get-fonts.sh
```

---

## Empfehlungen

### Für Anfänger:
- **TileServer-GL** - Einfachste Installation, moderne Features

### Für Produktion mit hoher Last:
- **mod_tile/renderd** - Bewährte Lösung, beste Performance

### Für Vektorkacheln:
- **TileServer-GL** - Native MVT-Unterstützung

### Für Routing:
- **OSRM** - Spezialisiert auf Routing-Anfragen

### Für Caching/Proxy:
- **MapProxy** - Flexibles Caching für bestehende Kachelserver

---

## Nützliche Ressourcen

- [OpenStreetMap Wiki - Tile Servers](https://wiki.openstreetmap.org/wiki/Tile_servers)
- [TileServer-GL Dokumentation](https://tileserver.org/)
- [MapProxy Dokumentation](https://mapproxy.org/)
- [OSRM Dokumentation](http://project-osrm.org/)
- [osm2pgsql Dokumentation](https://osm2pgsql.org/)
- [OpenStreetMap Carto](https://github.com/gravitystorm/openstreetmap-carto)

---

## Fehlerbehebung

### Häufige Probleme:

1. **PostGIS-Erweiterung fehlt**
   ```bash
   sudo -u postgres psql -d gis -c "CREATE EXTENSION postgis;"
   ```

2. **Berechtigungsprobleme**
   ```bash
   sudo -u postgres psql -c "ALTER USER renderaccount WITH SUPERUSER;"
   ```

3. **Mapnik findet Schriftarten nicht**
   ```bash
   sudo fc-cache -fv
   ```

4. **osm2pgsql Import scheitert**
   - Prüfen Sie die Datenbankgröße: `df -h`
   - Erhöhen Sie den Shared Memory: `sudo sysctl -w kernel.shmmni=4096`

5. **Renderd startet nicht**
   - Prüfen Sie die Logs: `journalctl -u renderd -f`
   - Prüfen Sie die Konfiguration: `/usr/local/etc/renderd.conf`

6. **Apache-Proxy-Einstellungen**
   - Aktivieren Sie erforderliche Module: `sudo a2enmod proxy proxy_http`
   - Starten Sie Apache neu: `sudo systemctl restart apache2`
