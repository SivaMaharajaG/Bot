# app.py

import streamlit as st
from auth import show_login_page, show_signup_page, show_profile_page, show_admin_dashboard
from chatbot import chat_interface
from database import create_tables

st.set_page_config(page_title="IT Placement Bot", page_icon="🤖")

# Initialize
create_tables()

# Session Setup
if "page" not in st.session_state:
    st.session_state.page = "Login"
if "role" not in st.session_state:
    st.session_state.role = None
if "username" not in st.session_state:
    st.session_state.username = ""
if "user_id" not in st.session_state:
    st.session_state.user_id = None

# Navigation
if st.session_state.page == "Login":
    show_login_page()
elif st.session_state.page == "Signup":
    show_signup_page()
elif st.session_state.page == "User":
    chat_interface()
elif st.session_state.page == "Profile":
    show_profile_page()
elif st.session_state.page == "Admin":
    show_admin_dashboard()
elif st.session_state.page == "Logout":
    for key in list(st.session_state.keys()):
        del st.session_state[key]
    st.session_state.page = "Login"
    st.experimental_rerun()
