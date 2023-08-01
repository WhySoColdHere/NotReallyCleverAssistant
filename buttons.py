from PyQt5 import QtWidgets
from speaker import Start, wb
from threading import Thread


class Button:
    def __init__(self, q_main_window):
        # В качестве q_main_window будет выступать self из interface так как self будет являться ссылкой на QWainWindow
        self.q_main_window = q_main_window

        # Здесь происходит инициализация переменных для кнопок
        self._btn_start_speak = None
        self._btn_about_author = None

    ##### BUTTON #####
    def btn_start_speak_func(self):
        self._btn_start_speak = QtWidgets.QPushButton(self.q_main_window)
        self._btn_start_speak.move(230, 250)
        self._btn_start_speak.setFixedWidth(150)
        self._btn_start_speak.setText("Speak")
        self._btn_start_speak.clicked.connect(self._btn_start_speak_func_clicked)  # Не забывай убирать скобки

    @staticmethod
    def _btn_start_speak_func_clicked():
        print("Speak..")
        Thread(target=Start().start_program).start()

    ##### BUTTON #####
    def btn_about_author_func(self):
        self._btn_about_author = QtWidgets.QPushButton(self.q_main_window)
        self._btn_about_author.move(205, 222)
        self._btn_about_author.setFixedWidth(200)
        self._btn_about_author.setText("Push me to check out my github!")
        self._btn_about_author.clicked.connect(self._btn_about_author_func_clicked)

    @staticmethod
    def _btn_about_author_func_clicked():
        wb.open("https://github.com/WhySoColdHere")
