from tkinter import * 
from tkinter import ttk
from conexion import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.title("Crud Estacionamiento")
ventana.geometry("1360x500")



#instancia para usar la base de datos
db = DataBase()
modificar=False

patente=StringVar()
hora_ingreso=StringVar()
e_disponible=StringVar()
c_auto=StringVar()
c_tipo_a=StringVar()
c_mensual=StringVar()
c_anual=StringVar()
funcionario=StringVar()

def seleccionar(event):
    id=id=tvEstacionamiento.selection()[0]
    if int(id)>0:
        patente.set(tvEstacionamiento.item(id, "values")[1])
        hora_ingreso.set(tvEstacionamiento.item(id, "values")[2])
        e_disponible.set(tvEstacionamiento.item(id, "values")[3])
        c_auto.set(tvEstacionamiento.item(id, "values")[4])
        c_tipo_a.set(tvEstacionamiento.item(id, "values")[5])
        c_mensual.set(tvEstacionamiento.item(id, "values")[6])
        c_anual.set(tvEstacionamiento.item(id, "values")[7])
        funcionario.set(tvEstacionamiento.item(id, "values")[8])

#Marco para ingreso de labels y buttons
marco= LabelFrame(ventana, text="Formulario de control")
marco.place(x=50, y=20, width=1300, height=460)

# labels and entries. 

lblPatente =Label(marco, text="Patente").grid(column=1, row=0, )
txtPatente =Entry(marco, textvariable=patente)
txtPatente.grid(column=2,row=0)

lblHora_ingreso =Label(marco, text="Hora Ingreso").grid(column=1, row=1, )
txtHora_ingreso =Entry(marco, textvariable=hora_ingreso)
txtHora_ingreso.grid(column=2,row=1)

lblE_disponible =Label(marco, text="Estacionamiento disponible").grid(column=1, row=2, )
txtE_disponible =Entry(marco, textvariable=e_disponible)
txtE_disponible.grid(column=2,row=2)


lblC_auto =Label(marco, text="Costo tipo Auto").grid(column=1, row=3, )
txtC_auto =Entry(marco, textvariable=c_auto)
txtC_auto.grid(column=2,row=3)

# SEGUNDA COLUMNA DE DATOS
lblC_tipo_a =Label(marco, text="Costo Día").grid(column=3, row=0, )
txtC_tipo_a =Entry(marco, textvariable=c_tipo_a)
txtC_tipo_a.grid(column=4,row=0)

lblC_mensual =Label(marco, text="Costo Mensual").grid(column=3, row=1, )
txtC_mensual =Entry(marco, textvariable=c_mensual)
txtC_mensual.grid(column=4,row=1)

lblC_anual =Label(marco, text="Costo Anual").grid(column=3, row=2, )
txtC_anual =Entry(marco, textvariable=c_anual)
txtC_anual.grid(column=4,row=2)

lblFuncionario =Label(marco, text="Funcionario ").grid(column=3, row=3, )
txtFuncionario =Entry(marco, textvariable=funcionario)
txtFuncionario.grid(column=4,row=3)

lblMesagge = Label(marco, text="aqui van los mensajes", fg="green")
lblMesagge.grid(column=1, row=4, columnspan=3)

# tabla de los datos de los  vehiculos

tvEstacionamiento= ttk.Treeview(marco, selectmode=NONE)
tvEstacionamiento.grid(column=1, row=6, columnspan=4)
#contenido columnas
tvEstacionamiento["columns"]=("ID","patente","h_ingreso","e_disponible","c_auto","c_tipo_a","c_mensual","c_anual","funcionario")
tvEstacionamiento.column("#0",width=0,stretch=NO)
tvEstacionamiento.column("patente",width=50,anchor=CENTER)
tvEstacionamiento.column("h_ingreso",width=100,anchor=CENTER)
tvEstacionamiento.column("e_disponible",width=100,anchor=CENTER)
tvEstacionamiento.column("c_auto",width=100,anchor=CENTER)
tvEstacionamiento.column("c_tipo_a",width=110,anchor=CENTER)
tvEstacionamiento.column("c_mensual",width=100,anchor=CENTER)
tvEstacionamiento.column("c_anual",width=100,anchor=CENTER)
tvEstacionamiento.column("funcionario",width=100,anchor=CENTER)

