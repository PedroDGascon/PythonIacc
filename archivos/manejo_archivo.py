        #El metodo open crea un archivo en caso de que no exista.
try:
    archivo = open('prueba.txt','w', encoding='utf8')
    #Agregando información en el archivo txt
    archivo.write('Agregando información de prueba\n')
    archivo.write('Saludos!')
except Exception as e:
    print(e)
finally:
    #cuando se llega a la función "close", no se puede agregar mas nada al archivo
    archivo.close()
    print('Fin del archivo.')
    #lo que significa que si escribimos aqui un  achivo.write(), la información no seria tomada.