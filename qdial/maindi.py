# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplos
from random import randint

class MainDi(QMainWindow):
    def __init__(self):
        super(MainDi, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)
        
        # capturar valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        valor = self.raiz.dialk1.value()
        print('valor',valor)

        # establecer valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.dialk1.setValue(15)

        # establecer valor minimo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        "self.raiz.dialk1.setMinimum(12)"

        # establecer valor maximo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        "self.raiz.dialk1.setMaximum(999)"

        # evento cambio de valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.dialk1.valueChanged.connect(lambda valor: print(valor))

        # obtener valor (boton) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnk1.clicked.connect(lambda : print(self.raiz.dialk1.value()))

        # establecer valor (boton) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnk2.clicked.connect(lambda :  self.raiz.dialk1.setValue(50))
