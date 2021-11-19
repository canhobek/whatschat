from model.core.operators import Operators
import pickle

class ComandRequest():
    def __init__(self, command: Operators, t1: tuple):
        self._command = command
        self._data = t1

    def encode(self):
        obj = object()
        pickle.dump(self, obj)
        return obj


    def decode(self):
        return pickle.load(self)

    @property
    def command(self):
        return self._command

    @property
    def data(self):
        return self._data

