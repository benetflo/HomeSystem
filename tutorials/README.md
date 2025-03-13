# SETUP AND TUTORIAL


## CircuitPython setup

## Adafruit LTR390 UV Light Sensor




## DS18B20 Temperature Sensor

### Requirements:
* adafruit_onewire
* adafruit_ds18x20.mpy

#### adafruit_onewire
- Go to https://github.com/adafruit/Adafruit_CircuitPython_OneWire/releases
- Download 'adafruit-circuitpython-onewire-9.x-mpy-2.0.9.zip'   !! This is what I am using. Download other version if you are using older or newer version.
-  Add the onewire folder to your lib folder on the Pico W.

Your lib folder should now look like this:

* lib
  * adafruit_onewire
    - __init__.py
    - device.mpy
    - bus.mpy

#### adafruit_ds18x20.mpy
- Go to https://github.com/adafruit/Adafruit_CircuitPython_DS18X20/releases
- Download 'adafruit-circuitpython-ds18x20-9.x-mpy-1.4.3.zip'  !! This is the version I am using. Download the right version for your system!
- Add the 'adafruit_ds18x20.mpy' to your lib folder on the Pico W.

Your lib folder should now look like this:

* lib
  * adafruit_onewire
    - __init__.py
    - device.mpy
    - bus.mpy
  * adafruit_ds18x20.mpy



