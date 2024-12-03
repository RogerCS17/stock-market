import streamlit as st
from utils.api_client import login_user

def login_page():
    st.title("Iniciar Sesión")
    with st.form(key="login_form"):
        email = st.text_input("Correo electrónico")
        password = st.text_input("Contraseña", type="password")
        submit_login = st.form_submit_button("Iniciar sesión")
        
        if submit_login:
            if email and password:
                success, response = login_user(email, password)
                if success:
                    st.session_state.logged_in = True
                    st.session_state.user_email = email
                    st.session_state.page = "home"
                    st.rerun()
                else:
                    st.error(response)
            else:
                st.error("Por favor complete todos los campos.")

    if st.button("¿No tienes cuenta? Regístrate aquí"):
        st.session_state.page = "register"
        st.rerun()
