import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from buttons import Button


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle("My window!")
        self.setGeometry(610, 400, 600, 600)

        self.buttons_init()

    # Инициализатор кнопок
    def buttons_init(self):
        Button(self).btn_start_speak_func()


def application():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()
