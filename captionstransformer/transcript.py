from captionstransformer import core
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


class Reader(core.Reader):
    def text_to_captions(self):
        soup = BeautifulSoup(self.rawcontent)
        texts = soup.find_all('text')
        for text in texts:
            caption = core.Caption()
            caption.start = self.get_start(text)
            caption.duration = self.get_duration(text)
            caption.text = text.text
            self.add_caption(caption)

        return self.captions

    def get_start(self, text):
        return self.get_raw_time(text['start'], format="date")

    def get_duration(self, text):
        return self.get_raw_time(text['dur'], format="timedelta")

    def get_raw_time(self, utime, format="date"):
        if '.' in utime:
            second_f = float(utime)
            second = int(second_f)
            millisecond = int(1000 * (second_f - second))
        else:
            second = int(utime)
            millisecond = 0
        if format == "date":
            return core.get_date(second=second, millisecond=millisecond)
        else:
            return timedelta(seconds=second, milliseconds=millisecond)


class Writer(core.Writer):
    DOCUMENT_TPL = u"""<?xml version="1.0" encoding="utf-8" ?><transcript>%s</transcript>"""
    CAPTION_TPL = u"""<text start="%(start)s" dur="%(end)s">%(text)s</text>"""

    def format_time(self, caption):
        """Return start and end time for the given format"""
        return {'start': self.get_utime(caption.start),
                'end': self.get_utime(caption.end)}

    def get_utime(self, dt):
        start = dt
        start_seconds = 3600 * start.hour + 60 * start.minute + start.second
        start_milliseconds = start.microsecond / 1000

        if start_milliseconds:
            ustart = u"%s.%s" % (start_seconds, start_milliseconds)
        else:
            ustart = u"%s" % start_seconds

        return ustart
