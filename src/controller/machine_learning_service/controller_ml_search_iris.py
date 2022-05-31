from src.view.machine_learning.ml_search_iris_view import MLSearchIrisView


class MLSearchIrisController:
    def __init__(self):
        self.view = MLSearchIrisView()
        self.view.init_ui()
