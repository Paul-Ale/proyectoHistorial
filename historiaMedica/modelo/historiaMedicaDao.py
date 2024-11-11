from .conexion import conexionDB
from tkinter import messagebox

#02
def guardarHistoria(idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
    conexion = conexionDB()
                             # SENTENCIA SQL --
    sql = f"""INSERT INTO historiamedica (idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle) VALUES
            ({idPersona},'{fechaHistoria}','{motivo}','{examenAuxiliar}','{tratamiento}','{detalle}')"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Registro de Historia Medica'
        mensaje = 'Historia Registrada Exitosamente'
        messagebox.showinfo(title,mensaje)
    except:
        title = 'Registro de Historia Medica'
        mensaje = 'Error al Registar Historia'
        messagebox.showerror(title,mensaje)

#03
def listarHistoria(idPersona):
    conexion = conexionDB()
    listaHistoria = []
    sql = f'SELECT h.idHistoriaMedica, p.apellidoPaterno || " " || p.apellidoMaterno AS Apellidos, h.fechaHistoria, h.motivo, h.examenAuxiliar, h.tratamiento, h.detalle FROM historiaMedica h INNER JOIN Persona p ON p.idPersona = h.idPersona WHERE p.idPersona = {idPersona}'
    
    try:
        conexion.cursor.execute(sql)
        listaHistoria = conexion.cursor.fetchall()
        conexion.cerrarConexion()
    except:
        titulo = 'LISTAR HISTORIA'
        mensaje = 'Error al listar Historia Medica'
        messagebox.showwarning(titulo, mensaje)

    return listaHistoria

#****************************************************************************************

def eliminarHistoria(idHistoriaMedica):
    conexion = conexionDB()
    sql = f'DELETE FROM historiaMedica WHERE idHistoriaMedica = {idHistoriaMedica}'

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        titulo = 'Eliminar Historial Paciente'
        mensaje = 'Historial Paciente eliminado exitosamente'
        messagebox.showwarning(titulo, mensaje)
    except:
        titulo = 'Eliminar Historial Paciente'
        mensaje = 'Error al eliminar Historial Paciente'
        messagebox.showwarning(titulo, mensaje)


def editarHistoria(fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle, idhistoriaMedica):
    conexion = conexionDB()
    sql = f"""UPDATE historiaMedica SET fechaHistoria = '{fechaHistoria}', motivo = '{motivo}', examenAuxiliar = '{examenAuxiliar}', tratamiento = '{tratamiento}', detalle = '{detalle}' WHERE idhistoriaMedica = {idhistoriaMedica}"""

    try:
        conexion.cursor.execute(sql)
        conexion.cerrarConexion()
        title = 'Editar historia de Paciente'
        mensaje = 'Historia de Paciente editada Exitosamente'
        messagebox.showinfo(title,mensaje)
    except:
        title = 'Editar Historia de Paciente'
        mensaje = 'Error al editar Historia Medica'
        messagebox.showerror(title,mensaje)

# 01
#PARA INGRESAR DATOS A LA TABLA ----------------------------------------------------
class historiaMedica:
    def __init__(self, idPersona, fechaHistoria, motivo, examenAuxiliar, tratamiento, detalle):
        self.idHistoriaMedica = None
        self.idPersona = idPersona
        self.fechaHistoria = fechaHistoria
        self.motivo = motivo
        self.examenAuxiliar = examenAuxiliar
        self.tratamiento = tratamiento
        self.detalle = detalle
        

    def __str__(self):
        return f'historiaMedica[{self.idPersona},{self.fechaHistoria},{self.motivo},{self.examenAuxiliar},{self.tratamiento},{self.detalle}]'