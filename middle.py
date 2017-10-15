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

@app.route('/form', methods=['GET', 'POST'])
def new_clientform():
    if request.method == 'POST':
        if request.form['submit'] == 'newclient':
            return render_template('newclientform.html')
        elif request.form['submit'] == 'editclient':
                 return render_template('editclientform.html')
        else:
            pass
    elif request.method == 'GET':
        return render_template('index.html')

@app.route('/login', methods=['POST'])
def do_admin_login():
    print (request.form["password"])
    if request.form["password"] == 'password' and request.form["username"] == 'admin':
        session['logged_in'] = True
    return home()

@app.route('/charts')
def charts():
    return render_template('charts.html')

@app.route("/logout")
def logout():
    session['logged_in'] = False
    return home()

@app.route("/forgot")
def forgotPassword():
    return render_template('forgot-password.html')

@app.route("/forgot", methods=['POST'])
def passwordReset():
    return "Hello"

@app.route("/tables")
def show_tables():
    return render_template('tables.html')

@app.route("/register")
def show_register():
    return render_template('register.html')



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
