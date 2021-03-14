# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplo
from random import randint

class MainSpin(QMainWindow):
    def __init__(self):
        super(MainSpin, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)
        
        # capturar valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        valor = self.raiz.sboxh1.value()
        print('valor',valor)

        # establecer valor *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.sboxh1.setValue(15)

        # evento de spinbox *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.sboxh1.valueChanged.connect(lambda valor: print(valor))

        # establecer valor minimo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        "self.raiz.sboxh1.setMinimum(12)"

        # establecer valor maximo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        "self.raiz.sboxh1.setMaximum(999)"

        # obtener valor mediante boton *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnh1.clicked.connect(lambda : print(self.raiz.sboxh1.value()))

        # lo mismo sea plica para el "double_spin" *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.dsboxh1.valueChanged.connect(lambda valor: print(valor)) # evento
        self.raiz.btnh2.clicked.connect(lambda : print(self.raiz.dsboxh1.value())) # valor
