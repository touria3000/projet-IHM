# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface_calc.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        MainWindow.setMinimumSize(QtCore.QSize(300, 400))
        MainWindow.setMaximumSize(QtCore.QSize(300, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 271, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);\n"
"color: rgb(255, 0, 255);\n"
"font: 16pt \"MS Shell Dlg 2\";\n"
"border-color: rgb(0, 0, 0);")
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.b_8 = QtWidgets.QPushButton(self.centralwidget)
        self.b_8.setGeometry(QtCore.QRect(80, 160, 51, 41))
        self.b_8.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.b_8.setObjectName("b_8")
        self.b_pf = QtWidgets.QPushButton(self.centralwidget)
        self.b_pf.setGeometry(QtCore.QRect(80, 110, 51, 41))
        self.b_pf.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.b_pf.setObjectName("b_pf")
        self.b_7 = QtWidgets.QPushButton(self.centralwidget)
        self.b_7.setGeometry(QtCore.QRect(20, 160, 51, 41))
        self.b_7.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.b_7.setObjectName("b_7")
        self.b_1 = QtWidgets.QPushButton(self.centralwidget)
        self.b_1.setGeometry(QtCore.QRect(20, 260, 51, 41))
        self.b_1.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);font: 14pt \"MS Shell Dlg 2\";")
        self.b_1.setObjectName("b_1")
        self.b_0 = QtWidgets.QPushButton(self.centralwidget)
        self.b_0.setGeometry(QtCore.QRect(80, 310, 51, 41))
        self.b_0.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(0, 170, 255);\n"
"color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);")
        self.b_0.setObjectName("b_0")
        self.b_egale = QtWidgets.QPushButton(self.centralwidget)
        self.b_egale.setGeometry(QtCore.QRect(200, 270, 81, 81))
        self.b_egale.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.b_egale.setObjectName("b_egale")
        self.b_mod = QtWidgets.QPushButton(self.centralwidget)
        self.b_mod.setGeometry(QtCore.QRect(110, 70, 81, 31))
        self.b_mod.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.b_mod.setObjectName("b_mod")
        self.b_3 = QtWidgets.QPushButton(self.centralwidget)
        self.b_3.setGeometry(QtCore.QRect(140, 260, 51, 41))
        self.b_3.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);font: 14pt \"MS Shell Dlg 2\";")
        self.b_3.setObjectName("b_3")
        self.b_moins = QtWidgets.QPushButton(self.centralwidget)
        self.b_moins.setGeometry(QtCore.QRect(200, 170, 81, 41))
        self.b_moins.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.b_moins.setObjectName("b_moins")
        self.b_mult = QtWidgets.QPushButton(self.centralwidget)
        self.b_mult.setGeometry(QtCore.QRect(200, 120, 81, 41))
        self.b_mult.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.b_mult.setObjectName("b_mult")
        self.b_divise = QtWidgets.QPushButton(self.centralwidget)
        self.b_divise.setGeometry(QtCore.QRect(200, 70, 81, 41))
        self.b_divise.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.b_divise.setObjectName("b_divise")
        self.b_6 = QtWidgets.QPushButton(self.centralwidget)
        self.b_6.setGeometry(QtCore.QRect(140, 210, 51, 41))
        self.b_6.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);font: 14pt \"MS Shell Dlg 2\";")
        self.b_6.setObjectName("b_6")
        self.b_ac = QtWidgets.QPushButton(self.centralwidget)
        self.b_ac.setGeometry(QtCore.QRect(140, 110, 51, 41))
        self.b_ac.setStyleSheet("background-color: rgb(255, 170, 127);font: 14pt \"MS Shell Dlg 2\";")
        self.b_ac.setObjectName("b_ac")
        self.b_2 = QtWidgets.QPushButton(self.centralwidget)
        self.b_2.setGeometry(QtCore.QRect(80, 260, 51, 41))
        self.b_2.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);font: 14pt \"MS Shell Dlg 2\";")
        self.b_2.setObjectName("b_2")
        self.b_9 = QtWidgets.QPushButton(self.centralwidget)
        self.b_9.setGeometry(QtCore.QRect(140, 160, 51, 41))
        self.b_9.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.b_9.setObjectName("b_9")
        self.b_div = QtWidgets.QPushButton(self.centralwidget)
        self.b_div.setGeometry(QtCore.QRect(20, 70, 71, 31))
        self.b_div.setStyleSheet("color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.b_div.setObjectName("b_div")
        self.b_del = QtWidgets.QPushButton(self.centralwidget)
        self.b_del.setGeometry(QtCore.QRect(20, 310, 51, 41))
        self.b_del.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";background-color: rgb(255, 170, 127);")
        self.b_del.setObjectName("b_del")
        self.b_plus = QtWidgets.QPushButton(self.centralwidget)
        self.b_plus.setGeometry(QtCore.QRect(200, 220, 81, 41))
        self.b_plus.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";color: rgb(85, 85, 255);\n"
"background-color: rgb(255, 255, 127);")
        self.b_plus.setObjectName("b_plus")
        self.b_po = QtWidgets.QPushButton(self.centralwidget)
        self.b_po.setGeometry(QtCore.QRect(20, 110, 51, 41))
        self.b_po.setStyleSheet("background-color: rgb(255, 170, 127);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.b_po.setObjectName("b_po")
        self.b_4 = QtWidgets.QPushButton(self.centralwidget)
        self.b_4.setGeometry(QtCore.QRect(20, 210, 51, 41))
        self.b_4.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.b_4.setObjectName("b_4")
        self.b_5 = QtWidgets.QPushButton(self.centralwidget)
        self.b_5.setGeometry(QtCore.QRect(80, 210, 51, 41))
        self.b_5.setStyleSheet("color: rgb(0, 0, 255);\n"
"background-color: rgb(85, 255, 255);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.b_5.setObjectName("b_5")
        self.b_point = QtWidgets.QPushButton(self.centralwidget)
        self.b_point.setGeometry(QtCore.QRect(140, 310, 51, 41))
        self.b_point.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";background-color: rgb(255, 170, 127);")
        self.b_point.setObjectName("b_point")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Calculatrice"))
        self.b_8.setText(_translate("MainWindow", "8"))
        self.b_pf.setText(_translate("MainWindow", ")"))
        self.b_7.setText(_translate("MainWindow", "7"))
        self.b_1.setText(_translate("MainWindow", "1"))
        self.b_0.setText(_translate("MainWindow", "0"))
        self.b_egale.setText(_translate("MainWindow", "="))
        self.b_mod.setText(_translate("MainWindow", "MOD"))
        self.b_3.setText(_translate("MainWindow", "3"))
        self.b_moins.setText(_translate("MainWindow", "-"))
        self.b_mult.setText(_translate("MainWindow", "x"))
        self.b_divise.setText(_translate("MainWindow", "/"))
        self.b_6.setText(_translate("MainWindow", "6"))
        self.b_ac.setText(_translate("MainWindow", "AC"))
        self.b_2.setText(_translate("MainWindow", "2"))
        self.b_9.setText(_translate("MainWindow", "9"))
        self.b_div.setText(_translate("MainWindow", "DIV"))
        self.b_del.setText(_translate("MainWindow", "DEL"))
        self.b_plus.setText(_translate("MainWindow", "+"))
        self.b_po.setText(_translate("MainWindow", "("))
        self.b_4.setText(_translate("MainWindow", "4"))
        self.b_5.setText(_translate("MainWindow", "5"))
        self.b_point.setText(_translate("MainWindow", "."))
    
