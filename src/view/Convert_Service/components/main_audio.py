#
# main_audio.py Copyright (c) 2022 Jalasoft.
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

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, QPushButton, \
    QComboBox, QSpacerItem, QSizePolicy, QFileDialog
from src.view.Convert_Service.components.title import Title
from src.view.Convert_Service.components.buttons_top import ButtonsTop


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.addLayout(ButtonsTop())
        self.layout.addWidget(Title())
        self.layout.addLayout(self.get_layout_body(), 10)
        self.setLayout(self.layout)

    def get_layout_body(self):

        body = QHBoxLayout()
        body.addLayout(self.left_layout(), 10)
        body.addLayout(self.right_layout(), 75)
        return body

    def right_layout(self):
        show_button = QPushButton("Show Image")
        right = QVBoxLayout()
        right.addWidget(QPlainTextEdit(), 75)
        right.addWidget(show_button)
        return right


    def left_layout(self):
        list_convert = QComboBox()
        list_convert.addItem("Audio")
        list_convert.addItem("OCR")
        list_convert.addItem("Video")
        list_convert.addItem("Metadata")
        list_convert.addItem("Image")
        list_convert.addItem("Translator")
        list_convert.addItem("Wav to Txt")

        acodex_field = QLineEdit()

        audio_channel_field = QLineEdit()

        bit_rate_field = QLineEdit()

        sample_rate_field = QLineEdit()

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)
        convert_button = QPushButton("Convert")

        output_format = QComboBox()
        output_format.addItem("mp3")
        output_format.addItem("mp4")

        text_area_message = QPlainTextEdit()

        vertical_spacer = QSpacerItem(10, 600, QSizePolicy.Expanding)

        menu = QVBoxLayout()
        menu.addWidget(QLabel("Convert:"))
        menu.addWidget(list_convert)
        menu.addWidget(QLabel("File Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button)
        menu.addWidget(QLabel("Acodex:"))
        menu.addWidget(acodex_field)
        menu.addWidget(QLabel("Audio Channel:"))
        menu.addWidget(audio_channel_field)
        menu.addWidget(QLabel("Bit Rate:"))
        menu.addWidget(bit_rate_field)
        menu.addWidget(QLabel("Sample Rate:"))
        menu.addWidget(sample_rate_field)
        menu.addWidget(QLabel("Output Format:"))
        menu.addWidget(output_format)
        menu.addWidget(convert_button)
        menu.addSpacerItem(vertical_spacer)
        menu.addWidget(QLabel("Message:"))
        menu.addWidget(text_area_message)
        return menu

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])
