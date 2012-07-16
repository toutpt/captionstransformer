

class Reader(object):
    def __init__(self, fileobject):
        self.fileobject = fileobject

    def read(self):
        content = self.fileobject.read()
        return content

    def close(self):
        self.fileobject.close()


class Writer(object):
    def __init__(self, fobject):
        self.fileobject = fobject

    def write(self, value):
        pass

    def close(self):
        self.fileobject.close()


class Caption(object):
    def __init__(self):
        self._duration = None
        self._start = None
        self._end = None
