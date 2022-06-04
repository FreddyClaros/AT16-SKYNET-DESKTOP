from src.view.main.ml_menu_view import MLMenuView


class ControllerMLMenu:
    def __init__(self):
        self.view = MLMenuView()
        self.view.init_ui()
        self.view.get_main_widget().get_button_emotion().clicked.connect(self.view.go_to_emotion)
        self.view.get_main_widget().get_button_object().clicked.connect(self.view.go_to_object)
        self.view.get_main_widget().get_button_face().clicked.connect(self.view.go_to_face)
        self.view.get_main_widget().get_button_iris_search().clicked.connect(self.view.go_to_search_iris)
        self.view.get_main_widget().get_button_iris_train().clicked.connect(self.view.go_to_train_iris)
       