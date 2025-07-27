import streamlit as st
import sqlite3

def login():
    st.title("🎓 Smart Study Assistant - Login")
    st.markdown("Please enter your credentials to proceed.")

    hallticket = st.text_input("Hallticket Number")
    password = st.text_input("Password", type="password")

    branches = {
        "CSE 💻": "CSE",
        "IT 🖥️": "IT",
        "ECE 📡": "ECE"
    }
    branch_label = st.radio("Select Branch", list(branches.keys()), horizontal=True)
    branch = branches[branch_label]

    if st.button("🔓 Login"):
        conn = sqlite3.connect("../users.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE hallticket=? AND password=? AND branch=?", (hallticket, password, branch))
        user = cursor.fetchone()
        conn.close()

        if user:
            st.session_state['user'] = hallticket
            st.session_state['branch'] = branch
            st.session_state.logged_in = True
            st.rerun()
        else:
            st.error("❌ Invalid credentials or branch")
