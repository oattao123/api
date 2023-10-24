from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
import mysql.connector
import requests
from werkzeug.security import generate_password_hash, check_password_hash

class StockPortfolioApp:
    API_KEY = "YOUR_ALPHA_VANTAGE_API_KEY"

    def __init__(self):
        self.app = Flask(__name__)
        self.app.secret_key = 'some_random_string'
        self.db_manager = DatabaseManager(self)

        # Routes
        self.app.route('/')(self.login)
        self.app.route('/sign_in', methods=['GET', 'POST'])(self.sign_in)
        self.app.route('/calculate', methods=['POST'])(self.calculate)
        self.app.route('/add_stock', methods=['POST'])(self.add_stock)
        self.app.route('/delete_stock', methods=['POST'])(self.delete_stock)
        self.app.route('/dashboard')(self.dashboard)
        self.app.route('/show_result/<int:user_id>')(self.show_result)
        self.app.route('/some_route')(self.some_route)
        self.app.route('/change_password', methods=['GET', 'POST'])(self.change_password)
        self.app.route('/data')(self.show_data)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.cursor.close()
        self.connection.close()
    def get_stock_price(self, symbol):
        BASE_URL = "https://www.alphavantage.co/query"
        parameters = {
            "function": "GLOBAL_QUOTE",
            "symbol": symbol,
            "apikey": self.API_KEY
        }

        response = requests.get(BASE_URL, params=parameters).json()
        try:
            return float(response["Global Quote"]["05. price"])
        except KeyError:
            # handle the error, e.g., by logging it and returning a default value or raising a custom exception
            print(f"Key '05. price' not found in response: {response}")
            return 0.0

    def get_crypto_price(self, symbol):
        BASE_URL = "https://api.coingecko.com/api/v3/simple/price"

        parameters = {
            "ids": symbol,
            "vs_currencies": "usd"
        }

        response = requests.get(BASE_URL, params=parameters).json()

        try:
            return response[symbol]["usd"]
        except KeyError:
            print(f"Could not get price for {symbol}")
            return 0.0

    def get_gold_price(self):
        BASE_URL = "https://www.goldapi.io/api/XAU/USD"  # ราคาทองคำเทียบกับ USD
        HEADERS = {
            "x-access-token": "YOUR_GOLD_API_KEY"
        }

        response = requests.get(BASE_URL, headers=HEADERS).json()
        try:
            return float(response["price"])
        except KeyError:
            print(f"Error: Could not get price for gold. Response: {response}")
            return 0.0
        
    def authenticate_user(self, username, password):
        stored_password = self.db_manager.get_password(username)
        if stored_password and check_password_hash(stored_password[0], password):
            return True
        return False

    def login(self):
        return render_template('index.html')

    def sign_in(self):
        if request.method == 'POST':
            username = request.form['username']
            email = request.form['email']  # เพิ่มส่วนนี้เพื่อรับค่า email จากแบบฟอร์ม
            password = request.form['password']

            if not self.db_manager.get_password(username):
                hashed_password = generate_password_hash(password)
                self.db_manager.register_user(username, email, hashed_password)  # ส่งค่า email ไปที่ฟังก์ชัน register_user
                return redirect(url_for('login'))
            else:
                return "Username already exists!", 400

        return render_template('sign_in.html')
    
    def calculate(self):
        username = request.form['username']
        password = request.form['password']

        if not self.authenticate_user(username, password):
            return "Invalid username or password!", 403

        user_id = session['user_id']

        stocks = self.db_manager.get_stocks(user_id)
        cryptocurrencies = self.db_manager.get_cryptocurrencies(user_id)
        gold = self.db_manager.get_gold(user_id)
        cash_holdings = self.db_manager.get_cash_holdings(user_id)

        # Calculate stocks value
        stock_value = 0.0
        for stock in stocks:
            stock_price = self.get_stock_price(stock[0])  # Using Alpha Vantage for stocks
            stock_value += stock_price * stock[1]

        # Placeholder values for cryptocurrency and gold values (you might want to replace with actual API calls)
        crypto_value = sum([crypto[2] * self.get_crypto_price(crypto[0]) for crypto in cryptocurrencies])
        gold_data = self.db_manager.get_gold(user_id) or []
        gold_value = sum([g[1] * self.get_gold_price() for g in gold_data])

        # Sum cash holdings
        cash_value = sum([cash[1] for cash in cash_holdings])

        # Total Portfolio value
        total_value = stock_value + crypto_value + gold_value + cash_value

        return render_template(
            'calculate.html',
            user_id=user_id,
            user=username,
            value=total_value,
            stocks=stocks,
            cryptocurrencies=cryptocurrencies,
            gold=gold,
            cash=cash_holdings
        )


    def add_stock(self):
        if 'user_id' not in session:
            return "User not logged in!", 403

        user_id = session['user_id']
        stock_name = request.form['stock_name']
        stock_quantity = int(request.form['stock_quantity'])

        existing_stock = self.db_manager.get_specific_stock(user_id, stock_name)
        if existing_stock:
            new_quantity = existing_stock[1] + stock_quantity
            self.db_manager.update_stock(user_id, stock_name, new_quantity)
        else:
            self.db_manager.add_stock(user_id, stock_name, stock_quantity)

        return redirect(url_for('dashboard'))

    def show_data(self):
        users = self.db_manager.get_all_users()
        stocks = self.db_manager.get_all_stocks()
        cryptocurrencies = self.db_manager.get_all_cryptocurrencies()
        gold = self.db_manager.get_all_gold()

        data = {
            'users': users,
            'stocks': stocks,
            'cryptocurrencies': cryptocurrencies,
            'gold': gold
        }

        return jsonify(data)

    def delete_stock(self):
        if 'user_id' not in session:
            return "User not logged in!", 403

        user_id = session['user_id']
        stock_name = request.form['stock_name']
        stock_quantity_to_delete = int(request.form['stock_quantity'])  # get the stock quantity to delete

        existing_stock = self.db_manager.get_specific_stock(user_id, stock_name)
        if existing_stock:
            new_quantity = existing_stock[1] - stock_quantity_to_delete

            # Check if the new quantity is zero or negative
            if new_quantity <= 0:
                self.db_manager.delete_stock(user_id, stock_name)
            else:
                self.db_manager.update_stock(user_id, stock_name, new_quantity)
        else:
            return "Stock does not exist!", 400

        return redirect(url_for('some_function'))
    
    def some_route():
        response = make_response(render_template('some_template.html'))
        response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
        response.headers['Pragma'] = 'no-cache'
        return response
    
    def dashboard(self):
        if 'user_id' not in session:
            return redirect(url_for('login'))

        user_id = session['user_id']
        stocks = self.db_manager.get_stocks(user_id)
        # สมมติว่าคุณมี template ชื่อ dashboard.html เพื่อแสดงรายการข้อมูล stock
        return render_template('dashboard.html', stocks=stocks)
    def show_result(user_id):
        # เรียก function ใน class DatabaseManager เพื่อรับข้อมูล username จากฐานข้อมูลโดยใช้ user_id
        username = app_instance.db_manager.get_username_by_user_id(user_id)
        
        if not username:
            # Handle error, e.g., user not found
            return "User not found!", 404

        stocks = app_instance.db_manager.get_stocks(user_id)
        return render_template('calculate.html', user_id=user_id, user=username, stocks=stocks)

    def change_password(self):
        if request.method == 'POST':
            username = request.form['username']
            current_password = request.form['current_password']
            new_password = request.form['new_password']
            confirm_new_password = request.form['confirm_new_password']

            # Authenticate the current password
            if not self.authenticate_user(username, current_password):
                return "Current password is incorrect!", 403

            # Check if new password matches the confirmation
            if new_password != confirm_new_password:
                return "New password and confirmation do not match!", 400

            # Update the password in the database
            hashed_new_password = generate_password_hash(new_password)
            self.db_manager.update_password(username, hashed_new_password)
            return "Password updated successfully!", 200

        return render_template('change_password.html')


