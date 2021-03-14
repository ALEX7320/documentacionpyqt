# Metodos y eventos (Widgets PyQT)

**Indice**
  * [Recursos utilizados](#recursos-utilizados)
  * [Detalles](#detalles)
  * [Previzualización](#previzualización)

# Recursos utilizados

`pip install PySide2`

# Detalles

Documentación interactiva con los widgets de QT (Pyside2), para ver los comentarios, dirijase a su respectivo paquete y modulo (main).

Estos son los Widgets contemplados en el programa:

| Widget  | PyQT  | Paquete |
| :------------ | :------------: | :------------: |
| QLabel  | [Documentación QT5](https://doc.qt.io/qt-5/qlabel.html  "Documentación QT") |`qlabel`|
| QPushButton  | [Documentación QT5](https://doc.qt.io/qt-5/qpushbutton.html  "Documentación QT") |`qpushbutton`|
|  QLineEdit |  [Documentación QT5](https://doc.qt.io/qt-5/qlineedit.html "Documentación QT") | `qlineedit`|
|  QComboBox |  [Documentación QT5](https://doc.qt.io/qt-5/qcombobox.html  "Documentación QT")  |`qcombobox`|
|  QCalendarWidget |    [Documentación QT5](https://doc.qt.io/qt-5/qcalendarwidget.html  "Documentación QT")  |`qcalendarwd`|
|  QDateEdit |    [Documentación QT5](https://doc.qt.io/qt-5/qdateedit.html  "Documentación QT")  |`qdateedit`|
|  QTimeEdit |    [Documentación QT5](https://doc.qt.io/qt-5/qtimeedit.html  "Documentación QT")  |`qtimeedit`|
|  QDateTimeEdit |    [Documentación QT5](https://doc.qt.io/qt-5/qdatetimeedit.html  "Documentación QT")  |`qdatetimeedit`|
|  QSpinBox |    [Documentación QT5](https://doc.qt.io/qt-5/qspinbox.html  "Documentación QT")  |`qspinbox`|
|  QDoubleSpinBox |    [Documentación QT5](https://doc.qt.io/qt-5/qdoublespinbox.html  "Documentación QT")  |`qspinbox`|
|  QPlainTextEdit |    [Documentación QT5](https://doc.qt.io/qt-5/qplaintextedit.html  "Documentación QT")  |`qplaintextedit`|
|  QSlider |    [Documentación QT5](https://doc.qt.io/qt-5/qslider.html  "Documentación QT")  |`qslider`|
|  QDial |    [Documentación QT5](https://doc.qt.io/qt-5/qdial.html  "Documentación QT")  |`qdial`|
|  QRadioButton |    [Documentación QT5](https://doc.qt.io/qt-5/qradiobutton.html  "Documentación QT")  |`qradiobutton`|
|  QCheckBox |    [Documentación QT5](https://doc.qt.io/qt-5/qcheckbox.html  "Documentación QT")  |`qcheckbutton`|
|  QLCDNumber |    [Documentación QT5](https://doc.qt.io/qt-5/qlcdnumber.html  "Documentación QT")  |`qlcdnumber`|
|  QListWidget |    [Documentación QT5](https://doc.qt.io/qt-5/qlistwidget.html  "Documentación QT")  |`qlistwidget`|
|  QStackedWidget |    [Documentación QT5](https://doc.qt.io/qt-5/qstackedwidget.html  "Documentación QT")  |`qstackedwidget`|
|  QTabWidget |    [Documentación QT5](https://doc.qt.io/qt-5/qtabwidget.html  "Documentación QT")  |`qtabwidget`|
|  QToolBox |    [Documentación QT5](https://doc.qt.io/qt-5/qtoolbox.html  "Documentación QT")  |`qtoolbox`|
|  QProgressBar |    [Documentación QT5](https://doc.qt.io/qt-5/qprogressbar.html  "Documentación QT")  |`qprogressbar`|
|  QFontComboBox |    [Documentación QT5](https://doc.qt.io/qt-5/qfontcombobox.html  "Documentación QT")  |`qfcombobox`|
|  QTableWidget |    [Documentación QT5](https://doc.qt.io/qt-5/qtablewidget.html  "Documentación QT")  |`qtablewidget`|
|  QScrollAarea |    [Documentación QT5](https://doc.qt.io/qt-5/qscrollarea.html  "Documentación QT")  |`qscrollarea`|

# Previzualización

Widget de muestra `QTableWidget`

**Parte del código**

```python
        # extraer fila,columna,item,lista_fila (evento) *-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*
        self.raiz.tablet1.cellClicked.connect(
            lambda fila,columna: 
                print(

                    # fila
                    f'\n*fila:\t{fila}',

                    # columna
                    f'\n*colum:\t{columna}',

                    # item seleccionado
                    f'\n*item:\t{self.raiz.tablet1.item(fila, columna).text()}',

                    # elementos de la fila
                    f'\n*lista:\t{[self.raiz.tablet1.item(fila, columna).text() for columna in range(self.raiz.tablet1.columnCount())]}',

                    # solo el 1er elemento (index 0)
                    f'\n*1er item:\t{self.raiz.tablet1.item(fila, 0).text()}',
                
                )
            )
```

**Vista usuario**

![](https://1.bp.blogspot.com/-G4hWrTY194c/YE6JdK6iHxI/AAAAAAAAAGA/KNrfNzsNZf4vVuU0A_CpWoqVZpoTQqjdwCLcBGAsYHQ/s1600/1461264.jpg)
