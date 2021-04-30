import tempfile
from io import BytesIO
import mimetypes
from bunia.output.base import Output, transcode_output


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

        return transcode_output(content, form)


class NullOutput(Output):
    def __init__(self):
        super(NullOutput, self).__init__()
        self.mimetype = None

    def text(self, str_data):
        pass

    def write(self, byte_content):
        pass

    def to(self, form='text'):
        return transcode_output(b'', form)


class FileOutput(BytesOutput):
    """
    An output as a file

    :ivar mimetype: (tp.Optional[str]) - mimetype or None if unavailable
    """
    def __init__(self, name, mimetype=None):
        super(FileOutput, self).__init__(name)
        self.file = open(name, 'wb')
        self.mimetype = mimetype or mimetypes.guess_type(name)[0]

    def write(self, byte_content):
        super(FileOutput, self).write(byte_content)
        self.file.write(byte_content)

    def __del__(self):
        self.file.close()

