import board
import busio
import adafruit_ltr390

i2c = busio.I2C(board.GP1, board.GP0) # PICO W uses GP, I'm using GPIO 1 & 0. NOTE: First parameter == SCL
                                                                                #   Second parameter == SDA
# Create instance of ltr sensor
ltr = adafruit_ltr390.LTR30(i2c)

# Test loop
while True:
    print("UV:", ltr.uvs, "\t\tAmbient Light:", ltr.light)
    print("UVI:", ltr.uvi, "\t\tLux:", ltr.lux)
    time.sleep(1.0)
