from src.view.machine_learning.ml_object_view import MLObjectView


class MLObjectController:
    def __init__(self):
        self.view = MLObjectView()
        self.view.init_ui()
