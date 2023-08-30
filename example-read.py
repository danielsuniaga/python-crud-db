import sqlite3

miConexion = sqlite3.connect("GestionProductos")#Conectar o crear base de datos

miCursor=miConexion.cursor()#Crear cursor

miCursor.execute("SELECT * FROM PRODUCTOS_EXPANSIVO WHERE SECCION='confeccion'")

productos=miCursor.fetchall()

print(productos)

miConexion.commit()

miConexion.close()#Cerrar conexion
