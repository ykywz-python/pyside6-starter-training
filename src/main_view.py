from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QLineEdit,
    QWidget,
    QVBoxLayout,
    QLabel,
    QMainWindow,
    QPushButton
)

class MainView(QMainWindow):

    def setup_ui(self):
        self.central_widget = QWidget()
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        self.button = QPushButton('Click Me')
        main_layout.addWidget(self.button)

        self.central_widget.setObjectName('central')
        self.central_widget.setStyleSheet("""
        QFrame#central {
            background: #e45b24;
        }
        """)
        self.central_widget.setLayout(main_layout)
        self.setCentralWidget(self.central_widget)