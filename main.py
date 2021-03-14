# modulos de PySide2 utilizados
from PySide2.QtWidgets import QDialog,QApplication

# diseño
from view.ui_opciones import Ui_Opciones

"""
Separado cada en cada clase y modulo para evitar 
que se combinen los metodos, dando asi una vista
ordenada.
"""
# ventana usadas
from qlabel.mainlbl import MainLbl
from qlineedit.mainln import MainLine 
from qpushbutton.mainbtn import MainBtn
from qcombobox.maincbox import MainCbox
from qdateedit.maindate import MainDate
from qcalendarwd.maincalewd import MainCalewd
from qtimeedit.maintime import MainTime
from qdatetimeedit.maindatime import MainDatime
from qspinbox.mainspin import MainSpin
from qplaintextedit.mainptext import MainPtext
from qslider.mainsli import MainSli
from qdial.maindi import MainDi
from qradiobutton.mainrbtn import MainRbtn
from qcheckbutton.mainchbox import MainChbox
from qlcdnumber.mainlcd import MainLcd
from qlistwidget.mainlistw import MainListw
from qstackedwidget.mainstw import MainStw
from qtabwidget.maintab import MainTab
from qtoolbox.maintbox import MainTbox
from qprogressbar.mainbar import MainBar
from qtablewidget.maintablew import MainTablew
from qfcombobox.mainfcbox import MainFcbox
from qscrollarea.mainsarea import MainSarea


class Ui_Controlador(QDialog):

    def __init__(self):
        super(Ui_Controlador, self).__init__()
        
        self.raizopc = Ui_Opciones()
        self.raizopc.setupUi(self)

        # elegir opciones (por index y clase)
        self.raizopc.btn0.clicked.connect(lambda: self.abrirventana(0,MainLine))
        self.raizopc.btn1.clicked.connect(lambda: self.abrirventana(1,MainCbox))
        self.raizopc.btn2.clicked.connect(lambda: self.abrirventana(2,MainCalewd))
        self.raizopc.btn3.clicked.connect(lambda: self.abrirventana(3,MainDate))
        self.raizopc.btn4.clicked.connect(lambda: self.abrirventana(4,MainTime))
        self.raizopc.btn5.clicked.connect(lambda: self.abrirventana(5,MainDatime))
        self.raizopc.btn6.clicked.connect(lambda: self.abrirventana(6,MainSpin))
        self.raizopc.btn7.clicked.connect(lambda: self.abrirventana(7,MainPtext))
        self.raizopc.btn8.clicked.connect(lambda: self.abrirventana(8,MainSli))
        self.raizopc.btn9.clicked.connect(lambda: self.abrirventana(9,MainDi))
        self.raizopc.btn10.clicked.connect(lambda: self.abrirventana(10,MainRbtn))
        self.raizopc.btn11.clicked.connect(lambda: self.abrirventana(11,MainChbox))
        self.raizopc.btn12.clicked.connect(lambda: self.abrirventana(12,MainLcd))
        self.raizopc.btn13.clicked.connect(lambda: self.abrirventana(13,MainListw))
        self.raizopc.btn14.clicked.connect(lambda: self.abrirventana(14,MainStw))
        self.raizopc.btn15.clicked.connect(lambda: self.abrirventana(15,MainTab))
        self.raizopc.btn16.clicked.connect(lambda: self.abrirventana(16,MainTbox))
        self.raizopc.btn17.clicked.connect(lambda: self.abrirventana(17,MainBar))
        self.raizopc.btn18.clicked.connect(lambda: self.abrirventana(18,MainTablew))
        self.raizopc.btn19.clicked.connect(lambda: self.abrirventana(19,MainFcbox))
        self.raizopc.btn20.clicked.connect(lambda: self.abrirventana(20,MainBtn))
        self.raizopc.btn21.clicked.connect(lambda: self.abrirventana(21,MainSarea)) 
        self.raizopc.btn22.clicked.connect(lambda: self.abrirventana(22,MainLbl)) 

    def abrirventana(self, index, clase = None):
        # index = ventana a escoger
        # calse = calse a cargar

        if(clase is None):
            return
        self.cerraclase() # cerrar clase

        self.raizprin=clase()
        self.raizprin.raiz.stackedWidget.setCurrentIndex(index)
        self.raizprin.show()

    def cerraclase(self):
        try: self.raizprin.close()
        except:pass

    def closeEvent(self, event):
        self.cerraclase() # cerrar clase
        event.accept()
     

if __name__ == "__main__":

    import sys

    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    
    mi_aplicacion = Ui_Controlador()
    mi_aplicacion.show()
    sys.exit(app.exec_())
