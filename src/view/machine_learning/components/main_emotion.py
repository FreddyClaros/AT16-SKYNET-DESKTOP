from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPlainTextEdit, QLabel, QLineEdit, \
                            QPushButton, QComboBox, QSpacerItem, QSizePolicy, QFileDialog
from src.view.machine_learning.components.title import Title
from src.view.machine_learning.components.buttons_top import ButtonsTop


class MainEmotionWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout()
        self.layout.addLayout(ButtonsTop())
        self.layout.addWidget(Title())
        self.layout.addLayout(self.get_layout_body(), 10)
        self.setLayout(self.layout)

    def get_layout_body(self):

        body = QHBoxLayout()
        body.addLayout(self.left_layout(self), 10)
        body.addLayout(self.right_layout(self), 65)
        return body

    @staticmethod
    def right_layout(self):

        show_button = QPushButton("Show Image")
        right = QVBoxLayout()
        right.addWidget(QPlainTextEdit(), 75)
        right.addWidget(show_button)
        return right

    @staticmethod
    def left_layout(self):
        list_machine_learning = QComboBox()
        list_machine_learning.addItem("Object Recognizer")
        list_machine_learning.addItem("Face Recognizer")
        list_machine_learning.addItem("Iris Recognizer search")
        list_machine_learning.addItem("Iris Recognizer train")
        list_machine_learning.addItem("Emotion Recognizer")

        self.file_path = QLineEdit()
        self.file_path.setReadOnly(True)

        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.browse_file)
        search_button = QPushButton("Search")

        models = QComboBox()
        models.addItem("Vgg16")
        models.addItem("InceptionV3")

        percentage = QComboBox()
        percentage.addItem("0%")
        percentage.addItem("10%")
        percentage.addItem("20%")
        percentage.addItem("30%")
        percentage.addItem("40%")
        percentage.addItem("50%")
        percentage.addItem("60%")
        percentage.addItem("70%")
        percentage.addItem("80%")
        percentage.addItem("90%")
        percentage.addItem("100%")

        vertical_spacer = QSpacerItem(10, 700, QSizePolicy.Expanding)

        menu = QVBoxLayout()
        menu.addWidget(QLabel("Search by:"))
        menu.addWidget(list_machine_learning)
        menu.addWidget(QLabel("Video Path:"))
        menu.addWidget(self.file_path)
        menu.addWidget(browse_button)
        menu.addWidget(QLabel("Word:"))
        menu.addWidget(QLineEdit())
        menu.addWidget(QLabel("Neuronal Network Model:"))
        menu.addWidget(models)
        menu.addWidget(QLabel("Percentage:"))
        menu.addWidget(percentage)
        menu.addWidget(search_button)
        menu.addSpacerItem(vertical_spacer)
        menu.addWidget(QLabel("Message:"))
        menu.addWidget(QPlainTextEdit())
        return menu

    def browse_file(self):
        file_name = QFileDialog.getOpenFileName(self, 'Open file', 'D:\\', '')
        self.file_path.setText(file_name[0])
