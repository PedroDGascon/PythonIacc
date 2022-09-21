"""

CALCULADORA:
  - Dos campos de texto
  - 4 botones para las operaciones
  - Mostrar el resultado de una alerta
  
"""

from cgitb import text
from tkinter import *
from tkinter import messagebox
from tokenize import String
from unittest import result

ventana = Tk()
ventana.title ("Ejercicio de Calculadora Tkinter")
ventana.geometry("400x400")
ventana.config(
    bd=25
)


#definimos una funcion para generar mensaje de error en caso que no se ingresen datos numericos

def cFloat(numero):
    try:
        result = float(numero)
    except:
        result = 0
        messagebox.showerror("Error", "Introduce bien los datos") 

    return result   

# definimos funciones a usar

def sumar():
    try:
        resultado.set(cFloat(numero1.get()) + cFloat(numero2.get()))
    except:
        messagebox.showerror("Error", "Introduce bien los datos")    
    mostrarResultado()

def restar():
    resultado.set(cFloat(numero1.get()) - cFloat(numero2.get()))
    mostrarResultado()

def multiplicar():
    resultado.set(cFloat(numero1.get()) * cFloat(numero2.get()))
    mostrarResultado()

def dividir():
    resultado.set(cFloat(numero1.get()) / cFloat(numero2.get()))
    mostrarResultado()
    
# funcion para mostrar el resultado
def mostrarResultado():
    messagebox.showinfo("Resultado", f"El Resultado de la operación es: {resultado.get()}")
    numero1.set("")
    numero2.set("")

numero1 = StringVar()
numero2 = StringVar()
resultado = StringVar()

marco = Frame(ventana, width=300, height=200)
marco.config(
    padx=15,
    pady=15,
    bd=5,
    relief=SOLID
)
marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text="Primer Numero").pack()
Entry(marco, textvariable=numero1, justify="center" ).pack()

Label(marco, text="Segundo Numero").pack()
Entry(marco, textvariable=numero2, justify="center").pack()

Label(marco, text="").pack()

Button(marco, text="Sumar", command=sumar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Restar", command=restar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Multiplicar", command=multiplicar).pack(side="left", fill=X, expand=YES)
Button(marco, text="Dividir",command=dividir).pack(side="left", fill=X, expand=YES)

ventana.mainloop()