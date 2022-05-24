#
# button Copyright (c) 2022 Jalasoft.
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
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtGui import QIcon


class Button(QPushButton):
    def __init__(self):
        super().__init__()

    @staticmethod
    def action_button(name_button):
        button = QPushButton(name_button)
        button.setFont(QFont("Calibre", 12))
        button.setStyleSheet('QPushButton {'
                             '  background-color: #005898;'
                             '  color: #FFFFFF;'
                             '  height: 40px;'
                             '  border-radius: 4px;'
                             '  margin: 0px 8px;'
                             '}'
                             'QPushButton:hover {'
                             '  background-color: #2696E7;'
                             '}')
        return button
