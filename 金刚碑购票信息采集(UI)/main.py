#!/usr/bin/python3
#coding=utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from MainDialog import *
from qt_material import apply_stylesheet, density
import sys
import os
import re

qss = '''
QFrame#frame {
    background-color : #EFE7E2;
    border-radius: 2px;
    border-width: 0px;
    padding: 4px;
}

QGroupBox {
    background:transparent;
    border-color: #ABABAB;
    border-radius: 0px;
    border-width: 1px;
}

QFrame#frame_2 {
    background-color : #D4F5FA;
    border-radius: 2px;
    border-width: 0px;
    padding: 4px;
}'''

class appMainDialog(QDialog, Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        #self.setFixedSize(self.width(),self.height())

if __name__ == '__main__':
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    app = QApplication(sys.argv)
    dlg = appMainDialog()

    extra = {
    # Density Scale
    'density_scale': '0',
    # Font Family
    'font_family': u'微软雅黑',
    }
    apply_stylesheet(app, theme='light_teal_500.xml', invert_secondary=True, extra=extra)
    dlg.setStyleSheet(qss)
    dlg.exec_()
