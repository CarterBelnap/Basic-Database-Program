#Carter Belnap
#April 3rd 2023
#Database Integration Program

import os, time, sqlite3 

connection = sqlite3.connect('database.db') 
cursor = connection.cursor()

connection.close()

def create_connection(db_file):
    #create a database connection to the SQLite database
    #return: Connection object or None
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return conn

def create_table(conn,table, columns):
    col = ",".join(columns)
    sql = f'''CREATE TABLE IF NOT EXISTS {table}( id INTEGER PRIMARY KEY, {col});'''
    conn.execute(sql)

def insert_db(conn,table, columns,data):
    sql=f'''INSERT INTO {table} {tuple(columns)} VALUES {tuple(data)};'''
    conn.execute(sql)
    conn.commit()


connection = create_connection('database.db')

sql = '''CREATE TABLE IF NOT EXISTS name_of_table( id INTEGER PRIMARY KEY, second TEXT,third REAL );'''

connection.execute(sql)

