# Stock-Market (Frontend)

Este es el frontend de la aplicación web de predicción bursátil. La interfaz está desarrollada con **Streamlit** y permite a los usuarios interactuar con el sistema a través de una experiencia visual y sencilla.

## Funcionalidades principales
1. **Módulo de Usuarios**:
   - Registro y autenticación de usuarios.
   - Inicio de sesión seguro con email y contraseña.

2. **Módulo de Historial de Activos**:
   - Visualización de datos históricos de activos bursátiles.
   - Descarga de datos históricos en formato CSV.

3. **Módulo Predictivo**:
   - Predicción del precio de cierre de un activo usando un modelo LSTM.
   - Visualización de gráficos comparativos entre los valores reales y las predicciones.

## Estructura del Proyecto
- **`app/`**: Contiene los módulos principales de la aplicación.
  - **`pages/`**: 
    - `home_page.py`: Página principal donde se visualiza el histórico y se generan predicciones.
    - `login_page.py`: Página para iniciar sesión.
    - `registration_page.py`: Página para el registro de nuevos usuarios.
  - **`utils/`**:
    - `api_client.py`: Módulo para comunicarse con el backend.
    - `__init__.py`: Inicialización del paquete de utilidades.
- **`main.py`**: Archivo principal que ejecuta la aplicación.
- **`requirements.txt`**: Lista de dependencias necesarias para ejecutar la aplicación.

## Requisitos
- Python 3.10 o superior.
- Librerías detalladas en `requirements.txt`.

## Ejecución
1. Instala las dependencias con `pip install -r requirements.txt`.
2. Ejecuta la aplicación con `streamlit run main.py`.
