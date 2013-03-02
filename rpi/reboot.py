from rpi.config import RaspberryPiConfig

class Reboot(RaspberryPiConfig):
    def status(self):
        return self.attrs["reboot"]
