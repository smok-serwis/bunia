import unittest

from bunia.api import Argument, Integer, Float

class TestArguments(unittest.TestCase):

    def test_base(self):
        arg = Argument('test', description=u'desc', required=False, default='wtf')

        self.assertEquals(arg.name, 'test')
        self.assertEquals(arg.description, u'desc')
        self.assertEquals(arg.required, False)
        self.assertEquals(arg.default, 'wtf')

    def test_argument(self):
        arg = Argument('test')

        self.assertEquals(arg.name, 'test')
        self.assertEquals('k', arg.clean('k'))

    def test_integer(self):
        arg = Integer('test')
        self.assertEquals(2, arg.clean('2'))
        self.assertRaises(ValueError, lambda: arg.clean('weer'))

    def test_float(self):
        arg = Float('test')
        self.assertEquals(2, arg.clean('2'))
        self.assertEquals(2.14, arg.clean('2.14'))
        self.assertRaises(ValueError, lambda: arg.clean('weer'))
