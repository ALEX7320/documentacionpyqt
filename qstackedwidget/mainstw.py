# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

class MainStw(QMainWindow):
    def __init__(self):
        super(MainStw, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # botones cambio de panel *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnp1.clicked.connect(lambda : self.raiz.stwp1.setCurrentIndex(0))
        self.raiz.btnp2.clicked.connect(lambda : self.raiz.stwp1.setCurrentIndex(1))

        # index de ventana actual *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnp3.clicked.connect(lambda : print(self.raiz.stwp1.currentIndex()))
