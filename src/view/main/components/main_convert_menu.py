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

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QHBoxLayout, QLabel
from PyQt5.QtGui import *
from PyQt5 import QtCore


class MainConvertMenuWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.label = QLabel('Convert Menu')
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.layout.addWidget(self.label)
        self.layout.addLayout(self.get_layout_body())
        self.setLayout(self.layout)
    
    def get_layout_body(self):
        
        body = QHBoxLayout()
        
        body.addLayout(self.get_left_body(), 35)
        body.addLayout(self.get_right_body(), 35)
        return body
    
    def get_left_body(self):

        self.emotion_button = QPushButton("Audio")
        self.object_button = QPushButton("OCR")
        self.face_button = QPushButton("Video")
        vertical_spacer = QSpacerItem(10, 400, QSizePolicy.Expanding)
        body = QVBoxLayout()
        body.addWidget(self.emotion_button)
        body.addWidget(self.object_button)
        body.addWidget(self.face_button)
        body.addSpacerItem(vertical_spacer)
        return body

    def get_right_body(self):
        
        self.iris_search_button = QPushButton("Metadata")
        self.iris_train_button = QPushButton("Image")
        self.translator_button = QPushButton("Translator")
        self.wavtotxt_button = QPushButton("Wav to txt")
        vertical_spacer = QSpacerItem(10, 400, QSizePolicy.Expanding)

        body = QVBoxLayout()
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
