#coding=utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from complex_window import *
import sys
import time

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.update_date()
        self.update_calendar()
        self.set_lcd()
        self.set_dial()
        self.set_font()
        self.update_progressbar()

    # 修改日期编辑器的数值
    def update_date(self):
        self.dateEdit.setDate(self.calendarWidget.selectedDate())

    # 日历信号槽
    def update_calendar(self):
        self.calendarWidget.selectionChanged.connect(self.update_date)

    # 设置LCD数字
    def set_lcd(self):
        self.lcdNumber.display(self.dial.value())

    # 刻度盘信号槽
    def set_dial(self):
        self.dial.valueChanged['int'].connect(self.set_lcd)

    # 更新字体选择结果
    def set_font(self):
        self.fontComboBox.activated['QString'].connect(self.label.setText)

    # 单选按钮信号槽
    def update_progressbar(self):
        self.radioButton.setText(u'开始')
        self.radioButton.clicked.connect(self.start_progressbar)
        self.radioButton_2.setText(u'暂停')
        self.radioButton_2.setChecked(True)
        self.radioButton_2.clicked.connect(self.stop_progressbar)
        self.radioButton_3.setText(u'重置')
        self.radioButton_3.clicked.connect(self.reset_progressbar)
        self.progress_value = 0
        self.stop_progress = False

    # 启动进度栏
    def start_progressbar(self):
        self.stop_progress = False
        self.progress_value = self.progressBar.value()

        while (self.progress_value <= 100.1) and not (self.stop_progress):
            self.progressBar.setValue(self.progress_value)
            self.progress_value += 1
            time.sleep(0.3)
            QApplication.processEvents()

    # 停止进度栏
    def stop_progressbar(self):
        self.stop_progress = True

    # 重置进度栏
    def reset_progressbar(self):
        self.progress_value = 0
        self.progressBar.reset()
        self.stop_progress = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
