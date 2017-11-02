from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os
import backend

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
    print(request.form["password"])

    if request.form["password"] == 'password' and request.form["username"] == 'admin':
        session['logged_in'] = True
    return home()

@app.route('/register.html')
def register():
    return render_template('register.html')

#@app.route('/register', methods=['GET', 'POST'])
#def submit_register():
#    print(request.form["exampleInputName"])
#   print(request.form["exampleInputLastName"])
#    db = backend.dbConnect()
#    db.cursor().execute("INSERT INTO users (username, firstName, lastName, password, email, usertype)" +
#     "VALUES ('admin3', 'Param', 'Ri', 'paramPass','param@hello.com', 'admin');")
#    return home()

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

@app.route("/submitted", methods=['GET', 'POST'])
def submit_client():
    errors = ''
    success = ''
    if request.method == "GET":
        return render_template('tables.html')
    else:
        #check params again, some dont fit the form, also need to check if query was successful
        params {
            '_first' = request.form['firstname']
            '_last' = request.form['lastname']
            '_dob' = request.form['birthdate']
            '_ssn' = request.form['ssn']
            '_addr' = request.form['zip']
            '_phone' = request.form['phonenum']
            '_email' = ''
            '_hometown' = request.form['lastcity']
            '_criminalbg' = request.form['arrest']
            '_druguse' = request.form['drugs']
            '_assgn' = ''
            '_sex' = request.form['gender']
            '_casemgr' = ''
            '_edu' = request.form['edu']
            '_meds' = ''
            '_health' = request.form['health']
            '_homeless' = request.form['homelessyears']
            '_disabilities' = request.form['restr']
            '_admindate' = '';
            backend.insert_Participant(params[0], params[1], params[2], params[3], params[4], params[5], params[6], params[7], params[8], params[9], params[10], params[11], params[12], params[13], params[14], params[15], params[16], params[17], params[18])
        }
        if not params:
            errors = 'Error! Duplicate client found'
        if not errors:

            success = 'Success! Client added'
            return render_template('newclientform.html', success = success)
    return render_template('newclientform.html', errors = errors)

@app.route("/register")
def show_register():
    return render_template('register.html')



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
