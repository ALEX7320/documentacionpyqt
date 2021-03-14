# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QTime,QDate

# diseño
from view.ui_elementos import Ui_Elementos

class MainDatime(QMainWindow):
    def __init__(self):
        super(MainDatime, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # extraer variable str *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        variablefecha = self.raiz.datimeg1.date().toString("dd/MM/yyyy") # fecha
        variablehora = self.raiz.datimeg1.time().toString("hh:mm AP") # hora
        print('variablefecha:',variablefecha,' variablehora:',variablehora)

        # establecer fecha y hora *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.datimeg1.setDate(QDate.fromString( "08/12/2020", "dd/MM/yyyy" )) # fecha
        self.raiz.datimeg1.setTime(QTime.fromString( "10:31 AM", "hh:mm AP" )) # hora

        # establecer fecha/hora minima *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.datimeg1.setMinimumDate(QDate.fromString("08/11/2020", "dd/MM/yyyy" ))'
        'self.raiz.datimeg1.setMinimumTime(QTime.fromString("06:00 PM", "hh:mm AP"))'

        # establecr fecha/hora maxima *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.datimeg1.setMaximumDate(QDate.fromString("20/12/2020", "dd/MM/yyyy" ))'
        'self.raiz.datimeg1.setMaximumTime(QTime.fromString("10:30 PM", "hh:mm AP"))'

        # establecr fecha/maxima maxima (fecha/hora actual) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.datimeg1.setMaximumDate(QDate.currentDate())'
        'self.raiz.datimeg1.setMaximumTime(QTime.currentTime())'

        # establecer rango de ... *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*

        # hora
        '''
        hora_minima = QTime.fromString("12:00 PM", "hh:mm AP")
        hora_maxima = QTime.fromString("12:50 PM", "hh:mm AP")
        self.raiz.datimeg1.setTimeRange(hora_minima, hora_maxima)
        '''

        # fecha
        '''
        fecha_minima = QDate.fromString("05/11/2020", "dd/MM/yyyy" )
        fecha_maxima = QDate.fromString("15/12/2020", "dd/MM/yyyy" )
        self.raiz.datimeg1.setDateRange(fecha_minima, fecha_maxima)
        '''

        # evento de cambio de... *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.datimeg1.dateChanged.connect(lambda date: print(date.toString("dd/MM/yyyy"))) # fecha
        self.raiz.datimeg1.timeChanged.connect(lambda time: print(time.toString("hh:mm AP"))) # hora
        self.raiz.datimeg1.dateTimeChanged.connect(lambda datetime: print(datetime.toString("dd/MM/yyyy hh:mm AP"))) # fecha-hora

        # obtener valor de... *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btng1.clicked.connect(lambda : print(self.raiz.datimeg1.date().toString("dd/MM/yyyy"))) # fecha
        self.raiz.btng2.clicked.connect(lambda : print(self.raiz.datimeg1.time().toString("hh:mm AP"))) # hora
        self.raiz.btng3.clicked.connect(lambda : print(self.raiz.datimeg1.dateTime().toString("dd/MM/yyyy hh:mm AP"))) # fecha-hora