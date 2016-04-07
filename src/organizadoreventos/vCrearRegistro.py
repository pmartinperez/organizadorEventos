from gi.repository import Gtk
import sqlite3 as dbapi
import conexionBD
import vMensaje


class CrearRegistro(Gtk.Window):
    ''' Ventana para insertar un nuevo registro en alguna tabla de la BD. Nos pide una serie de datos, los recoge y los
        inserta en la BD '''

    def __init__(self, cabecera, tabla):
        # Creamos la tabla
        Gtk.Window.__init__(self, title="Crear Registro")

        # Guardamos el parametro con el nombre de la tabla en la que queremos insertar
        self.tabla = tabla

        # Conectamos a la BD
        self.conexion = conexionBD.conectar(self)

        # Contenedor de tipo Box con dos coulmnas, una para los elementos Lable y otra para los Entry
        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        self.add(hbox)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        self.entries=[]

        # Bucle con el que recogemos la cabecera de la tabla y con ello determinamos cuantos elementos Label y Entry
        # ponemos en la ventana y el nombre de los Label
        for x in range(0,len(cabecera)):
            label = Gtk.Label(cabecera[x][0])
            label.set_margin_top(10)
            self.entries.append(Gtk.Entry())
            vbox_left.add(label)
            vbox_right.add(self.entries[x])

        # Botones de Crear y Cancelar
        button1 = Gtk.Button("Crear")
        button1.connect("clicked", self.on_botonCrear_clicked)
        button2 = Gtk.Button("Cancelar")
        button2.connect("clicked", self.on_botonCancelar_clicked)
        vbox_left.add(button1)
        vbox_right.add(button2)

        self.show_all()


    def on_botonCrear_clicked(self, widget):
        ''' Evento para el boton Crear. Recogemos los datos ingresados en los elementos Entry y los pasamos como
            parametros para realizar una insercion en la tabla'''
        cursor = self.conexion.cursor()

        tupla = []
        for x in range (0,len(self.entries)):
            tupla.append(self.entries[x].get_text())
            self.entries[x].set_text("")
        datos = [tupla]
        print(datos)

        conexionBD.insertar(cursor,self.tabla, datos)
        self.conexion.commit()
        self.conexion.close()

        # Mostramos una ventana con un mensaje de exito en la operacion
        window2 = vMensaje.Mensaje("Creado registro correctamente")
        window2.connect("delete-event", Gtk.main_quit)
        window2.show_all()
        Gtk.main()

    def on_botonCancelar_clicked(self, widget):
        ''' Evento para el boton Cancelar que cierra la ventana'''
        self.destroy()

