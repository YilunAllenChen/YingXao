from firebase import firebase
import time
import random

plantType = 'tulip' #change to customer's choice

plantInfo = firebase.FirebaseApplication('https://plants-info-5b86b-default-rtdb.firebaseio.com/', None)
result = plantInfo.get('/plants-info-5b86b-default-rtdb/plantDatabase', '')
humidity_required = result['-MU1BUKe1WbCZzV9npSN'][plantType]['humidity_s'] #standard humidity
sunlight_required = result['-MU1BUKe1WbCZzV9npSN'][plantType]['sunlight_s'] #standard sunlight
print(humidity_required)
print(sunlight_required)

firebase = firebase.FirebaseApplication('https://automated-gardener-default-rtdb.firebaseio.com/', None)
# data = {'humidity_sensor':0 , 'sunlight_sensor':'0'}
# 
# result = firebase.post('/automated-gardener-default-rtdb/realtime plant value/user1', data)

while True:
    humidity_sensor = random.randint(1,100) #change to sensor reading
    sunlight_sensor = random.randint(1,100) #change to sensor reading
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'humidity_sensor', humidity_sensor)
    firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'sunlight_sensor', sunlight_sensor)
    time.sleep(5) #send data once an hour
    