from cgitb import text 
from tkinter import Tk,Label,Button
from datetime import datetime
import os
os.system('cls')

#ventana basica
window = Tk()
window.title("Calculo de edad")
window.geometry("1280x680")

# **kwargs > claves de argumento 

lbl = Label(window,text="Este es un label")
lbl.pack()

#pack() te coloca el objeto en el centro de la ventana

def calculo_edad(f):
    today_date = datetime.now()
    dt = datetime.strptime(f, '%d-%m-%Y')
    calculo = today_date.year - dt.year
    if dt.month <= today_date.month:  
        if calculo.day <= calculo.day:
            print('Tienes', calculo, 'años')
        else: print('Tienes', calculo, 'años') 
    else: print('Tienes', calculo-1, 'años')
calculo_edad(input('Introduce tu fecha de nacimiento:')) 

btn = Button(window,text="Presionar", command = calculo_edad)
btn.pack()


window.mainloop()