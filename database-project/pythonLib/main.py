from database_operations import add_book, add_member

# Main program to interact with the database operations
while True:
    print("1. Add Book")
    print("2. Add Member")
    print("3. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        title = input("Enter title: ")
        author = input("Enter author: ")
        ISBN = input("Enter ISBN: ")
        quantity = input("Enter quantity: ")
        add_book(title, author, ISBN, quantity)
    elif choice == '2':
        name = input("Enter name: ")
        email = input("Enter email: ")
        member_type = input("Enter member type (student/teacher): ")
        add_member(name, email, member_type)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
