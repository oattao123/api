import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@oattao@123",
    database="StockPortfolio_main"
)

cursor = connection.cursor()

# Create users table with an added email field
cursor.execute("""
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    Firstname VARCHAR(255) NOT NULL,
    Lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL  # this should store the hashed password
)
""")

# Create stocks table
cursor.execute("""
CREATE TABLE stocks (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    stock_name VARCHAR(255) NOT NULL,
    stock_quantity INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

# Create cryptocurrencies table
cursor.execute("""
CREATE TABLE cryptocurrencies (
    crypto_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    crypto_name VARCHAR(255) NOT NULL,
    crypto_quantity FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

# Transactions Table
cursor.execute("""
CREATE TABLE transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    asset_type VARCHAR(255) NOT NULL,  # e.g. 'stock', 'crypto'
    asset_name VARCHAR(255) NOT NULL,  # e.g. 'Apple', 'Bitcoin'
    quantity FLOAT NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

# News Table
cursor.execute("""
CREATE TABLE news (
    news_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    date_published DATE NOT NULL,
    related_asset VARCHAR(255)  # e.g. 'Apple', 'Bitcoin'
)
""")

# Wallet Table
cursor.execute("""
CREATE TABLE wallet (
    wallet_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    asset_type VARCHAR(255) NOT NULL,  # e.g. 'stock', 'crypto'
    asset_name VARCHAR(255) NOT NULL,  # e.g. 'Apple', 'Bitcoin'
    current_quantity FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
)
""")

connection.commit()
cursor.close()
connection.close()  # Note: There was a typo in your original code. It should be "close()" not "Close()".
