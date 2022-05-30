from src.view.machine_learning.ml_train_iris_view import MLTrainIrisView


class MLTrainIrisController:
    def __init__(self):
        self.view = MLTrainIrisView()
        self.view.init_ui()
