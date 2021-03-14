# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow

# diseño
from view.ui_elementos import Ui_Elementos

class MainChbox(QMainWindow):
    def __init__(self):
        super(MainChbox, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)


        # cambiar de texto *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.chboxm1.setText('python 3')

        # capturar evento puede ser 'clicked' o 'toggled' *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*    
        'nota: *funciones en en final del codigo*'
        self.raiz.chboxm1.clicked.connect(lambda : self.eventoCheck())
        self.raiz.chboxm2.clicked.connect(lambda : self.eventoCheck())
        self.raiz.chboxm3.clicked.connect(lambda : self.eventoCheck())

        # establecer una seleccion (valores por defecto) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-* 
        self.raiz.chboxm3.setChecked(True)
        self.eventoCheck()


    def eventoCheck(self):
        '''se puede pasar parametro, pero esta es una manera'''

        listaSeleccion=[]
        if(self.raiz.chboxm1.isChecked()):
            listaSeleccion.append('chboxm1: '+self.raiz.chboxm1.text()) # obtener texto

        if(self.raiz.chboxm2.isChecked()):
            listaSeleccion.append('chboxm2: '+self.raiz.chboxm2.text()) # obtener texto

        if(self.raiz.chboxm3.isChecked()):
            listaSeleccion.append('chboxm3: '+self.raiz.chboxm3.text()) # obtener texto

        print(listaSeleccion) 

