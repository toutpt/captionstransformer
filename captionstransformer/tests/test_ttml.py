try:
    import unittest2 as unittest
except ImportError:
    import unittest
from StringIO import StringIO
from captionstransformer.ttml import Reader, Writer
from captionstransformer import core
from datetime import datetime, timedelta


class TestTTMLReader(unittest.TestCase):
    def setUp(self):
        test_content = StringIO(u"""
<tt xml:lang="" xmlns="http://www.w3.org/ns/ttml"><body><div>
<p begin="00:00:10" end="00:00:12">Hi, I&#39;m Emily from Nomensa</p>
<p begin="00:00:12" end="00:00:15">and today I&#39;m going to be talking
about the order of content on your pages.</p>
<p begin="00:00:16" end="00:00:22">Making sure the content on your web pages is
presented logically is a really important part of web accessibility.</p>
<p begin="00:00:23" end="00:00:25">Page content should be ordered so it makes</p>
</div></body></tt>""")
        self.reader = Reader(test_content)

    def test_read(self):
        captions = self.reader.read()
        self.assertTrue(len(captions), 4)
        first = captions[0]
        self.assertEqual(first.start.strftime('%H:%M:%S'), '00:00:10')
        self.assertEqual(first.end.strftime('%H:%M:%S'), '00:00:12')
        duration = first.duration
        self.assertEqual(first.duration.seconds, 2)
        self.assertTrue(not hasattr(first.duration, 'minutes'))
        self.assertEqual(first.text, u"Hi, I'm Emily from Nomensa")


class TestTTMLWriter(unittest.TestCase):
    def setUp(self):
        self.writer = Writer(StringIO())

    def test_captions_to_text(self):
        caption = core.Caption()
        start = datetime(year=1901, month=1, day=1, hour=0, minute=0, second=3)
        caption.start = start
        caption.duration = timedelta(2.0/24/60/60)
        caption.text = u"My first caption"

        self.writer.captions = [caption]
        content = self.writer.captions_to_text()
        self.assertTrue(content is not None)
        self.assertTrue(content.startswith(u'<tt'))
        self.assertTrue(u"""<p begin="00:00:03" end="00:00:05">My first caption</p>""" in content)


if __name__ == '__main__':
    unittest.main()