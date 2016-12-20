#coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest
import io


from bunia.runner import ConsoleRunner
from bunia.api import Command

class TestConsole(unittest.TestCase):

    def test_bug_consolerunner_has_no_stdout(self):

        class Cmd(Command):
            def run(self, runner):
                con = runner.new_console()
                con.text(u'lol')

        stdout = io.StringIO()

        cr = ConsoleRunner()
        cr.run(Cmd(), '', stdout=stdout)