#
# convert_menu_view.py Copyright (c) 2022 Jalasoft.
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
from src.view.main.components.main_convert_menu import MainConvertMenuWidget
from src.controller.Convert_Service.controller_convert_audio import ConvertControllerAudio
from src.controller.Convert_Service.controller_convert_image import ConvertControllerImage
from src.controller.Convert_Service.controller_convert_metadata import ConvertControllerMetadata
from src.controller.Convert_Service.controller_convert_ocr import ConvertControllerOCR
from src.controller.Convert_Service.controller_convert_translator import ConvertControllerTranslator
from src.controller.Convert_Service.controller_convert_video import ConvertControllerVideo
from src.controller.Convert_Service.controller_convert_wav_to_txt import ConvertControllerWavToTxt

class ConvertMenuView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_widget = MainConvertMenuWidget()

    def init_ui(self):
        self.setWindowTitle("Machine Learning Menu")
        self.setCentralWidget(self.main_widget)
        self.showMaximized()
        self.show()

    def get_main_widget(self):
        return self.main_widget
    
    def go_to_emotion(self):
        self.close()
        self.window = ConvertControllerAudio()
    
    def go_to_object(self):
        self.close()
        self.window = ConvertControllerOCR()

    def go_to_face(self):
        self.close()
        self.window = ConvertControllerVideo()
    
    def go_to_search_iris(self):
        self.close()
        self.window = ConvertControllerMetadata()
    
    def go_to_train_iris(self):
        self.close()
        self.window = ConvertControllerImage()
    
    def go_to_translator(self):
        self.close()
        self.window = ConvertControllerTranslator()
    
    def go_to_wav_to_txt(self):
        self.close()
        self.window = ConvertControllerWavToTxt()
