from firebase import firebase
import time
import random

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
    humidity_sensor = random.randint(1,100) #change to sensor reading
    moisture_sensor = random.randint(1,100) #change to sensor reading
    sunlight_sensor = random.randint(1,100) #change to sensor reading
    temperatureC_sensor = random.randint(1,100) #change to sensor reading
    temperatureF_sensor = random.randint(1,100) #change to sensor reading
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'humidity_sensor', humidity_sensor)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'moisture_sensor', moisture_sensor)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'sunlight_sensor', sunlight_sensor)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'temperatureC_sensor', temperatureC_sensor)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'temperatureF_sensor', temperatureF_sensor)
    time.sleep(5) #send data once an hour
    