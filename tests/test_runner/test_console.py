# coding=UTF-8
from __future__ import absolute_import, division, print_function
import unittest
from threading import Lock, Thread
import io


from bunia.runner import ConsoleRunner
from bunia.api import Command

from tests.test_runner.commands import AddTwoNumbers, ConsoleClusterfuck

class TestConsole(unittest.TestCase):

    def test_runs(self):
        cr = ConsoleRunner()
        cr.run(AddTwoNumbers(), ['2', '3'])

    def test_runs_and_outputs(self):
        out = io.StringIO()
        cr = ConsoleRunner()
        cr.run(AddTwoNumbers(), ['2', '3'], stdout=out)
        self.assertTrue('2+3=5' in out.getvalue())

    def test_console_clusterfuck(self):
        out = io.StringIO()
        cr = ConsoleRunner()
        cr.run(ConsoleClusterfuck(), ['2', '3'], stdout=out)
        self.assertTrue('2+3=5' in out.getvalue())
        self.assertTrue('2*3=6' in out.getvalue())
        self.assertTrue('2-3=-1' in out.getvalue())

    def test_stdout_passthru(self):
        lock = Lock()
        lock.acquire()

        im_here = Lock()
        im_here.acquire()

        class PassCmd(Command):
            def run(self, runner):
                con = runner.new_console()
                con.text('hello')
                im_here.release()
                lock.acquire()
                con.text('world')

        out = io.StringIO()

        class Runner(Thread):
            def run(self):
                ConsoleRunner().run(PassCmd(), [], stdout=out)

        r = Runner()
        r.start()
        im_here.acquire()
        v = out.getvalue()
        self.assertTrue('hello' in v)
        self.assertFalse('world' in v)
        lock.release()
        r.join()    # wait for command completion
        v += out.getvalue()
        self.assertTrue('world' in v)
