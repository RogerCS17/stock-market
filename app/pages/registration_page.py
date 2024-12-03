import streamlit as st
from utils.api_client import register_user

def registration_page():
    st.title("Registro de Usuario")
    with st.form(key="register_form"):
        user_name = st.text_input("Nombre de usuario")
        email = st.text_input("Correo electrónico")
        password = st.text_input("Contraseña", type="password")
        submit_register = st.form_submit_button("Registrarse")
        
        if submit_register:
            if user_name and email and password:
                success, message = register_user(user_name, email, password)
                if success:
                    st.success(message)
                    st.session_state.page = "login"
                    st.rerun()
                else:
                    st.error(message)
            else:
                st.error("Por favor complete todos los campos.")

    if st.button("¿Ya tienes cuenta? Inicia sesión aquí"):
        st.session_state.page = "login"
        st.rerun()
