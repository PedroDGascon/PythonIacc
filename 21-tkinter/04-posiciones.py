from cProfile import label
from tkinter import *
from typing import TextIO

ventana = Tk()
#ventana.geometry("700x500")

texto = Label(ventana, text="Bienvenido a mi programa")

texto.config(
            fg="white", 
            bg="black",
            padx=50,
            pady=20,
            font=("Consolas", 30)
)
texto.pack(side=TOP)

texto = Label(ventana, text="Hola soy Pedro Gascon")
texto.config(
            #width=400,
            height=3, #medida de lineas, no se procesa en pixeles
            bg="orange",
            font=("Arial",18),
            padx=10, 
            pady=20,
            cursor="spider"
)
texto.pack(side=TOP, fill=X, expand=YES)


texto = Label(ventana, text="Basico 1")
texto.config(
            #width=400,
            height=3, #medida de lineas, no se procesa en pixeles
            bg="green",
            font=("Robot",18),
            padx=10, 
            pady=20,
            cursor="clock"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico 2")
texto.config(
            #width=400,
            height=3, #medida de lineas, no se procesa en pixeles
            bg="red",
            font=("Robot",18),
            padx=10, 
            pady=20,
            cursor="clock"
)
texto.pack(side=LEFT, fill=X, expand=YES)

texto = Label(ventana, text="Basico 3")
texto.config(
            #width=400,
            height=3, #medida de lineas, no se procesa en pixeles
            bg="pink",
            font=("Robot",18),
            padx=10, 
            pady=20,
            cursor="clock"
)
texto.pack(side=LEFT, fill=X, expand=YES)


ventana.mainloop()