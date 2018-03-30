# coding=UTF-8
from __future__ import absolute_import, division, print_function

import random

from bunia.api import Command, Integer


class AddTwoNumbers(Command):
    NAME = 'add_two_numbers'
    DESCRIPTION = 'adds two numbers'
    ARGUMENTS = [Integer('a'), Integer('b')]

    def run(self, runner, a, b):
        con = runner.new_console()
        con.text('%s+%s=%s', a, b, a+b)


class ConsoleClusterfuck(Command):
    NAME = 'op_two_numbers'
    DESCRIPTION = 'ops two numbers'
    ARGUMENTS = [Integer('a'), Integer('b')]

    def run(self, runner, a, b):
        con = runner.new_console()
        con.text('%s+%s=%s', a, b, a+b)

        con2 = runner.new_console('con2')
        con.text('%s*%s=%s', a, b, a*b)

        con3 = runner.new_console('con3')
        con.text('%s-%s=%s', a, b, a-b)


class LoremIpsum(Command):
    NAME = 'lorem_ipsum'
    DESCRIPTION = 'Return few sentences of Lorem Ipsum'

    def run(self, runner, **kwargs):
        con = runner.new_console()
        lipsum = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel elit finibus, pharetra enim vel, accumsan urna.'

        con.write(lipsum.encode('ascii'))
