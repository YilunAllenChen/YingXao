import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
from time import sleep
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
chan = AnalogIn(ads, ADS.P0)
water_reading = 10416.0
air_reading = 16256.0
dry_soil_reading = 15616.0
def moisture_reading():
    return round((1 - (chan.value - water_reading) / water_reading) * 100, 2)
'''
while True:
    print("moisture level: " + str(moisture_reading()) + "%")
    print(chan.value, chan.voltage)
    sleep(1)
'''
