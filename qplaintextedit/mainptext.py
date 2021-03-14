# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplo
from random import randint

class MainPtext(QMainWindow):
    def __init__(self):
        super(MainPtext, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # extraer texto a variable *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        texto = self.raiz.ptexti1.toPlainText()
        print('texto:',texto)

        # cambiar de nombre (mediante evento) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btni2.clicked.connect(lambda : self.raiz.ptexti1.setPlainText('Texto'))

        # agregar texto *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btni1.clicked.connect(lambda : self.raiz.ptexti1.insertPlainText(' Nuevo mundo'))

        # restablecer *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btni3.clicked.connect(lambda : self.raiz.ptexti1.setPlainText(''))

        # evento de escritura *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.ptexti1.textChanged.connect(lambda : print(self.raiz.ptexti1.toPlainText()))
