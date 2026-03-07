import sqlite3
from sqlite3 import Error

def connect_db(path):
    con=None
    try:
        con=sqlite3.connect(path)
        print('connection successful')
        return con
    except Error as e:
        print(e)

def execute_query(con,query):
    try:
        cursor=con.cursor()
        cursor.execute(query)
        con.commit()
        print('Query Successful')
    except Error as e:
        print(e)

def execute_read_query(con,query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        results=cursor.fetchall()
        return results
    except Error as e:
        print(e)

def close_connection(con):
    try:
        if con:
            con.close()
    except Error as e:
        print(e)

drop_table = '''DROP TABLE IF EXISTS User;'''

create_table='''CREATE TABLE IF NOT EXISTS User
(UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Age INTEGER CHECK (Age >= 0)
);'''

add_users='''INSERT INTO User (FirstName, LastName, Email, Age)
VALUES
('John', 'Doe', 'john.doe@example.com', 30),
('Jane', 'Smith', 'jane.smith@example.com', 25),
('Alice', 'Brown', 'alice.brown@example.com', 28);'''

update_user = '''
UPDATE User
SET Age = 31
WHERE FirstName = 'John' AND LastName = 'Doe';
'''

delete_user = '''
DELETE FROM User
WHERE FirstName = 'Alice' AND LastName = 'Brown';
'''

select_users = '''
SELECT * FROM User;
'''

# Fixed path: Points to a .db file and uses r'' to avoid backslash errors
path = r'C:\Users\PGCP-AI\Documents\2026\PGCP-AI\PYTHON\DAYS\DAY07\my_database.db'
connection = connect_db(path)

execute_query(connection, drop_table)
execute_query(connection,create_table)
execute_query(connection,add_users)


users=execute_read_query(connection,select_users)
for user in users:
    print(user)

execute_query(connection,update_user)
users=execute_read_query(connection,select_users)
for user in users:
    print(user)

execute_query(connection,delete_user)
users=execute_read_query(connection,select_users)
for user in users:
    print(user)