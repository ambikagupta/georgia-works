from mysql.connector import MySQLConnection, Error
from python_mysql_dbconfig import read_db_config
 
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
def update_Employees(attribute, newValue ,Employee_Id):
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
                WHERE Paricipant_Id = %s AND Housing_Assign = %s"""
 
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
 
    data = (attribute, newValue ,EC_Id)
 
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
        
#Insert into         
def insert_Participant(Participant_Id, Last_Name, First_Name, DOB, SSN, Address, Phone, Email, Home_Town, Criminal_Background, Drug Used, Asssignment, Sex, Case_Manager, Education, Medications, Health_Conditions, Time_Homeless(Days), Disabilites, Admin_Date):
    #wrap the participant idea

    query = "INSERT INTO Participants(Participant_Id, Last_Name, First_Name, DOB, SSN, Address, Phone, Email, Home_Town, Criminal_Background, Drug Used, Asssignment, Sex, Case_Manager, Education, Medications, Health_Conditions, Time_Homeless(Days), Disabilites, Admin_Date) " \
            "VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    
    args = (Participant_Id, Last_Name, First_Name, DOB, SSN, Address, Phone, Email, Home_Town, Criminal_Background, Drug Used, Asssignment, Sex, Case_Manager, Education, Medications, Health_Conditions, Time_Homeless(Days), Disabilites, Admin_Date)
 
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
 