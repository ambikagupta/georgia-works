from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        print ("not logged in")
        return render_template('login.html')
    else:
        print ("logged in ")
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    print ("admin login")
    print (request.form["password"])
    if request.form["password"] == 'password' and request.form["username"] == 'admin':
        print ("top if")
        session['logged_in'] = True
    else:
        print ("bot if")
    print ("return home")
    return home()

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/forgot")
def forgotPassword():
    return render_template('forgot.html')

@app.route("/forgot", methods=['POST'])
def passwordReset():
    return "Hello"

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
