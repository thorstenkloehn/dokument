# Praxis-Guide: Blender 3D Python Automatisierung

**Blender** verfügt über eine vollständige Python-API (`bpy`), mit der sich 3D-Modelle, Lichter, Kamerafahrten und Renderings headless auf der Kommandozeile generieren lassen.

---

## 🐍 1. Blender Python-Skript (`create_scene.py`)

```python
import bpy

# 1. Szene leeren
bpy.ops.wm.read_factory_settings(use_empty=True)

# 2. Würfel erstellen
bpy.ops.mesh.primitive_cube_add(size=2, location=(0, 0, 1))
cube = bpy.context.active_object
cube.name = "MeinWuerfel"

# 3. Material mit Farbe erstellen
material = bpy.data.materials.new(name="RotMaterial")
material.use_nodes = True
bsdf = material.node_tree.nodes.get("Principled BSDF")
bsdf.inputs['Base Color'].default_value = (0.8, 0.1, 0.1, 1.0) # Rot
cube.data.materials.append(material)

# 4. Lichtquelle hinzufügen
bpy.ops.object.light_add(type='POINT', location=(4, -4, 5))
light = bpy.context.active_object
light.data.energy = 1000

# 5. Kamera hinzufügen & ausrichten
bpy.ops.object.camera_add(location=(5, -5, 4), rotation=(1.1, 0, 0.8))
bpy.context.scene.camera = bpy.context.active_object

# 6. Bild rendern & speichern
bpy.context.scene.render.filepath = "rendered_cube.png"
bpy.ops.render.render(write_still=True)
print("✅ 3D-Bild erfolgreich gerendert: rendered_cube.png")
```

---

## ⚡ 2. Headless auf der Kommandozeile ausführen

```bash
blender -b -P create_scene.py
```

---

## 🔗 Verwandte Themen
* [Design nach KI](design-nach-ki.md) – KI im Designprozess
* [Manim Animation Engine](../video/manim-animation-guide.md) – Erklärvideos
* [ComfyUI & SD Automatisierung](comfyui-workflow-anleitung.md) – Bildsynthese
