# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledzrwhIJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_metodosGraficos(object):
    def setupUi(self, metodosGraficos):
        if not metodosGraficos.objectName():
            metodosGraficos.setObjectName(u"metodosGraficos")
        metodosGraficos.resize(800, 618)
        self.centralwidget = QWidget(metodosGraficos)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(120, 10, 511, 41))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 111, 17))
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(640, 0, 160, 341))
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

        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(30, 70, 601, 511))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(30, 50, 591, 20))
        metodosGraficos.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(metodosGraficos)
        self.statusbar.setObjectName(u"statusbar")
        metodosGraficos.setStatusBar(self.statusbar)

        self.retranslateUi(metodosGraficos)

        QMetaObject.connectSlotsByName(metodosGraficos)
    # setupUi

    def retranslateUi(self, metodosGraficos):
        metodosGraficos.setWindowTitle(QCoreApplication.translate("metodosGraficos", u"Ecuaciones lineales - no lineales", None))
        self.lineEdit.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("metodosGraficos", u"example : x^2 + ((x+2)/x^3)", None))
        self.label.setText(QCoreApplication.translate("metodosGraficos", u"Input equation", None))
        self.label_2.setText(QCoreApplication.translate("metodosGraficos", u"Metodos cerrados", None))
        self.button_biseccion.setText(QCoreApplication.translate("metodosGraficos", u"Biseccion", None))
        self.button_falsa.setText(QCoreApplication.translate("metodosGraficos", u"Falsa posicion", None))
        self.label_3.setText(QCoreApplication.translate("metodosGraficos", u"Metodos abiertos", None))
        self.button_punto.setText(QCoreApplication.translate("metodosGraficos", u"Punto fijo", None))
        self.button_newton.setText(QCoreApplication.translate("metodosGraficos", u"Newton Raphson", None))
        self.button_secante.setText(QCoreApplication.translate("metodosGraficos", u"Secante", None))
        self.label_4.setText(QCoreApplication.translate("metodosGraficos", u"Raices de polinomios", None))
        self.button_raices.setText(QCoreApplication.translate("metodosGraficos", u"Calculo de las raices", None))
        self.label_5.setText(QCoreApplication.translate("metodosGraficos", u"Grafico", None))
    # retranslateUi
if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = Ui_metodosGraficos()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    # __main__

