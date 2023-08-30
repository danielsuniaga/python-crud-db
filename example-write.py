import sqlite3

miConexion = sqlite3.connect("PrimeraBase")#Conectar o crear base de datos

miCursor=miConexion.cursor()#Crear cursor

miCursor.execute("CREATE TABLE PRODUCTOS (NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))")

miCursor.execute("INSERT INTO PRODUCTOS VALUES('BALON',15,'DEPORTES')")

miConexion.commit()

miConexion.close()#Cerrar conexion