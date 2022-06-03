#!/usr/bin/python3
#coding=utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from MainDialog import *
from qt_material import apply_stylesheet, density
from configparser import ConfigParser
import logger
import DataServe
import sys
import os
import re
import time
import json

# for pyinstaller
import PySide2.QtXml

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

# 采集数据线程
# 参数列表为：
#   name ：线程名字（标识） String
#   staTime : 起始时间 QDateTime
#   endTime : 终止时间 QDateTime （实时采集时该参数为None）
#   capGap  : 采集间隔 int 单位为秒
#   realGap : 实际间隔 int 单位为秒 （实时采集时该参数与采集间隔一致）
#
# 内设定时器，每采集一次发射信息给主线程，信号参数为：
#   name ：线程名字 String
#   capStaTime : 本次采集的起始时间 QDateTime
#   capEndTime ：本次采集的终止时间 QDateTime
#   count      ：采集条数 int
#   isError    : 是否出错 bool
#   errMsg     : 出错信息 String
#   isEnd      : 是否采集结束 bool （实时采集除非出错或者手动停止，不会结束）
class dataCapThread(QThread):
    # 定义采集数据后发射的信号
    capResultSignal = Signal(str, QDateTime, QDateTime, int, bool, str, bool)

    # 初始化（构造函数）
    def __init__(self, name, staTime, endTime, capGap, realGap):
        super().__init__()
        self.name = name
        self.staTime = staTime
        self.endTime = endTime
        self.capGap = capGap
        self.realGap = realGap

    # 从API获取一次数据并入库
    # 参数   preTime, endTime : QDateTime 起止时间
    # 返回值 scnt, errflag, errmsg : 传输条数、出错标识 和 出错信息
    def getAndSaveData(self, preTime, endTime):
        stastr = preTime.toString('yyyy-MM-dd HH:mm:ss')
        endstr = endTime.toString('yyyy-MM-dd HH:mm:ss')
        cpdata = DataServe.get_data(DataServe.SIGNKEY, stastr, endstr, 'H', 'X')
        errmsg = 'no error'
        errflag = False
        if cpdata.status_code == 200:
            content = json.loads(cpdata.content)
            scnt = DataServe.save_to_db(content['data'])
        else:
            errmsg = 'get data error'
            errflag = True
            scnt = -2

        return (scnt, errflag, errmsg)

    # 线程主循环函数
    def run(self):
        preTime = self.staTime
        curTime = self.staTime

        # 如果是历史数据传输
        if self.endTime:
            print('历史数据传输线程.')
            while preTime < self.endTime:
                time.sleep(self.capGap)
                curTime = preTime.addSecs(self.realGap)
                (scnt, errflag, errmsg) = self.getAndSaveData(preTime, curTime)
                self.capResultSignal.emit(self.name, preTime, curTime, 
                        scnt, errflag, errmsg, curTime>=self.endTime)
                preTime = curTime
        # 如果是实时数据传输
        else:
            print('实时数据传输线程.')
            while True:
                time.sleep(self.capGap)
                curTime = preTime.addSecs(self.realGap)
                (scnt, errflag, errmsg) = self.getAndSaveData(preTime, curTime)
                self.capResultSignal.emit(self.name, preTime, curTime, 
                        scnt, errflag, errmsg, False)
                preTime = curTime

        print('采集线程运行结束.')

    # 线程结束
    def stop(self):
        print('thread is end')
        self.terminate()

