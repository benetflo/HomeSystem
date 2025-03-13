import board
from adafruit_onewire.bus import OneWireBus
import adafruit_ds18x20

ow_bus = OneWireBus(board.GP28)
devices = ow_bus.scan()

if not devices:
    raise RuntimeError("No sensor found on OneWire bus")

ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])

def get_temperature():
    return round(ds18b20.temperature, 3)
