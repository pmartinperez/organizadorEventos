from gi.repository import Gtk, Gdk
from gi.repository.GdkPixbuf import Pixbuf

import vCrearEvento

UI_INFO = """
<ui>
    <menubar name='BarraMenu'>
        <menu action='OrganizadorEventos'>
            <menuitem action='FileQuit' />
        </menu>

        <menu action='Evento'>
            <menuitem action='CrearEvento' />
        </menu>
    </menubar>
</ui>
"""

class Menu (Gtk.Window):

    def __init__(self):
        #Gtk.Window.__init__(self, title="Menu Evento")
        self.set_default_size(200, 200)


    def crearMenu(self):
        self.set_default_size(200, 200)
        grupo_accion = Gtk.ActionGroup("acciones")

        self.engadir_accions_menu_home(grupo_accion)
        #self.engadir_accions_menu_editar(grupo_accion)
        #self.engadir_accions_menu_elixir(grupo_accion)

        gestor_uimanager = self.create_ui_manager()
        gestor_uimanager.insert_action_group(grupo_accion)

        barraMenu = gestor_uimanager.get_widget("/BarraMenu")

        caixa = Gtk.Box (orientation=Gtk.Orientation.VERTICAL)
        caixa.pack_start(barraMenu, False, False, 0)

        self.add (caixa)
        return caixa



    def engadir_accions_menu_home(self, grupo_accion):
        #Menu Home
        accion_menuHome = Gtk.Action("OrganizadorEventos", "Organizador de Eventos", "Home", None) # None-> icono
        grupo_accion.add_action(accion_menuHome)

        homeSalir_accion = Gtk.Action("FileQuit",None, None, Gtk.STOCK_QUIT)
        homeSalir_accion.connect("activate", self.on_menu_sair)
        grupo_accion.add_action(homeSalir_accion)

        #Menu Evento
        accion_menuEvento = Gtk.Action("Evento", "Evento", "Evento", None) # None-> icono
        grupo_accion.add_action(accion_menuEvento)

        eventoCrear_accion = Gtk.Action("CrearEvento", "Crear Evento", None, Gtk.STOCK_NEW)
        eventoCrear_accion.connect("activate", self.on_menu_crear)
        grupo_accion.add_action(eventoCrear_accion)


    def create_ui_manager(self):
        uimanager = Gtk.UIManager()
        uimanager.add_ui_from_string(UI_INFO)

        accelgroup = uimanager.get_accel_group()
        self.add_accel_group(accelgroup)
        return uimanager

    def on_menu_sair(self, control):
        Gtk.main_quit()

    def on_menu_crear(self, control):
        window2 = vCrearEvento.CrearEvento()
        window2.connect("delete-event", Gtk.main_quit)
        window2.show_all()
        Gtk.main()

