#!/usr/bin/python3
#coding=utf-8

import sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2.QtCore import Slot


# @Slot()是一个装饰器，标志着这个函数是一个slot(槽)
@Slot()
def output():
    '''在控制台输出内容'''
    print("Button clicked")

app = QApplication(sys.argv)
# 创建一个button
button = QPushButton("clicked me")
# 将信号和槽进行连接
button.clicked.connect(output)
button.show()

app.exec_()
