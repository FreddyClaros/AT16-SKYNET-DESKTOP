#
# main_video.py Copyright (c) 2022 Jalasoft.
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
                     QComboBox, QSpacerItem, QSizePolicy, QFileDialog, QTableWidget, QHeaderView, QAbstractItemView
from src.view.Convert_Service.components.title import Title
from src.view.Convert_Service.components.buttons_top import ButtonsTop


class MainVideo(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.buttons = ButtonsTop()
        self.layout.addLayout(self.buttons)
        self.layout.addWidget(Title())
        self.layout.addLayout(self.get_layout_body(), 10)
        self.setLayout(self.layout)

    def get_layout_body(self):

        body = QHBoxLayout()
        body.addLayout(self.left_layout(), 10)
        body.addLayout(self.right_layout(), 75)
        return body

    def right_layout(self):
        self.table = QTableWidget()
        self.setting_table()
        show_button = QPushButton("Show Document")
        right = QVBoxLayout()
        right.addWidget(self.table)
        right.addWidget(show_button)
        return right

    def left_layout(self):

        list_frame = QComboBox()
        list_frame.addItem("10")
        list_frame.addItem("20")
        list_frame.addItem("30")
        list_frame.addItem("40")
        list_frame.addItem("50")
        list_frame.addItem("60")

        list_color = QComboBox()
        list_color.addItem("Gray")
        list_color.addItem("Original")

        list_format = QComboBox()
        list_format.addItem("txt")

        height_field = QLineEdit()

        width_field = QLineEdit()

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)

        convert_button = QPushButton("Convert")

        text_area_message = QPlainTextEdit()

        vertical_spacer = QSpacerItem(10, 600, QSizePolicy.Expanding)

        menu = QVBoxLayout()
        menu.addWidget(QLabel("Convert Video"))
        menu.addWidget(QLabel("File Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button)
        menu.addWidget(QLabel("Frame:"))
        menu.addWidget(list_frame)
        menu.addWidget(QLabel("Color:"))
        menu.addWidget(list_color)
        menu.addWidget(QLabel("Height:"))
        menu.addWidget(height_field)
        menu.addWidget(QLabel("Width:"))
        menu.addWidget(width_field)
        menu.addWidget(QLabel("Output Format:"))
        menu.addWidget(list_format)
        menu.addWidget(convert_button)
        menu.addSpacerItem(vertical_spacer)
        menu.addWidget(QLabel("Message:"))
        menu.addWidget(text_area_message)
        return menu

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])
    
    def get_layout(self):
        return self.buttons

    def setting_table(self):
        self.table.setColumnCount(3)
        self.table.setHorizontalHeaderLabels(('Colum1', 'Colum2', 'Colum3'))
        self.table.setColumnHidden(5, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
