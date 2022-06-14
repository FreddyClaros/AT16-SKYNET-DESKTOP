#
# controller_convert_menu.py Copyright (c) 2022 Jalasoft.
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

from src.view.main.convert_menu_view import ConvertMenuView


class ControllerConvertMenu:
    def __init__(self):
        self.view = ConvertMenuView()
        self.view.init_ui()
        self.view.get_main_widget().get_button_emotion().clicked.connect(self.view.go_to_emotion)
        self.view.get_main_widget().get_button_object().clicked.connect(self.view.go_to_object)
        self.view.get_main_widget().get_button_face().clicked.connect(self.view.go_to_face)
        self.view.get_main_widget().get_button_iris_search().clicked.connect(self.view.go_to_search_iris)
        self.view.get_main_widget().get_button_iris_train().clicked.connect(self.view.go_to_train_iris)
        self.view.get_main_widget().get_button_translator().clicked.connect(self.view.go_to_translator)
        self.view.get_main_widget().get_button_wav_to_txt().clicked.connect(self.view.go_to_wav_to_txt)
       