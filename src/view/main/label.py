#
# label.py Copyright (c) 2022 Jalasoft.
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
from PyQt5.QtGui import QFont


class Label:
    def tittle_label(self, name_label):
        label = QLabel(name_label)
        label.setFont(QFont("Arial", 24))
        return label

    def sub_label(self, name_label):
        label = QLabel(name_label)
        label.setFont(QFont('Inter', 12))
        label.setFixedHeight(40)
        label.setStyleSheet('QLabel {'
                            '  margin: 0px 8px;'
                            '}')
        label.resize(40, 20)
        return label
