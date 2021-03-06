import json
import os
import subprocess
import urllib

from util import memoize
from desktop import Desktop
from network import Network
from video import Video
from reboot import Reboot

class FarawayBox:
    def update(self):
        self.download_config()
        self.update_video()
        self.update_network()
        self.update_desktop()

        self.reboot()

    def download_config(self):
        print("Downloading config..."),
        self.show_result(self.config())

    def update_video(self):
        print("Updating video output..."),
        self.show_result(Video(self.config()["video"]).update())

    def update_network(self):
        print("Updating network interfaces..."),
        self.show_result(Network(self.config()["network"]).update())

    def update_desktop(self):
        print("Updating desktop configuration..."),
        self.show_result(Desktop(self.config()["desktop"]).update())

    def reboot(self):
        if Reboot(self.config()["maintenance"]).status():
            subprocess.call(["/sbin/shutdown", "-r", "now"])

    def show_result(self, result):
        if result:
            print "success"
        else:
            print "no changes"

    def get_config(self):
        response = urllib.urlopen(self.config_url())
        return response.read()

    @memoize
    def config(self):
        return json.loads(self.get_config())

    @memoize
    def serial_number(self):
        output = subprocess.check_output(["cat", "/proc/cpuinfo"])
        entry  = filter(None, output.split("\n"))[-1]
        return entry.split()[-1]

    @memoize
    def config_url(self):
        return "http://box.farawaylabs.com/boxes/" + self.serial_number() + ".json?auth_token=" + self.auth_token()

    def auth_token(self):
        path = os.path.expanduser("~/.standup")
        if os.path.exists(path):
            return open(path).read().strip()
        else:
            raise AttributeError, "Auth token .standup does not exist"
