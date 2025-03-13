import board
import busio
import adafruit_ltr390

# Create I2C-bus with GP3 & GP2
i2c = busio.I2C(board.GP3, board.GP2)

# Lock I2C-bus before scan or use of sensor
while not i2c.try_lock():
    pass

# Scan after I2C-devices
devices = i2c.scan()

# Unlock I2C-bus after use
i2c.unlock()

if not devices:
    print("No I2C-device was found. Check connections/wiring!")

# Create instance of ltr390 sensor
uv_sensor = adafruit_ltr390.LTR390(i2c)

# Functions for uv-sensor values
def get_uvs():
    return uv_sensor.uvs
def get_uvi():
    return uv_sensor.uvi
def get_light():
    return uv_sensor.light
def get_lux():
    return uv_sensor.lux
