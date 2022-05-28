#
# machine_learning_view.py Copyright (c) 2022 Jalasoft.
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

from PyQt5.QtWidgets import QMainWindow
from src.view.main.label import Label
from src.view.main.button import Button
from src.view.main.combobox import ComboBox
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QVBoxLayout
from PyQt5.QtWidgets import QHBoxLayout


class MachineLearningObject(QMainWindow):
    def __init__(self):
        super(MachineLearningObject, self).__init__()
        self.object_window()

    def object_window(self):
        self.setWindowTitle("AT16 Skynet project")
        self.setGeometry(20, 50, 1000, 750)
        # menu items
        model_list = ['Vgg16', 'InceptionV3', 'Resnet']
        percentage_list = ['0%', '10%', '20%', '30%', '40%', '50%', '60%', '70%', '80%', '90%']
        label_video = Label().sub_label("Video Path:")
        label_word = Label().sub_label("Word:")
        label_model = Label().sub_label("Neuronal network Model")
        #label_spacing = Label().sub_label("")
        label_percentage = Label().sub_label("Percentage")
        browse_button = Button().action_button("Browser")
        search_button = Button().action_button("Search")
        image_button = Button().action_button("Show Image")
        combobox_model = ComboBox().basic_combobox(model_list)
        combobox_percentage = ComboBox().basic_combobox(percentage_list)
        label_message = Label().sub_label("Message")
        # layouts
        background_layout = QHBoxLayout()
        menu_layout = QVBoxLayout()
        result_layout = QVBoxLayout()
        message_layout = QVBoxLayout()
        #charge layouts
        menu_layout.addWidget(label_video)
        menu_layout.addWidget(browse_button)
        menu_layout.addWidget(label_word)
        menu_layout.addWidget(label_model)
        menu_layout.addWidget(combobox_model)
        menu_layout.addWidget(label_percentage)
        menu_layout.addWidget(combobox_percentage)
        menu_layout.addWidget(search_button)
        message_layout.addWidget(label_message)
        menu_layout.addLayout(message_layout)
        result_layout.addWidget(image_button)

        background_layout.addLayout(menu_layout)
        background_layout.addLayout(result_layout)


        #layout = Layout().layout_vertical()
        #layout.addWidget(label_spacing)

        widget = QWidget()
        widget.setLayout(background_layout)
        self.setCentralWidget(widget)
