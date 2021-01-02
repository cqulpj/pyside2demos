#coding=utf-8
from PySide2 import QtWidgets
import pyqtgraph as pg
import sys
from random import random

# 读取数据
data = [random() for i in range(50)]

# 主窗口类
class MainWidget(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("上证指数收盘价历史走势|州的先生zmister.com") # 设置窗口标题
        main_widget = QtWidgets.QWidget() # 实例化一个widget部件
        main_layout = QtWidgets.QGridLayout() # 实例化一个网格布局层
        main_widget.setLayout(main_layout) # 设置主widget部件的布局为网格布局
        pw = pg.PlotWidget() # 实例化一个绘图部件
        pw.plot(data, ) # 在绘图部件中绘制折线图
        main_layout.addWidget(pw) # 添加绘图部件到网格布局层
        self.setCentralWidget(main_widget) # 设置窗口默认部件为主widget

# 运行函数
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainWidget()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
