# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

class MainRbtn(QMainWindow):
    def __init__(self):
        super(MainRbtn, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # cambiar de texto *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.rbtnl1.setText('python 3')

        # capturar evento puede ser 'clicked' o 'toggled' *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'nota: *funciones en en final del codigo*'
        self.raiz.rbtnl1.clicked.connect(lambda : self.eventoRadio())
        self.raiz.rbtnl2.clicked.connect(lambda : self.eventoRadio())
        self.raiz.rbtnl3.clicked.connect(lambda : self.eventoRadio())

        # establecer una seleccion (por defecto) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.rbtnl3.setChecked(True)
        self.eventoRadio()


    def eventoRadio(self):
        '''se puede pasar parametro, pero esta es una manera'''

        if(self.raiz.rbtnl1.isChecked()):
            print('rbtnl1',self.raiz.rbtnl1.text()) # obtener texto

        elif(self.raiz.rbtnl2.isChecked()):
            print('rbtnl2',self.raiz.rbtnl2.text()) # obtener texto

        else:
            print('rbtnl3',self.raiz.rbtnl3.text()) # obtener texto
