from rpi.config import RaspberryPiConfig

class Desktop(RaspberryPiConfig):
    CONFIG_PATH = "/etc/xdg/lxsession/LXDE/autostart"

    def config(self):
        conf = [
            self.lxpanel(),
            self.pcmanfm(),
            self.xserver(),
            self.browser(self.attrs["dashboard"])
        ]
        return "\n".join(conf)

    def lxpanel(self):
        return "@lxpanel --profile LXDE"

    def pcmanfm(self):
        return "@pcmanfm --desktop --profile LXDE"

    def xserver(self):
        return """
@xset s off
@xset -dpms
@xset s noblank
"""

    def browser(self, dashboard):
        if dashboard["browser"] == "chromium":
            return self.chromium(dashboard["url"])
        elif dashboard["browser"] == "kiosk-browser":
            return self.kiosk_browser(dashboard["url"])

    def chromium(self, url):
        return "@chromium --kiosk --incognito {}".format(url)

    def kiosk_browser(self, url):
        return "@/home/pi/kiosk-browser/kiosk-browser {}".format(url)

