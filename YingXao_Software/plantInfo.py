from firebase import firebase

firebase = firebase.FirebaseApplication('https://plants-info-5b86b-default-rtdb.firebaseio.com/', None)
data = { 'PlantType':'Tulip', 'Watering':'60', 'Sunlight':'80',
         'PlantType':'Lily', 'Watering':'100', 'Sunlight':'20'}

result = firebase.post('/plants-info-5b86b-default-rtdb/plantDatabase', data)
