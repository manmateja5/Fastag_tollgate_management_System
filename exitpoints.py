# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'exitpoints.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import MySQLdb as mdb

class Ui_Dialog(object):
    def connect(self):
        db=mdb.connect('localhost', 'root', '', 'fastag')

        with db:
           cur = db.cursor()
           cur.execute("SELECT * from cost")
           result = cur.fetchall()
           self.Exitpoints.append("(Exit,cost)")
           for i in result:
            self.Exitpoints.append(str(i))

    def setupUi(self, Dialog):
        Dialog.setObjectName("Exit number and their costs")
        Dialog.resize(571, 417)
        self.Exitpoints = QtWidgets.QTextEdit(Dialog)
        self.Exitpoints.setGeometry(QtCore.QRect(40, 20, 501, 371))
        self.Exitpoints.setObjectName("Exitpoints")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Exit number and their costs", "Exit number and their costs"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    ui.connect()
    Dialog.show()
    sys.exit(app.exec_())