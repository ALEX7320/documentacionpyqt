# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplos
from random import randint

class MainLbl(QMainWindow):
    def __init__(self):
        super(MainLbl, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)


        # extraer texto *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        texto = self.raiz.lblw1.text()
        print('texto',texto)

        # cambiar texto *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* 
        self.raiz.btnw1.clicked.connect(lambda : 
            self.raiz.lblw1.setText(f'Texto muestra {randint(1,100)}')
            )