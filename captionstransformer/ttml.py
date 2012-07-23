from datetime import datetime
from bs4 import BeautifulSoup
from captionstransformer import core

class Reader(core.Reader):
    def text_to_captions(self):
        soup = BeautifulSoup(self.rawcontent)
        texts = soup.find_all('p')
        for text in texts:
            caption = core.Caption()
            caption.start = self.get_date(text['begin'])
            caption.end = self.get_date(text['end'])
            caption.text = text.text
            self.add_caption(caption)

        return self.captions

    def get_date(self, time_str):
        return datetime.strptime(time_str, '%H:%M:%S')

class Writer(core.Writer):
    DOCUMENT_TPL = u"""<tt xml:lang="" xmlns="http://www.w3.org/ns/ttml"><body><div>%s</div></body></tt>"""
    CAPTION_TPL = u"""<p begin="%(start)s" end="%(end)s">%(text)s</p>"""

    def format_time(self, caption):
        """Return start and end time for the given format"""
        #should be seconds by default

        return {'start': caption.start.strftime('%H:%M:%S'),
                'end': caption.end.strftime('%H:%M:%S')}
