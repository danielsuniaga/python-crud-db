import sqlite3

miConexion = sqlite3.connect("GestionProductos")#Conectar o crear base de datos

miCursor=miConexion.cursor()#Crear cursor

miCursor.execute("SELECT * FROM PRODUCTOS_EXPANSIVO WHERE SECCION='confeccion'")

productos=miCursor.fetchall()

print(productos)

miConexion.commit()

miConexion.close()#Cerrar conexion

#LECTURA: https://www.youtube.com/watch?v=m_FzVf9JTV8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=58