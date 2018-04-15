import MySQLdb
from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
import json

"""
How does Georgia Works generate Ids for the clients?
    -Should the Ids be auto-generated in the table?
    -Are they assigned in-house and are separate from the table's rows
    -If they way they generate Ids is different, implement that in
    the create_ID() function.
    -The functions are currently formatted to work with Participant_Ids
    that are not auto-generated and must be entered.
"""
partID = 5
def create_ID():
	return partID + 1

"""
Change Notes:
    -Reverted back to using Participant_Id (no auto-incrementing primary key)
    -Criminal_Background is replaced by Prior_Felony
"""


#Insert into  
"""

-Currently works but does not include all the column headers possible.

Inserts a new participant into the Participants database.

Given all of the initial information about a participant, the participant
is added to the Participants database.

Example:
    insert_Participant("'501'", "'Aaron'", "'Brooks'", "'6/27/2017'", "'000-00-0000'", 
    "'120 North Avenue Northwest'", "'000-000-0000'", "'abc@gmail.com'", "'Atlanta'", 
    "'Perjury'", "'Heroin'", "'Assignment'", "'M'", "'CM'", "'7th Grade'", "'Xanax'", 
    "'Ebola'", "'7 years'", "'Dyslexia'", "'3/31/18'")

Args:
    Participant_Id: The unique participant ID for a specific participant.  
    Last_Name: The last name of the participant. ("'Last_Name'")
    First_Name: The first name of the participant. ("'First_Name'")
    DOB: The date of birth of the participant. ("'MM/DD/YYYY'")
    SSN: The social security number of the participant. ("'xxx-xx-xxxx'")
    Address: The current/previous address of the participant. ("'Address'")
    Phone: The current phone number of the participant. ("'xxx-xxx-xxxx'")
    Email: The email address of the participant. ("'email@email.com'")
    Home_Town: The home town of the participant. ("'Home_Town'")
    Prior_Felony: The prior felonies the participant has. ("'Prior_Felony'")
    Drug_Used: The drugs the participant has used. ("'Drug_Used'") 
    Assignment: The assignment of the participant. ("'Assignment'")
    Sex: The sex of the participant ("'Sex'")
    Case_Manager: The case manager assigned to the participant. ("'Case_Manager'")
    Education: The highest level of education of the participant. ("'Education'")
    Medications: The medications the participant needs. ("'Medications'")
    Health_Conditions: The health conditions the participant has. ("'Health_Conditions'")
    Time_Homeless: The time the participant has spent homeless. ("'Time_Homeless'")
    Disabilities: The disabilities the participant has. ("'Disabilities'")
    Admin_Date: The date the participant was administered into the program. ("'Admin_Date'")
"""  
def insert_Participant(Participant_Id, Last_Name, First_Name, DOB,
                       SSN, Address, Phone, Email, Home_Town,
                       Prior_Felony, Drug_Used, Assignment,
                       Sex, Case_Manager, Education, Medications,
                       Health_Conditions, Time_Homeless,
                       Disabilites, Admin_Date):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID
    print(DOB)

    ## TODO CHECK QUOTATIONS ON ALL OF THESE
    query = "INSERT INTO Participants(Participant_Id, Last_Name, First_Name, DOB, SSN, Address, Phone," \
            "Email, Home_Town, Prior_Felony, Drug_Used, Assignment, Sex, CM, Education," \
            " Medications, Health_Conditions,Time_Homeless, Disabilites, Admin_Date) " \
     "VALUES(\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\",\"%s\")" %(Participant_Id, Last_Name, First_Name, DOB, SSN,
            Address, Phone, Email, Home_Town, Prior_Felony,
            Drug_Used, Assignment, Sex, Case_Manager, Education,
            Medications, Health_Conditions, Time_Homeless,
            Disabilites, Admin_Date)
    print(DOB)
    print(Admin_Date)
    print(query)

     # Instead of Time
    # args = (create_ID(), Last_Name, First_Name, DOB, SSN,
    #         Address, Phone, Email, Home_Town, Criminal_Background,
    #         Drug_Used, Assignment, Sex, Case_Manager, Education,
    #         Medications, Health_Conditions, Time_Homeless,
    #         Disabilites, Admin_Date)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)#, args)

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

"""
The employee database still doesn't exist yet.
"""
def insert_Employees(Employee_Id, First_Name, Last_Name, Job_Title, Phone, Address, Email, DOB, SSN, Sex):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO Employees(Employee_Id, First_Name, Last_Name, Job_Title, Phone, Address, Email, DOB, SSN, Sex)" \
     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" %(Employee_Id, First_Name, Last_Name, Job_Title, Phone, Address, Email, DOB, SSN, Sex)

     # Instead of Time
    #args = (Employee_ID, First_Name, Last_Name, Job_Title, Phone, Address, Email, DOB, SSN, Sex)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)#, args)

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

