from PyQt5 import QtWidgets
from speak_oop import Start


class Button:
    def __init__(self, q_main_window):
        # В качестве q_main_window будет выступать self из interface так как self будет являться ссылкой на QWainWindow
        self.q_main_window = q_main_window

        # Здесь происходит инициализация переменных для кнопок
        self._btn_start_speak = None

    ##### BUTTON #####
    def btn_start_speak_func(self):
        self._btn_start_speak = QtWidgets.QPushButton(self.q_main_window)
        self._btn_start_speak.move(230, 250)
        self._btn_start_speak.setFixedWidth(150)
        self._btn_start_speak.setText("Push me to speak")
        self._btn_start_speak.clicked.connect(self._btn_start_speak_func_clicked)  # Не забывай убирать скобки

    @staticmethod
    def _btn_start_speak_func_clicked():
        print("Speak..")
        Start().start_program()

    ##### BUTTON #####

