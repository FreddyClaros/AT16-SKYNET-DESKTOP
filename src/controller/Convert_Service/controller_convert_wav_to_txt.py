#
# controller_convert_wav_to_txt.py Copyright (c) 2022 Jalasoft.
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


from src.view.Convert_Service.convert_wav_to_txt_view import ConvertWavToTxtView


class ConvertControllerWavToTxt:
    def __init__(self):
        self.view = ConvertWavToTxtView()
        self.view.init_ui()
