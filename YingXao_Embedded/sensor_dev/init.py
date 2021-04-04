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
import database as db

# global variable declaration
delay = 1.0 # step motor delay in ms
steps = 800  # 800 is the semicircle rotation steps
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
                    # UPLOAD TO DATABASE
                    
                    db.upload_data(('humidity',humidity))
                    db.upload_data(('temperature_in_Celsius',temp_c))
                    db.upload_data(('temperature_in_Fahrenheit',temp_f))
                    
                    dht_failed = False
                except KeyboardInterrupt:
                    raise
                except Exception as e:
                    # if failed to read humidity, read it again
                    print("Something bad happened : {}".format(str(e)))
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
                
                db.upload_data(("visible_light",visible))
                db.upload_data(("uv_index",uv))
                db.upload_data(("ir_light",ir))
            
            except:
                # if failed to read sunlight info, check SI1145
                print("Failed to read sunlight information")
            
            print("----------------------------")
            # moisture sensor reading 
            try: 
                mois = moisture.moisture_reading()
                print("moisture level: ",mois)
                # TODO: UPLOAD TO DATABASE
                
                db.upload_data(("moisture_level",mois))

                # check moisture level
               
                # turn water pump ON if moisture below 60.0, OFF otherwise
                if mois < 60.0:
                    print("moisture level below 60, turning ON water pump for 10 seconds")
                    pump.turn_on()
                    time.sleep(10)
                    pump.turn_off()
                else:
                    print("moisture level above 60, turning OFF water pump")
                    pump.turn_off()
            except:
                # if failed to read moisture level, check moisture sensor
                print("Failed to read moisture level")
            
            print("----------------------------")
            # TODO: get hours of sunlight needed for specific plant
            # from database
            # example using minutes from the value of the dictionary (ONLY FOR TESTING PURPOSE)
            # tuple inside the dictionary should be in hours
            # (hour to turn on solar shield, hour to turn off)
            plant_dict = {2:(10,12)}
            plant_hours = int(db.get_data('sunlightTime_s'))
            print("Sunlight needed for this plant: ",plant_hours," hours")
            if (int(now.strftime("%H"))) == (plant_dict[plant_hours][0]) and state == 0:
                print("current minute greater than {}, turn clockwise (open solar shield)".format(plant_dict[plant_hours][0]))
                try:
                    stepper.backward(delay / 1000, int(steps))
                    state = 1
                except:
                    print("Failed to turn solar gear")
            elif (int(now.strftime("%H"))) == (plant_dict[plant_hours][1]) and state == 1:
                print("current minute greater than {}, turn counterclockwise (close solar shield)".format(plant_dict[plant_hours][1]))
                try:
                    stepper.forward(delay / 1000, int(steps))
                    state = 0
                except:
                    print("Failed to turn solar gear")
            time.sleep(2)
    except KeyboardInterrupt:
        print("exiting the script")
    # clean up
    finally:
        pump.turn_off()


