#!/usr/bin/env python
#coding=UTF-8
from bunia.api import Command, Argument, Flag, Integer, ChoiceArgument

class AddTwo(Command):
    NAME = 'add_two'
    DESCRIPTION = u'Squares an integer. Or something else'
    ARGUMENTS=[
        Integer('n', description=u'Number to square'),
        Flag('sqrt', description=u'Do square root instead'),
        ChoiceArgument('wtf', [('a', 'A'), ('b', 'B')])
    ]

    def run(self, runner, n, wtf, sqrt=False):
        print wtf
        console = runner.new_console()
        if sqrt:
            import math
            console.text(math.sqrt(n))
        else:
            console.text(n**2)


COMMAND = AddTwo
if __name__ == '__main__':
    COMMAND().run_using_main()
