import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

# Step 1: Create the app
app = QApplication(sys.argv)

# Step 2: Create a main window
window = QWidget()
window.setWindowTitle("My First PyQt App")
window.setGeometry(100, 100, 400, 300)  # Set window size

# Step 3: Add a button
button = QPushButton("Click Me!")
button.setFixedSize(100, 40)  # Set button size
button.setStyleSheet("background-color: lightgray; border-radius: 10px;")

# Step 4: Layout (arrange widgets)
layout = QVBoxLayout()
layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignCenter)  # Center button
window.setLayout(layout)

# Step 5: Show the window
window.show()

# Step 6: Run the app
sys.exit(app.exec())

