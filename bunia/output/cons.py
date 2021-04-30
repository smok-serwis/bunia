import io
import six

from bunia.output.base import Output, transcode_output


class ConsoleOutput(Output):
    """
    Returns a unicode.

    You can silence and unsilence it by setting the .sink property to True/False.
    True silences output.
    """
    def __init__(self, name=None, eol='\n', stdout=None):
        Output.__init__(self, name)
        self.io = stdout or io.StringIO()
        self.eol = six.text_type(eol)

    def text(self, message, *args):
        """Write a message. It will be subject to processing with
        message % args. Appends an end of line"""
        self.io.write((six.text_type(message) % args))
        self.io.write(self.eol)

    def to(self, form='text'):
        content = self.io.getvalue()
        self.io.close()

        if form == 'html':
            if content:
                return '<pre>'+content+'</pre>'
            else:
                return '<em>Empty!</em>'

        return transcode_output(content, form, dtype='text')

