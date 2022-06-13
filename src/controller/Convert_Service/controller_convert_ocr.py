#
# controller_convert_ocr.py Copyright (c) 2022 Jalasoft.
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
import random
import shutil

import requests

from src.view.Convert_Service.convert_ocr_view import ConvertOCRView
from decouple import config

CONVERT_SERVICE_DIR = config('CONVERT_SERVICE_DIR')

class ConvertControllerOCR:
    def __init__(self):
        self.view = ConvertOCRView()
        self.view.init_ui()
        self.view.get_main_widget().get_layout().\
            get_button_menu_ml().clicked.connect(self.popWindowML)
        self.view.get_main_widget().get_layout().\
            get_button_menu_convert().clicked.connect(self.popWindowConvert)

        self.view.get_main_widget().get_convert_button().clicked.connect(self.call_convert_service)

    def call_convert_service(self):

        # Defines variables
        url = CONVERT_SERVICE_DIR
        file_path = self.view.get_main_widget().get_file_path()
        language = self.view.get_main_widget().get_language()
        _format = self.view.get_main_widget().get_format()

        file_name_loaded = file_path.split('/')
        num_file = str(random.randint(1, 1000))
        file_path_loaded = os.getcwd() + "/upload/" + num_file + file_name_loaded[-1]
        shutil.copy2(file_path, file_path_loaded)

        files = [
            ('file',
             (file_name_loaded[-1], open(file_path_loaded, 'rb'), 'application/octet-stream')
             )
        ]
        payload = {
            'language': language,
            'format': _format,
            'convert': 'OCR'
        }

        response = requests.post(url, files=files, data=payload, verify=False)
        message = (response.json())['message']
        _message = str(message).replace('\\', '/')
        file_name_result = (_message.split('/'))[-1]

        response_file = requests.request('GET', _message, headers={}, data={})
        file_path_download = os.getcwd()+'/Download/' + file_name_result

        if _format == "txt":
            with open(file_path_download, 'w') as new_file:
                new_file.write(response_file.text)

        self.view.get_main_widget().add_values_table(message, language, '', _format,
                                                     file_path_loaded, file_path_download)
        print(_message)
        print(file_name_result)



    def popWindowML(self):
        self.view.pop_window_machine()
    
    def popWindowConvert(self):
        self.view.pop_window_convert()
