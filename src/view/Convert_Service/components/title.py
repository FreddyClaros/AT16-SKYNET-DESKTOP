#
# title.py Copyright (c) 2022 Jalasoft.
# 2643 Av Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# Edificio Union № 1376 Av. General Inofuentes esquina Calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Confidential Information"). You shall not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft.
#

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
