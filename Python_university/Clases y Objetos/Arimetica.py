class Aritmetica:
    """
    Clase Aritmetica para realizar operaciones de suma, resta etc. 
    """
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB

    def sumar(self):
        return self.operandoA + self.operandoB
    
    def restar(self):
        return self.operandoA - self.operandoB

    def multiplicar(self):
        return self.operandoA * self.operandoB

    def dividir(self):
            return self.operandoA / self.operandoB

arimetica1 = Aritmetica(5,3)
print(f'Suma:  {arimetica1.sumar()}')
print(f'Resta: {arimetica1.restar()}')
print(f'Multiplicacion {arimetica1.multiplicar()}')
print(f'Division {arimetica1.dividir():.2f}')        