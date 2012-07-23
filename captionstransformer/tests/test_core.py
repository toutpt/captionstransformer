try:
    import unittest2 as unittest
except ImportError:
    import unittest
from StringIO import StringIO
from captionstransformer import core
from datetime import timedelta

class TestCoreReader(unittest.TestCase):
    def setUp(self):
        test_content = StringIO(u"CONTENT")
        self.reader = core.Reader(test_content)

    def test_read(self):
        captions = self.reader.read()
        self.assertEqual(captions, [])
        self.assertEqual(self.reader.rawcontent, u"CONTENT")

    def test_add_caption(self):
        caption = "test"
        self.reader.add_caption(caption)
        self.assertTrue(caption in self.reader.captions)

    def test__repr__(self):
        repr = self.reader.__repr__()
        self.assertEqual(self.reader.__repr__(),
                         u"captionstransformer.core.Reader: ")


class TestCoreWriter(unittest.TestCase):
    def setUp(self):
        self.stringio = StringIO()
        self.writer = core.Writer(self.stringio)
        caption = core.Caption()
        caption.start = core.get_date(second=3)
        caption.end = core.get_date(second=7)
        caption.text = u"TEST TEXT"
        self.writer.add_caption(caption)

    def test_captions_to_text(self):
        text = self.writer.captions_to_text()
        self.assertEqual(text, u"00:00:03 , 00:00:07 , TEST TEXT")


class TestCaption(unittest.TestCase):
    def setUp(self):
        self.caption = core.Caption()

    def test_set_start(self):
        start = core.get_date(second=3)
        self.caption.start = start
        self.assertEqual(self.caption.start, start)

    def test_set_end(self):
        end = core.get_date(second=3)
        self.caption.end = end
        self.assertEqual(self.caption.end, end)

    def test_set_duration(self):
        duration = timedelta(seconds=3)
        self.caption.duration = duration
        self.assertEqual(self.caption.duration, duration)

    def test_update_from_start_and_end(self):
        start = core.get_date(second=3)
        end = core.get_date(second=3)
        self.caption.start = start
        self.caption.end = end

        duration = end - start
        self.assertEqual(self.caption.duration, duration)

    def test_update_from_start_and_duration(self):
        start = core.get_date(second=3)
        duration = timedelta(seconds=3)
        self.caption.start = start
        self.caption.duration = duration

        end = start + duration
        self.assertEqual(self.caption.end, end)

    def test_set_text(self):
        self.caption.text = u"TEST CONTENT"
        self.assertEqual(self.caption.text, u"TEST CONTENT")
        self.assertRaises(ValueError, self.caption.set_text, 3)

    def test_repr(self):
        self.caption.text = u"Test CONTENT"
        self.assertEqual(self.caption.__repr__(),
                         u"captionstransformer.core.Caption: Test CONTENT")


class TestGetDate(unittest.TestCase):
    def test_get_date_default(self):
        date = core.get_date()

        self.assertEqual(date.year, 1900)
        self.assertEqual(date.month, 1)
        self.assertEqual(date.day, 1)
        self.assertEqual(date.hour, 0)
        self.assertEqual(date.minute, 0)
        self.assertEqual(date.second, 0)

    def test_get_date_second(self):
        date = core.get_date(second=3600)
        self.assertEqual(date.hour, 1)
        self.assertEqual(date.minute, 0)
        self.assertEqual(date.second, 0)

    def test_get_date_millisecond(self):
        date = core.get_date(millisecond=940)
        self.assertEqual(date.second, 0)
        self.assertEqual(date.microsecond, 940000)


if __name__ == '__main__':
    unittest.main()
