
# template_gui.py
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLabel, QFileDialog
import json

class TemplateGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Template Selector/Editor')
        
        self.layout = QVBoxLayout()
        
        # Template selector
        self.template_combo = QComboBox()
        self.layout.addWidget(QLabel('Select Application Template:'))
        self.layout.addWidget(self.template_combo)

        # Edit template button
        self.edit_btn = QPushButton('Edit Template')
        self.edit_btn.clicked.connect(self.edit_template)
        self.layout.addWidget(self.edit_btn)

        # Load templates
        self.load_templates()

        # Set layout
        self.setLayout(self.layout)

    def load_templates(self):
        # Load template files from the 'templates/' directory
        templates = ["<Select Template>"]
        try:
            with open("templates/templates.json", "r") as f:
                templates_data = json.load(f)
                templates.extend(templates_data["templates"])
        except FileNotFoundError:
            print("Templates file not found. Creating new one.")
        self.template_combo.addItems(templates)

    def edit_template(self):
        # Open the selected template for editing
        selected_template = self.template_combo.currentText()
        if selected_template == "<Select Template>":
            print("Please select a template first.")
        else:
            file_path = f"templates/{selected_template}.json"
            self.open_template_editor(file_path)

    def open_template_editor(self, file_path):
        # Open the template file for editing
        with open(file_path, "r") as file:
            template_data = json.load(file)
        print(f"Editing template: {file_path}")
        print(f"Template data: {template_data}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TemplateGUI()
    window.show()
    sys.exit(app.exec_())
