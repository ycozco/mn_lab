from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class ecuacionesAlgebraicas(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1920, 1020)
        MainWindow.setMaximumSize(QSize(1920, 1020))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(1690, 120, 211, 381))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(200, 20))

        self.verticalLayout.addWidget(self.label_2)

        self.pushButton_7 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(200, 20))

        self.verticalLayout.addWidget(self.label_3)

        self.pushButton_10 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout.addWidget(self.pushButton_10)

        self.pushButton_3 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout.addWidget(self.pushButton_3)

        self.pushButton_2 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.pushButton_8 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.verticalLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout.addWidget(self.pushButton_9)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1700, 890, 201, 25))
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(100, 120, 1511, 441))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalScrollBar = QScrollBar(self.horizontalLayoutWidget)
        self.verticalScrollBar.setObjectName(u"verticalScrollBar")
        self.verticalScrollBar.setOrientation(Qt.Vertical)

        self.horizontalLayout.addWidget(self.verticalScrollBar)

        self.tableWidget = QTableWidget(self.horizontalLayoutWidget)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem23)
        self.tableWidget.setObjectName(u"tableWidget")

        self.horizontalLayout.addWidget(self.tableWidget)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 30, 821, 61))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 40, 111, 17))
        self.graphicsView = QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(100, 590, 1511, 341))
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ecuaciones Algebraicas", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Metodos Directos", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"Eliminacion de Gauss", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Eliminacion de Gauss-Jordan", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Descomposicion LU", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Inversion de Matrices", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Metodos Iterativos", None))
        self.pushButton_10.setText(QCoreApplication.translate("MainWindow", u"Matrices Especiales", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Gauss Seidel", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Cholesky", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Limpiar Todo", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"column 1", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"column 2", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"column 3", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"column 4", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Row 1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Row 2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Row 3", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Row 4", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem16 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem17 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem18 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem20 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem21 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem22 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        ___qtablewidgetitem23 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"empty", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Input equation", None))
    # retranslateUi

if __name__ == "__main__":
        import sys
        app = QApplication(sys.argv)
        MainWindow = QMainWindow()
        ui = ecuacionesAlgebraicas()
        ui.setupUi(MainWindow)
        MainWindow.show()
        sys.exit(app.exec_())
    # __main__