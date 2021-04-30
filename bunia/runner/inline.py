# coding=UTF-8
import sys
import argparse
from bunia.runner.base import Runner
from bunia.api import ValuelessArgument
from bunia.output import ConsoleOutput, NullOutput
from bunia.discovery import from_name
import io


class InlineRunner(Runner):
    """
    For the cases where you execute the command as a callable inside your own code.
    Any output is discarded, result from .run() is returned.

    This is the default when you do:

        a_command(arg1, arg2, ...)

    """

    def new_file(self, filename=None, mimetype=None):
        no = NullOutput()
        no.mimetype = mimetype
        return no

    def new_console(self, name=None, sink=False):
        return NullOutput()

    def run(self, cmd, *args, **kwargs):
        """
        Run a command.

        Arguments are not sanitized as normal!

        args and kwargs are passed to run()

        :param cmd: Command instance to run
        :raise ValueError: argument was invalid
        """
        return cmd.run(self, *args, **kwargs)
