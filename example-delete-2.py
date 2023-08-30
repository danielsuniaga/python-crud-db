import sqlite3

miConexion = sqlite3.connect("GestionProductos")#Conectar o crear base de datos

miCursor=miConexion.cursor()#Crear cursor


miCursor.execute("DELETE FROM PRODUCTOS_EXPANSIVO WHERE ID=5")

miConexion.commit()

miConexion.close()#Cerrar conexion

