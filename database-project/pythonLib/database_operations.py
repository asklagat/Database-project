import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="lagat",
        database="Library"
    )

def add_book(title, author, ISBN, quantity):
    db = connect_to_database()
    cursor = db.cursor()
    sql = "INSERT INTO books (title, author, ISBN, quantity) VALUES (%s, %s, %s, %s)"
    val = (title, author, ISBN, quantity)
    cursor.execute(sql, val)
    db.commit()
    print("Book added successfully.")
    cursor.close()
    db.close()

def add_member(name, email, member_type):
    db = connect_to_database()
    cursor = db.cursor()
    sql = "INSERT INTO members (name, email, member_type) VALUES (%s, %s, %s)"
    val = (name, email, member_type)
    cursor.execute(sql, val)
    db.commit()
    print("Member added successfully.")
    cursor.close()
    db.close()
