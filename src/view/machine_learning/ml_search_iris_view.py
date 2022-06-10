#
# ml_seach_iris_view.py Copyright (c) 2022 Jalasoft.
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
from src.view.machine_learning.components.main_search_iris import MainSearchIrisWidget


class MLSearchIrisView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = MainSearchIrisWidget()

    def init_ui(self):
        self.setWindowTitle("Iris Recognizer")
        self.setCentralWidget(self.main_widget)
        self.showMaximized()
        self.show()
    
    def get_main_widget(self):
        return self.main_widget
    
    def pop_window_machine(self):
        from src.controller.menu.controller_ml_menu import ControllerMLMenu
        self.close()
        self.window = ControllerMLMenu()
    
    def pop_window_convert(self):
        from src.controller.menu.controller_convert_menu import ControllerConvertMenu
        self.close()
        self.window = ControllerConvertMenu()
