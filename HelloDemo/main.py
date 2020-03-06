#coding=utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from complex_window import *
import sys
import time

# 定义线程实现刷新进度栏
class RunThread(QThread):

    # 定义一个信号
    counter_value = Signal(int)

    def __init__(self, parent=None, counter_start=0):
        super().__init__(parent)
        self.counter = counter_start
        self.is_running = True

    def run(self):
        while self.counter < 100 and self.is_running:
            time.sleep(0.1)
            self.counter += 1
            print(self.counter)
            # 发射信号
            self.counter_value.emit(self.counter)

    def stop(self):
        self.is_running = False
        print('线程停止中...')
        self.terminate()

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

    # 启动线程
    def progressbar_counter(self, start_value=0):
        self.run_thread = RunThread(parent=None, counter_start=start_value)
        self.run_thread.start()
        self.run_thread.counter_value.connect(self.set_progressbar)

    # 线程中信号对应的槽函数
    def set_progressbar(self, counter):
        if not self.stop_progress:
            self.progressBar.setValue(counter)

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
        self.progressbar_counter(self.progress_value)

    # 停止进度栏
    def stop_progressbar(self):
        self.stop_progress = True
        try:
            self.run_thread.stop()
        except Exception as e:
            print(e)
            pass

    # 重置进度栏
    def reset_progressbar(self):
        self.progress_value = 0
        self.progressBar.reset()
        # 如果是运行状态，则从0重新开始
        if not self.stop_progress:
            self.run_thread.counter = 0
            self.radioButton.setChecked(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    sys.exit(app.exec_())
