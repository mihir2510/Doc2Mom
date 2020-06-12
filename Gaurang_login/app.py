import pyrebase
from flask import *

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