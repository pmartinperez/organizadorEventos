from gi.repository import Gtk, Gdk

import vCrearEvento


class Mensaje(Gtk.Window):
    ''' Ventana que muestra un mensaje que pasamos com parametro. La utilizamos para mostrar mensajes de exito,
        comprobacion, confirmacion o error '''

    def __init__(self, mensaje):
        # Creamos la ventan principal
        Gtk.Window.__init__(self, title = "Mensaje")
        self.set_border_width(10)
        self.set_default_size(200,200)

        # Contenedor de tipo Box para la ventana principal
        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        # Elementos Label y Button
        label = Gtk.Label(mensaje)
        label.set_margin_left(10)
        label.set_margin_right(10)
        label.set_margin_top(10)
        button = Gtk.Button("Aceptar")
        button.connect("clicked", self.on_botonAceptar_clicked)

        # Anhadimos los elementos al contenedor
        box.add(label)
        box.add(button)

        self.show_all()

    def on_botonAceptar_clicked(self, widget):
        ''' Evento del boton Aceptar que cierra la ventana'''
        self.destroy()
