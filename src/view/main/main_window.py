#
# main_window.py Copyright (c) 2022 Jalasoft.
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


from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout
from src.view.main.button import Button
from src.controller.menu.controller_convert_menu import ControllerConvertMenu
from src.controller.menu.controller_ml_menu import ControllerMLMenu


class MainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        
        self.init_ui()
        

    def init_ui(self):
        self.setWindowTitle("AT16 SKYNET")
        self.setGeometry(20, 50, 1440, 810)
        #widget
        image_widget = QWidget()
        #labels
        image_label = QLabel(self)
        # buttons
        booking_button = Button().action_button("Booking")
        converter_button = Button().action_button("Converter")
        converter_button.clicked.connect(self.pop_window_convert)
        machine_learning_button = Button().action_button("Machine Learning")
        machine_learning_button.clicked.connect(self.pop_window_machine)
        reporting_button = Button().action_button("Reporting")
        # layers
        background_layer = QGridLayout()
        background_layer.addWidget(booking_button, 0, 0)
        background_layer.addWidget(converter_button, 0, 1)
        background_layer.addWidget(machine_learning_button, 1, 0)
        background_layer.addWidget(reporting_button, 1, 1)
        # image
        
        image_label.setLayout(background_layer)
        self.setCentralWidget(image_label)
        self.showMaximized()

    def pop_window_convert(self):
        self.hide()
        self.ui2 = ControllerConvertMenu()

    def pop_window_machine(self):
        self.hide()
        self.ui1 = ControllerMLMenu()
