# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
 
import time
 
from board import SCL, SDA
import busio
 
from adafruit_seesaw.seesaw import Seesaw
 
i2c_bus = busio.I2C(SCL, SDA)
 
ss = Seesaw(i2c_bus, addr=0x36)

def soil_moisture():
    return round(ss.moisture_read(),2)

def soil_temp():
    return round(ss.get_temp(),2)

while True:
    # read moisture level through capacitive touch pad
    touch = soil_moisture()
 
    # read temperature from the temperature sensor
    temp = soil_temp()
 
    print("temp: " + str(temp) + "  moisture: " + str(touch))
    time.sleep(1)
