import time
from captionstransformer import core

class Reader(core.Reader):
    pass

DOCUMENT_TPL = u"""<tt xml:lang="" xmlns="http://www.w3.org/ns/ttml"><body><div>%s</div></body></tt>"""
CAPTION_TPL = u"""<p begin="%(start)s" end="%(end)s">%(text)s</p>"""


class Writer(core.Writer):
    def captions_to_text(self):
        text = DOCUMENT_TPL
        buffer = u""
        for caption in self.captions:
            time_info = self.format_time(caption)
            buffer+= CAPTION_TPL % {'start': time_info['start'],
                                    'end': time_info['end'],
                                    'text': caption.text}
        return text % buffer

    def format_time(self, caption):
        """Return start and end time for the given format"""
        #should be seconds by default
        start = caption.start
        end = caption.end
        if caption.time_unit == "mili second":
            start = caption.start / 1000
            end = caption.end / 1000

        return {'start': time.strftime('%H:%M:%S', time.gmtime(start)),
                'end': time.strftime('%H:%M:%S', time.gmtime(end))}
