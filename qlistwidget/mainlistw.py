# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow,QListWidgetItem

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplos
from random import randint

class MainListw(QMainWindow):
    def __init__(self):
        super(MainListw, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # lista de elementos a usar *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        listado = ['python 3','java','pealr','r','c#','html5']   

        # extraer variable str *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btno1.clicked.connect(lambda : self.raiz.listwo1.addItem(f'item_{randint(1,100)}') )

        # agregar lista de elemtos (en un index) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btno2.clicked.connect(lambda : self.raiz.listwo1.insertItems(0, listado) )

        # restablecer lista *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btno3.clicked.connect(lambda : self.raiz.listwo1.clear() )

        # obtener texto e index *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.listwo1.currentTextChanged.connect(lambda texto: print(texto) )
        self.raiz.listwo1.currentRowChanged.connect(lambda index: print(index) )

        # eliminar item de la fila *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        '''
        para esto deberas agregar un controlador para evitar que 
        los elementos se sigan eliminado con el boton.

        En este caso no se le agrego, esto solo es para mostrar la funcionalidad. 
        '''
        self.raiz.btno4.clicked.connect(lambda : 
                self.raiz.listwo1.takeItem(self.raiz.listwo1.currentRow())
                )  
    