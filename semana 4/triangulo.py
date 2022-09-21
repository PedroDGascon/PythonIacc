from tkinter import *
from traceback import format_list

formulario = Tk()
formulario.geometry("800x600")

etiqueta = Label(formulario, text="Descomponer")
etiqueta.pack()

entrada0=Entry(formulario)
etiqueta = Label(formulario, text="Ingrese valor 'A' de triángulo")
etiqueta.pack()
entrada0.pack()

entrada0=Entry(formulario)
etiqueta = Label(formulario, text="Ingrese valor 'A' de triángulo")
etiqueta.pack()
#entrada1.pack()

entrada0=Entry(formulario)
etiqueta = Label(formulario, text="Ingrese valor 'A' de triángulo")
etiqueta.pack()
#entrada2.pack()

def tipo():
    etiqueta = Label(formulario, text="El Tipo es")
    etiqueta.pack()
    Punta1=int(entrada0.get())

formulario.mainloop()