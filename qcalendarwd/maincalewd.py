# modulos de PySide2 utilizados
from PySide2.QtWidgets import QMainWindow,QToolButton,QSpinBox,QTableView,QColorDialog
from PySide2.QtCore import QEvent,QDate

# diseño
from view.ui_elementos import Ui_Elementos

# random para ejemplos
from random import randint

class MainCalewd(QMainWindow):
    def __init__(self):
        super(MainCalewd, self).__init__()
        
        self.raiz = Ui_Elementos()
        self.raiz.setupUi(self)

        # METODOS /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # extraer variable str *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        variablefecha = self.raiz.cald1.selectedDate().toString("dd/MM/yyyy")
        print('variablefecha',variablefecha)
        
        # establecer fecha *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.cald1.setSelectedDate(QDate.fromString("08/11/2020", "dd/MM/yyyy" ))
 
        # establecer fecha minima *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.cald1.setMinimumDate(QDate.fromString("08/11/2020", "dd/MM/yyyy" ))'

        # establecer fecha maxima *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.cald1.setMaximumDate(QDate.fromString("20/12/2020", "dd/MM/yyyy" ))'

        # establecer fecha maxima (con la fecha actual) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.cald1.setMaximumDate(QDate.currentDate())'

        # establecer un rango de fecha *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        '''
        fecha_minima = QDate.fromString("05/11/2020", "dd/MM/yyyy" )
        fecha_maxima = QDate.fromString("15/12/2020", "dd/MM/yyyy" )
        self.raiz.cald1.setDateRange(fecha_minima, fecha_maxima)
        '''

        # establece pagina basado en (AÑO,MES) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        'self.raiz.cald1.setCurrentPage(2020, 5)'

        # siguiente/pasado mes *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnd1.clicked.connect(lambda : self.raiz.cald1.showNextMonth()) 
        self.raiz.btnd2.clicked.connect(lambda : self.raiz.cald1.showPreviousMonth())

        # siguiente/pasado año *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.btnd3.clicked.connect(lambda : self.raiz.cald1.showNextYear()) 
        self.raiz.btnd4.clicked.connect(lambda : self.raiz.cald1.showPreviousYear())   

        # seleccion de fecha *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.cald1.clicked.connect(lambda date: print(date.toString("dd/MM/yyyy")))
        self.raiz.cald1.selectionChanged.connect(lambda : print("solo selecciona una vez el dia"))


        # OBJETOS DEL CALENDARIO /*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/*/

        # boton mes previo *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.btnCalPrev = self.raiz.cald1.findChild(QToolButton, "qt_calendar_prevmonth")
        self.btnCalPrev.clicked.connect(lambda: print('cal btn mesPrev'))

        # boton mes siguiente *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.btnCalNext = self.raiz.cald1.findChild(QToolButton, "qt_calendar_nextmonth")
        self.btnCalNext.clicked.connect(lambda aa: print('cal btn mesNext'))

        # boton seleccion mes *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.btnCalMes = self.raiz.cald1.findChild(QToolButton, "qt_calendar_monthbutton")
        self.btnCalMes.triggered.connect(lambda elemento:print('cal btn Mes',elemento.text()))

        # spinbox seleccion año *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.spinCalYear = self.raiz.cald1.findChild(QSpinBox, "qt_calendar_yearedit")
        self.spinCalYear.valueChanged.connect(lambda year: print('cal spin Año',year))

        # bloquear envento scroll en calendario *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.scrollcalen = self.raiz.cald1.findChild(QTableView, "qt_calendar_calendarview")
        self.scrollcalen.viewport().installEventFilter(self)

    def eventFilter(self, obj, event):
        # scroll de qcalendar widgets (bloquear evento scroll)
        if(obj is self.scrollcalen.viewport() and event.type() == QEvent.Wheel):
            return True
        else:
            return super(MainCalewd, self).eventFilter(obj, event)

