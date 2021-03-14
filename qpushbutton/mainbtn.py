# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplo
from random import randint

class MainBtn(QMainWindow):
    def __init__(self):
        super(MainBtn, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)
        
        # evento clic *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btna2.clicked.connect(lambda : print(f'Print {randint(1,100)}'))

        # cambiar de nombre (mediante evento) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btna1.clicked.connect(lambda : 
            self.raiz.btna1.setText(f'Boton {randint(1,100)}'))

