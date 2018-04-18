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
        elif request.form['submit'] == 'search':
            return render_template('search.html')
        elif request.form['submit'] == 'remove':
            return render_template('remove.html')
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

@app.route("/editdisplay", methods=['POST'])
def do():
    value = '' + request.form["value1"]
    parameter = '' + request.form["parameter1"]
    value2 = '' + request.form["value2"]
    parameter2 = '' + request.form['parameter2']
    items = backend.search(parameter, value, parameter2, value2)
    print(backend.search(parameter, value, parameter2, value2))
    return render_template('tables.html', **locals())

@app.route("/remove", methods=['POST'])
def remove():
    errors = ''
    success = ''
    if not request.form['id']:
        errors = "Action failed: Missing Participant Id"
        return render_template('remove.html', **locals())
    else:
        backend.remove_Participant(request.form['id'])
        success = "Participant successfully removed!"
        return render_template('remove.html', **locals())

@app.route("/submitted", methods=['GET', 'POST'])
def submit_client():
    errors = ''
    success = ''
    items = []
    if request.method == "GET":
        return render_template('tables.html', **locals())
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


        ## TODO CHECK THIS
        backend.insert_Participant(params['Participant_Id'], params['Last_Name'], params['First_Name'], params['DOB'], params['SSN'], params['Address'], params['Phone'], params['Email'], params['Home_Town'], params['Prior_Felony'], params['Drug_Used'], params['Assignment'], params['Sex'], params['Case_Manager'], params['Education'], params['Medications'], params['Health_Conditions'], params['Time_Homeless'], params['Disabilites'], params['Admin_Date'])
        #print(params[0])
        if not params:
            errors = 'Error! Duplicate client found'
        if not errors:

            success = 'Success! Client added'
            participant = backend.get_Participant(params['Participant_Id'])
            items.append(participant)
            # pid = participant[0] 
            # lastname = participant[2]
            # firstname = participant[3]
            # dob = participant[5]
            # ssn = participant[6]
            # address = participant[7]
            # phone = participant[8]
            # email = participant[9]
            # town = participant[10]
            # felony = participant[11]
            # drugs = participant[13]
            # assignment = participant[14]
            # sex = participant[15]
            # cm = participant[16]
            # education = participant[17]
            # medication = participant[19]
            # health = participant[20]
            # homeless = participant[21]
            # disabilities = participant[24]
            # admin = participant[25]
            return render_template('tables.html', **locals())
    return render_template('insert_form.html', errors = errors)

@app.route("/register")
def show_register():
    return render_template('register.html')

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.debug = True
    app.run()
