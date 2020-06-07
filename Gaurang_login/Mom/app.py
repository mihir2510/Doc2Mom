import pyrebase 
from firebase import firebase
config = {
	"apiKey": "",
    "authDomain": "",
    "databaseURL": "",
    "projectId": "",
    "storageBucket": "",
    "messagingSenderId": "",
    "appId": "",
    "measurementId": ""
}

firebase1 = pyrebase.initialize_app(config)

db = firebase1.database()

from flask import *

app = Flask(__name__)

@app.route('/')
def basic():
	if request.method == 'POST':
		if request.form['submit'] == 'add':
			name = request.form['name']
			db.child(str(name)).push(name)
			todo = db.child("todo").get()
			to = todo.val()
			#firebase2 = firebase.FirebaseApplication('https://fir-858f5.firebaseio.com/', None)
			#result = firebase2.get('/users', None)
			#print(result)
			return render_template('index.html', t=to.values())
		elif request.form['submit'] == 'delete':
			db.child("todo").remove()
		elif request.form['submit'] == 'display':
			todo = db.child("todo").get()
			to = todo.val()
			return render_template('qwerty.html', t=to.values())
		return render_template('qwerty.html')
	return render_template('qwerty.html')

if __name__ == '__main__':
	app.run(debug=True)