'''Topic: Database
The books database has Book table with isbn (int), title(string), author (string), price (int)
For this table perform following CRUD operations:
1. Insert new book data
2. Display data for all books
3. Update price for a book
4. delete data for a book
5. Display books with price >500'''
import mysql.connector
from mysql.connector import Error

def connect_db():
    try:
        # Update these values with your actual MySQL credentials
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='root',         # Default is often 'root'
            password='your_password',
            database='your_database_name'
        )
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def execute_query(con, query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        con.commit()
        print("Query successful")
    except Error as e:
        print(f"Error: {e}")

def execute_read_query(con, query):
    try:
        cursor = con.cursor()
        cursor.execute(query)
        return cursor.fetchall()
    except Error as e:
        print(f"Error: {e}")

# MySQL uses AUTO_INCREMENT (with a space)
create_books_table = '''
CREATE TABLE IF NOT EXISTS Book (
    isbn INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    author VARCHAR(255) NOT NULL,
    price INT
);'''

# --- Main execution ---
conn = connect_db()
if conn:
    execute_query(conn, create_books_table)
    # ... rest of your CRUD operations here ...
    conn.close()
