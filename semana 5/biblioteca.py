import re

class Biblioteca:

    def __init__(self, nombre_biblioteca, sillas, mesas,cantidad_libros):
        self.nombre_biblioteca = nombre_biblioteca
        self.sillas = sillas
        self.mesas = mesas
        self.cantidad_libros = cantidad_libros


    def describe_bib(self):
        print("Indiqueme el nombre de su biblioteca ", self.nombre_biblioteca)
        print("Cuantas sillas tiene disponibles? ", self.sillas)
        print("Cuantas mesas tiene? ",self.mesas)


    def alquila_libros(self):
        if self.cantidad_libros <= 0 :
            print('No podemos alquilar libros')
        else: print("Tenemos libros disponibles, cual deseas?")

    def __del__(self):
          print("Se ha destruido este objeto")
        

biblioteca_uno = Biblioteca("Antartica","20 sillas"," 4 mesas",10)
biblioteca_dos = Biblioteca("Nacional de chile","30 sillas","6 mesas",  0)

biblioteca_dos.describe_bib()
biblioteca_dos.alquila_libros()