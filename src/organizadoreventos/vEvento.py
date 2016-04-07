from gi.repository import Gtk

import conexionBD
import vTabla


class Evento(Gtk.Window):
    ''' Ventana que muestra las distintas tablas del evento en distintos tabs '''

    def __init__(self):
        # Creamos la ventana
        Gtk.Window.__init__(self, title="Evento")
        self.set_border_width(10)
        self.set_default_size(450,400)

        # Contenedor tipo Notebook de la ventana
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Nos conectamos a la BD y recogemos los datos de la tabla TABLAS
        conexion = conexionBD.conectar(self)
        cursor = conexion.cursor()
        lista = conexionBD.mostrarTablas(cursor, "tablas")

        # Creamos un contenedor de tipo Box donde guardamos la tabla donde mostramos los datos
        # Con el bucle damos nombre a las distintas paginas del Notebook
        for x in lista:
            box = Gtk.Box()
            vTabla.Tabla(x[0], box) # Pasamos como parametro el nombre de la tabla que vamos a mostrar
            label2 = Gtk.Label()
            label2.set_text(x[0]) # Nombre del tab
            self.notebook.append_page(box, label2) #Se inserta la tabla y el nombre del tab
