from cProfile import label
from string import whitespace
from tkinter import *

ventana= Tk()
ventana.geometry("700x400")
ventana.title("Formularios en Tkinter")

# Texto Encabezado
encabezado = Label(ventana, text="Formularios con Tkinter - Pedro Gascon")
encabezado.config(
    fg="white",
    bg="darkgray",
    font=("Open Sans", 18),
    padx=10,
    pady=10
)
encabezado.grid(row=0, column=0, columnspan=12, sticky=W)

#Label para el campo de nombre
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, padx=5, pady=5)

#Campo de texto nombre
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#-------------------------------------------------------------------------
# state= disabled (no permite que se escriba nada en el campo)
# justify= right or left (donde comienza la entrada del texto)

#Label para el campo de apellidos
label = Label(ventana, text="Apellidos")
label.grid(row=2, column=0, padx=5, pady=5)

#Campo de texto apellidos
campo_texto = Entry(ventana)
campo_texto.grid(row=2, column=1, sticky=W, padx=5, pady=5)
campo_texto.config(justify="left", state="normal")

#Label para el campo de texto GRANDE (Descripcion)
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, sticky=N, padx=5, pady=5)

#Campo de texto GRANDE (Descripcion)
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1)
campo_grande.config(
    width=30, 
    height=5,
    font=("Arial", 12),
    padx=15,
    pady=15
)

ventana.mainloop()