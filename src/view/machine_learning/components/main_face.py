import os
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, \
                            QPushButton, QComboBox, QSpacerItem, QSizePolicy, QFileDialog
from src.view.machine_learning.components.title import Title
from src.view.machine_learning.components.buttons_top import ButtonsTop


class MainFaceWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.style = os.getcwd() + "/resources/compiler.css"
        self.setStyleSheet(open(self.style).read())
        self.layout = QVBoxLayout()
        self.layout.addLayout(ButtonsTop())
        self.layout.addWidget(Title())
        self.layout.addLayout(self.get_layout_body(), 20)
        self.setLayout(self.layout)

    def get_layout_body(self):

        body = QHBoxLayout()
        body.addLayout(self.left_layout(self), 15)
        body.addLayout(self.right_layout(self), 65)
        return body

    @staticmethod
    def right_layout(self):

        show_button = QPushButton("Show Image")
        right = QVBoxLayout()
        right.addWidget(QPlainTextEdit(), 65)
        right.addWidget(show_button)
        return right

    @staticmethod
    def left_layout(self):
        list_machine_learning = QComboBox()
        list_machine_learning.addItem("Face Recognizer")
        list_machine_learning.addItem("Object Recognizer")
        list_machine_learning.addItem("Iris Recognizer search")
        list_machine_learning.addItem("Iris Recognizer train")
        list_machine_learning.addItem("Emotion Recognizer")

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)
        self.file_path_bottom = QLineEdit()
        self.file_path_bottom.setReadOnly(True)

        browse_button_top = QPushButton("Browse")
        browse_button_bottom = QPushButton("Browse")
        browse_button_top.clicked.connect(self.browse_file)
        browse_button_bottom.clicked.connect(self.browse_file_second)
        search_button = QPushButton("Search")

        models = QComboBox()
        models.addItem("VggFace")
        models.addItem("InceptionV3")
        models.addItem("Vgg16")


        vertical_spacer = QSpacerItem(10, 700, QSizePolicy.Expanding)

        menu = QVBoxLayout()
        menu.addWidget(QLabel("Search by:"))
        menu.addWidget(list_machine_learning)
        menu.addWidget(QLabel("Video Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button_top)
        menu.addWidget(QLabel("Person to Search:"))
        menu.addWidget(self.file_path_bottom)
        menu.addWidget(browse_button_bottom)

        menu.addWidget(QLabel("Neuronal Network Model:"))
        menu.addWidget(models)
        menu.addWidget(search_button)
        menu.addSpacerItem(vertical_spacer)
        menu.addWidget(QLabel("Message:"))
        menu.addWidget(QPlainTextEdit())
        return menu

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])

    def browse_file_second(self):
        file_name_bottom = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path_bottom.setText(file_name_bottom[0])
