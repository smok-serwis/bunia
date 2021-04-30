# coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest

from bunia.output import ConsoleOutput, NullOutput


class TestConsoleOutput(unittest.TestCase):

    def test_badform(self):
        c = ConsoleOutput()
        self.assertRaises(ValueError, lambda: c.to('nonexistant form'))

    def test_sink(self):
        c = NullOutput()
        c.text('hello')
        self.assertEquals(c.to('text'), '')
