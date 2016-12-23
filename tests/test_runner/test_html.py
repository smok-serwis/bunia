# coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest

from bunia.runner import HTMLRunner
from tests.test_runner.commands import AddTwoNumbers, ConsoleClusterfuck


class TestHtml(unittest.TestCase):
    def test_runs(self):
        hr = HTMLRunner()
        hr.run(AddTwoNumbers(), {'a': '2', 'b': '3'})

    def test_runs_and_outputs(self):
        hr = HTMLRunner()
        hr.run(AddTwoNumbers(), {'a': '2', 'b': '3'})
        self.assertTrue('2+3=5' in hr.get_html())

    def test_html_clusterfuck(self):
        hr = HTMLRunner()
        hr.run(ConsoleClusterfuck(), {'a': '2', 'b': '3'})
        out = hr.get_html()
        self.assertTrue('2+3=5' in out)
        self.assertTrue('2*3=6' in out)
        self.assertTrue('2-3=-1' in out)

