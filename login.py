import streamlit as st
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt

# Datos de ejemplo para el gráfico de líneas
data = pd.DataFrame({
    'x': [1, 2, 3, 4, 5],
    'y': [2, 4, 6, 8, 10]
})


# Función para obtener los datos del gráfico desde SQL Server
# Función para validar los datos de inicio de sesión con la tabla de usuarios en SQL Server
def validate_login(username_l, password_l):
    # Información de conexión a SQL Server
    server = '192.168.30.51' 
    database = 'ec_pruebas' 
    username = 'procesamiento' 
    password = 'pr0c3s@m13nt0' 

    conn=pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)
    query = f"SELECT COUNT(*) FROM [usuario] WHERE username = '{username_l}' AND password = '{password_l}'"
    result = conn.execute(query).fetchone()
    conn.close()
    return result[0] == 1


# validate_login('admin','#1_pr0c3ss')
# Página de inicio de sesión
def login_page():
    st.title("Inicio de sesión")

    username_input = st.text_input("Usuario")
    password_input = st.text_input("Contraseña", type="password")

    if st.button("Iniciar sesión"):
        if validate_login(username_input, password_input):
            st.success("Inicio de sesión exitoso")
            show_chart()
        else:
            st.error("Usuario o contraseña incorrectos")

# Página del gráfico de líneas
def show_chart():
    st.title("Gráfico de líneas")
    df = data
    st.line_chart(df)

# Ejecución de la aplicación
def main():
    login_page()

if __name__ == '__main__':
    main()
