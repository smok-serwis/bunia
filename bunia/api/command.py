class Command(object):
    """
    Base class for all StGeorge commands.

    You need to inherit from this, and override/extend what's needed
    """

    NAME = 'command'
    DESCRIPTION = u'Does nothing.'
    ARGUMENTS = [] # list of Argument instances

    def run(self, runner, **kwargs):
        """
        Run with specified arguments.
        :param runner: Runner instance - pertaining to where are you being ran
        """


COMMAND = Command   # for autodiscovery
