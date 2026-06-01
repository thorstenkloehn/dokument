## Konzeption & Scripting (Zwei-Spalten-Skript)

 - ONLYOFFICE Writer: Klingt banal, ist aber mit einer sauberen, zweispaltigen Tabellenvorlage der stabilste Profi-Weg unter Ubuntu.
 
 - VS Code / VSCodium + Markdown-Table-Extensions: Ideal, wenn du Skripte und technische Notizen direkt am gleichen Ort verwalten willst wie deine Code-Beispiele.
 
 - Kit Scenarist: Falls du doch lieber mit virtuellen Karteikarten (Storyboards) arbeiten willst, um Szenen flexibel hin- und herzuschieben.
## OBS Studio

Installation unter Ubuntu/Debian:

```bash
sudo add-apt-repository ppa:obsproject/obs-studio
sudo apt update
sudo apt-get update && sudo apt-get install obs-studio
```
### Zusatz-Tools für Cursor- & Tastatur-Effekte (Wichtig!)

* Key-Mon / Screenkey: Blendet gedrückte Tastenkombinationen (z. B. Strg + C) als Overlay auf dem Bildschirm ein. Screenkey lässt sich hervorragend visuell anpassen.
* Gromit-MPX: Ermöglicht es, per Hotkey direkt auf dem Bildschirm zu zeichnen (Pfeile, Einkreisen), während die Aufnahme läuft.
* Cursor-Highlighting: Um den gelben Kreis um die Maus zu bekommen, nutzt man unter Ubuntu am besten eine GNOME-Shell-Extension (wie Fly-Pie oder spezielle Cursor-Themes) oder das Tool Vibe.

## Der Video-Editor
### Kdenlive (Die native Open-Source-Empfehlung)
* Multi-Spur-Schnitt: Importiere die OBS-Aufnahme. Wenn du getrennte Spuren genutzt hast, liegen Video, Facecam und Mikrofon direkt sauber untereinander.
* Animation & Zoom: Über den Effekt "Transformieren" lassen sich Keyframes setzen. Damit baut man das typische "Heranzoomen an ein Software-Detail" perfekt nach.
* Callouts & Text: Das integrierte Titel-Werkzeug (Titler) erlaubt das Erstellen von Textboxen, Pfeilen und Unschärfe-Masken (zum Verpixeln von Passwörtern).


## Motion Graphics & Erklärvideos (Die besten Allrounder)
* Enve (2D Vector Animation)
* Synfig Studio
* OpenToonz
* Manim (Community Edition)
## Der "Profis-Weg": Blender (Grease Pencil & Motion Graphics)
* Natron
* Blender 3d
## Whiteboard-Animationen (Hand-zeichnet-Stil)
* OpenBoard 
## Offices
* ONLYOFFICE

## Moderner "Docs-as-Code" & KI-Workflow

* Autocut / LosslessCut: Für den schnellen Rohschnitt. LosslessCut erlaubt das superschnelle, verlustfreie Schneiden direkt anhand der Keyframes ohne langes Rendern.
* Whisper (KI-Transkription): Wer Untertitel oder textbasierten Schnitt sucht, nutzt lokale Tools wie whisper.cpp oder Subtitle Composer mit integriertem Whisper-Modell. Damit lassen sich präzise deutsche Untertitel komplett offline generieren (optimal über die GPU).




