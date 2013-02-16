import hashlib

class Wifi:
    def __init__(self, attrs):
        self.interfaces = open("/etc/network/interfaces", "rb").read()
        self.attrs = attrs

    def update(self):
        changed = self.changed()
        if changed:
            return changed
            f = open("/etc/network/interfaces", "wb")
            f.write(self.wireless_config(ssid, password))
            return f.close()

        return changed

    def changed(self):
        return hashlib.md5(self.interfaces).hexdigest() != hashlib.md5(self.wireless_config()).hexdigest()

    def wireless_config(self):
        return """auto lo

iface lo inet loopback
iface eth0 inet dhcp

auto wlan0
allow-hotplug wlan0
iface wlan0 inet dhcp
wpa-ssid "{0}"
wpa-psk "{1}"
""".format(self.attrs["ssid"], self.attrs["password"])
