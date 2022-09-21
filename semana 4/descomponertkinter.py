from cgitb import text
from tkinter import *


ventana = Tk()
ventana.geometry('600x400')
ventana.title('Descomponer un numero de 3 digitos')


# Definimos una variable que podremos modificar posteriormente (set), leer(get)
numeroD = StringVar(value='numero a descomponer')
numeroDescom = Entry(ventana, width=30,  justify="center", textvariable=numeroD)
numeroDescom.grid(row=0, column=0)

entrada_var1 = StringVar(value='El primer numero de izquierda a derecha')
entrada1 = Entry(ventana, width=50,  justify="center", textvariable=entrada_var1)
entrada1.grid(row=2, column=0)

entrada_var2 = StringVar(value='El segundo numero de izquierda a derecha')
entrada2 = Entry(ventana, width=50,  justify="center", textvariable=entrada_var2)
entrada2.grid(row=4, column=0)

entrada_var3 = StringVar(value='El tercer numero de izquierda a derecha')
entrada3 = Entry(ventana, width=50, justify="center", textvariable=entrada_var3 )
entrada3.grid(row=6, column=0)

# Etiqueta (label)
etiNumero = Label(ventana, text='Numero a descomponer')
etiNumero.grid(row=1, column=0, columnspan=12)

etiqueta1 = Label(ventana, text='Unidad')
etiqueta1.grid(row=3, column=0, columnspan=12)

etiqueta2 = Label(ventana, text='Decena')
etiqueta2.grid(row=5, column=0, columnspan=12)

etiqueta3 = Label(ventana, text='Centena')
etiqueta3.grid(row=7, column=0, columnspan=12)

def enviar():
    # Modificamos el texto del label
    etiqueta1.config(text=entrada_var1.get())
def enviar_2():   
    etiqueta2.config(text=entrada_var2.get())
def enviar_3():    
    etiqueta3.config(text=entrada_var3.get())

# Creamos un botón
boton1 = Button(ventana, text='Enviar', command=enviar)
boton1.grid(row=2, column=1)

boton2 = Button(ventana, text='Enviar', command=enviar_2)
boton2.grid(row=4, column=1)

boton3 = Button(ventana, text='Enviar', command=enviar_3)
boton3.grid(row=6, column=1)



ventana.mainloop()