class appMainDialog(QDialog, Ui_dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 设置图标
        self.setWindowIcon(QIcon('visitor.ico'))
        #self.setFixedSize(self.width(),self.height())
        # 添加最小最大化按钮
        self.setWindowFlag(Qt.WindowMinMaxButtonsHint)
        # 限制QPlainTextEdit最大行数
        self.consoleLogText.setMaximumBlockCount(2000)
        # 日志处理器
        self.logger = logger.get_logger(__name__)
        # 初始化历史数据起止时间
        self.his_statime = QDateTime.fromString('2022/01/01 00:00:00', 'yyyy/MM/dd HH:mm:ss')
        self.his_endtime = QDateTime.currentDateTime()
        # 日期时间控件设置初始值
        self.startTimeEdit.setDateTime(self.his_statime)
        self.endTimeEdit.setDateTime(self.his_endtime)
        # 是否采集历史数据标志
        self.hisDataCapFlag = False
        # 历史数据复选框回调函数
        self.hisDataCheckBox.stateChanged.connect(self.changeHisDataCheck)
        self.changeHisDataCheck(Qt.Unchecked)
        # 设置初始实时数据采集间隔
        self.capGapTime = 300
        self.capGapTimeSpin.setValue(self.capGapTime)
        self.capGapTimeSpin.setKeyboardTracking(False)
        self.capGapTimeSpin.valueChanged.connect(self.changeCapGapTime)
        # 从配置文件获取历史数据采集间隔和实际间隔
        config = ConfigParser()
        config.read('config.ini', encoding='gbk')
        self.his_cap_gap = int(config.get('cap_args', 'his_data_gap'))
        self.his_cap_clp = int(config.get('cap_args', 'his_data_clp'))
        # 设置按钮属性及回调函数
        self.testConnectButton.clicked.connect(self.onTestConnectButton)
        self.startCaptureButton.clicked.connect(self.onStartCaptureButton)
        self.startCaptureButton.setEnabled(False)
        # 验证数据库和API有效
        self.db_valid = self.api_valid = False
        self.onTestConnectButton()
        # 是否开始采集标识
        self.isCapping = False
        # 采集的数据总数
        self.totalData = 0
        # 程序启动时的初始时间（记录该时间后续处理要用到）
        self.appRecordTime = QDateTime.currentDateTime()

    # 日志打印，同时打印到console和logs目录下的日志文件
    def logOutput(self, msg):
        self.logger.info(msg)
        self.consoleLogText.appendPlainText(msg)

    # 历史数据采集复选框状态改变回调函数
    def changeHisDataCheck(self, state):
        if state == Qt.Checked:
            self.hisDataCapFlag = True
            self.startTimeEdit.setEnabled(True)
            self.endTimeEdit.setEnabled(True)
        else:
            self.hisDataCapFlag = False
            self.startTimeEdit.setEnabled(False)
            self.endTimeEdit.setEnabled(False)

    # 修改实时数据采集时间间隔
    def changeCapGapTime(self, value):
        self.capGapTime = value
        print('capGapTime=', self.capGapTime)
        self.logOutput('采集间隔调整为%d秒.' % self.capGapTime)

    # 开始采集按钮回调函数
    def onStartCaptureButton(self):
        # 获取历史数据起止时间
        if self.hisDataCapFlag:
            self.his_statime = self.startTimeEdit.dateTime()
            self.his_endtime = self.endTimeEdit.dateTime()
        
        # 改变按钮状态并启动/停止传输
        if not self.isCapping:
            self.isCapping = True
            self.startCaptureButton.setText('停止采集')
            print('self.hisDataCapFlag=', self.hisDataCapFlag)
            # 创建采集线程
            if self.hisDataCapFlag:
                self.logOutput('开始历史数据采集...')
                self.cappingData = dataCapThread('his_data', self.his_statime, 
                        self.his_endtime, self.his_cap_gap, self.his_cap_clp)
            else:
                self.logOutput('开始实时数据采集...')
                self.cappingData = dataCapThread('cur_data', self.appRecordTime, 
                        None, self.capGapTime, self.capGapTime)
            self.cappingData.start()
            self.cappingData.capResultSignal.connect(self.displayCaptureInfo)
        else:
            self.isCapping = False
            self.startCaptureButton.setText('开始采集')
            self.logOutput('停止数据采集...')
            # 停止采集线程
            self.cappingData.stop()

    # 处理采集线程发射来的信息
    def displayCaptureInfo(self, name, preTime, curTime, count, err, errmsg, isend):
        stastr = preTime.toString('yyyy/MM/dd HH:mm:ss')
        endstr = curTime.toString('yyyy/MM/dd HH:mm:ss')
        self.totalData += count
        msg = '%s - %s 采集%d条数据' % (stastr, endstr, count)
        self.logOutput(msg)
        msg = '共采集数据 %d 条' % self.totalData
        self.logOutput(msg)
        self.endTimeEdit.setDateTime(curTime)

        # 本次采集结束则根据采集类别选择后续处理
        if isend == True:
            self.dealOneCaptureFinished(name, curTime)

    # 一次采集结束后的后续操作
    def dealOneCaptureFinished(self, name, endTime):
        # 如果是历史数据采集结束
        if name == 'his_data':
            # 弹窗询问是否进行实时数据上传
            ret = QMessageBox.question(self, '询问', 
                    '历史数据采集完毕，是否进行后续实时数据采集？',
                    QMessageBox.Yes|QMessageBox.No, QMessageBox.Yes)
            if ret == QMessageBox.No:
                self.isCapping = False
                self.startCaptureButton.setText('开始采集')
                return
        # 如果是增量数据（从程序启动时间到上一次数据上传结束之间的数据）则更新时间戳
        elif name == 'rest_data':
            self.appRecordTime = endTime

        # 判断程序启动时间（上一次结束时间）到当前时间的时间差
        # 大于1小时则再以这两个时间为参数再次启动历史数据上传
        # 若小于1小时则直接启动实时数据上传
        cur = QDateTime.currentDateTime()
        dif = self.appRecordTime.secsTo(cur)
        if dif >= 60:
            self.logOutput('开启增量数据传输，时间范围为：%s-%s' % 
                    (self.appRecordTime.toString('yyyy/MM/dd HH:mm:ss'), cur.toString('yyyy/MM/dd HH:mm:ss')))
            self.cappingData = dataCapThread('rest_data', self.appRecordTime, cur, 
                    self.his_cap_gap, self.his_cap_clp)
        else:
            self.logOutput('开启实时数据传输，起始时间为：%s' % 
                    self.appRecordTime.toString('yyyy/MM/dd HH:mm:ss'))
            self.cappingData = dataCapThread('cur_data', cur, None, self.capGapTime, self.capGapTime)
        self.cappingData.start()
        self.cappingData.capResultSignal.connect(self.displayCaptureInfo)

    # 测试数据库及采集API连接
    def onTestConnectButton(self):
        tips = ['失败. ', '成功. ']
        retinfo = ''

        cdb = DataServe.check_db()[0]
        retinfo += '数据库连接' + tips[cdb]
        cpi = DataServe.check_api()
        retinfo += '采集接口测试' + tips[cpi]

        if cdb and cpi:
            self.startCaptureButton.setEnabled(True)
        else:
            self.startCaptureButton.setEnabled(False)

        self.logOutput(retinfo)
        self.db_valid, self.api_valid = cdb, cpi

    # 重写Dialog closeEvent函数，实在窗口关闭前先手动结束线程
    def closeEvent(self, event):
        # 弹窗询问是否关闭程序
        ret = QMessageBox.question(self, '询问', 
                '确定要退出采集程序？',
                QMessageBox.Yes|QMessageBox.No, QMessageBox.No)
        if ret == QMessageBox.No:
            event.ignore()
            return

        # 停止采集线程
        try:
            self.cappingData.stop()
        except:
            pass
        event.accept()

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
