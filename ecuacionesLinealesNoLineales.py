from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from nonlineal import biseccion, graficar_funcion, falsa_posicion, falsa_posicion2, punto_fijo
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#from matplotlib.figure import Figure

class Ui_metodosGraficos(object):

    size_of = 0
    value_lineEdit = '--'
    def setupUi(self, metodosGraficos):
        if not metodosGraficos.objectName():
            metodosGraficos.setObjectName(u"metodosGraficos")
        metodosGraficos.resize(1920, 979)
        metodosGraficos.setMaximumSize(QSize(1920, 1080))
        self.centralwidget = QWidget(metodosGraficos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 10, 601, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 17))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1740, 70, 171, 371))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(130, 24))

        self.verticalLayout.addWidget(self.label_2)

        self.button_biseccion = QPushButton(self.verticalLayoutWidget)
        self.button_biseccion.setObjectName(u"button_biseccion")

        self.verticalLayout.addWidget(self.button_biseccion)

        self.button_falsa = QPushButton(self.verticalLayoutWidget)
        self.button_falsa.setObjectName(u"button_falsa")

        self.verticalLayout.addWidget(self.button_falsa)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(135, 20))

        self.verticalLayout.addWidget(self.label_3)

        self.button_punto = QPushButton(self.verticalLayoutWidget)
        self.button_punto.setObjectName(u"button_punto")

        self.verticalLayout.addWidget(self.button_punto)

        self.button_newton = QPushButton(self.verticalLayoutWidget)
        self.button_newton.setObjectName(u"button_newton")

        self.verticalLayout.addWidget(self.button_newton)

        self.button_secante = QPushButton(self.verticalLayoutWidget)
        self.button_secante.setObjectName(u"button_secante")

        self.verticalLayout.addWidget(self.button_secante)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(145, 20))

        self.verticalLayout.addWidget(self.label_4)

        self.button_raices = QPushButton(self.verticalLayoutWidget)
        self.button_raices.setObjectName(u"button_raices")

        self.verticalLayout.addWidget(self.button_raices)
        #Graphics view
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(950, 70, 771, 881))

        #self.graphicsView.setStyleSheet(u"background-color: rgb(153, 255, 255);")
        

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(950, 50, 61, 20))
        self.button_limpiar = QPushButton(self.centralwidget)
        self.button_limpiar.setObjectName(u"button_limpiar")
        self.button_limpiar.setGeometry(QRect(1740, 920, 158, 25))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(750, 20, 131, 17))
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1040, 20, 131, 17))
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(1330, 20, 131, 17))
        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(880, 10, 131, 41))
        self.lineEdit_3 = QLineEdit(self.centralwidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(1170, 10, 131, 41))
        self.spinBox = QSpinBox(self.centralwidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(1440, 10, 51, 41))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(40, 70, 891, 881))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.horizontalLayoutWidget)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        font = QFont()
        font.setPointSize(13)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
    
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem12)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout.addWidget(self.tableWidget)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(50, 50, 211, 17))
        metodosGraficos.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(metodosGraficos)
        self.statusbar.setObjectName(u"statusbar")
        metodosGraficos.setStatusBar(self.statusbar)

        self.retranslateUi(metodosGraficos)

        QMetaObject.connectSlotsByName(metodosGraficos)
    # setupUi
    
    def retranslateUi(self, metodosGraficos):
    

        def clicked():
            print("clicked biseccion")
            function = self.lineEdit.text()
            limite_inferior = float(self.lineEdit_2.displayText())
            limite_superior = float(self.lineEdit_3.displayText())
            tolerancia = float(self.spinBox.value())
            print(limite_inferior)
            print(limite_superior)
            print(tolerancia)
            print(function)

            result_bisection = biseccion(limite_inferior, limite_superior, tolerancia, function)
            
            graficar_funcion(function, result_bisection[2][-1])
            print("TAMANO resultado de la biseccion: ", len(result_bisection[1]))
            if (self.tableWidget.rowCount() < len(result_bisection[1])):
                self.tableWidget.setRowCount(len(result_bisection[1]))

            #for i in result_bisection.length():
                #counter_j=0
                #for j in i:
                   #self.tableWidget.setItem(counter_j, 0, QTableWidgetItem(str(j[0])))
                   #self.tableWidget.setItem(counter_j+1, 0, QTableWidgetItem(str(j[counter_j+1])))
                   #self.tableWidget.setItem(counter_j+2, 0, QTableWidgetItem(str(j[counter_j+2])))
                   #self.tableWidget.setItem(counter_j+3, 0, QTableWidgetItem(str(j[counter_j+3])))
                   #counter_j+=1
            
            for i in range (0, len(result_bisection)):
                for j in range (0, len(result_bisection[i])):
                    self.tableWidget.setItem(j, i, QTableWidgetItem(str(result_bisection[i][j])))


            for b in result_bisection:
                print(b)
                print("\n")
        # FALSA POSICION CODE
        def clickedFalsaPosicion():
            print("click falsa posicion")
            function = self.lineEdit.text()
            limite_inferior = float(self.lineEdit_2.displayText())
            limite_superior = float(self.lineEdit_3.displayText())
            tolerancia = float(self.spinBox.value())

            result_falsa_posicion = falsa_posicion(limite_inferior, limite_superior, tolerancia, function)
            graficar_funcion(function, result_falsa_posicion[2][-1])
            print("TAMANO resultado de la falsa posicion: ", len(result_falsa_posicion[1]))
            if (self.tableWidget.rowCount() < len(result_falsa_posicion[1])):
                self.tableWidget.setRowCount(len(result_falsa_posicion[1]))
            for i in range (0, len(result_falsa_posicion)):
                for j in range (0, len(result_falsa_posicion[i])):
                    self.tableWidget.setItem(j, i, QTableWidgetItem(str(result_falsa_posicion[i][j])))
            for b in result_falsa_posicion:
                print(b)
                print("\n")
        # Punto fijo code

        def clickedPuntoFijo():
            print("click punto fijo")
            function = self.lineEdit.text()
            limite_inferior = float(self.lineEdit_2.displayText())
            tolerancia = float(self.spinBox.value())

            result_punto_fijo = punto_fijo(limite_inferior, tolerancia, function)
            graficar_funcion(function, result_punto_fijo[2][-1])
            print("TAMANO resultado de punto fijo: ", len(result_punto_fijo[1]))
            if (self.tableWidget.rowCount() < len(result_punto_fijo[1])):
                self.tableWidget.setRowCount(len(result_punto_fijo[1]))
            for i in range (0, len(result_punto_fijo)):
                for j in range (0, len(result_punto_fijo[i])): #view error?
                    self.tableWidget.setItem(j, i, QTableWidgetItem(str(result_punto_fijo[i][j])))
            for b in result_punto_fijo:
                print(b)
                print("\n")


        metodosGraficos.setWindowTitle(QCoreApplication.translate("metodosGraficos", u"Ecuaciones lineales - no lineales", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("metodosGraficos", u"example : x^2 + ((x+2)/x^3)", None))
        
        self.label.setText(QCoreApplication.translate("metodosGraficos", u"Input equation", None))
        self.label_2.setText(QCoreApplication.translate("metodosGraficos", u"Metodos cerrados", None))
        self.button_biseccion.setText(QCoreApplication.translate("metodosGraficos", u"Biseccion", None))
        self.button_biseccion.clicked.connect(clicked)
        
        self.button_falsa.setText(QCoreApplication.translate("metodosGraficos", u"Falsa posicion", None))
        self.button_falsa.clicked.connect(clickedFalsaPosicion)

        self.label_3.setText(QCoreApplication.translate("metodosGraficos", u"Metodos abiertos", None))
        self.button_punto.setText(QCoreApplication.translate("metodosGraficos", u"Punto fijo", None))
        self.button_punto.clicked.connect(clickedPuntoFijo)
        self.button_newton.setText(QCoreApplication.translate("metodosGraficos", u"Newton Raphson", None))
        self.button_secante.setText(QCoreApplication.translate("metodosGraficos", u"Secante", None))
        self.label_4.setText(QCoreApplication.translate("metodosGraficos", u"Raices de polinomios", None))
        self.button_raices.setText(QCoreApplication.translate("metodosGraficos", u"Calculo de las raices", None))
        self.label_5.setText(QCoreApplication.translate("metodosGraficos", u"Grafico", None))
        self.button_limpiar.setText(QCoreApplication.translate("metodosGraficos", u"Limpiar todo", None))
        self.label_6.setText(QCoreApplication.translate("metodosGraficos", u"Limite inferior  (a): ", None))
        self.label_7.setText(QCoreApplication.translate("metodosGraficos", u"Limite Superior  (b): ", None))
        self.label_8.setText(QCoreApplication.translate("metodosGraficos", u"Tolerancia 10^- ", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("metodosGraficos", u"Limite Inferior (a)", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("metodosGraficos", u"Limite Superior (b)", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("metodosGraficos", u"x", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("metodosGraficos", u"f(x)", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("metodosGraficos", u"error %", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("metodosGraficos", u"1", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("metodosGraficos", u"2", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("metodosGraficos", u"3", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("metodosGraficos", u"4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem9 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("metodosGraficos", u"empty", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_9.setText(QCoreApplication.translate("metodosGraficos", u"Tabla de iteraciones", None))
        value_lineEdit = self.lineEdit.displayText()
    # retranslateUi
    

#main Class

if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_metodosGraficos()
        ui.setupUi(MainWindow)
    
        MainWindow.show()
        sys.exit(app.exec_())
       
    # __main__

## 
