# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'try.ui'
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


class Ui_MainWindow(object):
    def imao(self):
        db = mdb.connect('localhost', 'root', '', 'fastag')
        mycursor = db.cursor()
        file = open('156 reorder.png', 'rb').read()
        file = base64.b64encode(file)
        args = ('pranesh','blue', 'vech3', file)
        print(args)
        query = 'INSERT INTO DOCUMS VALUES(%s ,%s, %s, %s)'
        result = mycursor.execute(query, args)
        print(result)

        db.commit()

    def ima(self):
        db = mdb.connect('localhost', 'root', '', 'fastag')
        mycursor = db.cursor()
        query = "SELECT imagedoc from docums WHERE Personid like '"+str(5)+"'"
        mycursor.execute(query)
        result = mycursor.fetchall()
        res = result[0][0]
        binary_data = base64.b64decode(res)
        print(binary_data)
        image = Image.open(io.BytesIO(binary_data))
        image.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 70, 631, 401))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.ima())
        self.pushButton_6.setGeometry(QtCore.QRect(70, 450, 100, 55))
        self.pushButton_6.resize(100, 100)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget, clicked=lambda: self.imao())
        self.pushButton_7.setGeometry(QtCore.QRect(140, 450, 100, 55))
        self.pushButton_7.resize(100, 100)
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())