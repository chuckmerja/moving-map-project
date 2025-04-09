
# Moving Map Logger

This is an offline moving map GPS logger designed to run on older laptops (Linux or Windows), with support for:

- Live GPS tracking from serial (or simulated GPS)
- Logging GPS positions as **points**, **lines**, or **polygons**
- Logging with metadata from application templates (e.g., chemical, rate, implement width)
- Live speed (MPH) and acres covered calculation
- Background map layers using SHP/KML/SID

---

## 📦 Directory Structure

```
moving-map-project/
├── gps_logger.py            # Main logger
├── template_gui.py          # GUI to select/edit templates
├── gps_simulator.py         # Sends fake NMEA GPS data for testing
├── launcher.py              # One-click launcher GUI
├── logs/                    # Saved logs (Shapefiles)
├── templates/               # Application templates (JSON)
├── background_layers/       # Background SHP/KML/SID layers
├── .gitignore               # Ignore logs, build files, etc.
└── README.md                # This file
```

---

## 🚀 How to Run

### Step 1: Select Template
```bash
python3 template_gui.py
```
Pick or create a new application template. This stores metadata like chemical name, rate, and implement width.

### Step 2: Start Logging
```bash
python3 gps_logger.py
```
Make sure your GPS device is connected (or use simulation).

### Step 3: Simulate GPS (Optional)
```bash
python3 gps_simulator.py
```
This sends fake GPS points over a virtual port (for testing).

---

## 🖥 Launcher GUI
You can also use the launcher:
```bash
python3 launcher.py
```
This lets you:
- Select logging mode (Point, Line, Polygon)
- Launch template selector
- Start GPS logger

---

## ⚙️ Requirements

- Python 3.7+
- PyQt5
- pyshp
- shapely
- pyproj
- matplotlib (for future live map view)

To install everything:
```bash
sudo apt update
sudo apt install python3-pyqt5 python3-pip
pip3 install pyshp shapely pyproj matplotlib
```

---

## 🧪 Template Format (JSON)

Example `templates/sprayer_field_1.json`:
```json
{
  "name": "sprayer_field_1",
  "chemical": "2,4-D",
  "rate": "1pt/acre",
  "implement_width_ft": "40"
}
```

---

## 💾 Output Files

Files are saved in the `logs/` folder as Shapefiles:
- `log_YYYYMMDD_HHMMSS_point.shp`
- `..._line.shp` or `..._polygon.shp`

Each logged feature includes metadata from the template.

---

## 📍 Background Map Layers

Drop your `.shp`, `.kml`, or `.sid` background layers into `background_layers/`. These will be used for display once the live map viewer is enabled.

---

## ✅ To Do (Upcoming Features)

- Live map view with matplotlib or folium
- Background layer display
- Template editor enhancements (dropdowns, units)
- SHP/KML export with styles

---

Built with ❤️ by ChatGPT + You
