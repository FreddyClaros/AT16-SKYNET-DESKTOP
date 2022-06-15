#
# controller_convert_image.py Copyright (c) 2022 Jalasoft.
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

from src.view.Convert_Service.convert_image_view import ConvertImageView
import os
import random
import shutil
import requests
from decouple import config

CONVERT_SERVICE_DIR = config('CONVERT_SERVICE_DIR')
UPLOAD_FOLDER = '/upload/'
DOWNLOAD_FOLDER = 'Download/'


class ConvertControllerImage:
    def __init__(self):
        self.view = ConvertImageView()
        self.view.init_ui()
        self.view.get_main_widget().get_layout().get_button_menu_ml().clicked.connect(self.popWindowML)
        self.view.get_main_widget().get_layout().get_button_menu_convert().clicked.connect(self.popWindowConvert)

        self.view.get_main_widget().get_convert_button().clicked.connect(self.show_result)
        self.table_result = self.view.get_main_widget().get_table()
        self.table_result.cellClicked.connect(self.update_image_loaded)

    def show_result(self):
        url = CONVERT_SERVICE_DIR

        file_path = self.view.main_widget.get_file_path()
        file = {'file': open(file_path, 'rb')}
        convert = 'Image'
        color = self.view.main_widget.get_color()
        height = self.view.main_widget.get_height()
        width = self.view.main_widget.get_width()
        formato = self.view.main_widget.get_output_format()
        rotate = self.view.main_widget.get_degrees()
        flip_vert = self.view.main_widget.get_vertical_flip()
        flip_hor = self.view.main_widget.get_horizontal_flip()

        file_name_loaded = file_path.split('/')
        num_file = str(random.randint(1, 1000))
        file_path_loaded = os.getcwd() + UPLOAD_FOLDER + num_file + file_name_loaded[-1]
        shutil.copy2(file_path, file_path_loaded)

        payload = {'color': color, 'rotate': rotate, 'height': height, 'width': width, 'format': formato,
                   'convert': convert, 'vertical_flip': flip_vert, 'horizontal_flip': flip_hor}
        response = requests.post(url, files=file, data=payload, verify=False)
        resp = response.json()
        message = resp['message']
        url = str(message).replace('\\', '/')
        file_name_result = (url.split('/'))[-1]
        url = message
        name_fyle = url.split('/')
        myfile = requests.get(url)
        folder = DOWNLOAD_FOLDER + name_fyle[-1]
        open(folder, 'wb').write(myfile.content)
        file_path_download = os.getcwd() + '/' + DOWNLOAD_FOLDER + file_name_result
        self.view.get_main_widget().add_values_table(message, file_path_loaded, '', formato,
                                                     file_path_loaded, file_path_download)

    def update_image_loaded(self):
        row = self.table_result.currentRow()
        new_dir = self.table_result.item(row, 4).text()
        self.view.get_main_widget().image_loaded.show_image(new_dir)

        _format = self.table_result.item(row, 3).text()
        path_downloaded = self.table_result.item(row, 5).text()
        self.view.get_main_widget().result.show_image(path_downloaded)

    def popWindowML(self):
        self.view.pop_window_machine()

    def popWindowConvert(self):
        self.view.pop_window_convert()
