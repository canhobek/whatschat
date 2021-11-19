from model.core.command_request import ComandRequest
from model.core.operators import Operators as O
from model.core.add_command import AddCommand
from model.core.sub_command import SubCommand
from model.core.exit_command import ExitCommand

class CommandHandler():
    command_dict = {O.ADD: AddCommand, O.SUB: SubCommand, O.EXIT: ExitCommand}
    def __init__(self):
        pass

    def execute_command(self, request):
        com = request.command
        which_command = CommandHandler.command_dict[com]
        return which_command(*request.data).calculate()




