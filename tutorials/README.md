# SETUP AND TUTORIAL

## Requirements checklist:
* Thonny setup
* CircuitPython setup
* DS18B20 Temperature Sensor setup
* Adafruit LTR390 UV Light Sensor setup


# Thonny setup

## Install Thonny
- Go to https://thonny.org
- Install latest version for your OS
- Follow and complete the installation guide.
- Open Thonny when the installation is finished

# Pico W CircuitPython setup
- Insert the USB-cable to your computer while holding down the BOOTSEL button on your Pico W.
- Navigate to the lower right corner in Thonny and click on 'Interpreter' -> 'Install CircuitPython'.
- Choose your Pico W as target (RPI-RP2).
- Choose CircuitPython(generic) version.
- Click 'Install' and wait for the process to finish.
- You should now have a device named CIRCUITPY on your computer!

CIRCUITPY default files:
* boot_out.txt - Displays CircuitPython version info.
* code.py (or main.py) - The main script that runs automatically.
* lib/ - For additional CircuitPython libraries. We will add files here later.
* settings.toml - Optional file for Wi-Fi/network setting on Pico W.

# DS18B20 Temperature Sensor setup

## STEP 1: adafruit_onewire
- Go to https://github.com/adafruit/Adafruit_CircuitPython_OneWire/releases
- Download 'adafruit-circuitpython-onewire-9.x-mpy-2.0.9.zip'   !! This is what I am using. Download other version if you are using older or newer version.
-  Add the onewire folder to your lib folder on the Pico W.

## STEP 2: adafruit_ds18x20.mpy
- Go to https://github.com/adafruit/Adafruit_CircuitPython_DS18X20/releases
- Download 'adafruit-circuitpython-ds18x20-9.x-mpy-1.4.3.zip'  !! This is the version I am using. Download the right version for your system!
- Add the 'adafruit_ds18x20.mpy' to your lib folder on the Pico W.

The lib folder on Pico W should now look like this:

* lib
  * adafruit_onewire
    - \_\_init\_\_.py
    - device.mpy
    - bus.mpy
  * adafruit_ds18x20.mpy

# Adafruit LTR390 UV Light Sensor

## STEP 1 adafruit_bus_device & adafruit_register:
- Go to https://circuitpython.org/libraries
- Download the zipfile 'Bundle for Version 9.x' (I am using this version but choose the version that matches your CircuitPython version).
- Add the 'adafruit_bus_device' & 'adafruit_register' folders to your Pico W's lib folder. 

## STEP 2 adafruit_ltr390.py
- Go to https://github.com/adafruit/Adafruit_CircuitPython_LTR390
- Download 'adafruit_ltr390.py'
- Add 'adafruit_ltr390.py' to your Pico W's lib folder.

The lib folder on Pico W should now look like this:

* lib
  * adafruit_bus_device
    - i2c_device.mpy
    - \_\_init\_\_.py
    - spi_device.mpy
  * adafruit_onewire
    - \_\_init\_\_.py
    - device.mpy
    - bus.mpy
  * adafruit_register
    - i2c_bcd_alarm.mpy
    - i2c_bcd_datetime.mpy
    - i2c_bit.mpy
    - i2c_bits.mpy
    - i2c_struct.mpy
    - i2c_struct_array.mpy
  * adafruit_ds18x20.mpy
  * adafruit_ltr390.py

