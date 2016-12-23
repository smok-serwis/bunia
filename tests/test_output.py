# coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest

from bunia.output import ConsoleOutput


class TestConsoleOutput(unittest.TestCase):

    def test_badform(self):
        c = ConsoleOutput()
        self.assertRaises(ValueError, lambda: c.to('nonexistant form'))

    def test_sink(self):
        c = ConsoleOutput(sink=True)
        self.assertTrue(c.sink)

        c = ConsoleOutput(sink=True)
        self.assertTrue(c.sink)
        c.text('hello')
        self.assertEquals(c.to('text'), '')

        c = ConsoleOutput()
        c.sink = True
        c.text('hello')
        self.assertEquals(c.to('text'), '')

        c = ConsoleOutput(sink=True)
        c.text('world')
        c.sink = False
        c.text('hello')
        self.assertTrue('hello' in c.to('text'))
