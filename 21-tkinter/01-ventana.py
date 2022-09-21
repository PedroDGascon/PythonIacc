# Tkinter
# Modulo para crear interfaces graficas de usuario

from cProfile import label
from tkinter import *
import os.path


class programa:

    def __init__(self):
        self.title = "Descomposición de un numero en unidad,decena,centena" #"Master en python con Victor Robles"
        self.icon = './imagenes/slime.ico'
        self.icon_alt = "./21-tkinter/imagenes/slime.ico"
        self.size = "770x470"
        self.resizable = False

    def cargar(self):

        #  Crear lla venta raiz
        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana
        ventana.title(self.title)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icon)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.icon_alt)

        # Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        # icono de la ventana
        # ventana.iconbitmap("./21-tkinter/imagenes/slime.ico")
        ventana.iconbitmap(ruta_icono)

        # Cambio del tamanio de la ventana
        ventana.geometry(self.size)

        # bloquear el tamanio de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0,0)
      

    def addTexto(self, dato):
        texto = Label(self.ventana, text=dato)
        texto.pack()
    
    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()
 
#Instanciar programa
programa = programa()
programa.cargar()
programa.addTexto("Texto para justificar parametros")
programa.mostrar()

        
