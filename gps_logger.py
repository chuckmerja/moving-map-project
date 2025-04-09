
# gps_logger.py
import time
import serial
import json
import shapefile
from PyQt5.QtWidgets import QApplication, QComboBox, QPushButton, QLabel, QVBoxLayout, QWidget
from datetime import datetime

# Simulate a GPS logger
class GPSLogger(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GPS Logger")
        
        # Layout
        self.layout = QVBoxLayout()
        
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(["Point", "Line", "Polygon"])
        self.layout.addWidget(QLabel("Select Logging Mode:"))
        self.layout.addWidget(self.mode_combo)
        
        self.start_btn = QPushButton("Start Logging")
        self.layout.addWidget(self.start_btn)
        
        self.setLayout(self.layout)

    def start_logging(self):
        logging_mode = self.mode_combo.currentText()
        print(f"Starting {logging_mode} logging...")
        
        # Simulate logging process (replace with actual GPS logic)
        if logging_mode == "Point":
            self.log_point()
        elif logging_mode == "Line":
            self.log_line()
        elif logging_mode == "Polygon":
            self.log_polygon()

    def log_point(self):
        print("Logging a point...")
        # Simulated GPS point data
        gps_data = {"latitude": 51.5074, "longitude": -0.1278}
        self.save_to_shapefile(gps_data, "point")

    def log_line(self):
        print("Logging a line...")
        # Simulated GPS line data (two points)
        gps_data = [{"latitude": 51.5074, "longitude": -0.1278},
                    {"latitude": 51.5079, "longitude": -0.1280}]
        self.save_to_shapefile(gps_data, "line")

    def log_polygon(self):
        print("Logging a polygon...")
        # Simulated GPS polygon data (multiple points)
        gps_data = [{"latitude": 51.5074, "longitude": -0.1278},
                    {"latitude": 51.5075, "longitude": -0.1280},
                    {"latitude": 51.5077, "longitude": -0.1282},
                    {"latitude": 51.5074, "longitude": -0.1278}]
        self.save_to_shapefile(gps_data, "polygon")

    def save_to_shapefile(self, gps_data, mode):
        # File path and name
        file_name = f"logs/{datetime.now().strftime('%Y%m%d_%H%M%S')}_{mode}.shp"
        # Create shapefile
        with shapefile.Writer(file_name) as w:
            if isinstance(gps_data, dict):
                w.field("ID", "N", 10)
                w.point(gps_data["longitude"], gps_data["latitude"])
            elif isinstance(gps_data, list):
                w.field("ID", "N", 10)
                for point in gps_data:
                    w.point(point["longitude"], point["latitude"])

        print(f"Data saved to {file_name}")
    
if __name__ == "__main__":
    app = QApplication([])
    window = GPSLogger()
    window.show()
    app.exec_()
