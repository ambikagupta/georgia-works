import MySQLdb
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import json

partID = 5

def create_ID():
	partID = partID + 1
	return partID


#Insert into    
def insert_Participant(Last_Name, First_Name, DOB,
                       SSN, Address, Phone, Email, Home_Town,
                       Criminal_Background, Drug_Used, Assignment,
                       Sex, Case_Manager, Education, Medications,
                       Health_Conditions, Time_Homeless,
                       Disabilites, Admin_Date):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO Participants(Participants_Id, Last_Name, First_Name, DOB, SSN, Address, Phone," \
            "Email, Home_Town, Criminal_Background, Drug Used, Assignment, Sex, Case_Manager, Education," \
            " Medications, Health_Conditions,Time_Homeless, Disabilites, Admin_Date) " \
     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

     # Instead of Time
    args = (create_ID(), Last_Name, First_Name, DOB, SSN,
            Address, Phone, Email, Home_Town, Criminal_Background,
            Drug_Used, Assignment, Sex, Case_Manager, Education,
            Medications, Health_Conditions, Time_Homeless,
            Disabilites, Admin_Date)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_Employees(Employee_ID, First_Name, Last_Name, Job_Title, Phone, Address, Email, DOB, SSN, Sex):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO Employees(Employee_ID, First_Name, Last_Name, Job_Title, Phone, Address, Email, DOB, SSN, Sex)" \
     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

     # Instead of Time
    args = (Employee_ID, First_Name, Last_Name, Job_Title, Phone, Address, Email, DOB, SSN, Sex)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_EC(Participant_ID, Last_Name, First_Name, DOB, Address, Phone):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO EC(Participant_ID, Last_Name, First_Name, DOB, Address, Phone)" \
     "VALUES(%s,%s,%s,%s,%s,%s)"

     # Instead of Time
    args = (Participant_ID, Last_Name, First_Name, DOB, Address, Phone)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_PostGrad(Participant_ID, First_Name, Last_Name, Duration_GAW, Time_Homeless, Times_Arrested, Resolved_Barriers, Date_Hired, New_Job, New_Address, Zip, Starting_Wage, Last_Followup):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO Post_Grad(Participant_ID, First_Name, Last_Name, Duration_GAW, Time_Homeless, Times_Arrested, Resolved_Barriers, Date_Hired, New_Job, New_Address, Zip, Starting_Wage, Last_Followup)" \
     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

     # Instead of Time
    args = (Participant_ID, First_Name, Last_Name, Duration_GAW, Time_Homeless, Times_Arrested, Resolved_Barriers, Date_Hired, New_Job, New_Address, Zip, Starting_Wage, Last_Followup)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def insert_Housing(Participant_ID, Housing_Assign, Bed, Admin_Date, Exit_Date):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO Housing(Participant_ID, Housing_Assign, Bed, Admin_Date, Exit_Date)" \
     "VALUES(%s,%s,%s,%s,%s)"

     # Instead of Time
    args = (Participant_ID, Housing_Assign, Bed, Admin_Date, Exit_Date)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query, args)

        if cursor.lastrowid:
            print('last insert id', cursor.lastrowid)
        else:
            print('last insert id not found')

        conn.commit()
    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


#remove participant
def remove_Participant(Participant_Id):
    # remove participant based on Id;
    db_config = read_db_config();

    query = "DELETE FROM Participants WHERE Participant_ID=%s "
    data = (Participant_Id);

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

#remove participant
def remove_Employee(Employee_Id):
    # remove participant based on Id;
    db_config = read_db_config();

    query = "DELETE FROM Employees" \
            "WHERE Employee_ID=%s "
    data = (Employee_Id); # inserts into query in cursor.execute

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def remove_EC(Participant_Id):
    # remove participant based on Id;
    db_config = read_db_config();

    query = "DELETE FROM EC WHERE Participant_ID=%s "
    data = (Participant_Id);

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def remove_PostGrad(Participant_Id):
    # remove participant based on Id;
    db_config = read_db_config();

    query = "DELETE FROM Post_Grad WHERE Participant_ID=%s "
    data = (Participant_Id);

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

def remove_Housing(Participant_Id):
    # remove participant based on Id;
    db_config = read_db_config();

    query = "DELETE FROM Housing WHERE Participant_ID=%s "
    data = (Participant_Id);

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

#Update Participant
"""Updates a specific attribute in the Participants Database

Given an attribute name (one of the column headers), a new value (to replace/set),
and a specific participant (specified by their participant ID). The function 
updates the old value of the attribute to the given new value. 

Example:
    update_Participant('Last_Name',"'Cho'", 1)

Args:
    attribute: A string that contains the name of the attribute/column header.
    newValue: The value that will replace the current value (String or Int).
    Participant_Id: The unique participant ID for a specific participant.    
"""
def update_Participant(attribute, newValue ,Participant_Id):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE Participants
                SET %s = %s
                WHERE Participant_Id = %s """ %(attribute, newValue, Participant_Id)


    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

#Update Employees
def update_Employees(attribute, newValue, Employee_Id):
    # attribute: age
    # newValue: 18
    # employee ID ...

    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE Employees
                SET %s = %s
                WHERE Employee_Id = %s """ %(attribute, newValue, Employee_Id)

    #data = (attribute, newValue ,Employee_Id)

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query)#, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


