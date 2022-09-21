#Clonacion (copia) de objetos
# Copia Superficial (shallow) o copia poco profunda.
import copy

lista_a = [[1,2],[3,4],[5,6]]

#Copia superficial (shallow)

lista_b = list(lista_a)

#Las listas son dos objetos distintos, apuntan a diferente posición de memoria
#pero los niveles internos solo se copio la referencia, no se crearon nuevos objetos

print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

#Comprobacion de que los objetos son distintos (a nivel superior)
#Un cambio en el nivel superior, no afecta a la otra lista.

lista_a.append([7,8])
print("Son distintos objetos (nivel superior)")
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

#Comprobación de que los objetos internos tiene la misma referencia (copia superficial)
#Un cambio en un elmento de una sublista, afecta a la otra sublista de la otra lista

lista_a[0][1]= "A"
print(f'La copia fue superficial, los elementos internos solo se copio la referencia')
print(f'Lista a: {lista_a}')
print(f'Lista b: {lista_b}')

registroC = ["Pedro","Gascon","Masculino","25"]

registroCo = copy.copy(registroC)

print(f'Registro : {registroC}')
print(f'Copia Registro: {registroCo}')