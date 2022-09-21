class Persona:
    def __init__(self, nombre, apellido, edad, *valores, **terminos):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.valores = valores
        self.terminos = terminos
    
    def mostrar_detalle(self):
        print(f'Persona: {self.nombre} {self.apellido} {self.edad} {self.valores} {self.terminos}')

#atributo de clase a la izquierda (self.nombre) y a la derecha el parametro. 

persona1 = Persona("Pedro","Gascon","25", '44553322', 2,3,5, m='manzana', p='pera')
#persona1.mostrar_detalle()
persona1.mostrar_detalle()

persona2 = Persona("Carlas","Gomez","28")
persona2.mostrar_detalle() 