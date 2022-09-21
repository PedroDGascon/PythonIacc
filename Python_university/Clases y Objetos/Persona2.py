class Persona:
    def __init__(self, nombre, apellido, edad,):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        
    
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad}')

#atributo de clase a la izquierda (self.nombre) y a la derecha el parametro. 

persona1 = Persona("Pedro","Gascon","25")

