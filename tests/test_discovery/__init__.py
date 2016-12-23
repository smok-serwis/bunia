# coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest
from bunia.api import Command
from tests.test_discovery import discovery as dis
from bunia.discovery import from_name, pick_from_module, from_module


class TestDiscovery(unittest.TestCase):
    def test_from_module(self):
        self.assertEquals(dis.Cmd1, from_name('tests.test_discovery'))
        self.assertEquals(dis.Cmd2, from_name('tests.test_discovery:Cmd2'))

    def test_pick_from_module(self):
        self.assertIs(dis.Cmd2, pick_from_module(dis, 'cmd2'))

    def test_from_module(self):
        to_find = [dis.Cmd1, dis.Cmd2]

        cmds = from_module(dis)
        print(repr(cmds))

        for cmd in cmds:
            print(repr(cmd))
            if cmd in to_find:
                to_find.remove(cmd)
            else:
                self.fail('strange, found %s' % (cmd.NAME, ))

        self.assertEquals(len(to_find), 0)

