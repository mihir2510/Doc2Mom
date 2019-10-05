import pyrebase
from flask import *

config = {
	"apiKey": "AIzaSyBVYmavv3NHr7LQZBXvv1WX7ow2rvIOf6c",
    "authDomain": "loginout-e3746.firebaseapp.com",
    "databaseURL": "https://loginout-e3746.firebaseio.com",
    "projectId": "loginout-e3746",
    "storageBucket": "",
    "messagingSenderId": "1058894289685",
    "appId": "1:1058894289685:web:62383ea6de6e3041d6671c",
    "measurementId": "G-3ETTM6MP3W"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def login():
	unsucessful = 'Please enter correct credentials!'
	if(request.method == 'POST'):
		email = request.form['email']
		password = request.form['password']
		successful = 'Login Successful'+'\nWelcome! '+str(email)
		try:
			auth.sign_in_with_email_and_password(email,password)
			return render_template('dashboard.html',s=successful) 
		except:
			return render_template('index.html', us=unsucessful)
	return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)