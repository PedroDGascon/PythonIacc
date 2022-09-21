import pymysql 

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host='localhost:3702',
            username='Root',
            password='vongola10',
            db='cliente'
        )

        self.cursor = self.connection.cursor()

        print("Conexion establecida exitosamente")

database = DataBase()



