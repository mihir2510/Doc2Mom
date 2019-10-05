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

@app.route('/mom_login')
def mom_login():
    return render_template('mom_login.html')   

@app.route('/doc_login')
def doc_login():
    return render_template('doc_login.html') 

@app.route('/mom_home')
def mom_home():
    return render_template('mom_home.html')         

@app.route('/mom_reports')
def mom_reports():
    return render_template('mom_reports.html')


if __name__=='__main__':
    app.run(debug=True)