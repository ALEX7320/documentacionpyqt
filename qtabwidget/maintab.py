# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

class MainTab(QMainWindow):
    def __init__(self):
        super(MainTab, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # botones cambio de titulo tab (por index) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnq4.clicked.connect(lambda : self.raiz.tabq1.setTabText(0,f"Tab 1: {randint(1,100)}"))

        # botones cambio de tab *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnq1.clicked.connect(lambda : self.raiz.tabq1.setCurrentIndex(0))
        self.raiz.btnq2.clicked.connect(lambda : self.raiz.tabq1.setCurrentIndex(1))

        # index de tab actual *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnq3.clicked.connect(lambda : print(self.raiz.tabq1.currentIndex()))

        # evento cambio de tab *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.tabq1.currentChanged.connect(lambda index: print(f'se cambio a index: {index}'))