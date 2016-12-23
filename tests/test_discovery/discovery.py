# coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest

from bunia.api import Command
from bunia.discovery import from_name, pick_from_module, from_module

from tests.test_discovery import discovery as dis

class TestDiscovery(unittest.TestCase):
    def test_from_module(self):
        self.assertIs(dis.Cmd1, from_name('tests.test_discovery'))
        self.assertIs(dis.Cmd2, from_name('tests.test_discovery:Cmd2'))


    def test_pick_from_module(self):
        self.assertIs(dis.Cmd2, pick_from_module('tests.test_discovery.discovery'))

    def test_from_module(self):
        to_find = [dis.md1, dis.Cmd2]

        for cmd in from_module('tests.test_discovery.discovery'):
            if cmd in to_find:
                to_find.remove(cmd)
            else:
                self.fail('strange')

        self.assertEquals(len(to_find), 0)
