#
# main.py Copyright (c) 2022 Jalasoft.
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

# Press the green button in the gutter to run the script.

import sys
from PyQt5.QtWidgets import QApplication
from src.view.main.main_window import MainWindow

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = MainWindow()
    controller.setStyleSheet("MainWindow{background-image: url(resources/terminator.jpg)}")
    controller.show()
    sys.exit(app.exec())
