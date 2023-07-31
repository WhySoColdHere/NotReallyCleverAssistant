import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel
from PyQt5.QtGui import QFont
from speaker import Start, wb
from threading import Thread


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My window!")
        self.setGeometry(610, 400, 600, 600)

        self._btn_start_speak = None
        self.btn_start_speak_func()

        self._btn_about_author = None
        self.btn_about_author_func()

        self.main_label = None
        self.main_label_func()

    ##### BUTTONS #####
    ##### button #####
    def btn_start_speak_func(self):
        self._btn_start_speak = QPushButton(self)
        self._btn_start_speak.move(230, 250)
        self._btn_start_speak.setFixedWidth(150)
        self._btn_start_speak.setText("Speak")
        self._btn_start_speak.clicked.connect(self._btn_start_speak_func_clicked)  # Не забывай убирать скобки

    @staticmethod
    def _btn_start_speak_func_clicked():
        print("Speak..")
        Thread(target=Start().start_program).start()

    ##### button #####
    def btn_about_author_func(self):
        self._btn_about_author = QPushButton(self)
        self._btn_about_author.move(205, 222)
        self._btn_about_author.setFixedWidth(200)
        self._btn_about_author.setText("Push me to check out my github!")
        self._btn_about_author.clicked.connect(self._btn_about_author_func_clicked)

    @staticmethod
    def _btn_about_author_func_clicked():
        wb.open("https://github.com/WhySoColdHere")

    ##### LABELS #####
    ##### label #####
    def main_label_func(self):
        self.main_label = QLabel(self)
        self.main_label.setFont(QFont("Comic Sans MS", 20))
        self.main_label.move(250, 50)
        self.main_label.setFixedWidth(500)
        self.main_label.setFixedHeight(100)
        self.main_label.setText("Hello")


def application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
