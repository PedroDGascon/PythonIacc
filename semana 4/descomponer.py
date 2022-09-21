from tkinter import *

import os
from tokenize import String

ventana = Tk()
ventana.geometry("700x500")
ventana.title("Descomponer Numero")

encabezado = Label(ventana, text="Descomponer Numero")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10,
    relief="solid"
)
encabezado.pack(fill=X)

numero = StringVar()
centenas=(numero%1000-numero%100)//100
decenas=(numero%100-numero%10)//10
unidades=numero%10

mq = Frame(ventana, width= 400, height=100)
mq.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
mq.pack(side=TOP, anchor=CENTER)
mq.pack_propagate(False)



Label(mq, text="Introduce un numero: ").pack(anchor=CENTER)
Entry(mq, textvariable=numero, justify="center" ).pack(anchor=CENTER)

Entry.get()(mq, text="Sumar").pack(side="left", fill=X)
Entry(mq, text="Sumar").pack(side="left", fill=X)
Entry(mq, text="Sumar").pack(side="left", fill=X)




ventana.mainloop()



#print ('Valor de centenas: ' + repr (centenas))
#print ('Valor de decenas: ' + repr (decenas))
#print ('Valor de unidades: ' + repr (unidades))
#print ()

