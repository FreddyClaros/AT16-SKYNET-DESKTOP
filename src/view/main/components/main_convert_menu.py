#
# main_convert_menu.py Copyright (c) 2022 Jalasoft.
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

import os
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, \
                            QPushButton, QComboBox, QSpacerItem, QSizePolicy, QFileDialog
from src.view.machine_learning.components.title import Title
from src.view.machine_learning.components.buttons_top import ButtonsTop


class MainConvertMenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.style = os.getcwd() + "/resources/compiler.css"
        self.setStyleSheet(open(self.style).read())
        self.layout = QVBoxLayout()
        self.layout.addWidget(Title())
        self.layout.addLayout(self.get_layout_body())
        self.setLayout(self.layout)

    def get_layout_body(self):
        
        self.emotion_button = QPushButton("Audio")
        self.object_button = QPushButton("OCR")
        self.face_button = QPushButton("Video")
        self.iris_search_button = QPushButton("Metadata")
        self.iris_train_button = QPushButton("Image")
        self.translator_button = QPushButton("Translator")
        self.wavtotxt_button = QPushButton("Wav to txt")
        vertical_spacer = QSpacerItem(10, 600, QSizePolicy.Expanding)

        body = QVBoxLayout()
        body.addWidget(self.emotion_button)
        body.addWidget(self.object_button)
        body.addWidget(self.face_button)
        body.addWidget(self.iris_search_button)
        body.addWidget(self.iris_train_button)
        body.addWidget(self.translator_button)
        body.addWidget(self.wavtotxt_button)
        body.addSpacerItem(vertical_spacer)
        
        return body
    
    def get_button_emotion(self):
        return self.emotion_button
    
    def get_button_object(self):
        return self.object_button
    
    def get_button_face(self):
        return self.face_button
    
    def get_button_iris_search(self):
        return self.iris_search_button
    
    def get_button_iris_train(self):
        return self.iris_train_button
    
    def get_button_translator(self):
        return self.translator_button
    
    def get_button_wav_to_txt(self):
        return self.wavtotxt_button
