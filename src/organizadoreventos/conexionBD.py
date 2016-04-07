import sqlite3 as dbapi

# Version de la api
print (dbapi.apilevel)
# De 0 a 3 como de seguro es el modulo para el uso de hilos
print (dbapi.threadsafety)

# Indica la sintaxis para la insercion de los parametros de forma dinamica
print (dbapi.paramstyle)

''' Metodos para operar con la base de datos'''
# Conectarse a la BD. Devuelve la conexion
def conectar(self):
	bbdd = dbapi.connect("eventosBD.dat")
	return bbdd

# Consultar en la BD pasandole como parametro el nombre de la tabla
def consultar(cursor, tabla):
	cursor.execute('''select * from ''' + tabla + ''' ''')

# Insertar en la BD pasandole como parametro el nombre de la tabla y los datos a ingresar
def insertar(cursor, tabla, datos):
    cursor.executemany('''INSERT INTO ''' + tabla + '''  VALUES (?,?,?)''', datos)

def borrar(cursor, tabla, nombre):
    cursor.execute('''delete from ''' + tabla + ''' where nombre=?''', nombre)

def buscar(cursor, tabla, datos):
    cursor.execute('''SELECT * FROM ''' + tabla + '''  WHERE ?=? OR ?=? OR ?=?''', datos)
    return cursor


def mostrarTablas(cursor, tabla):
    cursor.execute('''select * from ''' + tabla + ''' ''')
    return cursor
