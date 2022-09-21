import re
from tkinter import *
from tokenize import cookie_re
from tkinter import messagebox as MessageBox

ventana = Tk()
ventana.geometry("300x200")

def sacarAlerta():
    MessageBox.showinfo("Alerta", "Esta es una prueba")
    #MessageBox.showerror("Error", "Esa no es la opcion")
    #MessageBox.showinfo("Info", "Tranquilo es solo una informacion")



Button (ventana, text="Mostrar Alerta!!!", command=sacarAlerta).pack()

def salir(nombre):
    resultado = MessageBox.askquestion("Salir", "Continuar Ejecutando la aplicacion")

    if resultado != "yes":
        MessageBox.showinfo("Chaoo!!", f"Adios {nombre}")
        ventana.destroy()  

Button (ventana, text="Salir", command=lambda: salir("Pedro")).pack()

ventana.mainloop()