#Update Housing
"""Updates a specific attribute in the Housing Database

Given an attribute name (one of the column headers), a new value (to replace/set), 
a specific participant (specified by their participant ID), and a housing assignment value. 
The function updates the old value of the attribute to the given new value. 

Example:
    update_Housing('Housing_Assign', "'Q'", 1, "'A'")

Args:
    attribute: A string that contains the name of the attribute/column header.
    newValue: The value that will replace the current value (String or Int).
    Participant_Id: The unique participant ID for a specific participant.
    Housing_Assign: The housing assignment value/letter that the participant is assigned to.    
"""
def update_Housing(attribute, newValue ,Participant_Id, Housing_Assign):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE Housing
                SET %s = %s
                WHERE Participant_Id = %s AND Housing_Assign = %s """ %(attribute, newValue, Participant_Id, Housing_Assign)

    #data = (attribute, newValue ,Participant_Id, Housing_Assign)

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query)#, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()


#Update Post_Grad
"""Updates a specific attribute in the Post Graduation Database

Given an attribute name (one of the column headers), a new value (to replace/set),
and a specific participant (specified by their participant ID). The function 
updates the old value of the attribute to the given new value. 

Example:
    update_Post_Grad('Starting_Wage', "'$ 15.00 / hr.'", 233)

Args:
    attribute: A string that contains the name of the attribute/column header.
    newValue: The value that will replace the current value (String or Int).
    Participant_Id: The unique participant ID for a specific participant.    
"""
def update_Post_Grad(attribute, newValue, Participant_Id):
    #

    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE Post_Grad
                SET %s = %s
                WHERE Participant_Id = %s """ %(attribute, newValue, Participant_Id)

    #data = (attribute, newValue ,Participant_Id)

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query)#, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()



#Update EC
"""Updates a specific attribute in the Emergency Contact Database

Given an attribute name (one of the column headers), a new value (to replace/set),
and a specific participant (specified by their participant ID). The function 
updates the old value of the attribute to the given new value. 

Example:
    update_EC('Last_Name',"'Pump'", 2)

Args:
    attribute: A string that contains the name of the attribute/column header.
    newValue: The value that will replace the current value (String or Int).
    Participant_Id: The unique participant ID for a specific participant.    
"""
def update_EC(attribute, newValue, Participant_Id):
    # emergency contact
    # holds one Participant ID within each unique EC_Id

    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE EC
                SET %s = %s
                WHERE Participant_Id = %s """ %(attribute, newValue, Participant_Id)

    #data = (attribute, newValue, EC_Id)

    try:
        conn = MySQLConnection(**db_config)

        # update book title
        cursor = conn.cursor()
        cursor.execute(query)#, data)

        # accept the changes
        conn.commit()

    except Error as error:
        print(error)

    finally:
        cursor.close()
        conn.close()

# return JSON object of Participants given Id
"""Fetches all row elements based on a given ID in the Participants Database

Returns a JSON object/array containing the information of a specific participant given their participant ID.

Example:
    get_Participant(22)

Args:
    Participant_Id: The unique participant ID for a specific participant.

Returns:
    A JSON object/array that contains the attributes of a specific participant. Each of the 36
    attributes in the row is represented within the array. For example:

        (Participant_Id, Duration, Last_Name, First_Name, Job, DOB, SSN, Address, Phone, Email, Home_Town, Prior_Felony,
        Num_Times, Drug Used, Assignment, Sex, CM, Education, TABE Score, Medications, Health_Conditions, Time_Homeless,
        Time_Since_LJ, Work_Exp, Disabilities, Admin_Date, Program_Date, Recent DT Result, DT Result, Years in ATL,
        Veteren, SNAP, Liscense, BGC, BGC Comments)
"""
def get_Participant(Participant_Id):

    db_config = read_db_config()

    query = """ SELECT * FROM Participants WHERE participants.participant_Id = %s
    """ %Participant_Id

    #data = (Participant_Id) #tuple

    try:
        conn = MySQLConnection(**db_config)

        # update table
        cursor = conn.cursor()
        cursor.execute(query)#, data) # cursor obj holds result
        result = cursor.fetchone() # resulting JSON object

        return result
    except Error as error:
        print(error)
    finally:
        #close database connections
        cursor.close()
        conn.close()

# TODO: Make get_Participant for ALL participants
# get participant using last/first, ssn, or age
# returns JSON

# TODO: Create an Employee table or a new database
# All of the functions that deal with employees are 
# useless because no such table/database exists.
#
# update_Employees(attribute, newValue, Employee_Id)
# remove_Employee(Employee_Id)
# insert_Employees(Employee_ID, First_Name, Last_Name, Job_Title, Phone, Address, Email, DOB, SSN, Sex)

"""
Backend Testing:
"""
#print(get_Participant(22))
#update_Participant('Last_Name',"'GOEFEA'", 1)

#update_EC('Last_Name', "'Pump'", 2)

#update_Post_Grad('Starting_Wage', "'$ 15.00 / hr.'", 233)
#The only problem is some columns have to be formatted correctly
#before an update is done: Starting_Wage needs to be formatted like
# $ (number) / hr.

#update_Housing('Housing_Assign', "'Q'", 1, "'A'")
#Participant_Id, Housing_Assign, Bed, Admin_Date, Exit_Date
