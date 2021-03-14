# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow,QTableWidgetItem,QSizePolicy,QHeaderView
from PySide2.QtCore import Qt

# diseño
from view.ui_elementos import Ui_Elementos

class MainTablew(QMainWindow):
    def __init__(self):
        super(MainTablew, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # EVENTOS /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/
        
        # llenado de valores *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'definimos una lista de valores' 
        self.listadatos=[
                ['a12','nokia','nokia@gmail.com','nokia.org'],
                ['a15','huawei','huawei@gmail.com','huawei.org'],
                ['a16','asus','asus@gmail.com','asus.org'],
                ['a20','blackberry','blackberry@gmail.com','blackberry.org'],
                ['a24','oppo','oppo@gmail.com','oppo.org'],
                    ]

        'llenar tabla, para ello le pasamos la lista de valores'
        self.raiz.btnt1.clicked.connect(lambda : self.llenartabla(self.listadatos))

        # extraer fila,columna,item,lista_fila (evento) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.tablet1.cellClicked.connect(
            lambda fila,columna: 
                print(

                    # fila
                    f'\n*fila:\t{fila}',

                    # columna
                    f'\n*colum:\t{columna}',

                    # item seleccionado
                    f'\n*item:\t{self.raiz.tablet1.item(fila, columna).text()}',

                    # elementos de la fila
                    f'\n*lista:\t{[self.raiz.tablet1.item(fila, columna).text() for columna in range(self.raiz.tablet1.columnCount())]}',

                    # solo el 1er elemento (index 0)
                    f'\n*1er item:\t{self.raiz.tablet1.item(fila, 0).text()}',
                
                )
            )
    

        # insertar columna y fila en la ultima posicion *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.tablet1.insertRow(self.raiz.tablet1.rowCount())'
        'self.raiz.tablet1.insertColumn(self.raiz.tablet1.columnCount())'

        # crear columna y filas por rango *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.tablet1.setRowCount(10)'
        'self.raiz.tablet1.setColumnCount(10)'

        # insertar columna y fila por index *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.tablet1.insertRow(2)#se basa en index'
        'self.raiz.tablet1.insertColumn(2)#se basa en index'

        # eliminar fila de tabla *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        '''
        para esto deberas agregar un controlador para evitar que 
        los elementos se sigan eliminado con el boton.

        En este caso no se le agrego, esto solo es para mostrar la funcionalidad. 
        '''
        self.raiz.btnt4.clicked.connect(lambda : 
                self.raiz.tablet1.removeRow(
                    #NOTA: con este mismo index podremos eliminarlo de la matriz "self.listadatos"
                    self.raiz.tablet1.currentRow()
                )
            )

        # obtener lista de fila (por boton) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'nota: *funciones en en final del codigo*'
        self.raiz.btnt2.clicked.connect(lambda : self.listaRowTablaUno(self.raiz.tablet1.currentRow()))

        # obtener fila o columna actual *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.tablet1.currentRow()'
        'self.raiz.tablet1.currentColumn()'

        # borrado de elementos *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnt3.clicked.connect(lambda : self.raiz.tablet1.setRowCount(0))

        # total de filas y columnas *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        cantidadFilas = self.raiz.tablet1.rowCount()
        cantidadColumnas = self.raiz.tablet1.columnCount()
        

        # CONFIGURACIONES /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # establecer "filas" fija, elastica, interactiva (para todos) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*   
        'Fixed Stretch Interactive'
        self.raiz.tablet1.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)

        # establecer "columnas" fija, elastica, interactiva (para todos) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'Fixed Stretch Interactive'
        self.raiz.tablet1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        # establecer "columna" fija (por index) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        '1. primeramente elegimos el index 0'
        self.raiz.tablet1.horizontalHeader().setSectionResizeMode(0, QHeaderView.Fixed)

        # establecer tamaño de "columnas" por index *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        '2. despues le designamos un tamaño'
        self.raiz.tablet1.setColumnWidth(0, 50)


    def llenartabla(self,lista):
        '''llenar elementos a la tabla'''

        # borrar elementos de la tabla *-*-*-*-*-*-*-*-*
        self.raiz.tablet1.setRowCount(0)

        # crear filas con respecto a los elementos *-*-*-*-*-*-*-*-*
        self.raiz.tablet1.setRowCount(len(lista))

        # reocorrer columnas y lista de items *-*-*-*-*-*-*-*-*
        for fila,listaItem in enumerate(lista):
            # agregar items
            for columna,item in enumerate(listaItem):
                self.raiz.tablet1.setItem(fila, columna, QTableWidgetItem(str(item))) # insertar items
                self.raiz.tablet1.item(fila,columna).setTextAlignment(Qt.AlignCenter|Qt.AlignVCenter) # alinear items

    def listaRowTablaUno(self,fila):
        '''extraer lista de elementos de una fila'''

        #si no se selecciono nada, la fila sera -1
        if(fila>=0):

            # cantidad de columnas *-*-*-*-*-*-*-*-*
            columnas = self.raiz.tablet1.columnCount()

            # recorremos todas las columnas de la fila seleccionada *-*-*-*-*-*-*-*-*
            lista=[self.raiz.tablet1.item(fila, columna).text() for columna in range(columnas)]
            
            print(lista)
