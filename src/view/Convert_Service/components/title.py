from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import *


class Title(QLabel):
    def __init__(self):
        super().__init__()
        self.create_title()

    def create_title(self):
        self.label = QLabel('SKYNET - Convert', self)
        self.label.move(1000, 0)
        self.label.setFont(QFont('Arial', 10))

