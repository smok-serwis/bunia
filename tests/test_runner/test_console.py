# coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest
import io


from bunia.runner import ConsoleRunner
from bunia.api import Command

from tests.test_runner.commands import AddTwoNumbers

class TestConsole(unittest.TestCase):

    def test_runs(self):
        cr = ConsoleRunner()
        cr.run(AddTwoNumbers(), ['2', '3'])

    def test_runs_and_outputs(self):
        out = io.StringIO()
        cr = ConsoleRunner()
        cr.run(AddTwoNumbers(), ['2', '3'], stdout=out)
        self.assertTrue('2+3=5' in out.getvalue())