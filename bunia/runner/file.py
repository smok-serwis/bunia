from bunia.output.bytes import BytesOutput

from bunia.runner.base import Runner


class FileRunner(Runner):
    MIME = {
        'xlsx': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
        'txt': 'text/plain',
    }

    def __init__(self):
        self.output = None

    def new_console(self, name=None, sink=False):
        self.output = BytesOutput(name)

        return self.output

    def get_content(self, filename, form='raw'):
        extension = filename.split('.')[-1]

        if extension not in FileRunner.MIME:
            raise NotImplementedError('"%s" extension is not supported yet. You can implement this if you wish.')

        mime = FileRunner.MIME[extension]

        content = self.output.to(form=form)

        return mime, content

    def run(self, cmd, *args, **kwargs):
        return cmd.run(self, *args, **kwargs)
