from firebase import firebase

firebase = firebase.FirebaseApplication('https://automated-gardener-default-rtdb.firebaseio.com/', None)
data = { 'Datatype':'humidity', 'Value':'60'}

result = firebase.post('/automated-gardener-default-rtdb/realtime plant value', data)