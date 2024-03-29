#
# controller_convert_audio.py Copyright (c) 2022 Jalasoft.
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

from src.view.Convert_Service.convert_audio_view import ConvertAudioView
import requests
from PyQt5.QtWidgets import QTableWidgetItem
import os
from decouple import config


CONVERT_SERVICE_DIR = config('CONVERT_SERVICE_DIR')
UPLOAD_FOLDER = '/upload/'
DOWNLOAD_FOLDER = 'Download/'


class ConvertControllerAudio:
    def __init__(self):
        self.view = ConvertAudioView()
        self.view.init_ui()
        self.view.get_main_widget().get_layout().get_button_menu_ml().clicked.connect(self.popWindowML)
        self.view.get_main_widget().get_layout().get_button_menu_convert().clicked.connect(self.popWindowConvert)
        self.view.main_widget.get_convert_button().clicked.connect(self.show_result)
        self.table_result = self.view.main_widget.table
        self.count = 0
    
    def popWindowML(self):
        self.view.pop_window_machine()
    
    def popWindowConvert(self):
        self.view.pop_window_convert()
        

    def show_result(self):
        url = CONVERT_SERVICE_DIR
        convert = "Audio"
        file_path = self.view.main_widget.get_file_path()
        file = {'file': open(file_path, 'rb')}
        audio_channel = self.view.main_widget.get_audio_channel_field()
        bit_rate = self.view.main_widget.get_bit_rate_field()
        sample_rate = self.view.main_widget.get_sample_rate_field()
        output_format = self.view.main_widget.get_output_format()
        payload = {'convert': convert, 'bitrate': bit_rate, 'sample_rate': sample_rate,
                   'audio_channel': audio_channel, 'format': output_format}
        response = requests.post(url, files=file, data=payload, verify=False)
        res = response.json()
        message = res['message']
        url_return = message
        name_file = url_return.split("/")
        my_file = requests.get(url_return)
        folder = DOWNLOAD_FOLDER + name_file[-1]
        input_format_type = file_path.split(".")
        open(folder, 'wb').write(my_file.content)

        # Audio path
        simp_path = folder
        abs_path = os.path.abspath(simp_path)

        self.table_result.insertRow(self.count)
        self.table_result.setItem(self.count, 0, QTableWidgetItem(input_format_type[-1]))
        self.table_result.setItem(self.count, 1, QTableWidgetItem(output_format))
        self.table_result.setItem(self.count, 2, QTableWidgetItem(abs_path))
        self.count += 1
