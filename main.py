from PyQt5.QtWidgets import *
from PyQt5 import uic
import MySQLdb as mdb


class WelcomeUI(QMainWindow):
    def __init__(self):
       super(WelcomeUI, self).__init__()
       uic.loadUi("Welcom.ui", self)
       self.show()


def main():
    app = QApplication([])
    window = WelcomeUI()
    app.exec_()

def login(self):
     username=self.lineEdit.text()
     password=self.lineEdit_2.text()
     db=mdb.connect('localhost', 'host','','fastag')
     mycursor = db.cursor()

     query = "SELECT username,password from users WHERE username like '"+username + "' and password like '"+password+"'"
     mycursor.execute(query)
     result = mycursor.fetchone()

     if result==None:
         self.labelResult.setText("Invalid login")
     else:
         mydialog = QDialog()
         mydialog.setModal(True)
         mydialog.exec_()



if __name__ == '__main__':
    main()


