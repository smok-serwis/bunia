import base64
from io import BytesIO

from bunia.output.base import Output


class BytesOutput(Output):
    def __init__(self, name):
        Output.__init__(self, name)

        self.output = BytesIO()

    def write(self, byte_content):
        self.output.write(byte_content)

    def get_io(self):
        return self.output

    def to(self, form='raw'):
        self.output.seek(0)
        content = self.output.read()
        self.output.close()

        if form == 'raw':
            return content
        if form == 'ascii':
            return content.decode('ascii')
        if form == 'base64':
            return base64.b64encode(content)

        raise SyntaxError('"%s" is not a valid format' % form)
