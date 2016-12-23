# coding=UTF-8
from __future__ import absolute_import, division, print_function

from bunia.api import Command

class Cmd1(Command):
    NAME = 'cmd1'

class Cmd2(Command):
    NAME = 'cmd2'

COMMAND = Cmd1
