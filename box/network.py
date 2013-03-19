from box.config import FarawayBoxConfig

class Network(FarawayBoxConfig):
    CONFIG_PATH = "/etc/network/interfaces"

    def config(self):
        if self.attrs["type"] == "wireless": return self.wireless_config()
        else:                                return self.wired_config()

    ### Custom methods

    def wired_config(self):
        return """auto lo

iface lo inet loopback
iface eth0 inet dhcp
"""

    def wireless_config(self):
        return self.wired_config() + """
auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-ssid "{0}"
wpa-psk "{1}"
""".format(self.attrs["ssid"], self.attrs["psk"])

