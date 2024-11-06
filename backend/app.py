# app.py
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
import sqlite3
from flask_cors import CORS

app = Flask(__name__)
bcrypt = Bcrypt(app)
CORS(app)  # Enable CORS for Streamlit frontend

# Initialize SQLite database
def init_db():
    conn = sqlite3.connect("auth.db")
    cursor = conn.cursor()
    cursor.execute(
        """CREATE TABLE IF NOT EXISTS users (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               username TEXT UNIQUE,
               password TEXT
           )"""
    )
    conn.commit()
    conn.close()

# Register route
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    username = data['username']
    password = data['password']
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    
    conn = sqlite3.connect("auth.db")
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        return jsonify({'success': 'User registered successfully!'}), 201
    except sqlite3.IntegrityError:
        return jsonify({'error': 'Username already exists!'}), 400
    finally:
        conn.close()

# Login route
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data['username']
    password = data['password']

    conn = sqlite3.connect("auth.db")
    cursor = conn.cursor()
    cursor.execute("SELECT password FROM users WHERE username = ?", (username,))
    result = cursor.fetchone()
    conn.close()

    if result and bcrypt.check_password_hash(result[0], password):
        return jsonify({'success': 'Login successful!'}), 200
    return jsonify({'error': 'Invalid username or password!'}), 401

if __name__ == '__main__':
    init_db()  # Initialize the database when running the app
    app.run(port=5000)
