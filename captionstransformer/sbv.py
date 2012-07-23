from captionstransformer import core
#it appears that time.struct_time doesn't actually store milliseconds/microseconds.
#You may be better off using datetime
from datetime import datetime, timedelta


class Reader(core.Reader):
    def read(self):
        super(Reader, self).read()
        caption = core.Caption()
        captions = []
        for line in self.rawcontent.split('\n'):
            stripped_line = line.strip()
            if not stripped_line:
                continue
            start, end = self.get_time(stripped_line)
            if start is not None:
                #means it is a new caption so start by close previous one
                if caption.text:
                    captions.append(caption)

                caption = core.Caption()
                caption.start = start
                caption.end = end
            else:
                caption.text += u'%s\n' % stripped_line

        captions.append(caption)

        print len(captions)
        return captions

    def get_time(self, line):
        parts = line.split(',')
        if len(parts) != 2:
            return None, None
        try:
            start = datetime.strptime(parts[0], '%H:%M:%S.%f')
            end = datetime.strptime(parts[1], '%H:%M:%S.%f')
        except ValueError:
            return None, None
        return start, end


class Writer(core.Writer):
    DOCUMENT_TPL = u"%s"
    CAPTION_TPL = u"""%(start)s,%(end)s\n%(text)s\n"""

    def format_time(self, caption):
        """Return start and end time for the given format"""

        return {'start': caption.start.strftime('%H:%M:%S.%f')[:-3],
                'end': caption.end.strftime('%H:%M:%S.%f')[:-3]}
