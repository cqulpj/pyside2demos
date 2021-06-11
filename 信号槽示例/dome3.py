#!/usr/bin/python3
#coding=utf-8

import sys
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QObject, Signal, Slot

# 增加槽的接收参数
#@Slot(str)
#@Slot(int)
@Slot(str, int)
def output(str, int):
    print(str, int)

class Test(QObject):
	# 自定义不同参数类型的信号
	# 声明可接收的参数类型，但每次只能够接收其中一种
    output_str = Signal(str, int)

output_key = Test()
output_key.output_str.connect(output)
# 发射信号
output_key.output_str.emit("Signal emit with para", 111)

#app = QApplication(sys.argv)
#app.exec_()

