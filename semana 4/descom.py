from importlib.metadata import entry_points
from tkinter import *
from tkinter.tix import LabelEntry
from tokenize import String

ventana = Tk()
ventana.geometry("700x700")
ventana.title("Formulario Practica")
ventana.config(
    bd=50
)

def descomponCentena(centenas):  
    centenas = numero%1000-numero%100//100
    ('Valor de centenas: ' + repr (centenas))

#def getDato():
   # resultado.set(dato.get())
   # if len(resultado.get()) >= 1:
   #     texto_recogido.config(
   #        bg="green",
    #       fg="white"
      #  )   
    #else:

numero = ""

#decenas=(numero%100-numero%10)//10
#unidades=numero%10    
dato = StringVar()
resultado = StringVar()

Label(ventana, text="Coloca un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=numero).pack(anchor=NW)


Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=descomponCentena)
texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar Dato", command=descomponCentena).pack(anchor=NW)




ventana.mainloop()