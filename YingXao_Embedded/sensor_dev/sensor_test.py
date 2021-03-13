import time
import MoistureSensor.Moisture as Moisture
import DHT22.DHT22 as DHT 
import SI1145.SI1145 as light_sensor
import StepMotor.stepper as step

while True:
    try:
        # read environment humidity from DHT22
        humidity = DHT.get_humidity()
        print('humidity: {}'.format(humidity))
    except:
        print('Failed to read humidity, check DHT22 connection.')

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
        delay = 1.0
        steps = 1000
        if ir_light > 700.0:
            step.forward(int(delay) / 1000.0, int(steps))
    except:
        print('Failed to read sunlight information, check SI1145')
    time.sleep(2.0)
