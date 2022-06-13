#
# @image_loaded.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft .
#

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
