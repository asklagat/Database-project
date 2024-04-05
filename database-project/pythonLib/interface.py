import tkinter as tk
from tkinter import ttk
import mysql.connector

def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="lagat",
        database="Library"
    )

def add_book():
    title = book_title.get()
    author = book_author.get()
    isbn = book_isbn.get()
    quantity = book_quantity.get()
    db = connect_to_database()
    cursor = db.cursor()
    sql = "INSERT INTO books (title, author, ISBN, quantity) VALUES (%s, %s, %s, %s)"
    val = (title, author, isbn, quantity)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    status_label.config(text="Book added successfully.")

def add_member():
    name = member_name.get()
    email = member_email.get()
    member_type = member_type_var.get()
    db = connect_to_database()
    cursor = db.cursor()
    sql = "INSERT INTO members (name, email, member_type) VALUES (%s, %s, %s)"
    val = (name, email, member_type)
    cursor.execute(sql, val)
    db.commit()
    cursor.close()
    db.close()
    status_label.config(text="Member added successfully.")

def retrieve_data():
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    cursor.execute("SELECT * FROM members")
    members = cursor.fetchall()
    cursor.close()
    db.close()
    
    # Display data in a separate tab or window
    root2 = tk.Tk()
    root2.title("Database Data")
    
    notebook = ttk.Notebook(root2)
    notebook.pack(fill="both", expand=True)
    
    book_frame = ttk.Frame(notebook)
    notebook.add(book_frame, text="Books")
    member_frame = ttk.Frame(notebook)
    notebook.add(member_frame, text="Members")
    
    # Display books
    book_tree = ttk.Treeview(book_frame, columns=("Title", "Author", "ISBN", "Quantity"), show="headings")
    book_tree.heading("Title", text="Title")
    book_tree.heading("Author", text="Author")
    book_tree.heading("ISBN", text="ISBN")
    book_tree.heading("Quantity", text="Quantity")
    book_tree.pack(fill="both", expand=True)
    for book in books:
        book_tree.insert("", "end", values=book)
    
    # Display members
    member_tree = ttk.Treeview(member_frame, columns=("Name", "Email", "Member Type"), show="headings")
    member_tree.heading("Name", text="Name")
    member_tree.heading("Email", text="Email")
    member_tree.heading("Member Type", text="Member Type")
    member_tree.pack(fill="both", expand=True)
    for member in members:
        member_tree.insert("", "end", values=member)
    
    root2.mainloop()

root = tk.Tk()
root.title("Library Management System")

# Book Entry
book_label = tk.Label(root, text="Add Book")
book_label.grid(row=0, column=0, columnspan=2, pady=10)
book_title_label = tk.Label(root, text="Title:")
book_title_label.grid(row=1, column=0)
book_title = tk.Entry(root)
book_title.grid(row=1, column=1)
book_author_label = tk.Label(root, text="Author:")
book_author_label.grid(row=2, column=0)
book_author = tk.Entry(root)
book_author.grid(row=2, column=1)
book_isbn_label = tk.Label(root, text="ISBN:")
book_isbn_label.grid(row=3, column=0)
book_isbn = tk.Entry(root)
book_isbn.grid(row=3, column=1)
book_quantity_label = tk.Label(root, text="Quantity:")
book_quantity_label.grid(row=4, column=0)
book_quantity = tk.Entry(root)
book_quantity.grid(row=4, column=1)
add_book_button = tk.Button(root, text="Add Book", command=add_book)
add_book_button.grid(row=5, column=0, columnspan=2)

# Member Entry
member_label = tk.Label(root, text="Add Member")
member_label.grid(row=6, column=0, columnspan=2, pady=10)
member_name_label = tk.Label(root, text="Name:")
member_name_label.grid(row=7, column=0)
member_name = tk.Entry(root)
member_name.grid(row=7, column=1)
member_email_label = tk.Label(root, text="Email:")
member_email_label.grid(row=8, column=0)
member_email = tk.Entry(root)
member_email.grid(row=8, column=1)
member_type_label = tk.Label(root, text="Member Type:")
member_type_label.grid(row=9, column=0)
member_type_var = tk.StringVar()
member_type = ttk.Combobox(root, textvariable=member_type_var, values=["student", "teacher"])
member_type.grid(row=9, column=1)
member_type.set("student")
add_member_button = tk.Button(root, text="Add Member", command=add_member)
add_member_button.grid(row=10, column=0, columnspan=2)

# Retrieve Data Button
retrieve_button = tk.Button(root, text="Retrieve Data", command=retrieve_data)
retrieve_button.grid(row=11, column=0, columnspan=2)

status_label = tk.Label(root, text="")
status_label.grid(row=12, column=0, columnspan=2)

root.mainloop()
