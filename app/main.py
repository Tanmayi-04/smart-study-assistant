import streamlit as st
from login import login
from dashboard import show_dashboard

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login()
else:
    show_dashboard()
