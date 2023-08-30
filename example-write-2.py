import sqlite3

miConexion = sqlite3.connect("GestionProductos")#Conectar o crear base de datos

miCursor=miConexion.cursor()#Crear cursor

miCursor.execute('''CREATE TABLE PRODUCTOS_EXPANSIVO (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE_ARTICULO VARCHAR(50), PRECIO INTEGER, SECCION VARCHAR(20))''')

productos_expansivo = [

    ("pelota",20,"jugueteria"),
    ("pantalón",15,"confeccion"),
    ("destornillador",25,"ferreteria"),
    ("jarrón",45,"cerámica")
]

miCursor.executemany("INSERT INTO PRODUCTOS_EXPANSIVO VALUES(NULL,?,?,?)",productos_expansivo)

miConexion.commit()

miConexion.close()#Cerrar conexion

