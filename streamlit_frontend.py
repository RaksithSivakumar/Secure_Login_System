import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:5000"  # Flask server URL

# Helper functions for API calls
def register_user(username, password):
    response = requests.post(f"{BASE_URL}/register", json={"username": username, "password": password})
    return response.json()

def login_user(username, password):
    response = requests.post(f"{BASE_URL}/login", json={"username": username, "password": password})
    return response.json()

# Streamlit UI
st.title("Secure Login System")

# Registration section
st.header("Register")
register_username = st.text_input("Username", key="register_username")
register_password = st.text_input("Password", type="password", key="register_password")
if st.button("Register"):
    result = register_user(register_username, register_password)
    if "success" in result:
        st.success(result["success"])
    else:
        st.error(result["error"])

# Login section
st.header("Login")
login_username = st.text_input("Username", key="login_username")
login_password = st.text_input("Password", type="password", key="login_password")
if st.button("Login"):
    result = login_user(login_username, login_password)
    if "success" in result:
        st.success(result["success"])
        st.write("Welcome to your dashboard!")
    else:
        st.error(result["error"])
