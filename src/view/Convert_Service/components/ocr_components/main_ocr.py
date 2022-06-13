#
# main_ocr.py Copyright (c) 2022 Jalasoft.
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

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, \
    QHeaderView, \
    QPushButton, QComboBox, QSpacerItem, QSizePolicy, QFileDialog, QTableWidget, QAbstractItemView, \
    QTableWidgetItem
from src.view.Convert_Service.components.title import Title
from src.view.Convert_Service.components.buttons_top import ButtonsTop


class MainOCR(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.buttons = ButtonsTop()
        self.table = QTableWidget()
        self.file_path = QLineEdit()
        self.list_language = QComboBox()
        self.list_format = QComboBox()
        self.convert_button = QPushButton("Convert")
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

        self.setting_table()
        show_button = QPushButton("Show Document")
        right = QVBoxLayout()
        right.addWidget(self.table)
        right.addWidget(show_button)
        return right

    def left_layout(self):

        self.list_language.addItem("English")
        self.list_language.addItem("Spanish")
        self.list_language.addItem("Russian")

        self.list_format.addItem("txt")

        self.file_path.setReadOnly(True)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)

        text_area_message = QPlainTextEdit()

        vertical_spacer = QSpacerItem(10, 600, QSizePolicy.Expanding)

        menu = QVBoxLayout()
        menu.addWidget(QLabel("Convert OCR"))
        menu.addWidget(QLabel("File Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button)
        menu.addWidget(QLabel("Language:"))
        menu.addWidget(self.list_language)
        menu.addWidget(QLabel("Format:"))
        menu.addWidget(self.list_format)
        menu.addWidget(self.convert_button)
        menu.addSpacerItem(vertical_spacer)
        menu.addWidget(QLabel("Message:"))
        menu.addWidget(text_area_message)
        return menu

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])
    
    def get_layout(self):
        return self.buttons

    def get_file_path(self):
        return str(self.file_path.text())

    def get_language(self):
        match str(self.list_language.currentText()):
            case 'English': return 'eng'
            case 'Spanish': return 'esp'
            case 'Russian': return 'rus'

    def get_format(self):
        return str(self.list_format.currentText())

    def get_convert_button(self):
        return self.convert_button

    def setting_table(self):
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(('Link', 'Language', 'To', 'Format', 'path_saved',
                                              'path_download', 'path_translator'))
        self.table.setColumnHidden(2, True)
        self.table.setColumnHidden(4, True)
        self.table.setColumnHidden(5, True)
        self.table.setColumnHidden(6, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def add_values_table(self, link, language, _to, _format, path_saved, path_download):
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount()-1, 0, QTableWidgetItem(link))
        self.table.setItem(self.table.rowCount()-1, 1, QTableWidgetItem(language))
        self.table.setItem(self.table.rowCount()-1, 2, QTableWidgetItem(_to))
        self.table.setItem(self.table.rowCount()-1, 3, QTableWidgetItem(_format))
        self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem(path_saved))
        self.table.setItem(self.table.rowCount() - 1, 5, QTableWidgetItem(path_download))
