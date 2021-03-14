# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplo
from random import randint

class MainSli(QMainWindow):
    def __init__(self):
        super(MainSli, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)
        
        # capturar valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        valor = self.raiz.vslij1.value()
        print('valor:',valor)

        # establecer valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.vslij1.setValue(15)

        # evento de spinbox *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.vslij1.valueChanged.connect(lambda valor: print(valor)) # vertical
        self.raiz.hslij1.valueChanged.connect(lambda valor: print(valor)) # horizontal

        # establecer valor minimo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        "self.raiz.vslij1.setMinimum(12)"

        # establecer valor maximo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        "self.raiz.vslij1.setMaximum(999)"

        # obtener valor (boton) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnj2.clicked.connect(lambda : print(self.raiz.vslij1.value())) # vertical
        self.raiz.btnj1.clicked.connect(lambda : print(self.raiz.hslij1.value())) # horizontal

        # establecer valor valor (boton) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnj3.clicked.connect(lambda :  self.raiz.vslij1.setValue(randint(1,30)))
