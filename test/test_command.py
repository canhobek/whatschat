import unittest
from model.core.add_command import AddCommand
from model.core.sub_command import SubCommand


class MyTestCase(unittest.TestCase):
    def test_add_command(self):
        addcommand = AddCommand(1, 2, 3)
        self.assertEqual(6, addcommand.calculate())

    def test_sub_command(self):
        subcommand = SubCommand(1, 2, 3)
        self.assertEqual(-4, subcommand.calculate())




if __name__ == '__main__':
    unittest.main()
