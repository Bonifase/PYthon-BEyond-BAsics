import os
from reader.compressed import bzipped, gzipped

extension_map = {
    ".bz2": bzipped.opener,
    ".gz": gzipped.opener
}

class Reader:
    def __init__(self, filename):
        """
        Purpose: filename
        """
        extension = os.path.splitext(filename)[1]
        opener = extension_map.get(extension, open)
        self.file = opener(filename, 'rt')

    def close(self):
        self.file.close()

    def read(self):
        return self.file.read()