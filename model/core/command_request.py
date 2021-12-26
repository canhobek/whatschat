from model.core.operators import Operators
import pickle


class CommandRequest():
    def __init__(self, command: Operators, t1: tuple):
        self._command = command
        self._data = t1

    def encode(self):
        # f = open("tmp.bin", "wb")
        return pickle.dumps(self)
        # return f

    @staticmethod
    def decode(bytes):
        return pickle.loads(bytes, encoding="utf8")

    @property
    def command(self):
        return self._command

    @property
    def data(self):
        return self._data
