# coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest
import io
from bunia.runner import HTMLRunner
from tests.test_runner.commands import AddTwoNumbers


class TestHtml(unittest.TestCase):
    def test_runs(self):
        hr = HTMLRunner()
        hr.run(AddTwoNumbers(), {'a': '2', 'b': '3'})

    def test_runs_and_outputs(self):
        hr = HTMLRunner()
        hr.run(AddTwoNumbers(), {'a': '2', 'b': '3'})
        self.assertTrue('2+3=5' in hr.get_html())
