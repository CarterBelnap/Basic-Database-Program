#Carter Belnap
#April 3rd 2023
#Database Integration Program

import os, time, sqlite3 
run = False
#Database Methods
def create_connection(db_file):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def insert_db(conn,table, columns,data):
    sql=f'''INSERT INTO {table} {tuple(columns)} VALUES {tuple(data)};'''
    conn.execute(sql)
    conn.commit()

def create_table(conn,table, columns):
    col = ",".join(columns)
    sql = f'''CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY, {col});'''
    conn.execute(sql)

def select_db(conn,table,columns_and_data=None):
    if not columns_and_data==None:
        col = " AND ".join(columns_and_data)
        sql=f'''SELECT * FROM {table} WHERE {col}'''
        return conn.execute(sql)
    else:
        sql =f"SELECT * from {table}"
        return conn.execute(sql)  
    
def update_db(conn,table,columns_and_data,where_to_update):
    col = ",".join(columns_and_data)
    sql = f"UPDATE {table} set {col} where {where_to_update}"
    conn.execute(sql)
    conn.commit()

def delete_db(conn,table,column,what_to_remove):
    sql=f'''DELETE FROM {table} WHERE {column} = {what_to_remove}'''
    conn.execute(sql)
    conn.commit()  


#Methods For Each Input
def test_input(str_grade):
    grade = int(input(f"Add Class {str_grade}:"))
    while grade > 100 or grade < 0:
        print("Please Enter A Valid Grade")
        grade = int(input(f"Add Class {str_grade}: "))
    return grade   

def add_user():

    name = input("Add Student: ")
    grade1 = test_input("Grade 1")
    grade2 =  test_input("Grade 2")
    grade3 =  test_input("Grade 3")
    grade4 =  test_input("Grade 4")
   

    time.sleep(2)
    print("Student Added Successfully")
    update_db.append([name,grade1,grade2,grade3,grade4])

def list_user():
    for i in create_connection('database.db'):
        print(i)

def course_average(spot):
    crsav = 0
    for i in create_connection("database.db"):
        crsav += (i[spot])
    crsav=crsav//len(create_connection("database.db"))
    print(f"{crsav}")

def student_average():
    for i in create_connection('database.db'):
        average = (i[1]+i[2]+i[3]+i[4])//4
        print(f"{i[0]}, {average}%")

def menu():
    while run == True:
        #Main Menu UI
        print("\nStudent Gradebook")
        time.sleep(0.05)
        print("Enter A Number Between 1 & 5")
        time.sleep(0.05)
        print(" 1. Add A Student:")
        time.sleep(0.05)
        print(" 2. List Students:")
        time.sleep(0.05)
        print(" 3. Course Averages:")
        time.sleep(0.05)
        print(" 4. Student Averages:")
        time.sleep(0.05)
        print(" 5. Exit:")

        #Input 1-5
        try:
            print("Selection: ")

            #Adding Users To Array 
            if input() == 1:
                os.system("cls")
                add_user()
            
            #Listing Users In Array
            elif input() == 2:
                os.system("cls")
                list_user()
                    
            #Calculating Course Averages
            elif input() == 3:
                os.system("cls")
                print("Math:")
                (course_average(1))
                print("English:")
                (course_average(2))
                print("Science:")
                (course_average(3))
                print("French:")
                (course_average(4))
                time.sleep(2)

            #Calculating Student Averages
            elif input() == 4:
                os.system("cls")
                student_average()

            #Kill Program
            elif input() == 5:
                print("Goodbye")
                time.sleep(2)
                break
            
            #Incorrect Input
            else:
                print("Please Enter A Number Between 1-5")
                time.sleep(1)
                os.system("cls")
        except:
            print("Please Enter A Proper Selection")

#Conn Setup
connection = create_connection('database.db')
if connection is not None:
#ALL CODE HERE
    run == True
    menu()

else:
    print("Error! cannot create the database connection.")