"""
-Change any text-based fields to use text instead of varchar()
Inserts a new participant into the Participants database.

Inserts an emergency contact into the EC database.

Given a participant id that exists in the Participants database, a first name,
a last name, a date of birth, an address, and a phone number the emergency contact 
is added to the Emergency Contact database.

Example:
    insert_EC(6, "'Cho'", "'Austin'", "'11/11/2011'", "'Some Address, GA'", "'404-404-404'")

Args:
    Participant_Id: The unique participant ID for a specific participant.  
    Last_Name: The last name of the participant. ("'Last_Name'")
    First_Name: The first name of the participant. ("'First_Name'")
    DOB: The date of birth of the participant. ("'MM/DD/YYYY'")
    SSN: The social security number of the participant. ("'xxx-xx-xxxx'")
    Address: The current/previous address of the participant. ("'Address'")
    Phone: The current phone number of the participant. ("'xxx-xxx-xxxx'")
"""
def insert_EC(Participant_Id, Last_Name, First_Name, DOB, Address, Phone):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO EC(Participant_Id, Last_Name, First_Name, DOB, Address, Phone)" \
     "VALUES(%s,%s,%s,%s,%s,%s)" %(Participant_Id, Last_Name, First_Name, DOB, Address, Phone)

     # Instead of Time
    #args = (Participant_ID, Last_Name, First_Name, DOB, Address, Phone)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)#, args)

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

"""
-Should change a bunch of text based fields in the SQL database as: text instead of some varchar() amount

Inserts an post graduate into the PostGrad database.

Given a participant id and the information associated with a postgraduate,
the postgraduate is added to the PostGrad database.

Example:
    insert_PostGrad(7, "'Austin'", "'Cho'", 202, 20, 100, "'Homelessness, Addiction'", 
    "'3/31/2018'", "'Student at Georgia Tech'", "'120 North Avenue Northwest'", 
    "'30313'", "'$ 999.99 / hr.'", "'3/30/2018'")

Args:
    Participant_Id: The unique participant ID for a specific participant.  
    First_Name: The first name of the participant. ("'First_Name'")
    Last_Name: The last name of the participant. ("'Last_Name'")
    Duration_GAW: The amount of time in weeks spent at Georgia Works. (Duration_GAW)
    Time_Homeless: The amount of time spent homeless. (Time_Homeless)
    Times_Arrested: The amount of times arrested. (Times_Arrested)
    Resolved_Barriers: The resolved barriers at Georgia Works. ("'Resolved_Barriers'")
    Date_Hired: The date the postgrad was hired. ("'mm/dd/yyyy'")
    New_Job: The new job the postgrad has. ("'New_Job'")
    New_Address: The postgrad's current address. ("'New_Address'")
    Zip: The current zip code of the postgrad. ("'Zip'")
    Starting_Wage: The startin wage of the postgrad. ("'$ Starting_Wage / hr.'")
    Last_Followup: The date of the last followup with Georgia Works. ("'mm/dd/yyyy'")
    New_Address: The current/previous address of the participant. ("'Address'")
"""
def insert_PostGrad(Participant_Id, First_Name, Last_Name, Duration_GAW, Time_Homeless, Times_Arrested, Resolved_Barriers, Date_Hired, New_Job, New_Address, Zip, Starting_Wage, Last_Followup):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO Post_Grad(Participant_Id, First_Name, Last_Name, Duration_GAW, Time_Homeless, Times_Arrested, Resolved_Barriers, Date_Hired, New_Job, New_Address, Zip, Starting_Wage, Last_Followup)" \
     "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)" %(Participant_Id, First_Name, Last_Name, 
                                                        Duration_GAW, Time_Homeless, Times_Arrested, 
                                                        Resolved_Barriers, Date_Hired, New_Job, 
                                                        New_Address, Zip, Starting_Wage, Last_Followup)

     # Instead of Time
    #args = (Participant_ID, First_Name, Last_Name, Duration_GAW, Time_Homeless, Times_Arrested, Resolved_Barriers, Date_Hired, New_Job, New_Address, Zip, Starting_Wage, Last_Followup)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)#, args)

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

"""
insert_Housing(1, "'D'", "'7'", "'10/11/2012'", "'11/13/2013'")
The Participant_Id must exist in the Participant database already for the function to work.
"""
def insert_Housing(Participant_Id, Housing_Assign, Bed, Admin_Date, Exit_Date):
    #wrap the participant idea

    # GENERATE A PARTICIPANT ID

    query = "INSERT INTO Housing(Participant_Id, Housing_Assign, Bed, Admin_Date, Exit_Date)" \
     "VALUES(%s,%s,%s,%s,%s)" %(Participant_Id, Housing_Assign, Bed, Admin_Date, Exit_Date)

     # Instead of Time
    #args = (Participant_ID, Housing_Assign, Bed, Admin_Date, Exit_Date)

    try:
        db_config = read_db_config()
        conn = MySQLConnection(**db_config)

        cursor = conn.cursor()
        cursor.execute(query)#, args)

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
"""Removes a participant from the Participants Database given an ID

Given a participant (specified by their participant ID), the entry/row
is removed from the database.

Example:
    remove_Participant(6)

Args:
    Participant_Id: The unique participant ID for a specific participant.    
"""
def remove_Participant(Participant_Id):
    # remove participant based on Id;
    db_config = read_db_config();

    query = "DELETE FROM Participants WHERE Participant_ID=%s " %(Participant_Id)
    #data = (Participant_Id);

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

