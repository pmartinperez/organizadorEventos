from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table

import conexionBD


class Informe():
    ''' Clase que genera un informe'''

    def __init__(self, consulta):
        conexion = conexionBD.conectar(self)
        self.cursor = conexion.cursor()

        self.consulta = consulta
        self.cursor.execute(self.consulta)
        self.cabecera = self.cursor.description

        guion = []
        filas= []
        filaCabecera = []
        for x in range(0,len(self.cabecera)):
            unaCabecera = self.cabecera[x][0]
            filaCabecera.append(unaCabecera)

        filas.append(filaCabecera)

        for datos in self.cursor:
            filas.append(datos)


        tabla =  Table(filas)

        tabla.setStyle([('BACKGROUND',(0,0),(3,0),colors.aliceblue), ('INNERGRID',(0,1),(-1,-1),0.25,colors.black)])

        guion.append(tabla)

        doc = SimpleDocTemplate("informes/informe.pdf", pagesize=A4,showBoundray=1)

        doc.build(guion)