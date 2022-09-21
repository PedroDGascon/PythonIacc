#Escriba una función que permita identificar si los elementos de una lista son positivos o negativos (3 puntos). 
 
lista =  [-2,-9,22,1,7,-5,10,3,9]
positivos, negativos = 0,0

for num in lista:
        
        if num >=0:
            positivos +=1
        else:
            negativos +=1


print("Numeros positivos en la lista: ", positivos)
print("Numeros negativos en la lista: ", negativos)



















"""numero_como_cadena = input("Escribe un número: ")
numero = float(numero_como_cadena)
if numero == 0:
    print("Neutro")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")"""