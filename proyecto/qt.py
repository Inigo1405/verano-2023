# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qt.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(894, 432)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(70, 80, 701, 101))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Display = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.Display.setObjectName("Display")
        self.horizontalLayout.addWidget(self.Display)
        self.recorridoBFS = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.recorridoBFS.setObjectName("recorridoBFS")
        self.horizontalLayout.addWidget(self.recorridoBFS)
        self.recorridoDFS = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.recorridoDFS.setObjectName("recorridoDFS")
        self.horizontalLayout.addWidget(self.recorridoDFS)
        self.mostrarMatriz = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.mostrarMatriz.setObjectName("mostrarMatriz")
        self.horizontalLayout.addWidget(self.mostrarMatriz)
        self.dijkstra = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.dijkstra.setObjectName("dijkstra")
        self.horizontalLayout.addWidget(self.dijkstra)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(340, 40, 151, 41))
        self.label.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(0)
        self.label.setObjectName("label")
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(170, 190, 491, 192))
        self.graphicsView.setObjectName("graphicsView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 894, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Display.setText(_translate("MainWindow", "Display"))
        self.recorridoBFS.setText(_translate("MainWindow", "Recorrido BFS"))
        self.recorridoDFS.setText(_translate("MainWindow", "Recorrido DFS"))
        self.mostrarMatriz.setText(_translate("MainWindow", "Mostrar matriz"))
        self.dijkstra.setText(_translate("MainWindow", "Dijkstra"))
        self.label.setText(_translate("MainWindow", "Grafos"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())