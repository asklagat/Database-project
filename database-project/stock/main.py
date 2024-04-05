import mysql.connector

# Function to connect to the database
def connect_to_database():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="jobd", 
        database="stock"
    )

# Function to add a product
def add_product(name, description, price, quantity):
    db = connect_to_database()
    cursor = db.cursor()
    sql = "INSERT INTO products (name, description, price, quantity) VALUES (%s, %s, %s, %s)"
    values = (name, description, price, quantity)
    cursor.execute(sql, values)
    db.commit()
    cursor.close()
    db.close()

# Function to get all products
def get_all_products():
    db = connect_to_database()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    cursor.close()
    db.close()
    return products

# Function to delete a product
def delete_product(product_id):
    db = connect_to_database()
    cursor = db.cursor()
    sql = "DELETE FROM products WHERE product_id = %s"
    cursor.execute(sql, (product_id,))
    db.commit()
    cursor.close()
    db.close()

# Example usage:
# Add a product
add_product("Laptop", "High-performance laptop", 1500.00, 10)

# Get all products
products = get_all_products()
for product in products:
    print(product)

# Delete a product
delete_product(1)  # Assuming product_id 1 is the ID of the product to delete

