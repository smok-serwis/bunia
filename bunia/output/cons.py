import io

from .base import Output


class ConsoleOutput(Output):
    """
    UTF-8 output.
    """
    def __init__(self, name=None, eol=u'\n', stdout=None):
        Output.__init__(self, name)
        self.io = stdout or io.StringIO()
        self.eol = unicode(eol)

    def text(self, message, *args):
        """Write a message. It will be subject to processing with
        message % args. Appends an end of line"""
        self.io.write((unicode(message) % args))
        self.io.write(self.eol)

    def to(self, form='text'):
        content = self.io.getvalue().encode('utf8')
        self.io.close()

        if form == 'text':
            return content
        elif form == 'html':
            return '<pre>' + content + '</pre>'
        else:
            raise ValueError('Unsupported form')

