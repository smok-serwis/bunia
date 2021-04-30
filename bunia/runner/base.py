class Runner(object):

    def new_console(self, name=None, sink=False):
        """
        Return a new ConsoleOutput

        :rtype: ConsoleOutput
        """
        raise NotImplementedError('Abstract method!')

    def new_file(self, filename=None, mimetype=None):
        """
        Return a new FileOutput

        :rtype: BytesOutput
        """
        raise NotImplementedError('Abstract method!')
