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
            return render_template('insert_form.html')
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

@app.route('/tables')
def showTables():
    return render_template('tables.html')

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
        params = {
            'Participant_Id': int(request.form['id']), 
            'Last_Name': str('' + request.form['lastname']), 
            'First_Name': str('' + request.form['firstname']), 
            'DOB': str('' + request.form['dob']),
            'SSN': str('' + request.form['ssn']), 
            'Address': str('' + request.form['address']), 
            'Phone': str('' + request.form['phone']), 
            'Email': str('' + request.form['email']), 
            'Home_Town': str('' + request.form['hometown']),
            'Prior_Felony': str('' + request.form['priorfelony']), 
            'Drug_Used': str('' + request.form['drugsused']), 
            'Assignment': str('' + request.form['assignment']),
            'Sex': str('' + request.form['sex']), 
            'Case_Manager': str('' + request.form['casemanager']), 
            'Education': str('' + request.form['education']), 
            'Medications': str('' + request.form['medications']),
            'Health_Conditions': str('' + request.form['healthconditions']), 
            'Time_Homeless': str('' + request.form['timehomeless']),
            'Disabilites': str('' + request.form['disabilities']),
            'Admin_Date': str('' + request.form['admindate'])
        }

        backend.insert_Participant(params['Participant_Id'], params['Last_Name'], params['First_Name'], params['DOB'], params['SSN'], params['Address'], params['Phone'], params['Email'], params['Home_Town'], params['Prior_Felony'], params['Drug_Used'], params['Assignment'], params['Sex'], params['Case_Manager'], params['Education'], params['Medications'], params['Health_Conditions'], params['Time_Homeless'], params['Disabilites'], params['Admin_Date'])
        #print(params[0])
        if not params:
            errors = 'Error! Duplicate client found'
        if not errors:

            success = 'Success! Client added'
            return render_template('insert_form.html', success = success)
    return render_template('insert_form.html', errors = errors)

@app.route("/register")
def show_register():
    return render_template('register.html')



if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
