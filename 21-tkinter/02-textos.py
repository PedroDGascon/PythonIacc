from cProfile import label
from tkinter import *
from typing import TextIO

ventana = Tk()
ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
            fg="white", 
            bg="black",
            padx=50,
            pady=20,
            font=("Consolas", 30)
)
texto.pack()

texto = Label(ventana, text="Basico")
texto.config(
            #width=400,
            height=3, #medida de lineas, no se procesa en pixeles
            bg="orange",
            font=("Arial",18),
            padx=10, 
            pady=20,
            cursor="spider"
)
texto.pack(anchor=SE)

def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de  {pais}" 

texto = Label(ventana, text= pruebas(nombre="Pedro", apellidos="Gascon", pais="Chile"))
texto.config(
            #width=400,
            height=3, #medida de lineas, no se procesa en pixeles
            bg="blue",
            font=("Robot",18),
            padx=10, 
            pady=20,
            cursor="clock"
)
texto.pack(anchor=NW)



ventana.mainloop()