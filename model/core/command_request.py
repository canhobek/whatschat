from model.core.operators import Operators
import pickle

class ComandRequest():
    def __init__(self, command: Operators, t1: tuple):
        self._command = command
        self._data = t1

    def encode(self):
        f = open("tmp.bin", "wb")
        pickle.dump(self, f)
        return f

    @staticmethod
    def decode(self, f):
        return pickle.load(f)

    @property
    def command(self):
        return self._command

    @property
    def data(self):
        return self._data




