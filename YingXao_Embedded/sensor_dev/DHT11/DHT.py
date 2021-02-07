# NOTE: The import has a _ not - in the module name.
from pigpio_dht import DHT11, DHT22
from time import sleep
gpio = 21 # BCM Numbering
sensor = DHT11(gpio)
while True:
#sensor = DHT22(gpio)

    result = sensor.read()
    print(result)
    sleep(0.5)
