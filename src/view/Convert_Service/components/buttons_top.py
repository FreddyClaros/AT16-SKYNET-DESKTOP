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
        booking_button = QPushButton("Booking")
        converter_button = QPushButton("Converter")
        machine_learning_button = QPushButton("Machine Learning")
        reporting_button = QPushButton("Reporting")

        self.addWidget(booking_button)
        self.addWidget(converter_button)
        self.addWidget(machine_learning_button)
        self.addWidget(reporting_button)
