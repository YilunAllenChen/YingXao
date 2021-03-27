# init.py version 0.0
"""
This init file is the start up python script
for YingXao gardener. The main purpose of this file
is to read sensor datas and upload them to the database. 
"""
from datetime import datetime
import time
import os as o
import dht22
import si1145
import moisture
import stepper
import pump

# global variable declaration
delay = 1.0 # step motor delay in ms
step = 800  # 800 is the semicircle rotation steps
state = 0   # step motor state: 0 = solar shield OFF
            #                   1 = solar shield ON
dht_failed = True   # reading flag for dht22, True if dht22 failed to read
                    # False otherwise

if __name__ == "__main__":
    # make sure water pump is turned OFF initially
    pump.turn_off()
    # start operation
    try:
        while True:
            # clear screen for every data measurement
            # o.system('clear')  
            # get current time
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("----------------------------")
            print(current_time)
            
            print("----------------------------")
            # DHT22 sensor reading
            # environment humidity and temperature
            dht_failed = True   # RESET reading flag
            while dht_failed:
                try:
                    humidity = dht22.get_humidity()
                    temp_c = dht22.get_temperature_c()
                    temp_f = dht22.get_temperature_f()
                    print("humidity: ",humidity)
                    print("temperature in Celsius: ",temp_c)
                    print("temperature in Fahrenheit: ",temp_f)
                    # TODO: UPLOAD TO DATABASE
                    dht_failed = False
                except:
                    # if failed to read humidity, read it again
                    dht_failed = True
            
            print("----------------------------")
            # SI1145 sensor reading - sunlight info
            # visible light, uv light, and ir light
            try:
                visible = si1145.get_visible()
                uv = si1145.get_uv()
                ir = si1145.get_ir()
                print("visible light: ",visible)
                print("uv light: ",uv)
                print("ir light: ",ir)
                # TODO: UPLOAD TO DATABASE
            except:
                # if failed to read sunlight info, check SI1145
                print("Failed to read sunlight information")
            
            print("----------------------------")
            # moisture sensor reading 
            try: 
                mois = moisture.moisture_reading()
                print("moisture level: ",mois)
                # TODO: UPLOAD TO DATABASE
            except:
                # if failed to read moisture level, check moisture sensor
                print("Failed to read moisture level")
            time.sleep(2)
    except KeyboardInterrupt:
        print("exiting the script")
    # clean up
    finally:
        pump.turn_off()


