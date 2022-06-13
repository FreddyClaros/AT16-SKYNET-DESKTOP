from PyQt5 import QtCore
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel


class ImageLoaded(QWidget):
    def __init__(self):
        super().__init__()
        self.dir = ''
        self.image_label = QLabel(self)
        self.image_label.setAlignment(QtCore.Qt.AlignCenter)

    def show_image(self, _dir):
        self.dir = _dir
        self.image_label.setPixmap(QPixmap(self.dir).scaledToWidth(600))
        self.image_label.resize(600, 600)