# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

class MainSarea(QMainWindow):
    def __init__(self):
        super(MainSarea, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # primero extraer el elemento scrollbar del scrollarea *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.vbar = self.raiz.sareav1.verticalScrollBar()

        # set inicio scrollbar *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnv1.clicked.connect(lambda: 
            self.vbar.setValue(self.vbar.minimum())
            )

        # set final scrollbar *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnv2.clicked.connect(lambda: 
            self.vbar.setValue(self.vbar.maximum())
            )
