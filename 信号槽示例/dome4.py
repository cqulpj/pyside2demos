#!/usr/bin/python3
#coding=utf-8

from PySide2.QtWidgets import QLCDNumber, QSlider, QWidget, QVBoxLayout, QApplication, QGridLayout, QPushButton
from PySide2.QtCore import Qt
from PySide2.QtCore import Signal, Slot

class MyLCDNumber(QWidget):
    # 自定义一个信号，需要传入一个int类型的参数
    slider_valueChanged_signal = Signal(int)

    def __init__(self, parent=None):
        super().__init__(parent)

        self.lcd_number = QLCDNumber()
        # 初始化一个水平的slider，默认是垂直的
        self.slider = QSlider(Qt.Horizontal)
        self.btn_add = QPushButton('加一')
        # 垂直布局
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lcd_number)
        self.layout.addWidget(self.slider)
        self.layout.addWidget(self.btn_add)

        self.setLayout(self.layout)
        # 设置整个控件的固定大小
        self.setFixedSize(120, 140)

        # 设置最多显示两位数
        self.lcd_number.setDigitCount(2)
        # 设置可以调节的范围大小
        self.slider.setRange(0, 99)
        # 信号与信号的连接
        self.slider.valueChanged.connect(self.slider_valueChanged_signal)
        # 信号与槽点连接
        self.btn_add.clicked.connect(self.add)

    # 自定义一个槽
    @Slot()
    def setLCDNumberValue(self, val):
        self.lcd_number.display(val)

    @Slot()
    def add(self):
        v = self.slider.value() + 1
        self.slider.setValue(v)
        # 主动发送信号
        self.slider_valueChanged_signal.emit(v)

app = QApplication()
window = QWidget()
# 网格布局
layout = QGridLayout()
mylcdnumber01 = MyLCDNumber()
mylcdnumber02 = MyLCDNumber()
mylcdnumber01.slider_valueChanged_signal.connect(mylcdnumber01.setLCDNumberValue)
mylcdnumber02.slider_valueChanged_signal.connect(mylcdnumber02.setLCDNumberValue)
layout.addWidget(mylcdnumber01, 1, 1)
layout.addWidget(mylcdnumber02, 1, 2)
window.setLayout(layout)
window.show()
app.exec_()
