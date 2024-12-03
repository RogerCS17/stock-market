import requests

API_URL = "http://127.0.0.1:8000/"

def login_user(email: str, password: str):
    login_data = {"email": email, "password": password}
    response = requests.post(f"{API_URL}/login", json=login_data)
    if response.status_code == 200:
        return True, response.json()
    return False, response.json().get("detail", "Error desconocido")

def register_user(user_name: str, email: str, password: str):
    user_data = {"user_name": user_name, "email": email, "password": password}
    response = requests.post(f"{API_URL}/users", json=user_data)
    if response.status_code == 200:
        return True, "Usuario registrado exitosamente."
    return False, response.json().get("detail", "Error desconocido")
