from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QFont


class Label:
    def __init__(self, q_main_window):
        # В качестве q_main_window будет выступать self из interface так как self будет являться ссылкой на QWainWindow
        self.q_main_window = q_main_window

        # Здесь происходит инициализация переменных для лэйблов
        self.main_label = None

    def main_label_func(self):
        self.main_label = QLabel(self.q_main_window)
        self.main_label.setFont(QFont("Comic Sans MS", 20))
        self.main_label.move(250, 50)
        self.main_label.setFixedWidth(500)
        self.main_label.setFixedHeight(100)
        self.main_label.setText("*List of commands*")

