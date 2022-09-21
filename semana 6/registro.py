# Sistema que debe manejar las personas dentro del proceso como son Empleados, Clientes
# Atributos Empleados = nombre, apellido, rut, direccion
# Atributos de clientes = nombre, apellido, rut, direccion
# Ideal crear una superclase para que hereden los datos necesarios. 
#1.	La abstracción de clases, Interfaz de objetos, clases anónimas y sobrecarga en la POO (3 puntos). 

from sqlite3 import apilevel
import copy

class Registro():

#(Abstracción) las características específicas de un objeto, con las cuales este se puede diferenciar de los demás 
    
    def __init__(self, nombre,apellido,rut,direccion):
        self.nombre = nombre
        self.apellido = apellido
        self.rut = rut 
        self.direccion = direccion
    
    #Interfaz de objetos 

    def solicitarDatos(self):
        return self.nombre, self.apellido, self.rut, self.direccion  
    
    
nombre = input('Indique su nombre: ')
apellido = input('Indique su apellido: ')
rut = input('Indique su rut: ')
direccion = input('Indique su dirección: ')

registro1 = Registro (nombre,apellido,rut,direccion)
print(f'Datos registro: \n {registro1.solicitarDatos()}')

registro2 = Registro (nombre,apellido,rut,direccion)
print(f'Registro Copia: \n {registro2.solicitarDatos()}')



