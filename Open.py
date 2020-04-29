import sys
from PyQt5.QtWidgets import QApplication , QMainWindow ,QWidget, QFileDialog
from MainWin1 import Ui_MainWindow

class MainForm(QMainWindow , Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        self.actionFileClose.triggered.connect(self.close)
        self.actionAddWin.triggered.connect(self.openMsg)
        self.actionFileNew.triggered.connect(self.showmessage)

    def showmessage(self):
        print("please loading untill we finish that work")

    def openMsg(self):
        file,ok = QFileDialog.getOpenFileName(self,"打开","D:/","All Files(*)")
        self.statusbar.showMessage(file)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())