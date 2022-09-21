from select import select
from sqlite3 import connect
import mysql.connector
import pymysql

#https://postreslareposteracasera.com/Semana7_python/db.py


mydb = mysql.connector.connect(
   host='bh8946.banahosting.com',
   user='ihwkmyxy_usertest',
   password='#t{Ug*sA9!bz',
   database='ihwkmyxy_python_prueba'
)

#cursor = mydb.cursor()

#listar datos
#cursor.execute('select * from usuarios')
#resultado = cursos.fetchall()
#print(resultado)

# es un objeto que nos permite interactuar con la base de datos mediante el lenguaje sql

#insertar datos
sql = 'insert into usuarios (nombre, apellido, edad) values (%s,%s,%s)'
values = ('Pedro', 'Gascon', 25)

cursor.execute(sql, values)

mydb.commit()

print(cursor.rowcount)
