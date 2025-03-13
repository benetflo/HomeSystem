import board
import digitalio

led = digitalio.DigitalInOut(board.GP15)
led.direction = digitalio.Direction.OUTPUT

def led_on():
    led.value = True
def led_off():
    led.value = False
