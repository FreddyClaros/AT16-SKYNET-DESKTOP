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
import os
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, \
    QHeaderView, \
    QPushButton, QComboBox, QSpacerItem, QSizePolicy, QFileDialog, QTableWidget, QAbstractItemView, \
    QTableWidgetItem
from src.view.Convert_Service.components.title import Title
from src.view.Convert_Service.components.buttons_top import ButtonsTop
from src.view.Convert_Service.components.ocr_components.image_loaded import ImageLoaded


BACK_IMAGE = "/Download/back_img.jpg"

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.buttons = ButtonsTop()
        self.table = QTableWidget()
        self.layout.addLayout(self.buttons)
        self.image_loaded = ImageLoaded()
        self.result = ImageLoaded()
        self.layout.addWidget(Title())
        self.layout.addLayout(self.get_layout_body(), 10)
        self.setLayout(self.layout)

    def get_layout_body(self):

        body = QHBoxLayout()
        body.addLayout(self.left_layout(), 10)
        body.addLayout(self.right_layout(), 75)
        return body

    def right_layout(self):
        layout_results = QHBoxLayout()
        self.setting_table()
        layout_results.addWidget(self.table, 50)

        layout_images = QVBoxLayout()
        self.image_loaded.show_image(os.getcwd() + BACK_IMAGE)
        self.result.show_image(os.getcwd() + BACK_IMAGE)
        layout_images.addWidget(self.image_loaded, 50)
        layout_images.addWidget(self.result, 50)

        layout_results.addLayout(layout_images, 50)

        return layout_results

    def left_layout(self):

        self.list_color = QComboBox()
        self.list_color.addItem("gray")
        self.list_color.addItem("sRGB")

        self.list_degrees = QComboBox()
        self.list_degrees.addItem("0")
        self.list_degrees.addItem("90")
        self.list_degrees.addItem("180")
        self.list_degrees.addItem("270")
        self.list_degrees.addItem("360")

        self.list_vertical_flip = QComboBox()
        self.list_vertical_flip.addItem("True")
        self.list_vertical_flip.addItem("False")

        self.list_horizontal_flip = QComboBox()
        self.list_horizontal_flip.addItem("True")
        self.list_horizontal_flip.addItem("False")

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)

        self.height = QLineEdit()

        self.width = QLineEdit()

        self.browse_button = QPushButton("Browse")
        self.browse_button.clicked.connect(self.browse_file)

        self.convert = QPushButton("Convert")

        self.output_format = QComboBox()
        self.output_format.addItem("png")
        self.output_format.addItem("jpg")

        self.text_result = QPlainTextEdit()

        vertical_spacer = QSpacerItem(10, 600, QSizePolicy.Expanding)

        menu = QVBoxLayout()
        menu.addWidget(QLabel("Convert Image"))
        menu.addWidget(QLabel("File Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(self.browse_button)
        menu.addWidget(QLabel("Color:"))
        menu.addWidget(self.list_color)
        menu.addWidget(QLabel("Rotate:"))
        menu.addWidget(self.list_degrees)
        menu.addWidget(QLabel("Vertical flip:"))
        menu.addWidget(self.list_vertical_flip)
        menu.addWidget(QLabel("Horizontal flip:"))
        menu.addWidget(self.list_horizontal_flip)
        menu.addWidget(QLabel("Height:"))
        menu.addWidget(self.height)
        menu.addWidget(QLabel("Width:"))
        menu.addWidget(self.width)
        menu.addWidget(QLabel("Output Format:"))
        menu.addWidget(self.output_format)
        menu.addWidget(self.convert)
        menu.addSpacerItem(vertical_spacer)
        menu.addWidget(QLabel("Message:"))
        menu.addWidget(self.text_result)
        return menu

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])

    def get_file_path(self):
        return str(self.file_path.text())

    def set_result(self, message):
        self.pixmap = QPixmap(message)
        return self.label_right.setPixmap(self.pixmap)

    def get_list_convert(self):
        return str(self.list_convert.currentText())

    def get_color(self):
        return str(self.list_color.currentText())

    def get_degrees(self):
        return str(self.list_degrees.currentText())

    def get_horizontal_flip(self):
        result = ''
        rsp = str(self.list_horizontal_flip.currentText())
        if rsp == 'True':
            result = 'True'
        return result

    def get_vertical_flip(self):
        result = ''
        rsp = str(self.list_vertical_flip.currentText())
        if rsp == 'True':
            result = 'True'
        return result

    def get_height(self):
        return str(self.height.text())

    def get_width(self):
        return str(self.width.text())

    def get_output_format(self):
        return str(self.output_format.currentText())

    def get_convert_button(self):
        return self.convert
    
    def get_layout(self):
        return self.buttons

    def get_table(self):
        return self.table

    def clear_result(self):
        self.result.clear()

    def set_result(self, message):
        self.result.appendPlainText(message)

    def setting_table(self):
        self.table.setColumnCount(6)
        self.table.setHorizontalHeaderLabels(('Link', 'File', 'To', 'Format', 'path_saved',
                                              'path_download', 'path_translator'))
        self.table.setColumnHidden(2, True)
        self.table.setColumnHidden(4, True)
        self.table.setColumnHidden(5, True)
        self.table.setColumnHidden(6, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def add_values_table(self, link, language, _to, _format, path_saved, path_download):
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(link))
        self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(language))
        self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(_to))
        self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(_format))
        self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem(path_saved))
        self.table.setItem(self.table.rowCount() - 1, 5, QTableWidgetItem(path_download))