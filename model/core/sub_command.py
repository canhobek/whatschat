from model.core.calulation import Calculation


class SubCommand(Calculation):
    def __init__(self, *args):
        super().__init__(*args)


    def calculate(self):
        result = self._args[0]
        for i in self._args[1:]:
            result -= i

        return result

