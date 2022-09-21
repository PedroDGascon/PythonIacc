from flask import Flask
from flask import render_template,request,redirect
from flaskext.mysql import MySQL

app= Flask(__name__)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_PORT']=3306
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']='root'
app.config['MYSQL_DATABASE_DB']='empresas'
mysql.init_app(app)

@app.route('/')
def index():

    sql="SELECT * FROM `empleados`;"
    
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    
    empleados = cursor.fetchall()
    print(empleados)
    
    conn.commit()
    return render_template('empleados/index.html',empleados=empleados)

@app.route('/destroy/<int:id>')
def destroy(id):
    
    conn= mysql.connect()
    cursor=conn.cursor()
    
    cursor.execute("DELETE FROM empleados WHERE id=%s",(id))
    conn.commit()
    return redirect('/')



@app.route('/create')
def create():
    
    return render_template('empleados/create.html')

@app.route('/store', methods=['POST'])
def storage():
    
    _nombre =request.form['txtNombre']
    _apellido =request.form['txtApellido']
    _rut =request.form['txtRut']
    _direccion =request.form['txtDireccion']
  
    sql="INSERT INTO `empleados` (`id`, `nombre`, `apellido`, `rut`, `direccion`) VALUES (NULL,%s,%s, %s,%s);"
    datos=(_nombre,_apellido,_rut,_direccion)
    conn= mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return render_template('empleados/index.html')


if __name__== '__main__':
    app.run(debug=True)