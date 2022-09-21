import mysql.connector

class DataBase:
    def __init__(self):
        self.connection=mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="root",
            database="estacionamiento"
        )
        self.cursor=self.connection.cursor()
