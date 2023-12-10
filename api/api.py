from flask import Flask, request, jsonify, redirect, url_for
from flask_cors import CORS
import os
from dotenv import load_dotenv
from db_manager import DatabaseManager
from werkzeug.security import generate_password_hash

# Load environment variables
load_dotenv()

class FlaskApp:
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        self.db_manager = DatabaseManager(self.app)

    def setup_routes(self):
        @self.app.route('/register', methods=['POST'])
        def register_user():
            data = request.json
            success = self.db_manager.add_user(data['username'], data['password'])
            if success:
                return jsonify({"message": "User registered successfully"}), 200
            else:
                return jsonify({"error": "Registration failed"}), 400

        @self.app.route('/sign_in', methods=['POST'])
        def sign_in():
            data = request.json
            username = data['username']
            email = data['email']
            first_name = data['first_name']
            last_name = data['last_name']
            password = data['password']

            if not self.db_manager.get_password(username):
                hashed_password = generate_password_hash(password)
                success = self.db_manager.register_user(username, email, hashed_password, first_name, last_name)
                if success:
                    return jsonify({"message": "User registered successfully"}), 200
                else:
                    return jsonify({"error": "Registration failed"}), 400
            else:
                return jsonify({"error": "Username already exists!"}), 400

    def run(self):
        port = os.getenv('FLASK_PORT', 9000)
        self.app.run(host='0.0.0.0', port=port)

if __name__ == '__main__':
    flask_app = FlaskApp()
    flask_app.setup_routes()
    flask_app.run()
