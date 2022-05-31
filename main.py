#
# main.py Copyright (c) 2022 Jalasoft.
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

# Press the green button in the gutter to run the script.

import sys
from PyQt5.QtWidgets import QApplication
from src.controller.Convert_Service.controller_convert_audio import ConvertControllerAudio
from src.controller.Convert_Service.controller_convert_image import ConvertControllerImage
from src.controller.Convert_Service.controller_convert_ocr import ConvertControllerOCR
from src.controller.Convert_Service.controller_convert_translator import ConvertControllerTranslator
from src.controller.Convert_Service.controller_convert_video import ConvertControllerVideo
from src.controller.Convert_Service.controller_convert_metadata import ConvertControllerMetadata
from src.controller.Convert_Service.controller_convert_wav_to_txt import ConvertControllerWavToTxt
from src.controller.machine_learning_service.controller_ml_object import MLObjectController
from src.controller.machine_learning_service.controller_ml_face import MLFaceController
from src.controller.machine_learning_service.controller_ml_search_iris import MLSearchIrisController
from src.controller.machine_learning_service.controller_ml_train_iris import MLTrainIrisController
from src.controller.machine_learning_service.controller_ml_emotion import MLEmotionController
from src.view.main.main_window import MainWindow
if __name__ == "__main__":
    app = QApplication(sys.argv)
    #controller = ConvertControllerAudio()
    #controller = ConvertControllerImage()
    #controller = ConvertControllerOCR()
    #controller = ConvertControllerTranslator()
    #controller = ConvertControllerVideo()
    #controller = ConvertControllerMetadata()
    #controller = ConvertControllerWavToTxt()
    # controller = MLObjectController()
    # controller = MLFaceController()
    # controller = MLSearchIrisController()
    # controller = MLTrainIrisController()
    # controller = MLEmotionController()
    controller = MainWindow()
    controller.show()
    sys.exit(app.exec())
