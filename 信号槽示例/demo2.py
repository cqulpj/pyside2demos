#!/usr/bin/python3
#coding=utf-8

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject, Signal, Slot

# 定义一个带有字符串参数的槽
@Slot(str)
def output(str):
    print(str)

class Test(QObject):
	# 自定义一个信号
    output_str = Signal(str)

output_key = Test()
output_key.output_str.connect(output)
# 发射信号
output_key.output_str.emit("Signal emit with para")

app = QApplication(sys.argv)
app.exec_()
