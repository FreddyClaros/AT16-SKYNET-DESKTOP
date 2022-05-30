#
# main_image.py Copyright (c) 2022 Jalasoft.
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
        list_convert.addItem("Image")
        list_convert.addItem("OCR")
        list_convert.addItem("Video")
        list_convert.addItem("Metadata")
        list_convert.addItem("Audio")
        list_convert.addItem("Translator")
        list_convert.addItem("Wav to Txt")

        list_color = QComboBox()
        list_color.addItem("Gray")
        list_color.addItem("Original")

        list_degrees = QComboBox()
        list_degrees.addItem("90")
        list_degrees.addItem("180")
        list_degrees.addItem("270")
        list_degrees.addItem("360")

        list_vertical_flip = QComboBox()
        list_vertical_flip.addItem("True")
        list_vertical_flip.addItem("False")

        list_horizontal_flip = QComboBox()
        list_horizontal_flip.addItem("True")
        list_horizontal_flip.addItem("False")

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)

        convert_button = QPushButton("Convert")

        height_field = QLineEdit()

        width_field = QLineEdit()

        output_format = QComboBox()
        output_format.addItem("png")
        output_format.addItem("jpg")

        text_area_message = QPlainTextEdit()

        vertical_spacer = QSpacerItem(10, 600, QSizePolicy.Expanding)

        menu = QVBoxLayout()
        menu.addWidget(QLabel("Convert:"))
        menu.addWidget(list_convert)
        menu.addWidget(QLabel("File Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button)
        menu.addWidget(QLabel("Color:"))
        menu.addWidget(list_color)
        menu.addWidget(QLabel("Rotate:"))
        menu.addWidget(list_degrees)
        menu.addWidget(QLabel("Vertical flip:"))
        menu.addWidget(list_vertical_flip)
        menu.addWidget(QLabel("Horizontal flip:"))
        menu.addWidget(list_horizontal_flip)
        menu.addWidget(QLabel("Height:"))
        menu.addWidget(height_field)
        menu.addWidget(QLabel("Width:"))
        menu.addWidget(width_field)
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
