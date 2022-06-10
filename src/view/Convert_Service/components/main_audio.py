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

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, QHeaderView, \
                    QPushButton, QComboBox, QSpacerItem, QSizePolicy, QFileDialog, QTableWidget, QAbstractItemView
from src.view.Convert_Service.components.title import Title
from src.view.Convert_Service.components.buttons_top import ButtonsTop
from src.view.Convert_Service.components.player_view import PlayerView


class MainWidget(QWidget):
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
        self.show_button = QPushButton("Open player controls")
        self.show_button.clicked.connect(self.show_player)
        right = QVBoxLayout()
        self.table = QTableWidget()
        self.setting_table()
        right.addWidget(self.table, 75)
        right.addWidget(self.show_button)
        return right

    def show_player(self):
        index = self.table.selectionModel().currentIndex()
        if index.row() == -1:
            return
        audio_path = self.table.item(index.row(), 3).text()
        self.player = PlayerView()
        self.player.init_ui(audio_path)
        #self.player.play_btn
        self.player.play_btn.clicked.connect(self.player.play_it)
        self.player.pause_btn.clicked.connect(self.player.pause_it)
        self.player.stop_btn.clicked.connect(self.player.stop_it)


    def left_layout(self):
        
        self.audio_channel_field = QLineEdit()
        self.bit_rate_field = QLineEdit()
        self.sample_rate_field = QLineEdit()
        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)
        self.convert_button = QPushButton("Convert")
        self.output_format = QComboBox()
        self.output_format.addItem("mp3")
        self.output_format.addItem("wav")

        text_area_message = QPlainTextEdit()
        vertical_spacer = QSpacerItem(10, 600, QSizePolicy.Expanding)
        menu = QVBoxLayout()
        menu.addWidget(QLabel("Convert Audio"))
        menu.addWidget(QLabel("File Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button)
        menu.addWidget(QLabel("Audio Channel:"))
        menu.addWidget(self.audio_channel_field)
        menu.addWidget(QLabel("Bit Rate:"))
        menu.addWidget(self.bit_rate_field)
        menu.addWidget(QLabel("Sample Rate:"))
        menu.addWidget(self.sample_rate_field)
        menu.addWidget(QLabel("Output Format:"))
        menu.addWidget(self.output_format)
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

    def get_list_convert(self):
        return str(self.list_convert.currentText())

    def get_audio_channel_field(self):
        return str(self.audio_channel_field.text())

    def get_bit_rate_field(self):
        return str(self.bit_rate_field.text())

    def get_sample_rate_field(self):
        return str(self.sample_rate_field.text())

    def get_output_format(self):
        return str(self.output_format.currentText())

    def get_convert_button(self):
        return self.convert_button

    def set_result(self, message):
        self.text_result.appendPlainText(message)

    def setting_table(self):
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(('Status', 'Input format', 'Output format', 'Output path'))
        self.table.setColumnHidden(2, False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
