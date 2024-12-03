import streamlit as st
from pages.login_page import login_page
from pages.registration_page import registration_page
from pages.home_page import home_page

if "page" not in st.session_state:
    st.session_state.page = "login"
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if st.session_state.logged_in:
    if st.session_state.page == "home":
        home_page()
else:
    if st.session_state.page == "login":
        login_page()
    elif st.session_state.page == "register":
        registration_page()
