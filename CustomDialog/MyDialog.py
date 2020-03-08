#coding=utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from cusDialog import *
import sys

class MyDialog1(QDialog, Ui_CusDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.accept)
        self.pushButton_2.clicked.connect(self.reject)

    def get_data(self):
        arg1 = self.lineEdit.text()
        arg2 = self.comboBox.currentIndex()
        arg3 = self.spinBox.value()
        arg4 = self.dateTimeEdit.dateTime()

        return (arg1, arg2, arg3, arg4)

    @staticmethod
    def getOnceData():
        dialog = MyDialog1()
        result = dialog.exec_()
        data = dialog.get_data()
        return (data, result==QDialog.Accepted)

class MyDialog2(QDialog, Ui_CusDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setModal(True)
        self.pushButton.clicked.connect(self.onOK)
        self.pushButton_2.clicked.connect(self.onCancel)

    def get_data(self):
        arg1 = self.lineEdit.text()
        arg2 = self.comboBox.currentIndex()
        arg3 = self.spinBox.value()
        arg4 = self.dateTimeEdit.dateTime()

        return (arg1, arg2, arg3, arg4)

    def onOK(self):
        self.done(1)

    def onCancel(self):
        self.done(0)


# 第一种调用
#if __name__ == '__main__':
#    app = QApplication()
#    dlg = MyDialog1()
#    if dlg.exec_():
#        print(dlg.get_data())

# 第二种调用
#if __name__ == '__main__':
#    app = QApplication()
#    data, ok = MyDialog1.getOnceData()
#    print(data,ok)
#    #sys.exit(app.exec_())

# 第三种调用
class MWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(420, 360)
        self.main_widget = QWidget()
        self.main_layout = QVBoxLayout()
        self.main_widget.setLayout(self.main_layout)

        self.btn_1 = QPushButton("打开对话框")
        self.btn_1.clicked.connect(self.openDialog)
        self.main_layout.addWidget(self.btn_1)

        self.setCentralWidget(self.main_widget)
    
    def openDialog(self):
        self.dlg = MyDialog2()
        ret = self.dlg.show()
        print('ret=', ret)
        if ret == 1:
            print(self.dlg.get_data())


if __name__ == '__main__':
    app = QApplication()
    win = MWindow()
    win.show()
    sys.exit(app.exec_())

