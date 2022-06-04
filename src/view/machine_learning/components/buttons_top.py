#
# buttons_top.py Copyright (c) 2022 Jalasoft.
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

from PyQt5.QtWidgets import QPushButton, QHBoxLayout


class ButtonsTop(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.create_buttons()

    def create_buttons(self):
        self.converter_button = QPushButton("Menu Converter")
        self.machine_learning_button = QPushButton("Menu Machine Learning")
        self.addWidget(self.converter_button)
        self.addWidget(self.machine_learning_button)
    
    def get_button_menu_ml(self):
        return self.machine_learning_button
    
    def get_button_menu_convert(self):
        return self.converter_button




