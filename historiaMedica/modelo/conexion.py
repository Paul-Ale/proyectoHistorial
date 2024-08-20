import sqlite3


# CONEXION A LA BASE DE DATOS
class conexionDB:
    def __init__(self):
        self.baseDatos = 'database/dbhistorial.db'
        self.conexion= sqlite3.connect(self.baseDatos)
        self.cursor = self.conexion.cursor()

# CERRAR CONEXION
    def cerrarConexion(self):
        self.conexion.commit()
        self.conexion.close()