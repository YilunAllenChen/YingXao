import time
import MoistureSensor.Moisture as Moisture
import DHT22.DHT22 as DHT 
import SI1145.SI1145 as light_sensor
import StepMotor.stepper as step
import Pump.pump as pump
import datetime as dt

# global variables
# step motor delay and steps
delay = 1.0
steps = 800
# define step motor state
state = 0   # 0 is when solar shield OFF
            # 1 is when solar shield ON

try:
    while True:
        now = dt.datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print("Current Time = ", current_time)
        try:
            # read environment humidity from DHT22
            humidity = DHT.get_humidity()
            print('humidity: {}'.format(humidity))
        except:
            # print('Failed to read humidity, check DHT22 connection.')
            continue
        try:
            # read environment temperature from DHT22
            temperature_c = DHT.get_temperature_c() # temperature in Celsius
            print('temperature in Celsius: {}'.format(temperature_c))
            temperature_f = DHT.get_temperature_f() # temperature in Fahrenheit
            print('temperature in Fahrenheit: {}'.format(temperature_f))
        except:
            print('Failed to read temperature, check DHT22 connection.')
        try:
            # read moisture level from soil moisture sensor
            moisture = Moisture.moisture_reading()
            print('moisture level: {}'.format(moisture))
            if moisture < 60.0:
                # pump.turn_on()
                print('moisture level below 60, turning ON water pump')
            else:
                pump.turn_off()
                print('moisture level above 60, turning OFF water pump')
        except:
            print('Failed to read moisture level, check moisture sensor')
        try:
            # read sunlight information from SI1145
            visible_light = light_sensor.get_visible()
            print('visible light: {}'.format(visible_light))
            uv_light = light_sensor.get_uv()
            print('uv light: {}'.format(uv_light))
            ir_light = light_sensor.get_ir()
            print('ir light: {}'.format(ir_light))
            if ir_light > 700.0:
                step.forward(int(delay) / 1000.0, int(steps))
                print('ir light above 700, turning solar shield clockwise')

        except:
            print('Failed to read sunlight information, check SI1145')
        time.sleep(2.0)
        # if the current time is later than 6 o'clock, turn solar shield off
        # if int(now.strftime('%H')) > 6 and state == 0:
        #     step.backward(int(delay) / 1000.0, int(steps))
        #     state = 1
        # if current minute is even number, turn solar shield ON
        if (int(now.strftime('%M')) % 2) == 0 and state == 0:
            step.forward(int(delay) / 1000.0, int(steps))
            state = 1
        elif (int(now.strftime('%M')) % 2) == 1 and state == 1:
            step.backward(int(delay) / 1000.0, int(steps))
            state = 0

except:
    print('UNKNOWN ERROR')
finally:
    pump.turn_off()
