# moving_map.py
import matplotlib.pyplot as plt
import shapefile
import os
from matplotlib.animation import FuncAnimation
from matplotlib.patches import Rectangle
from pyproj import Transformer
from xml.etree import ElementTree as ET

# Constants
LOG_DIR = "logs/"
BACKGROUND_DIR = "background_layers/"
IMPLEMENT_WIDTH_METERS = 10  # Change to match your implement width

# Utility to load SHP files
def load_shp(file_path):
    points = []
    try:
        sf = shapefile.Reader(file_path)
        for shape_rec in sf.shapeRecords():
            points.extend(shape_rec.shape.points)
    except Exception as e:
        print(f"Error loading SHP: {e}")
    return points

# Utility to load KML files (Placemarks with coordinates)
def load_kml(file_path):
    points = []
    try:
        tree = ET.parse(file_path)
        root = tree.getroot()
        ns = {'kml': 'http://www.opengis.net/kml/2.2'}
        for placemark in root.findall(".//kml:Placemark", ns):
            coords = placemark.find(".//kml:coordinates", ns)
            if coords is not None:
                coord_text = coords.text.strip()
                coord_list = coord_text.split()
                for coord in coord_list:
                    lon, lat, *_ = map(float, coord.split(","))
                    points.append((lon, lat))
    except Exception as e:
        print(f"Error loading KML: {e}")
    return points

# Load all background layers (up to 3)
def load_background_layers():
    layers = []
    for file in os.listdir(BACKGROUND_DIR):
        if file.endswith(".shp"):
            layers.append(load_shp(os.path.join(BACKGROUND_DIR, file)))
        elif file.endswith(".kml"):
            layers.append(load_kml(os.path.join(BACKGROUND_DIR, file)))
        # Note: SID files require GDAL; can be added later
    return layers

# Load logged GPS data
def load_gps_logs():
    gps_points = []
    for file in os.listdir(LOG_DIR):
        if file.endswith(".shp"):
            gps_points.extend(load_shp(os.path.join(LOG_DIR, file)))
    return gps_points

# Convert meters to degrees (approximate for lat/lon)
def meters_to_degrees(meters):
    return meters / 111320.0  # Approximate conversion at equator

def update(frame, gps_points, scat, coverage_rects, ax):
    if frame >= len(gps_points):
        return scat,

    current = gps_points[frame]
    lon, lat = current

    # Update scatter points
    scat.set_offsets(gps_points[:frame + 1])

    # Draw coverage area rectangle
    width_deg = meters_to_degrees(IMPLEMENT_WIDTH_METERS)
    coverage = Rectangle(
        (lon - width_deg / 2, lat - width_deg / 2),
        width_deg, width_deg,
        color='green', alpha=0.3
    )
    ax.add_patch(coverage)
    coverage_rects.append(coverage)

    return scat,

def show_moving_map():
    fig, ax = plt.subplots()
    ax.set_title("Moving Map with Coverage and Background")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.grid(True)

    # Load GPS and background data
    background_layers = load_background_layers()
    gps_points = load_gps_logs()

    # Draw background layers
    for layer in background_layers:
        if layer:
            x, y = zip(*layer)
            ax.plot(x, y, color="gray", linewidth=1, alpha=0.5)

    # Initialize the GPS scatter and coverage display
    scat = ax.scatter([], [], color="blue", s=10, label="GPS Track")
    coverage_rects = []

    # Animate GPS points + coverage
    ani = FuncAnimation(
        fig, update,
        frames=len(gps_points),
        fargs=(gps_points, scat, coverage_rects, ax),
        interval=1000,
        repeat=False
    )

    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    show_moving_map()
