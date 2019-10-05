from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
#from flask_ngrok import run_with_ngrok

app = Flask(__name__)
#run_with_ngrok(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('js/sw.js')

@app.route('/mom1')
def mom1():
    return render_template('mom1.html')   

if __name__=='__main__':
    app.run(debug=True)