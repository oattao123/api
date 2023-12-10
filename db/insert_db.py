import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@oattao@123",
    database="StockPortfolio_main"
)

cursor = connection.cursor()

# Insert data into users table
cursor.execute("""
INSERT INTO users (username, Firstname, Lastname, email, password)
VALUES (%s, %s, %s, %s, %s)
""", ("exampleUsername", "Example", "User", "example@email.com", "hashedPassword123"))

# Assuming that user_id of the above user is 1, retrieve the ID
user_id = cursor.lastrowid

# Insert data into the stocks table
cursor.execute("""
INSERT INTO stocks (user_id, stock_name, stock_quantity)
VALUES (%s, %s, %s)
""", (user_id, "Apple", 50))

# Insert data into the cryptocurrencies table
cursor.execute("""
INSERT INTO cryptocurrencies (user_id, crypto_name, crypto_quantity)
VALUES (%s, %s, %s)
""", (user_id, "Bitcoin", 0.5))

cursor.execute("""
INSERT INTO transactions (user_id, asset_type, asset_name, quantity, transaction_date)
VALUES (%s, %s, %s, %s, %s)
""", (user_id, "stock", "Apple", 50, "2023-10-24"))

# Insert data into the transactions table for buying Bitcoin
cursor.execute("""
INSERT INTO transactions (user_id, asset_type, asset_name, quantity, transaction_date)
VALUES (%s, %s, %s, %s, %s)
""", (user_id, "crypto", "Bitcoin", 0.5, "2023-10-24"))

# Insert a sample news related to Apple
cursor.execute("""
INSERT INTO news (title, content, date_published, related_asset)
VALUES (%s, %s, %s, %s)
""", ("Apple Launches New Product", "Apple today announced the launch of its new product...", "2023-10-24", "Apple"))

# Insert a sample news related to Bitcoin
cursor.execute("""
INSERT INTO news (title, content, date_published, related_asset)
VALUES (%s, %s, %s, %s)
""", ("Bitcoin Price Surge", "Bitcoin price sees a significant surge today after...", "2023-10-24", "Bitcoin"))

# Insert data into the wallet table for Apple stocks
cursor.execute("""
INSERT INTO wallet (user_id, asset_type, asset_name, current_quantity)
VALUES (%s, %s, %s, %s)
""", (user_id, "stock", "Apple", 50))

# Insert data into the wallet table for Bitcoin
cursor.execute("""
INSERT INTO wallet (user_id, asset_type, asset_name, current_quantity)
VALUES (%s, %s, %s, %s)
""", (user_id, "crypto", "Bitcoin", 0.5))

# Commit changes
connection.commit()

# Close cursor and connection
cursor.close()
connection.close()
