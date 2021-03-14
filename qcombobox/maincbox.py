# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplo
from random import randint

class MainCbox(QMainWindow):
    def __init__(self):
        super(MainCbox, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)
        
        # lista de elemento a usar *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        lista_elementos = ['datos','gta iii','python 3','java']

        # establecer item por index *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.cboxc2.setCurrentIndex(0)

        # contar cuantos elementos tiene el combobox *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        print('Cantidad de elementos cbox1:',self.raiz.cboxc1.count())

        # agregar lista de elemtos (en un index) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnc1.clicked.connect(lambda: 
            self.raiz.cboxc2.insertItems(0, lista_elementos))

        # agregar solamente un elemento *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnc2.clicked.connect(lambda: 
            self.raiz.cboxc2.addItem(f'texto_{randint(1,100)}'))

        # restablecer combobox *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnc3.clicked.connect(lambda: 
            self.raiz.cboxc2.clear())

        # remover item por index *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnc4.clicked.connect(lambda: 
            self.raiz.cboxc2.removeItem(0))

        # obtener texto e index *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.cboxc1.currentTextChanged.connect(lambda texto: print('texto:',texto))
        self.raiz.cboxc1.currentIndexChanged.connect(lambda index: print('index:',index))



