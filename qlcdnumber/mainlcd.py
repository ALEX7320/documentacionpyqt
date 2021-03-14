# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplos
from random import randint

class MainLcd(QMainWindow):
    def __init__(self):
        super(MainLcd, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # insertar valores (int,float) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.lcdnn1.display(73.5)

        # extraer en evariable *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        valor = self.raiz.lcdnn1.value()
        print('valor:',valor)

        # obtener valor numerico *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnn2.clicked.connect(lambda : print(self.raiz.lcdnn1.value()))

        # establecer valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnn1.clicked.connect(lambda : self.raiz.lcdnn1.display(randint(10,500)))