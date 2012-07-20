from captionstransformer import core
from bs4 import BeautifulSoup

class Reader(core.Reader):
    def read(self):
        self.time_unit = "second"
        super(Reader, self).read()
        soup = BeautifulSoup(self.rawcontent)
        texts = soup.find_all('text')
        for text in texts:
            caption = core.Caption()
            caption.start = int(text['start'])
            caption.duration = int(text['dur'])
            caption.text = text.text
            self.add_caption(caption)

        return self.captions


class Writer(core.Writer):
    pass
