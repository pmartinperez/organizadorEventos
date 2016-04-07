import sqlite3 as dbapi

''' Clase que se conecta a la BD crea unas tablas y hace unas inserciones'''
bbdd = dbapi.connect("eventosBD.dat")
cursor = bbdd.cursor()

cursor.execute(''' DROP TABLE empleados ''')
cursor.execute(''' DROP TABLE usuarios ''')
cursor.execute(''' DROP TABLE local ''')
cursor.execute(''' DROP TABLE tablas ''')
cursor.execute(''' DROP TABLE evento ''')

# Create tables
cursor.execute('''CREATE TABLE if not exists evento(nombre text, tipo text, fecha text)''')
cursor.execute('''CREATE TABLE if not exists local(nombre text, direccion text, m2 text)''')
cursor.execute('''CREATE TABLE if not exists empleados(nombre text, dni text, funcion text)''')
cursor.execute('''CREATE TABLE if not exists usuarios(nombre text, dni text, asiste text)''')
cursor.execute('''CREATE TABLE if not exists tablas(nombre text)''')

# Insertar valores en las tablas
cursor.execute('''INSERT INTO tablas VALUES ("evento")''')
cursor.execute('''INSERT INTO tablas VALUES ("local")''')
cursor.execute('''INSERT INTO tablas VALUES ("empleados")''')
cursor.execute('''INSERT INTO tablas VALUES ("usuarios")''')

cursor.execute('''INSERT INTO evento VALUES ("Evento1", "Concierto", "12/06/16")''')
cursor.execute('''INSERT INTO local VALUES ("local1", "C/ Pascual", "200 m2")''')
cursor.execute('''INSERT INTO empleados VALUES ("Maria", "12345", "Publicidad")''')
cursor.execute('''INSERT INTO usuarios VALUES ("Pepe", "67890", "Si")''')


bbdd.commit()
bbdd.close()

