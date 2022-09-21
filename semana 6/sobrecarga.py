class Persona:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def __add__(self, other):
        return f'Persona: {self.nombre} {other.nombre}'  


persona1 = Persona("Pedro")
persona2 = Persona("David")
print(persona1 + persona2)
#self.edad = edad
# def __sub__(self, other):
     #   return self.edad - other.edad