# auth.py

import streamlit as st
import sqlite3
from database import get_user_by_credentials, add_user, get_all_users, update_qualification

def show_login_page():
    st.title("🔐 Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        user = get_user_by_credentials(username, password)
        if user:
            st.session_state.username = user[1]
            st.session_state.user_id = user[0]
            st.session_state.role = user[4]
            st.success("Login successful")
            st.session_state.page = "Admin" if user[4] == "admin" else "User"
            st.experimental_rerun()
        else:
            st.error("Invalid credentials")

    if st.button("Sign Up"):
        st.session_state.page = "Signup"

def show_signup_page():
    st.title("📝 Sign Up")
    username = st.text_input("New Username")
    password = st.text_input("New Password", type="password")
    qualification = st.text_input("Qualification")

    if st.button("Register"):
        if add_user(username, password, qualification):
            st.success("User registered successfully. You can now log in.")
            st.session_state.page = "Login"
        else:
            st.error("Username already exists.")

def show_profile_page():
    st.title("🧑‍💼 Edit Profile")
    new_qual = st.text_input("Update Qualification")
    if st.button("Update"):
        update_qualification(st.session_state.user_id, new_qual)
        st.success("Qualification updated.")

    if st.button("🔙 Back to Chat"):
        st.session_state.page = "User"
        st.experimental_rerun()

def show_admin_dashboard():
    st.title("🛠️ Admin Dashboard")
    users = get_all_users()
    st.write("### Registered Users")
    for u in users:
        st.write(f"👤 {u[1]} | 🎓 {u[3]} | 🧾 Role: {u[4]}")

    if st.button("Logout"):
        st.session_state.page = "Logout"
