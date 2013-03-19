from box.util import digest

class FarawayBoxConfig:
    def __init__(self, attrs):
        self.attrs = attrs

    def update(self):
        changed = self.changed()
        if changed:
            f = open(self.CONFIG_PATH, "wb")
            f.write(self.config())
            f.close()
            return True
        return False

    def changed(self):
        config = open(self.CONFIG_PATH).read()
        return digest(config) != digest(self.config())

    def config(self):
        raise NotImplementedError

