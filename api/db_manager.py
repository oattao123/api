
import mysql.connector
from werkzeug.security import generate_password_hash, check_password_hash

class DatabaseManager:
    def __init__(self, app_instance):
        self.app = app_instance
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345678",
            database="StockPortfolio_main"
        )
        self.cursor = self.connection.cursor()

    def get_user_id(self, username):
        self.cursor.execute("SELECT user_id FROM users WHERE username=%s", (username,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None

    def get_password(self, username):
        self.cursor.execute("SELECT password FROM users WHERE username=%s", (username,))
        return self.cursor.fetchone()

    def register_user(self, username, email, hashed_password, first_name, last_name):
        try:
            self.cursor.execute(
                "INSERT INTO users (username, email, password, Firstname, Lastname) VALUES (%s, %s, %s, %s, %s)",
                (username, email, hashed_password, first_name, last_name)  # Only include first_name and last_name here
            )
            self.connection.commit()
        except mysql.connector.IntegrityError:
            print("Username or email already exists.")


    def calculate_user_portfolio_value(self, username):
        self.cursor.execute("SELECT user_id FROM users WHERE username=%s", (username,))
        user_id = self.cursor.fetchone()
        if not user_id:
            return None, None

        # Calculate total stock value
        query = "SELECT stock_name, stock_quantity FROM stocks WHERE user_id=%s"
        self.cursor.execute(query, (user_id[0],))
        total_value = 0.0
        for stock_name, stock_quantity in self.cursor.fetchall():
            stock_price = self.app.get_stock_price(stock_name)
            total_value += stock_price * stock_quantity

        # Calculate total cryptocurrency value
        query = "SELECT crypto_name, crypto_quantity FROM cryptocurrencies WHERE user_id=%s"
        self.cursor.execute(query, (user_id[0],))
        for crypto_name, crypto_quantity in self.cursor.fetchall():
            crypto_price = self.app.get_crypto_price(crypto_name)
            total_value += crypto_price * crypto_quantity

        return user_id[0], total_value


    def add_stock(self, user_id, stock_name, stock_quantity):
        try:
            self.cursor.execute("INSERT INTO stocks (user_id, stock_name, stock_quantity) VALUES (%s, %s, %s)", (user_id, stock_name, stock_quantity))
            self.connection.commit()
        except Exception as e:
            print(f"Error adding stock: {e}")

    def update_stock(self, user_id, stock_name, stock_quantity):
        try:
            self.cursor.execute("UPDATE stocks SET stock_quantity=%s WHERE user_id=%s AND stock_name=%s", (stock_quantity, user_id, stock_name))
            self.connection.commit()
        except Exception as e:
            print(f"Error updating stock: {e}")

    def delete_stock(self, user_id, stock_name):
        try:
            self.cursor.execute("DELETE FROM stocks WHERE user_id=%s AND stock_name=%s", (user_id, stock_name))
            self.connection.commit()
        except Exception as e:
            print(f"Error deleting stock: {e}")

    def get_stocks(self, user_id):
        self.cursor.execute("SELECT stock_name, stock_quantity FROM stocks WHERE user_id=%s", (user_id,))
        return self.cursor.fetchall()
    def get_cryptocurrencies(self, user_id):
        self.cursor.execute("SELECT crypto_name, crypto_quantity FROM cryptocurrencies WHERE user_id=%s", (user_id,))
        return self.cursor.fetchall()

    def get_specific_stock(self, user_id, stock_name):
        self.cursor.execute("SELECT stock_name, stock_quantity FROM stocks WHERE user_id=%s AND stock_name=%s", (user_id, stock_name))
        return self.cursor.fetchone()
    def get_specific_crypto(self, user_id, crypto_name):
        self.cursor.execute("SELECT crypto_name, crypto_quantity FROM cryptocurrencies WHERE user_id=%s AND crypto_name=%s", (user_id, crypto_name))
        return self.cursor.fetchone()
    
    def calculate_user_portfolio_value_by_user_id(self, user_id):
        # Calculate total stock value
        query = "SELECT stock_name, stock_quantity FROM stocks WHERE user_id=%s"
        self.cursor.execute(query, (user_id,))
        total_value = 0.0
        for stock_name, stock_quantity in self.cursor.fetchall():
            stock_price = self.app.get_stock_price(stock_name)
            total_value += stock_price * stock_quantity

        # Calculate total cryptocurrency value
        query = "SELECT crypto_name, crypto_quantity FROM cryptocurrencies WHERE user_id=%s"
        self.cursor.execute(query, (user_id,))
        for crypto_name, crypto_quantity in self.cursor.fetchall():
            crypto_price = self.app.get_crypto_price(crypto_name)
            total_value += crypto_price * crypto_quantity

        return user_id, total_value

    
    def get_username_by_user_id(self, user_id):
        self.cursor.execute("SELECT username FROM users WHERE user_id=%s", (user_id,))
        result = self.cursor.fetchone()
        if result:
            return result[0]
        return None
    

    def update_password(self, username, hashed_new_password):
        try:
            self.cursor.execute("UPDATE users SET password=%s WHERE username=%s", (hashed_new_password, username))
            self.connection.commit()
        except Exception as e:
            print(f"Error updating password: {e}")

    def add_crypto(self, user_id, crypto_name, crypto_quantity):
        try:
            self.cursor.execute("INSERT INTO cryptocurrencies (user_id, crypto_name, crypto_quantity) VALUES (%s, %s, %s)", (user_id, crypto_name, crypto_quantity))
            self.connection.commit()
        except Exception as e:
            print(f"Error adding cryptocurrency: {e}")

    def delete_crypto(self, user_id, crypto_name):
        try:
            self.cursor.execute("DELETE FROM cryptocurrencies WHERE user_id=%s AND crypto_name=%s", (user_id, crypto_name))
            self.connection.commit()
        except Exception as e:
            print(f"Error deleting cryptocurrency: {e}")

    
    def update_crypto(self, user_id, crypto_name, crypto_quantity):
        try:
            self.cursor.execute("UPDATE cryptocurrencies SET crypto_quantity=%s WHERE user_id=%s AND crypto_name=%s", (crypto_quantity, user_id, crypto_name))
            self.connection.commit()
        except Exception as e:
            print(f"Error updating cryptocurrency: {e}")

    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    def get_all_stocks(self):
        self.cursor.execute("SELECT * FROM stocks")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    def get_all_cryptocurrencies(self):
        self.cursor.execute("SELECT * FROM cryptocurrencies")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    def get_all_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    # def get_all_news(self):
    #     self.cursor.execute("SELECT * FROM news")
    #     return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    def get_all_wallet(self):
        self.cursor.execute("SELECT * FROM wallet")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    
    def get_all_news(self):
        self.cursor.execute("SELECT * FROM news")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]



    def close(self):
        self.cursor.close()
        self.connection.close()

