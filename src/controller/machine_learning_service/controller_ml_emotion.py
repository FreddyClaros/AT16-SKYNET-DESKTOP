from src.view.machine_learning.ml_emotion_view import MLEmotionView


class MLEmotionController:
    def __init__(self):
        self.view = MLEmotionView()
        self.view.init_ui()
