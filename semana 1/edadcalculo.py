from datetime import datetime
import os
os.system('cls')

#definimos la funcion y le agregamos un parametro 'f', que es la fecha que vamos a introducir nosotros
# datetime.now() es la fecha actual
# datetime.strptime() nos genera un objeto en forma String - ( aqui se encuentra el formato de fecha, existen otros)
#
#
#

def calculo_edad(f):
    today_date = datetime.now()
    dt = datetime.strptime(f, '%d-%m-%Y')
    calculo = today_date.year - dt.year
#print(calculo)  

#validamos la edad
    if dt.month <= today_date.month:  
        if calculo.day <= calculo.day:
            print('Tienes', calculo, 'años')
        else: print('Tienes', calculo, 'años') 
    else: print('Tienes', calculo-1, 'años')

calculo_edad(input('Introduce tu fecha de nacimiento:'))    

