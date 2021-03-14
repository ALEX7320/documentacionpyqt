# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplos
from random import randint

class MainLine(QMainWindow):

    def __init__(self):
        super(MainLine, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # extraer texto de cadena *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        variabletexto = self.raiz.lnb1.text()
        print('variabletexto:',variabletexto)

        # enviar texto por parametro *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.lnb2.textChanged.connect(lambda texto: print(texto))

        # agregar texto (agrega a la caja el texto) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnb2.clicked.connect(lambda : self.raiz.lnb1.insert(' Nuevo'))

        # establecer texto *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnb1.clicked.connect(lambda : self.raiz.lnb1.setText(f'texto_{randint(1,100)}'))

        # restablecer texto *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnb3.clicked.connect(lambda : self.raiz.lnb1.setText(''))
