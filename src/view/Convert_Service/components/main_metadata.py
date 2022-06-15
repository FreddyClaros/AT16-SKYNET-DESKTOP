#
# main_metadata.py Copyright (c) 2022 Jalasoft.
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
    QComboBox, QSpacerItem, QSizePolicy, QFileDialog, QTableWidget, QHeaderView, QAbstractItemView, QTableWidgetItem, QToolBar, QAction
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, QHeaderView, \
                    QPushButton, QComboBox, QSpacerItem, QSizePolicy, QFileDialog, QTableWidget, QAbstractItemView, QTableWidgetItem
from src.view.Convert_Service.components.title import Title
from src.view.Convert_Service.components.buttons_top import ButtonsTop


class MainMetadata(QWidget):
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
        self.editor = QPlainTextEdit()
        right = QVBoxLayout()
        right.addWidget(self.table, 50)
        right.addWidget(self.editor, 25)
        return right

    def left_layout(self):

        self.list_format = QComboBox()
        self.list_format.addItem("txt")
        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)

        self.convert_button = QPushButton("Convert")

        text_area_message = QPlainTextEdit()
        vertical_spacer = QSpacerItem(10, 600, QSizePolicy.Expanding)
        menu = QVBoxLayout()
        menu.addWidget(QLabel("Convert:"))
        menu.addWidget(self.list_convert)
        menu.addWidget(QLabel("Convert Metadata"))
        menu.addWidget(QLabel("File Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button)
        menu.addWidget(QLabel("Output Format:"))
        menu.addWidget(self.list_format)
        menu.addWidget(self.convert_button)
        menu.addSpacerItem(vertical_spacer)
        menu.addWidget(QLabel("Message:"))
        menu.addWidget(text_area_message)
        return menu

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])

    def get_file_path(self):
        return str(self.file_path.text())

    def get_list_convert(self):
        return str(self.list_convert.currentText())

    def get_convert_button(self):
        return self.convert_button

    def get_output_format(self):
        return str(self.list_format.currentText())

    def get_editor_text(self):
        return self.editor

    def get_table(self):
        return self.table

    def file_open3(self, path):
        print(path)
        with open(path, "r") as f:
            text = f.read()
        self.editor.setPlainText(text)

    def setting_table(self):
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('Link', 'Output Format', 'Status', 'Path Saved', 'Path Download'))
        self.table.setColumnHidden(3, True)
        self.table.setColumnHidden(4, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def add_values_table(self, link, output_format, status, path_saved, path_download):
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(link))
        self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(output_format))
        self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(status))
        self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(path_saved))
        self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem(path_download))
    
    def get_file_path(self):
        return str(self.file_path.text())

    def get_list_convert(self):
        return str(self.list_convert.currentText())

    def get_convert_button(self):
        return self.convert_button

    def get_output_format(self):
        return str(self.list_format.currentText())

    def get_editor_text(self):
        return self.editor

    def get_table(self):
        return self.table

    def get_layout(self):
        return self.buttons

    def setting_table(self):
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels(('Link', 'Output Format', 'Status', 'Path Saved', 'Path Download'))
        self.table.setColumnHidden(3, True)
        self.table.setColumnHidden(4, True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)

    def add_values_table(self, link, output_format, status, path_saved, path_download):
        self.table.insertRow(self.table.rowCount())
        self.table.setItem(self.table.rowCount() - 1, 0, QTableWidgetItem(link))
        self.table.setItem(self.table.rowCount() - 1, 1, QTableWidgetItem(output_format))
        self.table.setItem(self.table.rowCount() - 1, 2, QTableWidgetItem(status))
        self.table.setItem(self.table.rowCount() - 1, 3, QTableWidgetItem(path_saved))
        self.table.setItem(self.table.rowCount() - 1, 4, QTableWidgetItem(path_download))
