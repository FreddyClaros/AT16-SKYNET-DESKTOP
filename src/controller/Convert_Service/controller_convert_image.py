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
import requests

class ConvertControllerImage:
    def __init__(self):
        self.view = ConvertImageView()
        self.view.init_ui()
        self.view.main_widget.get_convert_button().clicked.connect(self.show_result)
        self.view.get_main_widget().get_layout().get_button_menu_ml().clicked.connect(self.popWindowML)
        self.view.get_main_widget().get_layout().get_button_menu_convert().clicked.connect(self.popWindowConvert)
    
    def popWindowML(self):
        self.view.pop_window_machine()
    
    def popWindowConvert(self):
        self.view.pop_window_convert()


    def show_result(self):
        url = "http://127.0.0.1:5000/convert"
        file_path = self.view.main_widget.get_file_path()
        file = {'file': open(file_path, 'rb')}
        convert = self.view.main_widget.get_list_convert()
        color = self.view.main_widget.get_color()
        height = self.view.main_widget.get_height()
        width = self.view.main_widget.get_width()
        formato = self.view.main_widget.get_output_format()
        rotate = self.view.main_widget.get_degrees()
        flip_vert = self.view.main_widget.get_vertical_flip()
        flip_hor = self.view.main_widget.get_horizontal_flip()
        payload = {'color': color, 'rotate': rotate, 'height': height, 'width': width, 'format': formato,
                   'convert': convert, 'vertical_flip': flip_vert, 'horizontal_flip': flip_hor}
        response = requests.post(url, files=file, data=payload, verify=False)
        print(response)
        resp = response.json()
        message = resp['message']
        url = message
        name_fyle = url.split('/')
        myfile = requests.get(url)
        folder = 'Download/'+name_fyle[-1]
        open(folder, 'wb').write(myfile.content)
        self.view.main_widget.set_result(folder)
