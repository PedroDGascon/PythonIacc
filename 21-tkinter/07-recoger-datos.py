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

def getDato():
    resultado.set(dato.get())
    if len(resultado.get()) >= 1:
        texto_recogido.config(
           bg="green",
           fg="white"
        )   
    #else:
dato = StringVar()
resultado = StringVar()

Label(ventana, text="Coloca un texto: ").pack(anchor=NW)
Entry(ventana, textvariable=dato).pack(anchor=NW)


Label(ventana, text="Dato recogido: ").pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.pack(anchor=NW)

Button(ventana, text="Mostrar Dato", command=getDato).pack(anchor=NW)




ventana.mainloop()