#remove an employee
"""Removes an employee from the Employees Database given an ID

Given an employee (specified by an ID), the entry/row
is removed from the database.

Example:
    remove_EC()

Args:
    Employee_Id: The unique participant ID for a specific emergency contact.    
"""
def remove_Employee(Employee_Id):
    # remove participant based on Id;
    db_config = read_db_config();

    query = "DELETE FROM Employees" \
            "WHERE Employee_ID=%s " %(Employee_Id)
   # data = (Employee_Id); # inserts into query in cursor.execute

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

# remove emergency contact based on Id;
"""Removes emergency contact from the EC Database given an ID

Given an emergency contact (specified by an ID), the entry/row
is removed from the database.

Example:
    remove_EC(1)

Args:
    Participant_Id: The unique participant ID for a specific emergency contact.    
"""
def remove_EC(Participant_Id):
    db_config = read_db_config();

    query = "DELETE FROM EC WHERE Participant_ID=%s " %(Participant_Id)
    #data = (Participant_Id);

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

# remove post graduate based on Id;
"""Removes post graduate from the post_grad Database given an ID

Given a post graduate (specified by an ID), the entry/row
is removed from the database.

Example:
    remove_PostGrad(233)

Args:
    Participant_Id: The unique participant ID for a specific post graduate.    
"""
def remove_PostGrad(Participant_Id):
    db_config = read_db_config();

    query = "DELETE FROM Post_Grad WHERE Participant_ID=%s " %(Participant_Id)
    #data = (Participant_Id);

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

# remove housing based on Id;
"""Removes a housing entry from the housing Database given an ID

Given a housing entry (specified by an ID), the entry/row
is removed from the database.

Example:
    remove_Housing(1)

Args:
    Participant_Id: The unique participant ID for a specific housing entry.    
"""
def remove_Housing(Participant_Id):
    db_config = read_db_config();

    query = "DELETE FROM Housing WHERE Participant_ID=%s " %(Participant_Id)
    #data = (Participant_Id);

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
"""Updates a specific attribute in the Employee Database

Given an attribute name (one of the column headers), a new value (to replace/set), 
and a specific employee (specified by their employee ID). 
The function updates the old value of the attribute to the given new value. 

Example:
    update_Employees()

Args:
    attribute: A string that contains the name of the attribute/column header.
    newValue: The value that will replace the current value (String or Int).
    Employee_Id: The unique participant ID for a specific participant.   
"""
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
    """ %(Participant_Id)

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

# update_Housing('Housing_Assign', "'Q'", 1, "'A'")
# Participant_Id, Housing_Assign, Bed, Admin_Date, Exit_Date

# insert_Participant(Last_Name, First_Name, DOB,
#                        SSN, Address, Phone, Email, Home_Town,
#                        Criminal_Background, Drug_Used, Assignment,
#                        Sex, Case_Manager, Education, Medications,
#                        Health_Conditions, Time_Homeless,
#                        Disabilites, Admin_Date)

#remove_Participant(6)

#insert_Participant('Brooks', 'Aaron', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null ', 'null '   )

#insert_Housing("'D'", "'7'", "'10/11/2012'", "'11/13/2013'")

#insert_Participant(501, "'Aaron'", "'Brooks'", "'6/27/17'", "'000-00-0000'", "'120 North Avenue Northwest'", "'000-000-0000'", "'abc@gmail.com'", "'Atlanta'", "'Perjury'", "'Heroin'", "'Assignment'", "'M'", "'CM'", "'7th Grade'", "'Xanax'", "'Ebola'", "'7 years'", "'Dyslexia'", "'3/31/18'")
#remove_Participant(501)

#insert_Housing(1, "'D'", "'7'", "'10/11/2012'", "'11/13/2013'")
#remove_Housing(1)

#insert_PostGrad(7, "'Austin'", "'Cho'", 202, 20, 100, "'Homelessness, Addiction'", "'3/31/2018'", "'Student at Georgia Tech'", "'120 North Avenue Northwest'", "'30313'", "'$ 999.99 / hr.'", "'3/30/2018'")

#insert_EC(6, "'Cho'", "'Austin'", "'11/11/2011'", "'Some Address, GA'", "'404-404-404'")