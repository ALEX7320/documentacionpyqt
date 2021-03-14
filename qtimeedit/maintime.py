# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QTime

# diseño
from view.ui_elementos import Ui_Elementos

class MainTime(QMainWindow):
    def __init__(self):
        super(MainTime, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)
        
        # extraer variable str *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        variabletime = self.raiz.timef1.time().toString("hh:mm AP")
        print(variabletime)

        # establecer hora *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.timef1.setTime(QTime.fromString("12:32 PM", "hh:mm AP"))

        # mandar hora por evento *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.timef1.timeChanged.connect(lambda time: print(time.toString("hh:mm AP")))

        # hora maximo y minimo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.timef1.setMinimumTime(QTime.fromString("06:00 PM", "hh:mm AP"))'
        'self.raiz.timef1.setMaximumTime(QTime.fromString("10:30 PM", "hh:mm AP"))'

        # establecr hora maxima (hora actual) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.timef1.setMaximumTime(QTime.currentTime())'

        # establecer rango de hora *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        """
        hora_minima = QTime.fromString("12:00 PM", "hh:mm AP")
        hora_maxima = QTime.fromString("12:50 PM", "hh:mm AP")
        self.raiz.timef1.setTimeRange(hora_minima, hora_maxima)
        """

        # obtener hora por boton *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnf1.clicked.connect(lambda : 
            print(self.raiz.timef1.time().toString("hh:mm AP"))
            )