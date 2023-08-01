import pyttsx3
from multiprocessing import Process


class Speech:
    def __init__(self, text):
        self.text = text

    def speech_text_process(self):
        Process(target=self._engine_init).start()

    def _engine_init(self):
        engine = pyttsx3.init()
        engine.say(self.text)
        engine.runAndWait()
