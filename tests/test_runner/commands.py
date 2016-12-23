# coding=UTF-8
from __future__ import absolute_import, division, print_function

from bunia.api import Command, Integer


class AddTwoNumbers(Command):
    NAME = 'add_two_numbers'
    DESCRIPTION = 'adds two numbers'
    ARGUMENTS = [Integer('a'), Integer('b')]

    def run(self, runner, a, b):
        con = runner.new_console()
        con.text('%s+%s=%s', a, b, a+b)