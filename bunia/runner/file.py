import mimetypes
import warnings

from bunia.output.bytes import BytesOutput, FileOutput

from bunia.runner.base import Runner


class FileRunner(Runner):
    MIME = {
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'txt': 'text/plain',
    }

    def __init__(self):
        self.output = None
        self.files = {}

    def new_console(self, name=None, sink=False):
        self.output = BytesOutput(name)

        return self.output

    def new_file(self, filename=None, mimetype=None):
        fo = FileOutput(filename, mimetype)
        self.files[filename] = fo
        return fo

    def get_content(self, filename, form='raw'):
        warnings.warn('get_content is deprecated', DeprecationWarning)
        return mimetypes.guess_type(filename)[0], self.output.to(form)

    def run(self, cmd, *args, **kwargs):
        return cmd.run(self, *args, **kwargs)
