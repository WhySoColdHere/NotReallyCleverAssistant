from codecs import open
import speech_recognition
import webbrowser as wb
from speech import Speech


class Start:
    def __init__(self):
        self.sr = speech_recognition.Recognizer()
        self.sr.pause_threshold = 1  # Максимальная пауза между словами

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
            Speech("Your command is not recognizable").speech_text_process()

    def listen_command(self):
        try:
            with speech_recognition.Microphone() as mic:
                self.sr.adjust_for_ambient_noise(mic, 0.5)  # Регулировка шума
                audio = self.sr.listen(mic)
                self.query = self.sr.recognize_google(audio, language='ru-RU').lower()
                return self.query
        except speech_recognition.UnknownValueError:
            Speech("Something goes wrong. Tap speak to continue").speech_text_process()
            print(self.query)
            exit()

    ##### Доп. функции #####
    def tasks(self):
        Speech("What do you want to add to todo list?").speech_text_process()
        self.query = self.listen_command()

        # open - не python функция, а codecs.open() - необходима для записи русских слов в файл
        with open("todo.txt", 'a', "utf-8") as file:
            file.write(f"{self.query}\n")

        Speech("Your task has added in your todo list").speech_text_process()
        return 'tasks'

    def find_in_the_internet(self):
        Speech("What you want to search?").speech_text_process()
        self.query = self.listen_command()

        wb.open(f"https://yandex.ru/search/?text={self.query}")
        return 'find_in_the_internet'

    @staticmethod
    def greeting():
        Speech("Hello").speech_text_process()
        return ''

    @staticmethod
    def close_program():
        Speech("Good bye!").speech_text_process()
        print("End")
        exit()

    def start_program(self):
        while True:
            self.main()

