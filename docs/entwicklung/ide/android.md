## Vorbereitung auf dem Redmi 9A

* Gehe in die Einstellungen > Über das Telefon.

* Tippe 7-mal auf die MIUI-Version, bis "Du bist jetzt Entwickler" erscheint.

* Gehe zu Zusätzliche Einstellungen > Entwickleroptionen.

* Aktiviere USB-Debugging und Wireless Debugging (Drahtloses Debugging).


## Verbindung unter Ubuntu herstellen

Öffne dein Terminal. Du nutzt das Tool adb (Android Debug Bridge). Falls noch nicht installiert:

```bash
sudo apt install adb
```

Klicke im Handy auf "Wireless Debugging" und dann auf "Gerät mit Kopplungscode koppeln".

Du siehst eine IP-Adresse, einen Port und einen Code.

Gib im Ubuntu-Terminal ein:

```bash
adb pair [DEINE_IP]:[PORT_ZUM_KOPPELN] [DER_CODE]
```

Danach verbindest du dich (mit dem Port, der auf der Hauptseite von Wireless Debugging steht):

```bash
adb connect [DEINE_IP]:[PORT]
```
