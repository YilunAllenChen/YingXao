from firebase import firebase
import time
import random
# import MoistureSensor.Moisture as Moisture 
# import DHT22.DHT22 as DHT
# import SI1145.SI1145 as light_sensor
plantType = 'lily' #change to customer's choice

plantInfo = firebase.FirebaseApplication('https://plants-info-5b86b-default-rtdb.firebaseio.com/', None)
# plantInfo.put('/plants-info-5b86b-default-rtdb/plantDatabase/-MUZV5yiF3xw9A9wqEMl/lily', 'sunlightTime_s', 3)
# plantInfo.put('/plants-info-5b86b-default-rtdb/plantDatabase/-MUZV5yiF3xw9A9wqEMl/tulip', 'sunlightTime_s', 8)
result = plantInfo.get('/plants-info-5b86b-default-rtdb/plantDatabase', '')

#dataType can be 'humidity_s', 'moisture_s', 'sunlight_s', 'temperatureC_s', 'temperatureF_s', 'sunlightTime_s'
def get_data(dataType):
	return result['-MUZV5yiF3xw9A9wqEMl'][plantType][dataType]
	

humidity_required = get_data('humidity_s')             #sample test
# moisture_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['moisture_s']
# sunlight_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['sunlight_s'] #standard sunlight
# temperatureC_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['temperatureC_s']
# temperatureF_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['temperatureF_s']
# #sunlightTime_required = result['-MUZV5yiF3xw9A9wqEMl'][plantType]['sunlightTime']
# print("humidity_required: ",humidity_required)			#sample test
# print('moisture_required: ',moisture_required)
# print('sunlight_required: ',sunlight_required)
# print('temperatureC_required: ',temperatureC_required)
# print('temperatureF_required: ',temperatureF_required)

firebase = firebase.FirebaseApplication('https://automated-gardener-default-rtdb.firebaseio.com/', None)

def upload_data(dataTuple):
	firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', dataTuple[0], dataTuple[1])

if __name__ == "__main__":
    while True:
        #humidity_sensor = random.randint(1,100) #change to sensor reading
        humidity = DHT.get_humidity()                        #sample test case
        humidityTuple = ('humidity', humidity)

        temperature_c = DHT.get_temperature_c()
        temperature_cTuple = ('temperature in Celsius', temperature_c)
        
        temperature_f = DHT.get_temperature_f()
        temperature_fTuple = ('temperature in Fahrenheit', temperature_f)
        #moisture_sensor = random.randint(1,100) #change to sensor reading
        moisture = Moisture.moisture_reading()
        moistureTuple = ('moisture', moisture)
        #sunlight_sensor = random.randint(1,100) #change to sensor reading
        visible_light = light_sensor.get_visible()
        visible_lightTuple = ('visible light intensity', visible_light)

        uv_light = light_sensor.get_uv()
        uv_lightTuple = ('uv light intensity', uv_light)

        ir_light = light_sensor.get_ir()
        ir_lightTuple = ('ir light intensity', ir_light)

        upload_data(humidityTuple)												#sample test case

        # firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'humidity', humidity)
        # firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'temperature in Celsius', temperature_c)
        # firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'temperature in Fahrenheit', temperature_f)
        # firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'moisture', moisture)
        # firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'visible light intensity', visible_light)
        # firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'uv light intensity', uv_light)
        # firebase.put('/automated-gardener-default-rtdb/realtime-plant-value/user1', 'ir light intensity', ir_light)
        print("upload success")
        time.sleep(5) #send data once an hour
