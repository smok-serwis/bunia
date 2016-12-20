import unittest

from bunia.api import Command

class TestInline(unittest.TestCase):

    def test_inline(self):

        a = {}

        class InlineCommand(Command):
            def run(self, runner, *args, **kwargs):
                a['args'] = args
                a['kwargs'] = kwargs

        InlineCommand()(1, 2, ala=3)

        self.assertEquals(a['args'][0], 1)
        self.assertEquals(a['args'][1], 2)
        self.assertEquals(a['kwargs']['ala'], 3)
