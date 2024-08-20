from calendar import LocaleHTMLCalendar
import tkinter as tk
from modelo.pacienteDao import Persona, guardarDatoPaciente, listarCondicion, listar, editarDatoPaciente, eliminarPaciente
from tkinter import *
from tkinter import Button, ttk, scrolledtext, Toplevel
from tkinter import messagebox
import tkcalendar as tc
from tkcalendar import *
from tkcalendar import DateEntry
from datetime import datetime, date





class Frame(tk.Frame):
    def __init__(self, root):

        super().__init__(root, width=1280, height=720)
        self.root = root
        self.pack()
        self.config(bg='#CDD8FF')
        self.idPersona = None
        self.campoPaciente()
        self.deshabilitar()
        self.tablaPaciente()

    def campoPaciente(self):
# NOMBRE DE LOS CAMPOS ------------------------------------------------------
        self.lblNombre = tk.Label(self, text='Nombre: ')
        self.lblNombre.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblNombre.grid(column=0, row=0,padx=10, pady=5)
        #APELLIDO PATERNO
        self.lblApellidoPaterno = tk.Label(self, text='Apellido Paterno: ')
        self.lblApellidoPaterno.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblApellidoPaterno.grid(column=0, row=1,padx=10, pady=5)
        #APELLIDO MATERNO
        self.lblApellidoMaterno = tk.Label(self, text='Apellido Materno: ')
        self.lblApellidoMaterno.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblApellidoMaterno.grid(column=0, row=2,padx=10, pady=5)
        #DNI 
        self.lblDni = tk.Label(self, text='DNI: ')
        self.lblDni.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblDni.grid(column=0, row=3,padx=10, pady=5)
        #FECHA DE NACIMIENTO
        self.lblFechaNacimiento = tk.Label(self, text='Fecha de Nacimiento: ')
        self.lblFechaNacimiento.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblFechaNacimiento.grid(column=0, row=4,padx=10, pady=5)
        # EDAD
        self.lblEdad = tk.Label(self, text='Edad: ')
        self.lblEdad.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblEdad.grid(column=0, row=5,padx=10, pady=5)
        # ANTECEDENTES
        self.lblAntecedentes = tk.Label(self, text='Antecedentes: ')
        self.lblAntecedentes.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblAntecedentes.grid(column=0, row=6,padx=10, pady=5)
        # CORREO
        self.lblCorreo = tk.Label(self, text='Correo: ')
        self.lblCorreo.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblCorreo.grid(column=0, row=7,padx=10, pady=5)
        # TELEFONO
        self.lblTelefono = tk.Label(self, text='Telefono: ')
        self.lblTelefono.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblTelefono.grid(column=0, row=8,padx=10, pady=5)
        # ACTIVO    
        # 
        # 
        # ENTRYS: SON LAS CAJAS DE TEXTO ---------- 
        # NOBRE
        self.svNombre = tk.StringVar()
        self.entryNombre = tk.Entry(self,textvariable=self.svNombre)
        self.entryNombre.config(width=50, font=('ARIAL',15))
        self.entryNombre.grid(column=1, row=0, padx=10, pady=5, columnspan=2)
        # APELLIDO PATERNO
        self.svApellidoPaterno = tk.StringVar()
        self.entryApellidoPaterno = tk.Entry(self,textvariable=self.svApellidoPaterno)
        self.entryApellidoPaterno.config(width=50, font=('ARIAL',15))
        self.entryApellidoPaterno.grid(column=1, row=1, padx=10, pady=5, columnspan=2)
        # APELLIDO MATERNO
        self.svApellidoMaterno = tk.StringVar()
        self.entryApellidoMaterno = tk.Entry(self,textvariable=self.svApellidoMaterno)
        self.entryApellidoMaterno.config(width=50, font=('ARIAL',15))
        self.entryApellidoMaterno.grid(column=1, row=2, padx=10, pady=5, columnspan=2)
        # DNI
        self.svDni = tk.StringVar()
        self.entryDni = tk.Entry(self,textvariable=self.svDni)
        self.entryDni.config(width=50, font=('ARIAL',15))
        self.entryDni.grid(column=1, row=3, padx=10, pady=5, columnspan=2)
        # FECHA DE NACIMIENTO
        self.svFechaNacimiento = tk.StringVar()
        self.entryFechaNacimiento = tk.Entry(self,textvariable=self.svFechaNacimiento)
        self.entryFechaNacimiento.config(width=50, font=('ARIAL',15))
        self.entryFechaNacimiento.grid(column=1, row=4, padx=10, pady=5, columnspan=2)
        # EDAd
        self.svEdad = tk.StringVar()
        self.entryEdad = tk.Entry(self, textvariable=self.svEdad)
        self.entryEdad.config(width=50, font=('ARIAL',15))
        self.entryEdad.grid(column=1, row=5, padx=10, pady=5, columnspan=2)
        
        #ANTECEDENTES
        self.svAntecedentes = tk.StringVar()
        self.entryAntecedentes = tk.Entry(self,textvariable=self.svAntecedentes)
        self.entryAntecedentes.config(width=50, font=('ARIAL',15))
        self.entryAntecedentes.grid(column=1, row=6, padx=10, pady=5, columnspan=2)
        
        # CORREO
        self.svCorreo = tk.StringVar()
        self.entryCorreo = tk.Entry(self,textvariable=self.svCorreo)
        self.entryCorreo.config(width=50, font=('ARIAL',15))
        self.entryCorreo.grid(column=1, row=7, padx=10, pady=5, columnspan=2)
        # TELEFONO
        self.svTelefono = tk.StringVar()
        self.entryTelefono = tk.Entry(self,textvariable=self.svTelefono)
        self.entryTelefono.config(width=50, font=('ARIAL',15))
        self.entryTelefono.grid(column=1, row=8, padx=10, pady=5, columnspan=2)   

        #BUTTONS  
        # 
        # 
        # NUEVO

        self.btnNuevo = tk.Button(self, text='Nuevo', command=self.habilitar)
        self.btnNuevo.config(width=20, font=('ARIAL',12, 'bold'),fg='#faf8f7', 
                             bg='#3d823b', cursor='hand2', activebackground='#8ce988')
        self.btnNuevo.grid(column=0, row=9, padx=10, pady=5) 

        #GUARDAR
        # 
        self.btnGuardar = tk.Button(self, text='Guardar', command=self.guardarPaciente)
        self.btnGuardar.config(width=20, font=('ARIAL',12, 'bold'),fg='#faf8f7', 
                             bg='#383938', cursor='hand2', activebackground='#6f6f6f')
        self.btnGuardar.grid(column=1, row=9, padx=10, pady=5)  

        #CANCELAR
        # 
        self.btnCancelar = tk.Button(self, text='Cancelar', command=self.deshabilitar)
        self.btnCancelar.config(width=20, font=('ARIAL',12, 'bold'),fg='#faf8f7', 
                             bg='#f54f4f', cursor='hand2', activebackground='#9c2c2c')
        self.btnCancelar.grid(column=2, row=9, padx=10, pady=5)          

