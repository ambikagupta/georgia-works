from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import json

#Insert into
def insert_Participant(Participant_Id, Last_Name, First_Name, DOB,
                       SSN, Address, Phone, Email, Home_Town,
                       Criminal_Background, Drug_Used, Assignment,
                       Sex, Case_Manager, Education, Medications,
                       Health_Conditions, Time_Homeless(Days),
                       Disabilites, Admin_Date):
    #wrap the participant idea

    query = "INSERT INTO Participants(Participant_Id, Last_Name, First_Name, DOB, SSN, Address, Phone, Email, Home_Town, Criminal_Background, Drug_Used, Assignment, Sex, Case_Manager, Education, Medications, Health_Conditions, Time_Homeless(Days), Disabilites, Admin_Date) "
     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

    args = (Participant_Id, Last_Name, First_Name, DOB, SSN,
            Address, Phone, Email, Home_Town, Criminal_Background,
            Drug_Used, Assignment, Sex, Case_Manager, Education,
            Medications, Health_Conditions, Time_Homeless(Days),
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

    query = "DELETE FROM Employees
             WHERE Employee_ID=%s "
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

#Update Participant
def update_Participant(attribute, newValue ,Participant_Id):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE Participant
                SET %s = %s
                WHERE Participant_Id = %s """

    data = (attribute, newValue ,Participant_Id)

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

#Update Employees
def update_Employees(attribute, newValue, Employee_Id):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE Employees
                SET %s = %s
                WHERE Employee_Id = %s """

    data = (attribute, newValue ,Employee_Id)

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


#Update Housing
def update_Housing(attribute, newValue ,Participant_Id, Housing_Assign):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE Housing
                SET %s = %s
                WHERE Paricipant_Id = %s AND Housing_Assign = %s """

    data = (attribute, newValue ,Participant_Id, Housing_Assign)

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


#Update Post_Grad
def update_Post_Grad(attribute, newValue ,Participant_Id):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE Post_Grad
                SET %s = %s
                WHERE Participant_Id = %s """

    data = (attribute, newValue ,Participant_Id)

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



#Update EC
def update_EC(attribute, newValue ,EC_Id):
    # read database configuration
    db_config = read_db_config()

    # prepare query and data
    query = """ UPDATE EC
                SET %s = %s
                WHERE EC_Id = %s """

    data = (attribute, newValue, EC_Id)

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

# return JSON object of Participants given Id
def get_Participant(Participant_Id):

    db_config = read_db_config()

    query = """ SELECT JSON_OBJECT('Participant_Id', %s)
                FROM Participants """

    data = (Participant_Id) #tuple

    try:
        conn = MySQLConnection(**db_config)

        # update table
        cursor = conn.cursor()
        cursor.execute(query, data) # cursor obj holds result
        result = cursor.fetchone() # resulting JSON object

        return result
    except Error as error:
        print(error)
    finally:
        #close database connections
        cursor.close()
        conn.close()

# get participant using last/first, ssn, or age
# returns JSON
def get_Participant(Last_Name=None, First_Name=None, ssn=None
                    age=None):
    ## WARNING: If using Last/First or Age, may have duplicates
    ## In which case, will choose the first one returned

    # require at least one param (Last/First is one param both be given)
    if (Last_Name == None or First_Name == None)
        and
        ssn == None
        and
        age == None:

        db_config = read_db_config()

        if (Last_Name != None and First_Name != None): # last/first given
            name_cond = "Last_Name: " + Last_Name
                          + " AND" +
                        "First_Name" + First_Name
        if (ssn != None):
            ssn_cond = "SSN: " + ssn
        if (age != None):
            age_cond = "Age: " + age

        conditional = ""
        if (name_cond != None):
            conditional += name_cond
        # insert AND
        if (ssn != None and conditional != ""):
            conditional += "AND"
            conditional += ssn_cond
        if (age != None and conditional != ""):
            conditional += "AND"
            conditional += age_cond

       query = """ SELECT Participant_Id FROM Participants
                   WHERE""" + conditional

    try:
        conn = MySQLConnection(**db_config)

        # update table
        cursor = conn.cursor()
        cursor.execute(query) # cursor obj holds result

        # get Participant_Id
        result = cursor.fetchone() # gets one row, query may give more than
                                   # one if using Last/First or age?

        return get_Participant(result) # use Participant_Id to get JSON
    except Error as error:
        print(error)
    finally:
        #close database connections
        cursor.close()
        conn.close()

# get employee
