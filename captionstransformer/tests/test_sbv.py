
try:
    import unittest2 as unittest
except ImportError:
    import unittest
from StringIO import StringIO
from captionstransformer.sbv import Reader, Writer
from captionstransformer import core
from datetime import timedelta

class TestSBVReader(unittest.TestCase):
    def setUp(self):
        test_content = StringIO(u"""
        0:00:03.490,0:00:07.430
        >> FISHER: All right. So, let's begin.
        This session is: Going Social
        
        0:00:07.430,0:00:11.600
        with the YouTube APIs. I am
        Jeff Fisher,
        
        0:00:11.600,0:00:14.009
        and this is Johann Hartmann,
        we're presenting today.
        
        0:00:14.009,0:00:15.889
        [pause]
        """)
        self.reader = Reader(test_content)

    def test_read(self):
        captions = self.reader.read()
        self.assertTrue(captions is not None)
        self.assertEqual(len(captions), 4)
        first = captions[0]
        self.assertEqual(type(first.text), unicode)
        self.assertEqual(first.text, u">> FISHER: All right. So, let's begin.\nThis session is: Going Social\n")
        self.assertEqual(first.start, core.get_date(second=3, millisecond=490))
        self.assertEqual(first.end, core.get_date(second=7, millisecond=430))
        self.assertEqual(first.duration, timedelta(seconds=3, milliseconds=940))


class TestSBVWriter(unittest.TestCase):
    def setUp(self):
        test_content = StringIO(u"""
        0:00:03.490,0:00:07.430
        >> FISHER: All right. So, let's begin.
        This session is: Going Social
        
        0:00:07.430,0:00:11.600
        with the YouTube APIs. I am
        Jeff Fisher,
        
        0:00:11.600,0:00:14.009
        and this is Johann Hartmann,
        we're presenting today.
        
        0:00:14.009,0:00:15.889
        [pause]
        """)
        self.reader = Reader(test_content)
        self.writer = Writer(StringIO())

    def test_transformtext(self):
        captions = self.reader.read()
        self.writer.captions = captions
        text = self.writer.captions_to_text()
        should_be = u"""00:00:03.490,00:00:07.430\n>> FISHER: All right. So, let's begin.\nThis session is: Going Social\n\n00:00:07.430,00:00:11.600\nwith the YouTube APIs. I am\nJeff Fisher,\n\n00:00:11.600,00:00:14.009\nand this is Johann Hartmann,\nwe're presenting today.\n\n00:00:14.009,00:00:15.889\n[pause]\n\n"""
        self.assertEqual(text, should_be)

    def test_format_time(self):
        caption = core.Caption()
        caption.start = core.get_date(second=3, millisecond=490)
        caption.end = core.get_date(second=7, millisecond=430)
        time_info = self.writer.format_time(caption)
        self.assertEqual(time_info['start'], '00:00:03.490')
        self.assertEqual(time_info['end'], '00:00:07.430')


if __name__ == '__main__':
    unittest.main()