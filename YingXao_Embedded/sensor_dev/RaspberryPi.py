from firebase import firebase
import time
import random
import MoistureSensor.Moisture as Moisture 
import DHT22.DHT22 as DHT
import SI1145.SI1145 as light_sensor
plantType = 'tulip' #change to customer's choice

plantInfo = firebase.FirebaseApplication('https://plants-info-5b86b-default-rtdb.firebaseio.com/', None)
result = plantInfo.get('/plants-info-5b86b-default-rtdb/plantDatabase', '')
humidity_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['humidity_s'] #standard humidity
moisture_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['moisture_s']
sunlight_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['sunlight_s'] #standard sunlight
temperatureC_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['temperatureC_s']
temperatureF_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['temperatureF_s']
print("humidity_required: ",humidity_required)
print('moisture_required: ',moisture_required)
print('sunlight_required: ',sunlight_required)
print('temperatureC_required: ',temperatureC_required)
print('temperatureF_required: ',temperatureF_required)


firebase = firebase.FirebaseApplication('https://automated-gardener-default-rtdb.firebaseio.com/', None)


while True:
    # humidity_sensor = random.randint(1,100) #change to sensor reading
    humidity = DHT.get_humidity()
    temperature_c = DHT.get_temperature_c()
    temperature_f = DHT.get_temperature_f()
    # moisture_sensor = random.randint(1,100) #change to sensor reading
    moisture = Moisture.moisture_reading()
    # sunlight_sensor = random.randint(1,100) #change to sensor reading
    visible_light = light_sensor.get_visible()
    uv_light = light_sensor.get_uv()
    ir_light = light_sensor.get_ir()
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'humidity', humidity)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'temperature in Celsius', temperature_c)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'temperature in Fahrenheit', temperature_f)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'moisture', moisture)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'visible light intensity', visible_light)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'uv light intensity', uv_light)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'ir light intensity', ir_light)

    time.sleep(5) #send data once an hour
    
