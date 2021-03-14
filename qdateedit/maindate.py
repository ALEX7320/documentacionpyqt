# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QDate

# diseño
from view.ui_elementos import Ui_Elementos

class MainDate(QMainWindow):
    def __init__(self):
        super(MainDate, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # extraer variable str *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        variablefecha = self.raiz.datee1.date().toString("dd/MM/yyyy")
        print('variablefecha',variablefecha)

        # establecer fecha minima *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.datee1.setMinimumDate(QDate.fromString("08/11/2020", "dd/MM/yyyy"))'

        # establecr fecha maxima *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.datee1.setMaximumDate(QDate.fromString("20/12/2020", "dd/MM/yyyy"))'

        # establecr fecha maxima (fecha actual) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.datee1.setMaximumDate(QDate.currentDate())'

        # establecer rango de fecha *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        '''
        fecha_minima = QDate.fromString("05/11/2020", "dd/MM/yyyy" )
        fecha_maxima = QDate.fromString("15/12/2020", "dd/MM/yyyy" )
        self.raiz.datee1.setDateRange(fecha_minima, fecha_maxima)
        '''
        
        # establecer fecha *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.datee1.setDate(QDate.fromString("06/12/2020", "dd/MM/yyyy"))

        # obtener fecha por evento *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.datee1.dateChanged.connect(lambda date: print("fecha",date.toString("dd/MM/yyyy")))
        self.raiz.datee1.dateChanged.connect(lambda date: print("año:",date.toString("yyyy"),"mes:",date.toString("MM")))

        # obtener fecha por boton *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btne1.clicked.connect(lambda : 
            print(self.raiz.datee1.date().toString("dd/MM/yyyy"))
            )

