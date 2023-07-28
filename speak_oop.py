from playsound import playsound
from os import listdir
from random import choice
from codecs import open
import speech_recognition
import webbrowser as wb


class Start:
    def __init__(self):
        self.query = str
        self.commands_dict_init = dict
        self.sr = speech_recognition.Recognizer()
        self.sr.pause_threshold = 1

    ##### Технические функции #####
    def main(self):
        self.query = self.listen_command()
        counter = 0
        for command, cur_command in self.commands_dict()["commands"].items():
            if self.query in cur_command:
                print(command())
            else:
                counter += 1
        if counter == 4:  # Если добавляешь новую функцию с заданием, то инкриментируй число
            print("Your command is not recognizable")

    def commands_dict(self):
        self.commands_dict_init = {
            "commands": {
                self.greeting: ["привет", "здравствуй", "включайся сука"],
                self.tasks: ["добавить задачу", "открыть записную книжку", "добавь задачу"],
                self.play_music: ["включи музло", "включи музыку"],
                self.find_in_the_internet: ["найти", "поиск"]
            }
        }
        return self.commands_dict_init

    def listen_command(self):
        try:
            with speech_recognition.Microphone() as mic:
                self.sr.adjust_for_ambient_noise(mic, 0.5)
                audio = self.sr.listen(mic)
                self.query = self.sr.recognize_google(audio, language='ru-RU').lower()
                return self.query
        except speech_recognition.UnknownValueError:
            return "Something went wrong.. try again later little slut!"

    ##### Доп. функции #####
    def tasks(self):
        print("Hello, what do u wanna add to todo list?")

        self.query = self.listen_command()

        with open("todo.txt", 'a', "utf-8") as file:
            file.write(f"{self.query}\n")

        return f"Task '{self.query}' has added in your todo list"

    def find_in_the_internet(self):
        print("Hello, what you want to search?")
        self.query = self.listen_command()

        wb.open(f"https://yandex.ru/search/?text={self.query}")

    def play_music(self):
        playsound(fr"music\{choice(listdir('music'))}")
        self.query = self.listen_command()
        return "Dancing guys, dancing!"

    @staticmethod
    def greeting():
        return "Hello stutii peace of shit!"

    def start_program(self):
        while True:
            self.main()
