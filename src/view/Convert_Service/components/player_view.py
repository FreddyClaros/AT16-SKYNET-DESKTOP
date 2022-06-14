from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtWidgets import QApplication, QStyle
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QPushButton
import sys


class PlayerView(QWidget):
    def __init__(self):
        super().__init__()

    def init_ui(self, path):
        self.layout = QHBoxLayout()
        self.play_btn = QPushButton()
        self.pause_btn = QPushButton()
        self.stop_btn = QPushButton()
        self.layout.addWidget(self.play_btn)
        self.layout.addWidget(self.pause_btn)
        self.layout.addWidget(self.stop_btn)
        self.setLayout(self.layout)
        self.player = QMediaPlayer()
        self.player.setMedia(QMediaContent(QUrl.fromLocalFile(path)))
        icon_play = self.style().standardIcon(getattr(QStyle, "SP_MediaPlay"))
        self.play_btn.setIcon(icon_play)
        icon_pause = self.style().standardIcon(getattr(QStyle, "SP_MediaPause"))
        self.pause_btn.setIcon(icon_pause)
        icon_stop = self.style().standardIcon(getattr(QStyle, "SP_MediaStop"))
        self.stop_btn.setIcon(icon_stop)
        self.show()

    def play_it(self):
        self.player.play()

    def pause_it(self):
        self.player.pause()

    def stop_it(self):
        self.player.stop()