#headers columnas
tvEstacionamiento.heading("#0", text="")
tvEstacionamiento.heading("patente", text="Patente", anchor=CENTER)
tvEstacionamiento.heading("h_ingreso", text="Hora Ingreso", anchor=CENTER)
tvEstacionamiento.heading("e_disponible", text="Estacionamiento Disponible", anchor=CENTER)
tvEstacionamiento.heading("c_auto", text="Costo tipo Auto", anchor=CENTER)
tvEstacionamiento.heading("c_tipo_a", text="Costo por Día", anchor=CENTER)
tvEstacionamiento.heading("c_mensual", text="Costo Mensual", anchor=CENTER)
tvEstacionamiento.heading("c_anual", text="Costo Anual", anchor=CENTER)
tvEstacionamiento.heading("funcionario", text="Funcionario", anchor=CENTER)

tvEstacionamiento.bind("<<TreevieSelect>>", seleccionar)


#Botones de accion
btnEliminar=Button(marco, text="Eliminar", command=lambda:eliminar())
btnEliminar.grid(column=2, row=7)
btnNuevo=Button(marco, text="Nuevo", command=lambda:nuevo())
btnNuevo.grid(column=3, row=7)
btnModificar=Button(marco, text="Seleccionar", command=lambda:actualizar())
btnModificar.grid(column=4, row=7)



#functions

def modificarFalse():
    global modificar
    modificar=False
    tvEstacionamiento.config(selectmode=NONE)
    btnNuevo.config(text="Guardar")
    btnModificar.config(text="Seleccionar")
    btnEliminar.config(state=DISABLED)
    

def modificarTrue():
    global modificar
    modificar=True
    tvEstacionamiento.config(selectmode=BROWSE)
    btnNuevo.config(text="Nuevo")
    btnModificar.config(text="Modificar")
    btnEliminar.config(state=NORMAL)
    

def validarCampos():
    return len(patente.get()) and len(hora_ingreso.get()) and len(e_disponible.get()) and len(e_disponible.get()) and len(c_auto.get()) and len(c_tipo_a.get()) and len(c_mensual.get()) and len(c_anual.get()) and len(funcionario.get())
   

def vaciarCampos():
    patente.set("")
    hora_ingreso.set("")
    e_disponible.set("")
    c_auto.set("")
    c_tipo_a.set("")
    c_mensual.set("")
    c_anual.set("")
    funcionario.set("")


def vaciar_tabla():      
    filas = tvEstacionamiento.get_children()
    for fila in filas:
        tvEstacionamiento.delete(fila)

def llenar_tabla():
    vaciar_tabla()
    sql="SELECT * FROM ingreso_vehiculos"
    db.cursor.execute(sql)
    filas= db.cursor.fetchall()
    for fila in filas:
        id = fila[0]
        tvEstacionamiento.insert("",END,id, text=id, values= fila)

def eliminar():
    id=tvEstacionamiento.selection()[0]
    if int(id)>0:
        sql="DELETE FROM ingreso_vehiculos WHERE id="+id
        db.cursor.execute(sql)
        db.connection.commit()
        tvEstacionamiento.delete(id)
        lblMesagge.config(text="Se ha eliminado el registro correctamente")
        vaciarCampos()
    else:
        lblMesagge.config(text="seleccione un registro para eliminar")

def nuevo():
    if modificar==False:
        if validarCampos():
            val=(patente.get(),hora_ingreso.get(),e_disponible.get(),c_auto.get(),c_tipo_a.get(),c_mensual.get(),c_anual.get(),funcionario.get())
            sql="INSERT INTO ingreso_vehiculos (patente,hora_ingreso,e_disponible,c_auto,c_tipo_a,c_mensual,c_anual,funcionario) values(%s,%s,%s,%s,%s,%s,%s,%s) "
            db.cursor.execute(sql, val)
            db.connection.commit()
            lblMesagge.config(text="Se ha ingrasado un registro correctamente", fg="green")
            llenar_tabla()
            vaciarCampos()
        else:
            lblMesagge.config(text="los campos no deben estar vacios", fg="red")
    else:
        modificarFalse()

def actualizar():
    if modificar == True:
        if validarCampos():
         id=tvEstacionamiento.selection()[0]
         val=(patente.get(),hora_ingreso.get(),e_disponible.get(),c_auto.get(),c_tipo_a.get(),c_mensual.get(),c_anual.get(),funcionario.get())
         sql="update ingreso_vehiculos set patente=%s, hora_ingreso=%s, e_disponible=%s, c_auto=%s, c_tipo_a=%s, c_mensual=%s, c_anual=%s, funcionario=%s where id="+id
         db.cursor.execute(sql, val)
         db.connection.commit()
         lblMesagge.config(text="Se ha actualizado el registro correctamente", fg="green")
         llenar_tabla()
         vaciarCampos()
        else:
            lblMesagge.config(text="los campos no deben estar vacios", fg="red")
    else:
        modificarTrue()



llenar_tabla()
ventana.mainloop()