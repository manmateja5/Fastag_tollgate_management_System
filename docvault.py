# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'docvault.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import base64

from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb
from PIL import Image
from pandas import io
import io
from insert import Ui_ManWindow


class Ui_DWindow(object):
    def docvault(self):
        username = self.lineEdit.text()
        password = self.lineEdit_2.text()
        db = mdb.connect('localhost', 'root', '', 'fastag')
        mycursor = db.cursor()
        query = "SELECT docname from docums WHERE username like '"+username+"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        if result==None:
            self.lineEdit_3.setEnabled(False)
        else:
            self.lineEdit_3.setEnabled(True)
        for i in result:
            self.textEdit.append(i[0])
        return username,password
    def ima(self):
        docname = self.lineEdit_3.text()
        db = mdb.connect('localhost', 'root', '', 'fastag')
        mycursor = db.cursor()
        query = "SELECT imagedoc from docums WHERE docname like '"+docname+"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        res = result[0][0]
        binary_data = base64.b64decode(res)
        image = Image.open(io.BytesIO(binary_data))
        image.show()
    def addi(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_ManWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(180, 10, 591, 101))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 115, 271, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 170, 271, 41))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 220, 331, 41))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(260, 110, 201, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(260, 170, 201, 41))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(360, 220, 201, 41))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_3.setEnabled(False)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget ,clicked =  lambda: self.docvault())
        self.pushButton.setGeometry(QtCore.QRect(480, 180, 31, 28))
        self.pushButton.setObjectName("pushButton")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 270, 391, 251))
        self.textEdit.setObjectName("textEdit")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda: self.ima())
        self.pushButton_2.setGeometry(QtCore.QRect(570, 230, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget,clicked = lambda :self.addi())
        self.pushButton_3.setGeometry(QtCore.QRect(460, 440, 93, 81))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">WELCOME TO FasTag DOC_VAULT</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter FasTag Username : </span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Enter FasTag Password : </span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Please Select and type your doc name : </span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "OK"))
        self.pushButton_2.setText(_translate("MainWindow", "OPEN"))
        self.pushButton_3.setText(_translate("MainWindow", "ADD NEW DOC"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_DWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
