from rpi.config import RaspberryPiConfig

class Video(RaspberryPiConfig):
    CONFIG_PATH = "/boot/config.txt"

    def config(self):
        overscan = self.attrs["overscan"]
        conf = [
            self.disable_overscan(overscan["disable"]),
            self.overscan_left(overscan["left"]),
            self.overscan_right(overscan["right"]),
            self.overscan_top(overscan["top"]),
            self.overscan_bottom(overscan["bottom"]),
        ]
        return "\n".join(conf)

    ### Custom methods

    def disable_overscan(self, disable):
        return "disable_overscan={}".format(disable)

    def overscan_left(self, pixels):
        if pixels: return "overscan_left={}".format(pixels)

    def overscan_right(self, pixels):
        if pixels: return "overscan_right={}".format(pixels)

    def overscan_top(self, pixels):
        if pixels: return "overscan_top={}".format(pixels)

    def overscan_bottom(self, pixels):
        if pixels: return "overscan_bottom={}".format(pixels)

