#!/usr/bin/env python
#coding=UTF-8
from bunia.api import Command, Argument, Flag, Integer

class AddTwo(Command):
    NAME = 'add_two'
    DESCRIPTION = u'Squares an integer. Or something else'
    ARGUMENTS=[
        Integer('n', description=u'Number to square'),
        Flag('sqrt', description=u'Do square root instead')
    ]

    def run(self, runner, n, sqrt=False):
        console = runner.new_console()
        if sqrt:
            import math
            console.text(math.sqrt(n))
        else:
            console.text(n**2)


COMMAND = AddTwo
if __name__ == '__main__':
    COMMAND.run_using_main()
