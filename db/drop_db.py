import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="@oattao@123",
    database="StockPortfolio_main"
)

cursor = connection.cursor()

# Drop wallet table
cursor.execute("DROP TABLE IF EXISTS wallet")

# Drop news table
cursor.execute("DROP TABLE IF EXISTS news")

# Drop transactions table
cursor.execute("DROP TABLE IF EXISTS transactions")

# Drop cryptocurrencies table
cursor.execute("DROP TABLE IF EXISTS cryptocurrencies")

# Drop stocks table
cursor.execute("DROP TABLE IF EXISTS stocks")

# Drop users table
cursor.execute("DROP TABLE IF EXISTS users")

connection.commit()
cursor.close()
connection.close()  # Note: Fixed the typo from "Close()" to "close()".
