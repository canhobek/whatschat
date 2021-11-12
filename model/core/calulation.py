from model.core.operators import Operators
import pickle


class Calculation:
    def __init__(self, operator:Operators, operant1, operant2):
        self._operator = operator
        self._operant1 = operant1
        self._operant2 = operant2

    def encode(self):
        byte_obj = b''
        pickle.dump(self, byte_obj)
        return byte_obj

    def decode(self):
        return pickle.load(self)


    def calculate(self):
        """
        returns calculated value operator bağlı olarak
        :return:
        """
