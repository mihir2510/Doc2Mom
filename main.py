from pprint import pprint as pp
from flask import Flask, flash, redirect, render_template, request, url_for
import pyrebase
from flask import *

config = {
  "apiKey": "AIzaSyDJnFzPavlkBjV6qwOI0JdyngqukOKtoL0",
  "authDomain": "doc2-28123.firebaseapp.com",
  "databaseURL": "https://doc2-28123.firebaseio.com",
  "projectId": "doc2-28123",
  "storageBucket": "",
  "messagingSenderId": "897488738576",
  "appId": "1:897488738576:web:424ff33ff93cb401eb2d95",
  "measurementId": "G-HJ32FYCXCK"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

app = Flask(__name__)

@app.route('/')
def index():
    users = db.child("doctors").get()
    print(users.val())
    for row in users.each():
        print(row)
    return render_template('index.html')

@app.route('/sw.js', methods=['GET'])
def sw():
    return app.send_static_file('js/sw.js')

@app.route('/mom_login', methods=['GET','POST'])
def mom_login():
#    print('here')
    if(request.method == 'POST'):
        print('here2')
        email = request.form['id']
        password = request.form['pass']
        try:
            auth.sign_in_with_email_and_password(email,password)
            all_users = db.child("mothers").get()
            for user in all_users.each():
                if user.val()['email'] == email:
                    key = user.key()
                    print(key)
            print('here3')
            return redirect(url_for('mom_home', id=key))
        except:
            print('here4')
            return render_template('mom_login.html', us = True)  
    return render_template('mom_login.html')   

@app.route('/doc_login', methods=['GET','POST'])
def doc_login():
#    print('here')
    if(request.method == 'POST'):
        print('here2')
        email = request.form['id']
        password = request.form['pass']
        key = ''
        try:
            auth.sign_in_with_email_and_password(email,password)
            all_users = db.child("doctors").get()
            for user in all_users.each():
                if user.val()['email'] == email:
                    key = user.key()
                    print(key)
                # print(user.key()) # Morty
                # print(user.val()['email']) # {name": "Mortimer 'Morty' Smith"}
            print('here3')
            return redirect(url_for('doc_home', id=key))
        except:
            print('here4')
            return render_template('doc_login.html', us = True)  
    return render_template('doc_login.html')   

@app.route('/mom_home/<id>')
def mom_home(id):
    return render_template('mom_home.html')  

@app.route('/doc_home/<id>')
def doc_home(id):
    all_users = db.child("doctors").get()
    for user in all_users.each():
        if user.key()==id:
            print(user.val()['patients'])
            print(len(user.val()['patients']))
            print('bhagwan')
            req_moms = []
            patients = user.val()['patients']
            all_moms = db.child("mothers").get()
            for mom in all_moms.each():
                if mom.key() in patients:
                    req_moms.append(mom.val())
                    patients.remove(mom.key())
                if len(patients) == 0:
                    break

    return render_template('doc_home.html', key = id, moms = req_moms)

@app.route('/doc_add_mom/<id>', methods=['GET','POST'])
def add_mom(id):
    print(id)
    if request.method == 'POST':
        email = request.form['email']
        name = request.form['name']
        contact = request.form['contact']
        bldgrp = request.form['bldgrp']
        dtb = request.form['dtb']
        data = {
            "email" : email,
            "name" : name,
            "contact" : contact,
            "bldgrp" : bldgrp,
            "dtb" : dtb,
            "father_name" : ''        
        }
        db.child("mothers").child(contact).set(data)
        password = name+name
        auth.create_user_with_email_and_password(email, password)
        all_users = db.child("doctors").get()
        for user in all_users.each():
            if user.key()==id:
                if len(user.val()['patients']) == 0:
                    numbers = [contact]
                else:
                    numbers = user.val()['patients']
                    numbers.append(contact)
                db.child("doctors").child(id).update({"patients":numbers})
                print(user.val()['patients'])
                # print(len(user.val()['patients']))
                print('bhagwan')
    return render_template('doc_unique_code.html', key=id)

@app.route('/doc_reports/<id>')
def doc_reports(id):
    print(id)
    all_moms = db.child("mothers").get()
    for mom in all_moms.each():
        if mom.key()==id:
            print(mom.val())
        return render_template('doc_reports.html', deets = mom.val())

@app.route('/mom_reports')
def mom_reports():
    return render_template('mom_reports.html')

@app.route('/add_doc', methods=['GET', 'POST'])
def add_doc():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        name = request.form['name']
        phone = request.form['phone']
        data = {
            "name": name,
            "email": email,
            "phone": phone,
            "patients": ''                
        }
        db.child("doctors").child(phone).set(data)
        auth.create_user_with_email_and_password(email, password)

    return render_template('newdoc.html')

if __name__=='__main__':
    app.run(debug=True)