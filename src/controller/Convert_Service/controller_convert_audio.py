from src.view.Convert_Service.convert_audio_view import ConvertAudioView


class ConvertControllerAudio:
    def __init__(self):
        self.view = ConvertAudioView()
        self.view.init_ui()
