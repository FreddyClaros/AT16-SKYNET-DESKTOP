from PyQt5.QtWidgets import QMainWindow
from src.view.machine_learning.components.main_face import MainFaceWidget


class MLFaceView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = MainFaceWidget()

    def init_ui(self):
        self.setWindowTitle("Machine Learning")
        self.setCentralWidget(self.main_widget)
        self.showMaximized()
        self.show()
