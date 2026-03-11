import sqlite3

conn = sqlite3.connect("books.db")
cur = conn.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS Book(isbn INT PRIMARY KEY, title TEXT, author TEXT, price INT)")

# Insert Method
def insert():
    try:
        isbn = int(input("Enter ISBN: "))
        title = input("Enter Title: ")
        author = input("Enter Author: ")
        price = int(input("Enter Price: "))

        cur.execute("INSERT INTO Book VALUES(?,?,?,?)", (isbn, title, author, price))
        conn.commit()
        print("Book Inserted Successfully!")
    except:
        print("Error while inserting!")


# Display Method
def display():
    try:
        cur.execute("SELECT * FROM Book")
        data = cur.fetchall()
        for row in data:
            print(row)
    except:
        print("Error while displaying!")


# Update Method
def update():
    try:
        isbn = int(input("Enter ISBN: "))
        price = int(input("Enter New Price: "))
        cur.execute("UPDATE Book SET price=? WHERE isbn=?", (price, isbn))
        conn.commit()
        print("Price Updated!")
    except:
        print("Error while updating!")


# Delete Method
def delete():
    try:
        isbn = int(input("Enter ISBN: "))
        cur.execute("DELETE FROM Book WHERE isbn=?", (isbn,))
        conn.commit()
        print("Book Deleted!")
    except:
        print("Error while deleting!")


# Display price > 500
def expensive():
    try:
        cur.execute("SELECT * FROM Book WHERE price > 500")
        for row in cur.fetchall():
            print(row)
    except:
        print("Error!")


# Menu
while True:
        print("\n1.Insert\n2.Display\n3.Update\n4.Delete\n5.Price > 500\n6.Exit")
        ch = int(input("Enter choice: "))

        if ch == 1:
            insert()
        elif ch == 2:
            display()
        elif ch == 3:
            update()
        elif ch == 4:
            delete()
        elif ch == 5:
            expensive()
        elif ch == 6:
            break
        else:
            print("Invalid choice!")

conn.close()