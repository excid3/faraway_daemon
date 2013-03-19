from box.config import FarawayBoxConfig

class Reboot(FarawayBoxConfig):
    def status(self):
        return self.attrs["reboot"]
