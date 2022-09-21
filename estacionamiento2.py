from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL

estacionamiento= Flask(__name__)

mysql = MySQL()
estacionamiento.config['MYSQL_DATABASE_HOST']='localhost'
estacionamiento.config['MYSQL_DATABASE_PORT']=3306
estacionamiento.config['MYSQL_DATABASE_USER']='root'
estacionamiento.config['MYSQL_DATABASE_PASSWORD']='root'
estacionamiento.config['MYSQL_DATABASE_DB']='estacionamiento'
mysql.init_app(estacionamiento)

@estacionamiento.route('/')
def index():

    sql="SELECT * FROM `ingreso_vehiculos`;"
    
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    
    ingreso_vehiculos = cursor.fetchall()
    print(ingreso_vehiculos)
    
    conn.commit()
    return render_template('registro/index.html',ingreso_vehiculos=ingreso_vehiculos)

#Crear datos
@estacionamiento.route('/ingreso')
def ingreso():
    
    return render_template('registro/ingreso.html')


#Guardar datos
@estacionamiento.route('/guardar', methods=['POST'])
def guardar():
    
    _patente =request.form['txtPatente']
    _hora_ingreso =request.form['txtHoraIngreso']
    _e_disponible =request.form['txtEstacionamientoD']
    _e_ocupado =request.form['txtEstacionamientoOcu']
    _c_auto =request.form['txtCostoAuto']
    _c_tipo_a =request.form['txtCostoTipoA']
    _c_mensual =request.form['txtCostoMensual']
    _c_anual =request.form['txtCostoAnual']
    _funcionario =request.form['txtRegistroFuncionario']



    sql="INSERT INTO `ingreso_vehiculos` (`id`, `patente`, `hora_ingreso`, `e_disponible`, `e_ocupado`, `c_auto`,`c_tipo_a`,`c_mensual`,`c_anual`,`funcionario`) VALUES (NULL,%s,%s, %s,%s,%s,%s,%s,%s,%s,%s);"
    datos=(_patente,_hora_ingreso,_e_disponible, _e_ocupado,_c_auto,_c_tipo_a,_c_mensual,_c_anual,_funcionario)
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('registro/index.html')

#Borrar datos
@estacionamiento.route('/destroy/<int:id>')
def destroy(id):
    
    conn= mysql.connect()
    cursor=conn.cursor()
    
    cursor.execute("DELETE FROM ingreso_vehiculos WHERE id=%s",(id))
    conn.commit()
    return redirect('/')


if __name__== '__main__':
    estacionamiento.run(debug=True)