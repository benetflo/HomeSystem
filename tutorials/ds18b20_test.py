import board
from adafruit_onewire.bus import OneWireBus

# Initialize one-wire bus connection with ds18b20 sensor
ow_bus = OneWireBus(board.GP28) # change 28 to GPIO you have the sensor connected to (Pico W uses GP)

# Scan the one-wire bus to available devices. (IF YOU HAVE MULTIPLE SENSORS CONNECTED TO YOUR BOARD) Needed to choose the right sensor based on ID
# ROM = Unique ID
devices = ow_bus.scan()
for device in devices:
  print("ROM = {} \tFamily = 0x{:02x}".format([hex(i) for i in device.rom], device.family_code))

# Import module and create an instance of the DS18x20 sensor 
import adafruit_ds18x20
ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0]) # Choose device by index

# Now you can test the sensor! Print temperature:
print('Temperature: {0:0.3f} °C'.format(ds18b20.temperature))

