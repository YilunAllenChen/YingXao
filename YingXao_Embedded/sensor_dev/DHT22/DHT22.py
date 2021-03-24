# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT

import time
import board
import adafruit_dht

# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D21)

# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)

def get_temperature_c():
    return dhtDevice.temperature

def get_temperature_f():
    return round((dhtDevice.temperature) * (9 / 5) + 32, 1)

def get_humidity():
    return dhtDevice.humidity

if __name__=='__main__':
    while True:
        try:
            # Print the values to the serial port
            # temperature_c = dhtDevice.temperature
            # temperature_f = temperature_c * (9 / 5) + 32
            # humidity = dhtDevice.humidity
            print(
                "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                    get_temperature_f(), get_temperature_c(), get_humidity()
                )
            )

        except RuntimeError as error:
            # Errors happen fairly often, DHT's are hard to read, just keep going
            print(error.args[0])
            time.sleep(2.0)
            continue
        except Exception as error:
            print(error)
            dhtDevice.exit()
            raise error

        time.sleep(2.0)

