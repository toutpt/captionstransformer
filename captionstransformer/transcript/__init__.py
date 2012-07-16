from captionstransformer import core
from bs4 import BeautifulSoup

class Reader(core.Reader):
    def read(self):
        content = super(Reader, self).read()
        soup = BeautifulSoup(content)
        texts = soup.find_all('text')
        struct = []
        for text in texts:
            info = 
        for line in content:
            if not line:
                continue
            else:
                import pdb;pdb.set_trace()
        return content


class Writer(core.Writer):
    pass
