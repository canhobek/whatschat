from model.core.operators import Operators
import pickle
from abc import ABC, abstractmethod


class Calculation(ABC):
    def __init__(self, *args):
        self._args = args

    @abstractmethod
    def calculate(self):
        """
        returns calculated value operator bağlı olarak
        :return:
        """