class DatabaseManager:
    def __init__(self, app_instance):
        self.app = app_instance
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="@oattao@123",
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

    def register_user(self, username, email, hashed_password, balance=0.0):
        try:
            self.cursor.execute(
                "INSERT INTO users (username, email, password, balance) VALUES (%s, %s, %s, %s)",
                (username, email, hashed_password, balance)  # เพิ่มค่า email ที่นี่
            )
            self.connection.commit()
        except mysql.connector.IntegrityError:
            print("Username or email already exists.")

    def calculate_user_portfolio_value(self, username):
        self.cursor.execute("SELECT user_id FROM users WHERE username=%s", (username,))
        user_id = self.cursor.fetchone()
        if not user_id:
            return None, None

        query = "SELECT stock_name, stock_quantity FROM stocks WHERE user_id=%s"
        self.cursor.execute(query, (user_id[0],))

        total_value = 0.0
        for stock_name, stock_quantity in self.cursor.fetchall():
            stock_price = self.app.get_stock_price(stock_name)
            total_value += stock_price * stock_quantity

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

    def get_specific_stock(self, user_id, stock_name):
        self.cursor.execute("SELECT stock_name, stock_quantity FROM stocks WHERE user_id=%s AND stock_name=%s", (user_id, stock_name))
        return self.cursor.fetchone()
    def calculate_user_portfolio_value_by_user_id(self, user_id):
        query = "SELECT stock_name, stock_quantity FROM stocks WHERE user_id=%s"
        self.cursor.execute(query, (user_id,))

        total_value = 0.0
        for stock_name, stock_quantity in self.cursor.fetchall():
            stock_price = self.app.get_stock_price(stock_name)
            total_value += stock_price * stock_quantity

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
        def add_cryptocurrency(self, user_id, crypto_name, crypto_quantity):
            try:
                self.cursor.execute(
                    "INSERT INTO cryptocurrencies (user_id, crypto_name, crypto_quantity) VALUES (%s, %s, %s)",
                    (user_id, crypto_name, crypto_quantity)
                )
                self.connection.commit()
            except Exception as e:
                print(f"Error adding cryptocurrency: {e}")
            
    def add_gold(self, user_id, gold_weight):
        try:
            self.cursor.execute(
                "INSERT INTO gold (user_id, gold_weight) VALUES (%s, %s)",
                (user_id, gold_weight)
            )
            self.connection.commit()
        except Exception as e:
            print(f"Error adding gold: {e}")
            
    def add_cash(self, user_id, amount, currency):
        try:
            self.cursor.execute(
                "INSERT INTO cash_holdings (user_id, amount, currency) VALUES (%s, %s, %s)",
                (user_id, amount, currency)
            )
            self.connection.commit()
        except Exception as e:
            print(f"Error adding cash: {e}")
    def get_all_users(self):
        self.cursor.execute("SELECT * FROM users")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]

    def get_all_stocks(self):
        self.cursor.execute("SELECT * FROM stocks")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]

    def get_all_cryptocurrencies(self):
        self.cursor.execute("SELECT * FROM cryptocurrencies")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]

    def get_all_gold(self):
        self.cursor.execute("SELECT * FROM gold")
        return [dict(zip([column[0] for column in self.cursor.description], row)) for row in self.cursor.fetchall()]
    def get_cryptocurrencies(self, user_id):
        self.cursor.execute("SELECT crypto_name, crypto_quantity FROM cryptocurrencies WHERE user_id=%s", (user_id,))
        return self.cursor.fetchall()

    def get_gold(self, user_id):
        self.cursor.execute("SELECT gold_weight FROM gold WHERE user_id=%s", (user_id,))
        return self.cursor.fetchone()

    def get_cash_holdings(self, user_id):
        self.cursor.execute("SELECT amount, currency FROM cash_holdings WHERE user_id=%s", (user_id,))
        return self.cursor.fetchall()

    def calculate_user_portfolio_value(self, username):
        self.cursor.execute("SELECT user_id FROM users WHERE username=%s", (username,))
        user_id = self.cursor.fetchone()
        if not user_id:
            return None, None

        total_value = 0.0
        
        # Calculate value from stocks
        query = "SELECT stock_name, stock_quantity FROM stocks WHERE user_id=%s"
        self.cursor.execute(query, (user_id[0],))
        for stock_name, stock_quantity in self.cursor.fetchall():
            stock_price = self.app.get_stock_price(stock_name)
            total_value += stock_price * stock_quantity

        # Add value from cryptocurrencies (assuming each cryptocurrency is worth $2000 for simplicity)
        query = "SELECT crypto_quantity FROM cryptocurrencies WHERE user_id=%s"
        self.cursor.execute(query, (user_id[0],))
        for crypto_quantity in self.cursor.fetchall():
            total_value += crypto_quantity[0] * 2000

        # Add value from gold (assuming each unit of gold_weight is worth $1800 for simplicity)
        query = "SELECT gold_weight FROM gold WHERE user_id=%s"
        self.cursor.execute(query, (user_id[0],))
        for gold_weight in self.cursor.fetchall():
            total_value += gold_weight[0] * 1800

        # Add value from cash holdings (assuming the currency is USD for simplicity)
        query = "SELECT amount FROM cash_holdings WHERE user_id=%s"
        self.cursor.execute(query, (user_id[0],))
        for amount in self.cursor.fetchall():
            total_value += amount[0]

        return user_id[0], total_value




if __name__ == "__main__":
    app_instance = StockPortfolioApp()
    app_instance.app.run(debug=True) 
