
# Secure Login System
A simple Secure Login System demonstrating user registration and login functionalities with Flask as the backend, Streamlit as the frontend, and SQLite as the database. This system uses bcrypt for secure password hashing, ensuring user credentials are stored securely.

## Features
- User Registration: Create a new account with a unique username and a secure password.

- User Login: Authenticate existing users by validating their credentials.

- Secure Password Storage: Passwords are hashed using bcrypt before storing them in the database.

- Streamlit Frontend: A clean and simple user interface for interacting with the system.

- SQLite Database: Lightweight database to store user data.

### Folder Structure
```bash
secure_login_system/
├── app.py                # Flask backend for authentication
├── auth.db               # SQLite database file for storing user data
└── streamlit_frontend.py # Streamlit frontend for UI 
```
### Prerequisites

- Python 3.7 or higher

- Installed libraries from requirements.txt

- Installation and Setup

### Clone the repository:

```bash
git clone https://github.com/yourusername/secure_login_system.git
cd secure_login_system
```
### Install dependencies:

```bash
pip install -r requirements.txt
```
### Run the Flask backend:

```bash
python app.py
```
### Run the Streamlit frontend:

```bash
streamlit run streamlit_frontend.py
```
### Open your browser to access the Streamlit interface, typically at:

```arduino
http://localhost:8501
```

## Usage
1. #### Register

- Go to the Register section in the Streamlit UI.

- Enter a unique username and password, then click Register.

2. #### Login

- Go to the Login section in the Streamlit UI.

- Enter your username and password, then click Login.

- Upon successful login, you’ll be redirected to a simple dashboard.

## Technologies Used

- Backend: Flask

- Frontend: Streamlit

- Database: SQLite

- Security: bcrypt for password hashing

- API Communication: requests and JSON

## Future Enhancements

- Add email verification for user registration.

- Implement session management for logged-in users.

- Enable deployment to a cloud platform like Heroku or AWS.

- Extend the dashboard with personalized features for users.
