"""
Place all StGeorge commands here. Classes must be "seeable" by importing this module.
"""

from bunia.api import Command, Argument
import sys


class AddTwo(Command):
    NAME = 'add_two'
    DESCRIPTION = u'Squares a number'
    ARGUMENTS=[
        Argument('n', 'x', description=u'Number to square')
    ]

    def run(self, runner, x):
        console = runner.new_console()
        console.text(int(x)**2)

COMMAND = AddTwo

