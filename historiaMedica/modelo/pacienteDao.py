from .conexion import conexionDB 
from tkinter import messagebox

def editarDatoPaciente(persona, idPersona):
    conexion = conexionDB()
    sql = f"""UPDATE Persona SET nombre ='{persona.nombre}', apellidoPaterno = '{persona.apellidoPaterno}', apellidoMaterno = '{persona.apellidoMaterno}', dni = {persona.dni}, fechaNacimiento = '{persona.fechaNacimiento}', edad = {persona.edad}, antecedentes = '{persona.antecedentes}', correo = '{persona.correo}', telefono = '{persona.telefono}', activo = 1 WHERE idPersona = {idPersona}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar Paciente'
        mensaje = 'Paciente editado Exitosamente'
        messagebox.showinfo(title,mensaje)
    except:
        title = 'Editar Paciente'
        mensaje = 'Error al editar Paciente'
        messagebox.showerror(title,mensaje)

def guardarDatoPaciente(persona):
    conexion = conexionDB()
                             # SENTENCIA SQL --
    sql =f"""INSERT INTO Persona (nombre, apellidoPaterno, apellidoMaterno,
            dni, fechaNacimiento, edad, antecedentes, correo, telefono, activo) VALUES
            ('{persona.nombre}','{persona.apellidoPaterno}','{persona.apellidoMaterno}',{persona.dni},'{persona.fechaNacimiento}',{persona.edad},'{persona.antecedentes}',
            '{persona.correo}', '{persona.telefono}',1)"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registrar Paciente'
        mensaje = 'Paciente Registrado Exitosamente'
        messagebox.showinfo(title,mensaje)
    except:
        title = 'Registrar Paciente'
        mensaje = 'Error al Registar Paciente'
        messagebox.showerror(title,mensaje)

        # LISTAR PACIENTES 

#-----------------------------------------------------------------------

def listar():
    conexion = conexionDB()
    listaPersona = []
    sql = 'SELECT * FROM Persona WHERE activo = 1'
    
    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        titulo = 'Datos'
        mensaje = 'Registros no existen'
        messagebox.showwarning(titulo, mensaje)
    return listaPersona

# BUSCAR A PACIENTE POR DNI 
def listarCondicion(where):
    conexion = conexionDB()
    listaPersona = []
    sql = f'SELECT * FROM Persona {where}'

    try:
        conexion.cursor.execute(sql)
        listaPersona = conexion.cursor.fetchall()
        conexion.cerrarConexion()

    except:
        titulo = 'Datos'
        mensaje = 'Registro no existen'
        messagebox.showwarning(titulo, mensaje)
    return listaPersona

# FUNCION ELIMINAR DATOS PACIENTE

def eliminarPaciente(idPersona):
    conexion = conexionDB()
    sql = f"""UPDATE Persona SET activo = 0 WHERE idPersona = {idPersona}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = 'Eliminar Paciente'
        mensaje = 'Paciente eliminado exitosamente'
        messagebox.showwarning(titulo, mensaje)
    except:
        titulo = 'Eliminar Paciente'
        mensaje = 'Error al eliminar Paciente'
        messagebox.showwarning(titulo, mensaje)


#PARA INGRESAR DATOS A LA TABLA ----------------------------------------------------
class Persona:
    def __init__(self, nombre, apellidoPaterno, apellidoMaterno, dni, fechaNacimiento, edad, antecedentes, correo, telefono):
        self.idPersona = None
        self.nombre = nombre
        self.apellidoPaterno = apellidoPaterno
        self.apellidoMaterno = apellidoMaterno
        self.dni = dni
        self.fechaNacimiento = fechaNacimiento
        self.edad = edad
        self.antecedentes = antecedentes
        self.correo = correo
        self.telefono = telefono

    def __str__(self):
        return f'Persona[{self.nombre},{self.apellidoPaterno},{self.apellidoMaterno},{self.dni},{self.fechaNacimiento},{self.edad},{self.antecedentes},{self.correo},{self.telefono}]'