# MODULO BUSCAR PACIENTE 

        self.lblbuscarDni = tk.Label(self, text='Buscar DNI: ')
        self.lblbuscarDni.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblbuscarDni.grid(column=3, row=0,padx=10, pady=5)

        self.lblbuscarApellido = tk.Label(self, text='Buscar Apellido: ')
        self.lblbuscarApellido.config(font=('ARIAL',15,'bold'), bg='#CDD8FF')
        self.lblbuscarApellido.grid(column=3, row=1,padx=10, pady=5)
        
        self.svbuscarDni = tk.StringVar()
        self.entrybuscarDni = tk.Entry(self,textvariable=self.svbuscarDni)
        self.entrybuscarDni.config(width=15, font=('ARIAL',15))
        self.entrybuscarDni.grid(column=4, row=0, padx=10, pady=5, columnspan=2) 


        self.svbuscarApellido = tk.StringVar()
        self.entrybuscarApellido = tk.Entry(self,textvariable=self.svbuscarApellido)
        self.entrybuscarApellido.config(width=15, font=('ARIAL',15))
        self.entrybuscarApellido.grid(column=4, row=1, padx=10, pady=5, columnspan=2)

        # BOTON BUSCAR

        self.btnBuscar = tk.Button(self, text='Buscar', command=self.buscarCondicion)
        self.btnBuscar.config(width=20, font=('ARIAL',12, 'bold'),fg='#faf8f7', 
                             bg='#383938', cursor='hand2', activebackground='#6f6f6f')
        self.btnBuscar.grid(column=3, row=2, padx=10, pady=5)

        # BOTON LIMPIAR BUSCADOR

        self.btnLimpiar = tk.Button(self, text='Limpiar Buscador', command=self.limpiar)
        self.btnLimpiar.config(width=20, font=('ARIAL',12, 'bold'),fg='#faf8f7', 
                             bg='#bd24ee', cursor='hand2', activebackground='#e191fb')
        self.btnLimpiar.grid(column=3, row=3, padx=10, pady=5)

 #BOTON CALENDARIO 

        self.btnCalendario = tk.Button(self, text='Calendario', command=self.vistaCalendario)
        self.btnCalendario.config(width=12, font=('ARIAL',12, 'bold'),fg='#faf8f7', 
                             bg='#16d6d9', cursor='hand2', activebackground='#81f6f8')
        self.btnCalendario.grid(column=3, row=4, padx=10, pady=5)

        #VENTANA FLOTANTE PARA COLOCAR EL CALENDARIO, CUANDO SE PRESIONE EL BOTON CALENDARIO

    def vistaCalendario(self): 
        self.calendario = Toplevel()
        self.calendario.title("FECHA NACIMIENTO")
        self.calendario.resizable(500,350)
        self.calendario.config(bg='#CDD8FF')

        self.svCalendario = StringVar()
        self.cal= DateEntry(self.calendario, width=30 , bg="darkblue", fg="white", selectmode='day', year=1990, month=1, day=1, locale = 'es_US', cursor = 'hand2', date_pattern='dd-mm-Y',textvariable=self.svCalendario)
        self.cal.pack(pady=22)
            
    # aca se utiliza el TRACE PARA ENVIAR LA FECHA 
        
        self.svCalendario.trace('w', self.enviarFecha)
        
        
        

    # ESTA FUNCION ES PARA ENVIAE LA FECHA A LA CASILLA DE FECHA

    def enviarFecha(self, *args):
        self.svFechaNacimiento.set('' + self.svCalendario.get())
        if self.cal > 1:
            self.svCalendario.trace('w', self.calcularEdad)

    # CALCULAR EDAD MEDIANTE FECHA DE NACIMIENTO

    def calcularEdad(self, *args):
        self.fechaActual = date.today() # dd-mm-yy fecha actual
        self.date1 = self.cal.get_date() # dato escogido en el calendario
        self.conver = datetime.strptime(self.date1, "%d-%m-%Y") # se convierte en d-m-a

        self.resul = self.fechaActual.year - self.conver.year
        self.resul -= ((self.fechaActual.month, self.fechaActual.day) < (self.conver.month , self.conver.day))
        self.svEdad.set(self.resul)



        # PROGRAMA EL BOTON BUSCAR

    def buscarCondicion(self): 
        if len(self.svbuscarDni.get()) > 0 or len(self.svbuscarApellido.get()) > 0:
            where = "WHERE 1=1"
            if (len(self.svbuscarDni.get())) > 0:
                where = "WHERE dni = " + self.svbuscarDni.get() + ""
            if (len(self.svbuscarApellido.get())) > 0:
                where = "WHERE apellidoPaterno LIKE '" + self.svbuscarApellido.get() +"%' AND activo = 1" 

            self.tablaPaciente(where)
        else:
            self.tablaPaciente()

   
        

        #PROGRAMAR BOTON LIMPIAR

    def limpiar(self):
        self.svbuscarDni.set('')
        self.svbuscarApellido.set('')
        self.tablaPaciente()

        #self.entrybuscarDni.config(state='disabled')
        #self.entrybuscarApellido.config(state='disabled')
        
