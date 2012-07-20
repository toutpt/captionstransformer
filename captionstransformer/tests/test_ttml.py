try:
    import unittest2 as unittest
except ImportError:
    import unittest
from StringIO import StringIO
from captionstransformer.ttml import Writer
from captionstransformer import core

class TestTranscriptReader(unittest.TestCase):
    def setUp(self):
        self.writer = Writer(StringIO())

    def test_read(self):
        caption = core.Caption()
        caption.time_unit = "second"
        caption.start = 3
        caption.duration = 2
        caption.text = u"My first caption"

        self.writer.captions = [caption]
        content = self.writer.captions_to_text()
        self.assertTrue(content is not None)
        self.assertTrue(content.startswith(u'<tt'))
        self.assertTrue(u"""<p begin="00:00:03" end="00:00:05">My first caption</p>""" in content)


if __name__ == '__main__':
    unittest.main()