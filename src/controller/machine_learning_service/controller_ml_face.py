from src.view.machine_learning.ml_face_view import MLFaceView


class MLFaceController:
    def __init__(self):
        self.view = MLFaceView()
        self.view.init_ui()
