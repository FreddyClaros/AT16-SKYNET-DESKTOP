from PyQt5.QtWidgets import QPushButton, QHBoxLayout


class ButtonsTop(QHBoxLayout):
    def __init__(self):
        super().__init__()
        self.create_buttons()

    def create_buttons(self):
        booking_button = QPushButton("Booking")
        converter_button = QPushButton("Converter")
        machine_learning_button = QPushButton("Machine Learning")
        reporting_button = QPushButton("Reporting")

        self.addWidget(booking_button)
        self.addWidget(converter_button)
        self.addWidget(machine_learning_button)
        self.addWidget(reporting_button)




