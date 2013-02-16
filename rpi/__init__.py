from memoize import memoize
import json
import subprocess
import urllib
from wifi import Wifi

CONFIG_URL = "http://excid3.com/rpi/"

class RaspberryPi:
    @memoize
    def serial_number(self):
        return "000000005a9d1068"
        output = subprocess.check_output(["cat", "/proc/cpuinfo"])
        entry  = filter(None, output.split("\n"))[-1]
        return entry.split()[-1]

    @memoize
    def config(self):
        return json.loads(self.get_config())

    @memoize
    def config_url(self):
        return CONFIG_URL + self.serial_number() + "/config.json"

    def get_config(self):
        response = urllib.urlopen(self.config_url())
        return response.read()

    def update(self):
        config = self.config()

        print("Updating network interfaces..."),
        print Wifi(config["network"]).update()
