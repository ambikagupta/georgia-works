from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__)

@app.route('/')
def home():
    if not session.get('logged_in'):
        return render_template('login.html')
    else:
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    print (request.form["password"])
    if request.form["password"] == 'password' and request.form["username"] == 'admin':
        session['logged_in'] = True
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

@app.route("/tables")
def show_tables():
    return render_template('tables.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
