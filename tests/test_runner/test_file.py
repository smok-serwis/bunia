import unittest

from bunia.runner.file import FileRunner
from tests.test_runner.commands import LoremIpsum


class TestFile(unittest.TestCase):
    def test_should_return_raw_bytes(self):
        fr = FileRunner()
        fr.run(LoremIpsum())

        mime, content = fr.get_content('lorem.txt', 'raw')

        self.assertEqual(mime, 'text/plain')
        self.assertEqual(content, b'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel elit finibus, pharetra enim vel, accumsan urna.')

    def test_should_return_base64(self):
        fr = FileRunner()
        fr.run(LoremIpsum())

        mime, content = fr.get_content('lorem.txt', 'base64')

        self.assertEqual(mime, 'text/plain')
        self.assertEqual(content, 'TG9yZW0gaXBzdW0gZG9sb3Igc2l0IGFtZXQsIGNvbnNlY3RldHVyIGFkaXBpc2NpbmcgZWxpdC4gTmFtIHZlbCBlbGl0IGZpbmlidXMsIHBoYXJldHJhIGVuaW0gdmVsLCBhY2N1bXNhbiB1cm5hLg==')

    def test_should_return_ascii(self):
        fr = FileRunner()
        fr.run(LoremIpsum())

        mime, content = fr.get_content('lorem.txt', 'ascii')

        self.assertEqual(mime, 'text/plain')
        self.assertEqual(content, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam vel elit finibus, pharetra enim vel, accumsan urna.')
