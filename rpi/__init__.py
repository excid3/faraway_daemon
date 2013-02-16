from memoize import memoize
import json
import subprocess
import urllib
from wifi import Wifi

CONFIG_URL = "http://excid3.com/rpi/"

class RaspberryPi:
    def update(self):
        print("Downloading config..."),
        config = self.config()
        print "success"

        print("Updating network interfaces..."),
        if Wifi(config["network"]).update(): print "success"

    def config(self):
        return json.loads(self.get_config())

    def get_config(self):
        response = urllib.urlopen(self.config_url())
        return response.read()

    @memoize
    def serial_number(self):
        output = subprocess.check_output(["cat", "/proc/cpuinfo"])
        entry  = filter(None, output.split("\n"))[-1]
        return entry.split()[-1]

    @memoize
    def config_url(self):
        return CONFIG_URL + self.serial_number() + "/config.json"
