
-- Create users table with an added email field (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    Firstname VARCHAR(255) NOT NULL,
    Lastname VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL  # this should store the hashed password
);

-- Create stocks table (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS stocks (
    stock_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    stock_name VARCHAR(255) NOT NULL,
    stock_quantity INT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create cryptocurrencies table (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS cryptocurrencies (
    crypto_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    crypto_name VARCHAR(255) NOT NULL,
    crypto_quantity FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create transactions Table (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS transactions (
    transaction_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    asset_type VARCHAR(255) NOT NULL,  # e.g. 'stock', 'crypto'
    asset_name VARCHAR(255) NOT NULL,  # e.g. 'Apple', 'Bitcoin'
    quantity FLOAT NOT NULL,
    transaction_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- Create news Table (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS news (
    news_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    date_published DATE NOT NULL,
    related_asset VARCHAR(255)  # e.g. 'Apple', 'Bitcoin'
);

-- Create wallet Table (if it doesn't already exist)
CREATE TABLE IF NOT EXISTS wallet (
    wallet_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    asset_type VARCHAR(255) NOT NULL,  # e.g. 'stock', 'crypto'
    asset_name VARCHAR(255) NOT NULL,  # e.g. 'Apple', 'Bitcoin'
    current_quantity FLOAT NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

