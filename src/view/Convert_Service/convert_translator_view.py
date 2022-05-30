#
# convert_translator_view.py Copyright (c) 2022 Jalasoft.
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
from src.view.Convert_Service.components.main_translator import MainTranslator


class ConvertTranslatorView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = MainTranslator()

    def init_ui(self):
        self.setWindowTitle("Convert Translator")
        self.setCentralWidget(self.main_widget)
        self.showMaximized()
        self.show()
