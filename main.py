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
from view.main_window import MainWindow
from view.machine_learning_view import MachineLearningObject


def main():
    app = QApplication(sys.argv)
    window = MainWindow() # for main window
    window.show()
    #ml = MachineLearningObject()  # for secondary view
    #ml.show()
    app.exec()


if __name__ == '__main__':
    main()
