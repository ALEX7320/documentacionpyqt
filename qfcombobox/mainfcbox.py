# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

class MainFcbox(QMainWindow):
    def __init__(self):
        super(MainFcbox, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)


        # obtener texto e index *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.fcboxu1.currentTextChanged.connect(lambda texto: print('texto:',texto))
        self.raiz.fcboxu1.currentIndexChanged.connect(lambda index: print('index:',index))


        # obtener texto mediante boton *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnu1.clicked.connect(lambda: 
            print(self.raiz.fcboxu1.currentText()))

        # evento font (y aplicar efecto a label) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.fcboxu1.currentTextChanged.connect(lambda texto: 
            self.raiz.lblu1.setStyleSheet(f'font-size: 25px; font-family:{texto};'))

