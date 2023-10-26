
from flask import Flask, render_template, request, redirect, url_for, session, make_response, jsonify
import requests
from flask.views import MethodView
from werkzeug.security import generate_password_hash, check_password_hash
from db_manager import DatabaseManager

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
        self.app.route('/change_password', methods=['GET', 'POST'])(self.change_password)
        self.app.route('/data')(self.show_data)
        self.app.route('/add_crypto', methods=['POST'])(self.add_crypto)
        self.app.route('/delete_crypto', methods=['POST'])(self.delete_crypto)
        self.app.route('/news')(self.display_news)



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
        
    def get_crypto_price(self, crypto_symbol, base_currency="usd"):
        BASE_URL = "https://api.coingecko.com/api/v3/simple/price"
        parameters = {
            "ids": crypto_symbol,   # The ids of the cryptocurrency (e.g., "bitcoin")
            "vs_currencies": base_currency  # The currency in which you want the value (e.g., "usd")
        }

        response = requests.get(BASE_URL, params=parameters).json()
        try:
            return float(response[crypto_symbol][base_currency])
        except KeyError:
            # handle the error, e.g., by logging it and returning a default value or raising a custom exception
            print(f"Price for '{crypto_symbol}' in '{base_currency}' not found in response: {response}")
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
            email = request.form['email']
            first_name = request.form['first_name']  # Get first_name
            last_name = request.form['last_name']    # Get last_name
            password = request.form['password']

            if not self.db_manager.get_password(username):
                hashed_password = generate_password_hash(password)
                self.db_manager.register_user(username, email, hashed_password, first_name, last_name)  # Pass first_name and last_name
                return redirect(url_for('login'))
            else:
                return "Username already exists!", 400

        return render_template('sign_in.html')
    
    def calculate(self):
        username = request.form['username']
        password = request.form['password']

        if not self.authenticate_user(username, password):
            return "Invalid username or password!", 403

        user_id, portfolio_value = self.db_manager.calculate_user_portfolio_value(username)
        session['user_id'] = user_id  # Storing user_id in session

        # Fetch stocks and cryptocurrencies for the user
        stocks = self.db_manager.get_stocks(user_id)
        cryptocurrencies = self.db_manager.get_cryptocurrencies(user_id)

        # Render the template with fetched data
        return render_template('calculate.html', user_id=user_id, user=username, value=portfolio_value, stocks=stocks,  cryptocurrencies=cryptocurrencies)

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

        return redirect(url_for('dashboard'))
    
    def add_crypto(self):
        if 'user_id' not in session:
            return "User not logged in!", 403

        user_id = session['user_id']
        crypto_name = request.form['crypto_name']
        crypto_quantity = int(request.form['crypto_quantity'])

        existing_crypto = self.db_manager.get_specific_crypto(user_id, crypto_name)
        if existing_crypto:
            new_quantity = existing_crypto[1] + crypto_quantity
            self.db_manager.update_crypto(user_id, crypto_name, new_quantity)
        else:
            self.db_manager.add_crypto(user_id, crypto_name, crypto_quantity)

        return redirect(url_for('dashboard'))
    
    def delete_crypto(self):
        if 'user_id' not in session:
            return "User not logged in!", 403

        user_id = session['user_id']
        crypto_name = request.form['crypto_name']
        crypto_quantity_to_delete = int(request.form['crypto_quantity'])

        existing_crypto = self.db_manager.get_specific_crypto(user_id, crypto_name)
        if existing_crypto:
            new_quantity = existing_crypto[1] - crypto_quantity_to_delete
            if new_quantity <= 0:
                self.db_manager.delete_crypto(user_id, crypto_name)
            else:
                self.db_manager.update_crypto(user_id, crypto_name, new_quantity)
        else:
            return "Cryptocurrency not found!", 404

        return redirect(url_for('dashboard'))
    
    
    def dashboard(self):
        if 'user_id' not in session:
            return redirect(url_for('login'))

        user_id = session['user_id']
        stocks = self.db_manager.get_stocks(user_id)
        
        # Assuming you have a method called 'get_cryptocurrencies' in your 'db_manager' to fetch the user's cryptocurrencies
        cryptocurrencies = self.db_manager.get_cryptocurrencies(user_id)


        # Pass both stocks and cryptocurrencies to the dashboard.html template
        return render_template('dashboard.html', stocks=stocks, cryptocurrencies=cryptocurrencies)

    def show_result(user_id):
        # เรียก function ใน class DatabaseManager เพื่อรับข้อมูล username จากฐานข้อมูลโดยใช้ user_id
        username = app_instance.db_manager.get_username_by_user_id(user_id)
        
        if not username:
            # Handle error, e.g., user not found
            return "User not found!", 404

        stocks = app_instance.db_manager.get_stocks(user_id)
        cryptocurrencies = app_instance.db_manager.get_cryptocurrencies(user_id)
        return render_template('calculate.html', user_id=user_id, user=username, stocks=stocks, crypto=cryptocurrencies)

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
    

    def show_data(self):
        users = self.db_manager.get_all_users()
        stocks = self.db_manager.get_all_stocks()
        cryptocurrencies = self.db_manager.get_all_cryptocurrencies()
        transactions = self.db_manager.get_all_transactions()
        news = self.db_manager.get_all_news()
        wallet = self.db_manager.get_all_wallet()

        data = {
            'users': users,
            'stocks': stocks,
            'cryptocurrencies': cryptocurrencies,
            'transactions': transactions,
            'news': news,
            'wallet': wallet
        }

        return jsonify(data)


    def display_news(self):
        news_items = self.db_manager.get_all_news()
        return render_template('news.html', news_items=news_items)

    
if __name__ == "__main__":
    app_instance = StockPortfolioApp()
    app_instance.app.run(debug=True)
