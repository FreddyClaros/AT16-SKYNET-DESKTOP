#
# main_object.py Copyright (c) 2022 Jalasoft.
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
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, QHeaderView, \
                     QPushButton, QComboBox, QSpacerItem, QSizePolicy, QFileDialog, QTableWidget, QAbstractItemView
from src.view.machine_learning.components.title import Title
from src.view.machine_learning.components.buttons_top import ButtonsTop


class MainObjectWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.style = os.getcwd() + "/resources/compiler.css"
        self.setStyleSheet(open(self.style).read())
        self.layout = QVBoxLayout()
        self.buttons = ButtonsTop()
        self.layout.addLayout(self.buttons)
        self.layout.addWidget(Title())
        self.layout.addLayout(self.get_layout_body(), 10)
        self.setLayout(self.layout)

    def get_layout_body(self):

        body = QHBoxLayout()
        body.addLayout(self.left_layout(self), 10)
        body.addLayout(self.right_layout(self), 65)
        return body

    @staticmethod
    def right_layout(self):
        self.table = QTableWidget()
        self.setting_table()
        show_button = QPushButton("Show Image")
        right = QVBoxLayout()
        right.addWidget(self.table)
        right.addWidget(show_button)
        return right

    @staticmethod
    def left_layout(self):

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)
        search_button = QPushButton("Search")

        models = QComboBox()
        models.addItem("InceptionV3")
        models.addItem("Vgg16")

        percentage = QComboBox()
        percentage.addItem("0%")
        percentage.addItem("10%")
        percentage.addItem("20%")
        percentage.addItem("30%")
        percentage.addItem("40%")
        percentage.addItem("50%")
        percentage.addItem("60%")
        percentage.addItem("70%")
        percentage.addItem("80%")
        percentage.addItem("90%")
        percentage.addItem("100%")

        vertical_spacer = QSpacerItem(10, 700, QSizePolicy.Expanding)

        menu = QVBoxLayout()
        menu.addWidget(QLabel("Object Recognizer"))
        menu.addWidget(QLabel("Video Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button)
        menu.addWidget(QLabel("Word:"))
        menu.addWidget(QLineEdit())
        menu.addWidget(QLabel("Neuronal Network Model:"))
        menu.addWidget(models)
        menu.addWidget(QLabel("Percentage:"))
        menu.addWidget(percentage)
        menu.addWidget(search_button)
        menu.addSpacerItem(vertical_spacer)
        menu.addWidget(QLabel("Message:"))
        menu.addWidget(QPlainTextEdit())
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
