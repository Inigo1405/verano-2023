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
        MainWindow.resize(1091, 681)
        MainWindow.setStyleSheet("color: #F9F4F4;\n""background: #13131A;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(110, 90, 861, 81))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(15)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.display = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.display.setStyleSheet("QPushButton:hover{\n""    background-color: white;\n""    color: #13131A\n""}\n""")
        self.display.setObjectName("display")
        self.horizontalLayout.addWidget(self.display)
        self.recorridoBFS = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.recorridoBFS.setFont(font)
        self.recorridoBFS.setStyleSheet("QPushButton:hover{\n"
"    background-color: white;\n"
"    color: #13131A\n"
"}\n"
"")
        self.recorridoBFS.setObjectName("recorridoBFS")
        self.horizontalLayout.addWidget(self.recorridoBFS)
        self.recorridoDFS = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.recorridoDFS.setStyleSheet("QPushButton:hover{\n"
"    background-color: white;\n"
"    color: #13131A\n"
"}\n"
"")
        self.recorridoDFS.setObjectName("recorridoDFS")
        self.horizontalLayout.addWidget(self.recorridoDFS)
        self.mostrarMatriz = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.mostrarMatriz.setStyleSheet("QPushButton:hover{\n"
"    background-color: white;\n"
"    color: #13131A\n"
"}\n"
"")
        self.mostrarMatriz.setObjectName("mostrarMatriz")
        self.horizontalLayout.addWidget(self.mostrarMatriz)
        self.dijkstra = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.dijkstra.setStyleSheet("QPushButton:hover{\n"
"    background-color: white;\n"
"    color: #13131A\n"
"}\n"
"")
        self.dijkstra.setObjectName("dijkstra")
        self.horizontalLayout.addWidget(self.dijkstra)
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(470, 40, 151, 41))
        self.title.setMinimumSize(QtCore.QSize(0, 13))
        font = QtGui.QFont()
        font.setFamily("Tw Cen MT")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.title.setFont(font)
        self.title.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.title.setAlignment(QtCore.Qt.AlignCenter)
        self.title.setIndent(0)
        self.title.setObjectName("title")
        self.canvas = QtWidgets.QWidget(self.centralwidget)
        self.canvas.setGeometry(QtCore.QRect(80, 190, 931, 421))
        self.canvas.setStyleSheet("background: #F0EBEB;\n"
"border-radius: 30px;")
        self.canvas.setObjectName("canvas")
        self.label = QtWidgets.QLabel(self.canvas)
        self.label.setGeometry(QtCore.QRect(30, -50, 651, 471))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1091, 21))
        self.menubar.setObjectName("menubar")
        self.menuMen = QtWidgets.QMenu(self.menubar)
        self.menuMen.setObjectName("menuMen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuMen.addSeparator()
        self.menubar.addAction(self.menuMen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.display.setText(_translate("MainWindow", "Display"))
        self.recorridoBFS.setText(_translate("MainWindow", "Recorrido BFS"))
        self.recorridoDFS.setText(_translate("MainWindow", "Recorrido DFS"))
        self.mostrarMatriz.setText(_translate("MainWindow", "Mostrar matriz"))
        self.dijkstra.setText(_translate("MainWindow", "Dijkstra"))
        self.title.setText(_translate("MainWindow", "Grafos"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><img src=\":/cct/grafosback.png\"/></p></body></html>"))
        self.menuMen.setTitle(_translate("MainWindow", "Menú"))

#import fondo_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
