import sqlite3

miConexion = sqlite3.connect("GestionProductos")#Conectar o crear base de datos

miCursor=miConexion.cursor()#Crear cursor


miCursor.execute("UPDATE PRODUCTOS_EXPANSIVO SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

miConexion.commit()

miConexion.close()#Cerrar conexion
