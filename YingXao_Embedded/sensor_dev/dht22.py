import Adafruit_DHT
import time

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 16

def get_temperature_c():
    return round(Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)[1],1)

def get_temperature_f():
    return round(get_temperature_c() * (9 / 5) + 32,1)

def get_humidity():
    return round(Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)[0],1)

if __name__ == "__main__":
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
            print("Temp in C = {}, F = {}, Humidity = {}".format(get_temperature_c(),get_temperature_f(),get_humidity()))
        else:
            print("Failed to retrieve data from humidity sensor")
        time.sleep(2)
