

class Reader(object):
    def __init__(self, fileobject):
        self.fileobject = fileobject
        self.captions = []
        self.rawcontent = None
        self.time_unit = "mili second"

    def read(self):
        self.rawcontent = self.fileobject.read()
        return self.captions

    def add_caption(self, caption):
        self.captions.append(caption)

    def __repr__(self):
        return u"%s" % [caption.text for caption in self.captions]

    def close(self):
        self.fileobject.close()

class Writer(object):
    def __init__(self, fobject, captions=None):
        self.fileobject = fobject
        self.captions = []
        if captions is not None:
            self.captions = captions

    def write(self, captions=None):
        if captions is not None:
            self.captions = captions
        value = self.captions_to_text()
        self.fileobject.write(value)
        self.close()

    def close(self):
        self.fileobject.close()

    def captions_to_text(self):
        raise NotImplementedError("must be implemented in subclass")


class Caption(object):
    def __init__(self):
        self._duration = None
        self._start = None
        self._end = None
        self.time_unit = "milisecond"
        self._text = u""
        self.encoding = "utf-8"

    def update(self):
        if self._end is None and\
           self._start is not None and\
           self._duration is not None:
            self._end = self.start + self.duration
        if self._duration is None and\
           self._start is not None and\
           self._end is not None:
            self._duration = self._end - self._start

    def get_duration(self):
        return self._duration

    def set_duration(self, value):
        if type(value) != int:
            raise ValueError('duration must be an int: %s' % value)
        self._duration = value
        self.update()

    duration = property(get_duration, set_duration)

    def get_start(self):
        return self._start

    def set_start(self, value):
        if type(value) != int:
            raise ValueError('start must be an int: %s' % type(value))
        self._start = value
        self.update()

    start = property(get_start, set_start)

    def get_end(self):
        return self._end

    def set_end(self, value):
        if type(value) != int:
            raise ValueError('end must be an int: %s' % value)
        self._end = value
        self.update()

    end = property(get_end, set_end)

    def get_text(self):
        return self._text

    def set_text(self, value):
        if type(value) == str:
            value = str.decode(self.encoding)
        elif type(value) != unicode:
            raise ValueError("text must be either encoded string or unicode")
        self._text = value

    text = property(get_text, set_text)

    def __repr__(self):
        return self.text