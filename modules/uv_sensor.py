import board
import busio
import adafruit_ltr390

i2c = busio.I2C(board.GP1, board.GP0)

uv_sensor = adafruit_ltr390.LTR390(i2c)

# returns the raw ambient light measurement
def get_light():
    return uv_sensor.light

# returns the raw UV light measurement
def get_uvs():
    return uv_sensor.uvs

# returns the calculated UV Index value
def get_uvi():
    return uv_sensor.uvi

# returns the calculated Lux ambient light value
def get_lux():
    return uv_sensor.lux
