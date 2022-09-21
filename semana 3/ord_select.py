#A través de la función ord_seleccion, escriba el código de una aplicación que permita buscar el mayor de todos los 
# elementos de la lista de 3 elementos ingresados por el usuario (3 puntos)

def orden_seleccion(lista):
    for n in range(len(lista) - 1, 0,- 1):
        max_pos = 0

        for l  in range(1, n + 1):
            if lista[l] >  lista[max_pos]:
                max_pos = l

        temporal = lista[n]
        lista[n] = lista[max_pos]
        lista[max_pos] = temporal

numeros = [19,17,2,29,3,5,11,7,13]
print (numeros)

orden_seleccion(numeros)
print (numeros)
