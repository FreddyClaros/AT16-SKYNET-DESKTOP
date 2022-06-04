#
# ml_menu_view.py Copyright (c) 2022 Jalasoft.
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
from src.view.main.components.main_ml_menu import MainMLMenuWidget
from src.controller.machine_learning_service.controller_ml_emotion import MLEmotionController
from src.controller.machine_learning_service.controller_ml_object import MLObjectController
from src.controller.machine_learning_service.controller_ml_face import MLFaceController
from src.controller.machine_learning_service.controller_ml_search_iris import MLSearchIrisController
from src.controller.machine_learning_service.controller_ml_train_iris import MLTrainIrisController

class MLMenuView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = MainMLMenuWidget()

    def init_ui(self):
        self.setWindowTitle("Machine Learning Menu")
        self.setCentralWidget(self.main_widget)
        self.showMaximized()
        self.show()

    def get_main_widget(self):
        return self.main_widget
    
    def go_to_emotion(self):
        self.close()
        self.window = MLEmotionController()
    
    def go_to_object(self):
        self.close()
        self.window = MLObjectController()

    def go_to_face(self):
        self.close()
        self.window = MLFaceController()
    
    def go_to_search_iris(self):
        self.close()
        self.window = MLSearchIrisController()
    
    def go_to_train_iris(self):
        self.close()
        self.window = MLTrainIrisController()
