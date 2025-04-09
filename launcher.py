
# launcher.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QComboBox, QLabel
import subprocess

class LoggerLauncher(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('GPS Logger Launcher')

        self.layout = QVBoxLayout()

        # Mode selector (Point/Line/Polygon)
        self.mode_combo = QComboBox()
        self.mode_combo.addItems(['Point', 'Line', 'Polygon'])
        self.layout.addWidget(QLabel('Select Logging Mode:'))
        self.layout.addWidget(self.mode_combo)

        # Template selection
        self.template_combo = QComboBox()
        self.template_combo.addItems(['<Select Template>', 'New Template'])
        self.layout.addWidget(QLabel('Choose Template:'))
        self.layout.addWidget(self.template_combo)

        # Start logging button
        self.start_btn = QPushButton('Start Logging')
        self.start_btn.clicked.connect(self.start_logging)
        self.layout.addWidget(self.start_btn)

        # Set layout
        self.setLayout(self.layout)

    def start_logging(self):
        mode = self.mode_combo.currentText()
        template = self.template_combo.currentText()
        print(f'Selected Mode: {mode}, Template: {template}')

        # Start the GPS logger based on the selected mode/template
        subprocess.run(['python3', 'gps_logger.py'])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = LoggerLauncher()
    window.show()
    sys.exit(app.exec_())
