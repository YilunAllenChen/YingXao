from firebase import firebase

firebase = firebase.FirebaseApplication('https://plants-info-5b86b-default-rtdb.firebaseio.com/', None)
data = { 'Datatype':'humidity', 'Value':'60'}

result = firebase.get('/plants-info-5b86b-default-rtdb/plantDatabase', '')
print(result)