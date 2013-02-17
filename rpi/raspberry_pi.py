import json
import subprocess
import urllib

from util import memoize
from video import Video
from network import Network

class RaspberryPi:
    def update(self):
        self.download_config()
        self.update_video()
        self.update_network()

    def download_config(self):
        print("Downloading config..."),
        self.show_result(self.config())

    def update_video(self):
        print("Updating video output..."),
        self.show_result(Video(self.config()["video"]).update())

    def update_network(self):
        print("Updating network interfaces..."),
        self.show_result(Network(self.config()["network"]).update())

    def show_result(self, result):
        if result: print "success"
        else:      print "no changes"

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
        return "http://excid3.com/rpi/" + self.serial_number() + "/config.json"
