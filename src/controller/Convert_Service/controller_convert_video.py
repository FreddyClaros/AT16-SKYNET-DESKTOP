#
# controller_convert_video.py Copyright (c) 2022 Jalasoft.
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


from src.view.Convert_Service.convert_video_view import ConvertVideoView


class ConvertControllerVideo:
    def __init__(self):
        self.view = ConvertVideoView()
        self.view.init_ui()
        self.view.get_main_widget().get_layout().get_button_menu_ml().clicked.connect(self.popWindowML)
        self.view.get_main_widget().get_layout().get_button_menu_convert().clicked.connect(self.popWindowConvert)
    
    def popWindowML(self):
        self.view.pop_window_machine()
    
    def popWindowConvert(self):
        self.view.pop_window_convert()
