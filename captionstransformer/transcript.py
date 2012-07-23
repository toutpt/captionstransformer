from captionstransformer import core
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


class Reader(core.Reader):
    def text_to_captions(self):
        soup = BeautifulSoup(self.rawcontent)
        texts = soup.find_all('text')
        for text in texts:
            caption = core.Caption()
            caption.start = core.get_date(second=int(text['start']))
            caption.duration = timedelta(seconds=int(text['dur']))
            caption.text = text.text
            self.add_caption(caption)

        return self.captions


class Writer(core.Writer):
    DOCUMENT_TPL = u"""<?xml version="1.0" encoding="utf-8" ?><transcript>%s</transcript>"""
    CAPTION_TPL = u"""<text start="%(start)s" dur="%(end)s">%(text)s</text>"""


    def format_time(self, caption):
        """Return start and end time for the given format"""

        return {'start': caption.start.strftime('%H:%M:%S.%f')[:-3],
                'end': caption.end.strftime('%H:%M:%S.%f')[:-3]}

