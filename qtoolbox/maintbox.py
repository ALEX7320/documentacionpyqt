# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

class MainTbox(QMainWindow):
    def __init__(self):
        super(MainTbox, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # botones cambio de titulo page (por index) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnr5.clicked.connect(lambda : self.raiz.tboxr1.setItemText(0,f"Page 1: {randint(1,100)}"))

        # botones cambio de pagina *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnr1.clicked.connect(lambda : self.raiz.tboxr1.setCurrentIndex(0))
        self.raiz.btnr2.clicked.connect(lambda : self.raiz.tboxr1.setCurrentIndex(1))
        self.raiz.btnr3.clicked.connect(lambda : self.raiz.tboxr1.setCurrentIndex(2))

        # index de pagina actual *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnr4.clicked.connect(lambda : print(self.raiz.tboxr1.currentIndex()))

        # evento cambio de pagina *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.tboxr1.currentChanged.connect(lambda index: print(f'se cambio a index: {index}'))