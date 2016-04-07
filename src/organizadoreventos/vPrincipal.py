from gi.repository import Gtk, Gdk
import vCrearEvento
import vEvento
import conexionBD
import Menu


class Principal(Gtk.Window):
    ''' Ventana que muestra los eventos creados con su nombre y tipo de evento mas un boton para editarlo.
        Tambien tenemos un boton para crear un nuevo evento'''
    def __init__(self):
        Gtk.Window.__init__(self, title = "Principal")
        #self.set_border_width(10)
        #self.set_default_size(500,500)

        #Obtenemos la conexion a la BD
        self.conexion = conexionBD.conectar(self)

        # Cabecera
        # Titulo, subtitulo y botones de minimizar, maximizar, cerrar
        header = Gtk.HeaderBar(title="Eventos")
        header.set_subtitle("Organizador eventos")
        header.props.show_close_button = True
        self.set_titlebar(header)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        # Scroll
        scrolled = Gtk.ScrolledWindow()
        scrolled.set_size_request(500,500)
        scrolled.set_border_width(10)
        scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)

        # Contenedor de tipo FlowBox para la ventana
        flowbox = Gtk.FlowBox()
        flowbox.set_valign(Gtk.Align.START)
        flowbox.set_max_children_per_line(3)
        flowbox.set_column_spacing(10)
        flowbox.set_row_spacing(10)
        flowbox.set_selection_mode(Gtk.SelectionMode.NONE)

        # Añadimos al flowbox contenedores de tipo Box que contienen los eventos
        self.crear_ventanas(flowbox)

        # Añadimos los elementos a la ventana

        scrolled.add(flowbox)
        caixa = Menu.Menu().crearMenu()
        vbox.pack_start(caixa, True, True, 0)
        vbox.pack_start(scrolled, True, True, 0)

    def crear_ventanas(self, flowbox):
        ''' Metodo para crear los distintos contenedores para mostrar los eventos '''

        # Obtenemos los datos de los eventos a partir de la BD
        lista = self.conexion.cursor()
        conexionBD.consultar(lista, "evento")

        # Contedor de tipo Box que contiene un boton para añadir eventos
        hbox = Gtk.Box(spacing=20)
        hbox.set_homogeneous(False)
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox.set_homogeneous(False)
        vbox.override_background_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(1.0,1.0,1.0,1))
        hbox.pack_start(vbox, True, True, 0)

        # Elementos Label y Button
        label = Gtk.Label("Nuevo Evento")
        label.set_margin_left(10)
        label.set_margin_right(10)
        label.set_margin_top(10)
        label2 = Gtk.Label("")

        botonCrear = Gtk.Button()
        image = Gtk.Image.new_from_icon_name("document-new",Gtk.IconSize.MENU)
        botonCrear.add(image)
        botonCrear.connect("clicked", self.on_botonCrear_clicked)

        vbox.pack_start(label, True, True, 0)
        vbox.pack_start(label2, True, True, 0)
        vbox.pack_start(botonCrear, True, True, 0)

        flowbox.add(hbox)

        # Bucle que crea una ventana de tipo Box donde se muestran los datos de los distintos eventos
        for resultado in lista:
            hbox = Gtk.Box(spacing=20)
            hbox.set_homogeneous(False)

            vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
            vbox.set_homogeneous(False)
            vbox.override_background_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(1.0,1.0,1.0,1))
            hbox.pack_start(vbox, True, True, 0)

            # Elementos Label y Button
            label = Gtk.Label(resultado[0])
            label.set_margin_left(10)
            label.set_margin_right(10)
            label.set_margin_top(10)

            label2 = Gtk.Label(resultado[1])
            label2.set_margin_left(10)
            label2.set_margin_right(10)
            botonVer = Gtk.Button()
            image = Gtk.Image.new_from_icon_name("emblem-documents",Gtk.IconSize.MENU)
            botonVer.add(image)
            botonVer.connect("clicked", self.on_botonVer_clicked)

            vbox.pack_start(label, True, True, 0)
            vbox.pack_start(label2, True, True, 0)
            vbox.pack_start(botonVer, True, True, 0)
            flowbox.add(hbox)




    # Definimos el evento del boton Crear Evento
    def on_botonCrear_clicked(self, widget):
        ''' Evento del boton Crear para crear un neuvo evento. Llama a la clase CrearEvento para mostrar la ventana '''
        window2 = vCrearEvento.CrearEvento()
        window2.connect("delete-event", Gtk.main_quit)
        window2.show_all()
        Gtk.main()

    # Definimos el evento del boton Crear Evento
    def on_botonVer_clicked(self, widget):
        ''' Evento del boton Ver para mostrar los datos del evento. Llama a la clase Evento que crea una ventana
        con las tablas de la BD '''
        ventanaEvento = vEvento.Evento()
        ventanaEvento.connect("delete-event", Gtk.main_quit)
        ventanaEvento.show_all()
        Gtk.main()


# Creamos la ventana
window = Principal()
window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()