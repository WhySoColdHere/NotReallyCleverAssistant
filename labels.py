from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class Label:
    def __init__(self, q_main_window):
        # В качестве q_main_window будет выступать self из interface так как self будет являться ссылкой на QWainWindow
        self._q_main_window = q_main_window

        # Здесь происходит инициализация переменных для лэйблов
        self._main_label = None

    def main_label_func(self):
        self._main_label = QLabel(self._q_main_window)
        self._main_label.setFont(QFont("Comic Sans MS", 20))
        self._main_label.move(250, 50)
        self._main_label.setFixedWidth(500)
        self._main_label.setFixedHeight(100)
        self._main_label.setText("*List of commands*")

