from rpi import RaspberryPi

rpi = RaspberryPi()
print rpi.serial_number()
print rpi.config_url()
print rpi.config()
print rpi.config()["overscan"]
