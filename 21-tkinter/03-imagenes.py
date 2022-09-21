from cProfile import label
from multiprocessing.spawn import import_main_path
from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry = ("700x500")

Label(ventana, text= "Hola!, soy Pedro").pack(anchor=W)

imagen = Image.open('./21-tkinter/imagenes/aritmetica.jpg')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack()


ventana.mainloop()                                                                                                   