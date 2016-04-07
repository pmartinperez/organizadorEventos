"""Tabla de resultados.
   :author: Patricia Martin Perez
   :version: 0.1"""

from gi.repository import Gtk, Gdk
import conexionBD
import vCrearRegistro
from informes import informe


class Tabla(Gtk.Window):
    """Muestra una *tabla*, que le hemos pasado como parametro, con los datos de la base de datos de dicha tabla.
    Ademas tiene una serie de botones para realizar distintas operaciones con sobre los resultados """

    def __init__(self, tabla, box=None ):
        """Inicializador de la clase **Tabla**.

           :Parameters:
             - `tabla`: Nombre de la tabla a consultar en la base de datos.
             - `box`: contenedor tipo BOx donde se guardara la tabla.
        """
        self.tabla = tabla
        self.box = box
        self.conexionBaseDatos()
        self.crearTabla()

    def conexionBaseDatos(self):
        """ Conexion a la base de tados. Recogemos los datos de la consulta que realizamos """
        self.conexion = conexionBD.conectar(self)
        self.cursor = self.conexion.cursor()
        self.consulta = """select * from """ + self.tabla
        self.cursor.execute(self.consulta)

    def crearTabla(self):
        """ Creamos la tabla """
        # Contenedor de tipo Grid
        grid = Gtk.Grid()
        grid.set_row_spacing(5)
        # Anhadimos este contenedor al Box que pasamos como parametro
        self.box.add(grid)

        # Scroll
        scrolledwindow = Gtk.ScrolledWindow()
        scrolledwindow.set_vexpand(True)
        scrolledwindow.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.NEVER)
        grid.attach(scrolledwindow, 0, 0, 1, 1)

        # Definimos el ListStore con el que mostramos los datos
        self.liststore = Gtk.ListStore(str, str, str)
        treemodelfilter = self.liststore.filter_new()

        # Barra con los distintos botones para Consultar, Crear reistro, Borrar registro y Actualizar la tabla
        box = Gtk.Box()
        self.entry = Gtk.Entry()
        box.add(self.entry)
        bConsultar = Gtk.Button()
        bConsultar.connect("clicked", self.on_botonConsultar_clicked)
        image = Gtk.Image.new_from_icon_name("system-search",Gtk.IconSize.MENU)
        bConsultar.add(image)
        box.add(bConsultar)
        bCrear = Gtk.Button("Crear")
        bCrear.connect("clicked", self.on_botonCrear_clicked)
        box.add(bCrear)
        bEditar = Gtk.Button("Editar")
        bEditar.connect("clicked", self.on_botonEditar_clicked)
        box.add(bEditar)
        bInforme = Gtk.Button("Informe")
        bInforme.connect("clicked", self.on_botonInforme_clicked)
        box.add(bInforme)
        bBorrar = Gtk.Button("Borrar")
        bBorrar.override_color(Gtk.StateFlags.NORMAL,Gdk.RGBA(255, 0, 0, 0.8))
        bBorrar.connect("clicked", self.on_botonBorrar_clicked)
        box.add(bBorrar)

        grid.attach(box, 0, 1, 1, 1)

        # Recorremos la lista con los datos de la tabla para guardarlos en el Liststore
        for datos in self.cursor:
            self.liststore.append(datos)
            print(datos)


        # Creamos la tabla
        self.treeview = Gtk.TreeView()
        self.treeview.set_model(treemodelfilter)
        scrolledwindow.add(self.treeview)


        # Creamos la cabecera de cada tabla
        cellrenderertext = Gtk.CellRendererText()
        self.cabecera = self.cursor.description
        for x in range(0,len(self.cabecera)):
            treeviewcolumn = Gtk.TreeViewColumn(self.cabecera[x][0], cellrenderertext, text=x)
            self.treeview.append_column(treeviewcolumn)

        self.show_all()

    def on_botonCrear_clicked(self, widget):
        ''' Evento del *boton Crear* que llama a la clase **CrearRegistro** con la que insertamos un registro en la tabla'''
        window2 = vCrearRegistro.CrearRegistro(self.cabecera, self.tabla)
        window2.connect("delete-event", Gtk.main_quit)
        window2.show_all()
        # Gtk.main()
        self.actualizar()

    def on_botonBorrar_clicked(self, widget):
        ''' Evento del boton *Borrar* que borra un registro seleccionado '''
        selection = self.treeview.get_selection()
        print("selection:")
        print(selection)

        # Recogemos una tupla con el ListStore y las filas seleccionadas
        liststore, filas = selection.get_selected_rows()

        if filas != None:
            print("You selected", liststore[filas][0])
            nombre = [(liststore[filas][0])]
            conexionBD.borrar(self.cursor,self.tabla, nombre)
            self.conexion.commit()

        self.actualizar()


    def on_botonInforme_clicked(self, widget):
        ''' Evento del boton *Informe* que crea el informe de la tabla visualizada'''
        informe.Informe(self.consulta)

    def on_botonConsultar_clicked(self, widget):
        ''' Evento del boton *Borrar* que borra un registro seleccionado '''
        texto = self.entry.get_text()

        datos = [self.cabecera[0][0], texto,self.cabecera[1][0], texto, self.cabecera[2][0], texto]
        for dato in datos:
            print(dato)
        cursor = conexionBD.buscar(self.cursor,self.tabla, datos)
        self.liststore.clear()
        for registro in cursor:
            self.liststore.append(registro)
            print(registro)

    def on_botonEditar_clicked(self, widget):
        print("editar")

    def actualizar(self):
        self.cursor.execute(self.consulta)
        self.liststore.clear()
        for datos in self.cursor:
            self.liststore.append(datos)
            print(datos)