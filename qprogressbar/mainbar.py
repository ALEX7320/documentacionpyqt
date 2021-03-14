# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplo
from random import randint

class MainBar(QMainWindow):
    def __init__(self):
        super(MainBar, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # obtener el valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* 
        valor = self.raiz.bars1.value()
        print('valor:',valor)

        # establecer rango *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.bars1.setRange(0,200)'

        # resetar barra *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btns1.clicked.connect(lambda : self.raiz.bars1.reset())

        # establecer valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btns3.clicked.connect(lambda : self.raiz.bars1.setValue(randint(0,100)))

        # obtener valor (boton) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btns2.clicked.connect(lambda : print('valor:',self.raiz.bars1.value()))