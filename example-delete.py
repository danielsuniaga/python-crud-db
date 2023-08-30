import sqlite3

miConexion = sqlite3.connect("GestionProductos")#Conectar o crear base de datos

miCursor=miConexion.cursor()#Crear cursor


miCursor.execute("UPDATE PRODUCTOS_EXPANSIVO SET PRECIO=35 WHERE NOMBRE_ARTICULO='pelota'")

miConexion.commit()

miConexion.close()#Cerrar conexion

#UPDATE: https://www.youtube.com/watch?v=m_FzVf9JTV8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=58