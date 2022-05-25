#
# combobox.py Copyright (c) 2022 Jalasoft.
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

from PyQt5.QtWidgets import QComboBox
from PyQt5.QtGui import QFont


class ComboBox:
    def basic_combobox(self, list_items):
        combo_box = QComboBox()
        combo_box.addItems(list_items)
        combo_box.setFont(QFont("Calibre", 12))
        combo_box.setStyleSheet('QComboBox {'
                                '  background-color: #3C93C4;'
                                '  color: white;'
                                '  margin: 0px 8px;'
                                '  padding: 12px;'
                                '  border: none;'
                                '  border-radius: 4px;'
                                '  font-size: 20px;'
                                '}'
                                'QComboBox:hover {'
                                '  background-color: #2696E7;'
                                '}'
                                'QComboBox::down-arrow {'
                                '  border: 4px black;'
                                '  width: 30px'
                                '}'
                                'QComboBox::drop-down {'
                                '  color: rgb(87, 96, 134) '
                                '  padding: 12px 16px;'
                                '  z-index: 1'
                                '  background-color: #3C93C4;'
                                '  margin: 0px 8px;'
                                '}')

        return combo_box
