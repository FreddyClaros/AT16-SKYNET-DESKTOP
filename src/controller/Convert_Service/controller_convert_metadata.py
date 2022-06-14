#
# controller_convert_metadata.py Copyright (c) 2022 Jalasoft.
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


from src.view.Convert_Service.convert_metadata_view import ConvertMetadataView
import requests
import os

class ConvertControllerMetadata:

    def __init__(self):
        self.view = ConvertMetadataView()
        self.view.init_ui()
        self.view.main_widget.get_convert_button().clicked.connect(self.show_result)
        self.view.main_widget.get_editor_text().appendPlainText("hola")
        self.view.main_widget.get_table().cellClicked.connect(self.file_open)

    def show_result(self):
        url = "http://127.0.0.1:6008/convert"
        file_path = self.view.main_widget.get_file_path()
        file = {'file': open(file_path, 'rb')}
        convert = self.view.main_widget.get_list_convert()
        formato = self.view.main_widget.get_output_format()
        payload = {'format': formato, 'convert': convert}
        response = requests.post(url, files=file, data=payload, verify=False)
        resp = response.json()
        message = resp['message']
        status = str(resp['status'])
        url = message
        name_fyle = url.split('/')
        my_file = requests.get(url)
        folder = 'Download/'+name_fyle[-1]
        simp_path = folder
        self.abs_path = os.path.abspath(simp_path)
        open(self.abs_path, 'wb').write(my_file.content)
        print(message)
        self.view.main_widget.add_values_table(message, formato, status, '', self.abs_path)

    def file_open(self):
        row = self.view.main_widget.get_table().currentRow()
        new_dir = self.view.main_widget.get_table().item(row, 4).text()
        with open(new_dir, "r") as f:
            text = f.read()
        self.view.main_widget.get_editor_text().setPlainText(text)
        self.view.get_main_widget().get_layout().get_button_menu_ml().clicked.connect(self.popWindowML)
        self.view.get_main_widget().get_layout().get_button_menu_convert().clicked.connect(self.popWindowConvert)
    
    def popWindowML(self):
        self.view.pop_window_machine()
    
    def popWindowConvert(self):
        self.view.pop_window_convert()
