# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'TravelHistory.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import *
import MySQLdb as mdb


class Ui_Dialog(object):
    def TravH(self):
        user = self.lineEdit.text()
        db = mdb.connect('localhost', 'root', '', 'fastag')
        cur = db.cursor()
        cur.execute("SELECT exitpoint,charge from travel history where username like'"+user+"'")
        result = cur.fetchone()
        print(result)


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Dialog")
        MainWindow.resize(1007, 461)
        self.label = QtWidgets.QLabel(MainWindow)
        self.label.setGeometry(QtCore.QRect(20, 60, 291, 71))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(360, 60, 181, 61))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(60, 150, 571, 291))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(Dialog,clicked = lambda: self.TravH())
        self.pushButton.setGeometry(QtCore.QRect(600, 60, 91, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:14pt;\">Please enter your username</span></p></body></html>"))
        self.pushButton.setText(_translate("Dialog", "submit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
