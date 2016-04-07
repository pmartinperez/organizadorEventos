from gi.repository import Gtk
import conexionBD
import vMensaje


class CrearEvento(Gtk.Window):
    ''' Clase que nos permite crear un nuevo evento. Nos pide introducir unos datos que se guardaran en la BD '''

    def __init__(self):
        # Creamos la ventana
        Gtk.Window.__init__(self, title="Crear Evento")
        self.set_border_width(10)
        self.set_default_size(400,200)
        # Conexion a la BD
        self.conexion = conexionBD.conectar(self)

        # Creamos el contenedor principal de tipo Table
        table = Gtk.Table(4, 2, True)
        self.add(table)

        # Elementos Label, Entry y Button
        label = Gtk.Label("Nombre:")
        label.set_margin_top(10)
        label.set_margin_bottom(10)
        label2 = Gtk.Label("Tipo:")
        label2.set_margin_bottom(10)
        label3 = Gtk.Label("Fecha:")
        label3.set_margin_bottom(10)

        self.entry1 = Gtk.Entry()
        self.entry1.set_margin_top(10)
        self.entry1.set_margin_bottom(10)
        self.entry2 = Gtk.Entry()
        self.entry2.set_margin_bottom(10)
        self.entry3 = Gtk.Entry()
        self.entry3.set_margin_bottom(10)

        button1 = Gtk.Button("Crear")
        button1.connect("clicked", self.on_botonCrear_clicked)
        button2 = Gtk.Button("Cancelar")
        button2.connect("clicked", self.on_botonCancelar_clicked)

        # Colocamos los distintos widgets en la tabla
        table.attach(label, 0, 1, 0, 1)
        table.attach(label2, 0, 1, 1, 2)
        table.attach(label3, 0, 1, 2, 3)

        table.attach(self.entry1, 1, 3, 0, 1)
        table.attach(self.entry2, 1, 3, 1, 2)
        table.attach(self.entry3, 1, 3, 2, 3)

        table.attach(button1, 1, 2, 3, 4)
        table.attach(button2, 2, 3, 3, 4)

    def on_botonCrear_clicked(self, widget):
        ''' Evento del boton Crear que recoge los datos introducidos en los distintos elementos de tipo Entry y los
            guarda como un registro de la tabla EVENTO en la BD '''

        # Realizamos la insercion en la BD
        lista = self.conexion.cursor()
        datos = [(self.entry1.get_text(), self.entry2.get_text(), self.entry3.get_text())]
        conexionBD.insertar(lista,'evento', datos)
        self.conexion.commit()
        self.conexion.close()

        # Borramos el texto de los elementos tipo Entry
        self.entry1.set_text("")
        self.entry2.set_text("")
        self.entry3.set_text("")

        # Mostramos una ventana con un mensaje de exito en la operacion
        window2 = vMensaje.Mensaje("Creado correctamente")
        window2.connect("delete-event", Gtk.main_quit)
        window2.show_all()
        Gtk.main()

    def on_botonCancelar_clicked(self, widget):
        ''' Evento del boton Cancelar que cierra la ventana '''
        self.destroy()

