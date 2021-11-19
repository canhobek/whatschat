from model.core.calulation import Calculation


class AddCommand(Calculation):
    def __init__(self, *args):
        super().__init__(*args)

    def calculate(self):
        a = self._args[0]
        return sum(self._args)

