from pygame import mixer, error
from os import listdir
from random import choice
from codecs import open
import speech_recognition
import webbrowser as wb
from speech import speech_text


class Start:
    def __init__(self):
        self.sr = speech_recognition.Recognizer()
        self.sr.pause_threshold = 1

        # Переменная, хранящая обработанный текст
        self.query = ''
        # Переменная для хранения команд (Ее возвращает функция commands_dict и использует main)
        self.commands_dict_init = {}

    ##### Технические функции #####

    def commands_dict(self):
        self.commands_dict_init = {
            "commands": {
                ### <ПРИВЕТСТВИЕ> ###
                self.greeting: ["привет", "здравствуй", "включайся"],
                ### <ЛИСТ С ЗАДАЧАМИ> ###
                self.tasks: ["добавить задачу", "открыть записную книжку", "добавь задачу"],
                ### <МУЗЫКА> ###
                self.play_music: ["включи музло", "включи музыку"],
                self.stop_music: ["выключи музло", "выключи музыку", "останови музыку"],
                ### <ПОИСК В БРАУЗЕРЕ> ###
                self.find_in_the_internet: ["найти", "поиск"],
                ### ЗАКРЫТИЕ ПРОГРАММЫ ###
                self.close_program: ["заканчивай", "прощай", "пока"]
            }
        }
        return self.commands_dict_init

    def main(self):
        self.query = self.listen_command()
        counter = 0
        for command, cur_command in self.commands_dict()["commands"].items():
            if self.query in cur_command:
                print(command())
            else:
                counter += 1
        if counter == 6:  # Если добавляешь новую функцию с заданием, то инкриментируй число
            speech_text("Your command is not recognizable")

    def listen_command(self):
        try:
            with speech_recognition.Microphone() as mic:
                self.sr.adjust_for_ambient_noise(mic, 0.5)
                audio = self.sr.listen(mic)
                self.query = self.sr.recognize_google(audio, language='ru-RU').lower()
                return self.query
        except speech_recognition.UnknownValueError:
            return True

    ##### Доп. функции #####
    def tasks(self):
        speech_text("Hello, what do you want to add to todo list?")

        self.query = self.listen_command()

        # open - не python функция, а codecs.open() - необходима для записи русских слов в файл
        with open("todo.txt", 'a', "utf-8") as file:
            file.write(f"{self.query}\n")

        speech_text(f"Your task has added in your todo list")
        return ''

    def find_in_the_internet(self):
        speech_text("Hello, what you want to search?")
        self.query = self.listen_command()

        wb.open(f"https://yandex.ru/search/?text={self.query}")
        return ''

    # Функция включает или выключает музыку, в зависимости от запроса.
    def _music_mode(self, mode):
        try:
            mixer.init()
            mixer.music.load(fr"music\{choice(listdir('music'))}")
            mode()
        except error:
            speech_text("Ops, you get an error. Be proud! And.. try again")
        finally:
            self.query = self.listen_command()

    def play_music(self):
        speech_text("Dancing guys, dancing!")
        self._music_mode(mixer.music.play)  # Не забывай убирать скобки
        return ''

    def stop_music(self):
        self._music_mode(mixer.music.stop)
        speech_text("Music is stopped!")
        return ''

    @staticmethod
    def greeting():
        speech_text("Hello")
        return ''

    @staticmethod
    def close_program():
        speech_text("Good bye!")
        print("End")
        exit()

    def start_program(self):
        while True:
            self.main()