# CREANDO LA FUNCION AL BOTON GUARDAR
#todos los datos q se estan ingresando en esta clase persona, 
# se van a enviar en este orden
# SE COLOCAN LOS DATOS DEL ENTRY svNombre, svApellidoPaterno
    def guardarPaciente(self):            
        persona = Persona(
            self.svNombre.get(), self.svApellidoPaterno.get(), self.svApellidoMaterno.get(), self.svDni.get(), self.svFechaNacimiento.get(), self.svEdad.get() ,self.svAntecedentes.get(),self.svCorreo.get(), self.svTelefono.get())
        
        if self.idPersona == None:
            guardarDatoPaciente(persona)

        else:
            editarDatoPaciente(persona, self.idPersona)

        self.deshabilitar()
        self.tablaPaciente()
        
    # HABILITAR CAMPOS
    def habilitar(self):
        #self.idPersona = None
        self.svNombre.set('')
        self.svApellidoPaterno.set('')
        self.svApellidoMaterno.set('')
        self.svDni.set('')
        self.svFechaNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')

        self.entryNombre.config(state='normal')
        self.entryApellidoPaterno.config(state='normal')
        self.entryApellidoMaterno.config(state='normal')
        self.entryDni.config(state='normal')
        self.entryFechaNacimiento.config(state='normal')
        self.entryEdad.config(state='normal')
        self.entryAntecedentes.config(state='normal')
        self.entryCorreo.config(state='normal')
        self.entryTelefono.config(state='normal')
        
        # HABILITA BOTON GUARDAR Y CANCELAR
        self.btnGuardar.config(state='normal')
        self.btnCancelar.config(state='normal')
        self.btnCalendario.config(state='normal')
     


    #Se crea la funcion para desactivar las casillas     
    def deshabilitar(self):
        self.idPersona = None
     #  ESTO ES PARA QUE 
     # UNA VEZ CUNADO SE GUARDEN LOS DATOS, SE VUELVA A DESACTIVAR LAS CASILLAS
        self.svNombre.set('')
        self.svApellidoPaterno.set('')
        self.svApellidoMaterno.set('')
        self.svDni.set('')
        self.svFechaNacimiento.set('')
        self.svEdad.set('')
        self.svAntecedentes.set('')
        self.svCorreo.set('')
        self.svTelefono.set('')
        
        # FUNCION DESABILITAR LAS CAJAS DE TEXTO, PARA HABILITARLAS
        #SE LES DEBE DAR EN EL BOTON NUEVO
        self.entryNombre.config(state='disabled')
        self.entryApellidoPaterno.config(state='disabled')
        self.entryApellidoMaterno.config(state='disabled')
        self.entryDni.config(state='disabled')
        self.entryFechaNacimiento.config(state='disabled')
        self.entryEdad.config(state='disabled')
        self.entryAntecedentes.config(state='disabled')
        self.entryCorreo.config(state='disabled')
        self.entryTelefono.config(state='disabled')
        
        # DESABILITA BOTON GUARDAR Y CANCELAR
        self.btnGuardar.config(state='disabled')
        self.btnCancelar.config(state='disabled')
        self.btnCalendario.config(state='disabled')

    def tablaPaciente(self, where=""):

        if len(where) > 0:
            self.listaPersona = listarCondicion(where)
        else:
            self.listaPersona = listar()

        self.tabla = ttk.Treeview(self, column=('Nombre', 'APaterno', 'AMaterno', 'Dni', 'FNacimiento', 'Edad', 'Antecedentes', 'Correo','Telefono'))
        self.tabla.grid(column=0, row=10, columnspan=10, sticky="nse")
        
        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=10, column=11, sticky='nse')

        self.tabla.configure(yscrollcommand = self.scroll.set)

        self.tabla.tag_configure('evenrow', background='#C5EAFE')

        # CABECERA DE LA TABLA
        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Ape. Paterno')
        self.tabla.heading('#3', text='Ape. Materno')
        self.tabla.heading('#4', text='Dni')
        self.tabla.heading('#5', text='F. Nacimiento')
        self.tabla.heading('#6', text='Edad')
        self.tabla.heading('#7', text='Antecedentes')
        self.tabla.heading('#8', text='Correo')
        self.tabla.heading('#9', text='Telefono')

        # LAS COLUMNAS 

        self.tabla.column('#0', anchor=W, width=50)
        self.tabla.column('#1', anchor=W, width=100) #Nombre
        self.tabla.column('#2', anchor=W, width=100) #Ape. Paterno
        self.tabla.column('#3', anchor=W, width=100) #Ape. Materno
        self.tabla.column('#4', anchor=W, width=80)  #Dni
        self.tabla.column('#5', anchor=W, width=90) #F. Nacimiento
        self.tabla.column('#6', anchor=W, width=40)  #Edad
        self.tabla.column('#7', anchor=W, width=120) #Antecedentes
        self.tabla.column('#8', anchor=W, width=200) #Correo
        self.tabla.column('#9', anchor=W, width=80)  #Telefono

        #LLENAR CON LOS DATOS LA TABLA

        for p in self.listaPersona:

            self.tabla.insert('',0,text=p[0], values=(p[1],p[2],p[3],p[4],p[5],p[6],p[7],p[8],p[9]), tags=('evenrow',))
        
        # BOTONES

        self.btnEditarPaciente = tk.Button(self, text='Editar Paciente', command=self.editarPaciente)
        self.btnEditarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#060600', bg='#ded825', activebackground='#f7f49c', cursor='hand2')
        self.btnEditarPaciente.grid(row=11, column=0, padx=10, pady=5)

        self.btnEliminarPaciente = tk.Button(self, text='Eliminar Paciente', command=self.eliminarPaciente)
        self.btnEliminarPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#060600', bg='#0fd2ba', activebackground='#8ff3e7', cursor='hand2')
        self.btnEliminarPaciente.grid(row=11, column=1, padx=10, pady=5)

        self.btnhistorialPaciente = tk.Button(self, text='historial Paciente')
        self.btnhistorialPaciente.config(width=20,font=('ARIAL',12,'bold'), fg='#060600', bg='#eb703b', activebackground='#f4bba3', cursor='hand2')
        self.btnhistorialPaciente.grid(row=11, column=2, padx=10, pady=5)

        self.btnsalir = tk.Button(self, text='Salir', command=self.root.destroy)
        self.btnsalir.config(width=20,font=('ARIAL',12,'bold'), fg='#060600', bg='#eb703b', activebackground='#f4bba3', cursor='hand2')
        self.btnsalir.grid(row=11, column=4, padx=10, pady=5)

    # FUNCION DE EDITAR PACIENTE

    def editarPaciente(self):
        try:
            self.idPersona= self.tabla.item(self.tabla.selection())['text']
            self.nombrePaciente = self.tabla.item(self.tabla.selection())['values'][0]
            self.apellidoPaternoPaciente = self.tabla.item(self.tabla.selection())['values'][1]
            self.apellidoMaternoPaciente = self.tabla.item(self.tabla.selection())['values'][2]
            self.dniPaciente = self.tabla.item(self.tabla.selection())['values'][3]
            self.fechaNacimientoPaciente= self.tabla.item(self.tabla.selection())['values'][4]
            self.edadPaciente = self.tabla.item(self.tabla.selection())['values'][5]
            self.antecedentesPaciente = self.tabla.item(self.tabla.selection())['values'][6]
            self.correoPaciente = self.tabla.item(self.tabla.selection())['values'][7]
            self.telefonoPaciente = self.tabla.item(self.tabla.selection())['values'][8]

            #HABILITAR LOS CAMPOS 

            self.habilitar()

            self.entryNombre.insert(0, self.nombrePaciente)
            self.entryApellidoPaterno.insert(0, self.apellidoPaternoPaciente)
            self.entryApellidoMaterno.insert(0, self.apellidoMaternoPaciente)
            self.entryDni.insert(0, self.dniPaciente)
            self.entryFechaNacimiento.insert(0, self.fechaNacimientoPaciente)
            self.entryEdad.insert(0, self.edadPaciente)
            self.entryAntecedentes.insert(0, self.antecedentesPaciente)
            self.entryCorreo.insert(0, self.correoPaciente)
            self.entryTelefono.insert(0, self.telefonoPaciente)


        except:
            titulo = 'Editar Paciente'
            mensaje = 'Error al editar Paciente'
            messagebox.showerror(titulo, mensaje)

    def eliminarPaciente(self):
        try:
            self.idPersona = self.tabla.item(self.tabla.selection())['text']
            eliminarPaciente(self.idPersona)
            

            self.tablaPaciente()
            self.idPersona = None

        except:
            titulo = 'Elimianr Paciente'
            mensaje = 'Error al eliminar Paciente'
            messagebox.showerror(titulo, mensaje)