import sys
import argparse
from .runner import Runner
from ..outputs import ConsoleOutput
import io

class ConsoleRunner(Runner):
    """
    A console-based runner. Arguments are strings, output is utf8 text.
    """

    def __init__(self):
        self.consoles = []

    def new_console(self, name=None):
        con = ConsoleOutput(name)
        self.consoles.append(con)
        return con

    def new_table(self, name=None, headers=[]):
        raise NotImplementedError

    def run(self, cmd, args, stdout=None):
        """
        Run a command.

        :param cmd: Command instance to run
        :param args: list of str, command-line arguments
        :raise ValueError: argument was invalid
        """
        if stdout is None:
            self.stdout = io.StringIO()

        parser = argparse.ArgumentParser(description=cmd.DESCRIPTION)

        argument_by_name = {}

        for argument in cmd.ARGUMENTS:
            argument_by_name[argument.name] = argument
            parser.add_argument(argument.name,
                                metavar=argument.username,
                                nargs=1,
                                type=str,
                                default=argument.default,
                                help=argument.description)

        params = {}

        for argument_name, value in vars(parser.parse_args(args)).iteritems():
            try:
                params[argument_name] = argument_by_name[argument_name].clean(value[0])
            except ValueError as e:
                raise ValueError('Invalid value of argument %s: %s' % (argument_name, e.message))

        cmd.run(self, **params)

        first = True

        for console in self.consoles:
            if not first:
                self.stdout.write('\n')
            else:
                first = True

            if console.name is not None:
                self.stdout.write(console.name)
                self.stdout.write('----------------')

            self.stdout.write(console.to('text').decode('utf8'))


if __name__ == '__main__':
    # First argument is name of the module to run
    if len(sys.argv) < 1:
        print('Expected command to run.\nCan be in form name.of.module:CommandClass or name.of.module, if command is available at module-level variable COMMAND')

    from bunia.discovery import from_name

    cmd = from_name(sys.argv[1])()
    cr = ConsoleRunner()
    cr.run(cmd, sys.argv[2:])
    print(cr.stdout.getvalue())
    cr.stdout.close()
