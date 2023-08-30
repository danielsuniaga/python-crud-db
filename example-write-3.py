import sqlite3

miConexion = sqlite3.connect("GestionProductos")#Conectar o crear base de datos

miCursor=miConexion.cursor()#Crear cursor

miCursor.execute('''CREATE TABLE PRODUCTOS_EXPANSIVO_2 (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ARTICULO VARCHAR(50) UNIQUE, PRECIO INTEGER, SECCION VARCHAR(20))''')

productos_expansivo = [

    ("pelota",20,"jugueteria"),
    ("pantalón",15,"confeccion"),
    ("destornillador",25,"ferreteria"),
    ("jarrón",45,"cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS_EXPANSIVO VALUES(NULL,?,?,?)",productos_expansivo)

miConexion.commit() 

miConexion.close()#Cerrar conexion

#UNIQUE: https://www.youtube.com/watch?v=m_FzVf9JTV8&list=PLU8oAlHdN5BlvPxziopYZRd55pdqFwkeS&index=58