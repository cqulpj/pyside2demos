#!/usr/bin/python3
#coding=utf-8

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from addDeviceFrame import *
import sys
import time
import os
import requests
import json
import xlrd
import datetime

# 定义线程实现设备添加
class RunThread(QThread):

    # 定义一个信号
    addedDevName = Signal(bool, str)

    def __init__(self, host, port, jwt, filename, appID, dpfID):
        super().__init__()
        self.host = host
        self.port = port
        self.jwt = jwt
        self.filename = filename
        self.appID = appID
        self.dpfID = dpfID
        self.is_running = True
        self.start()

    # 调用API添加一个设备到服务器
    def add_a_device(self, jwt, name, desc, eui, appID, dpfID):
        baseurl = 'http://' + self.host + ':' + self.port
        url = baseurl + '/api/devices'
        data = {
                "device":{
                    "name":name,
                    "description":desc,
                    "devEUI":eui,
                    "applicationID":appID,
                    "deviceProfileID":dpfID
                    }
                }
        val = json.dumps(data)
        print(url)
        print(val)

        try:
            res = requests.post(url, data=val, headers={'Authorization':'Bearer '+self.jwt})
            print(res.status_code, type(res.status_code))
            return (res.status_code == 200)
        except Exception as e:
            print(e)
            return False

    # 调用API设置一个设备的appKey
    def set_device_key(self, jwt, eui, appKey):
        baseurl = 'http://' + self.host + ':' + self.port
        url = baseurl + '/api/devices/' + eui + '/keys'
        data = {
                "deviceKeys":{
                    "devEUI":eui,
                    "nwkKey":appKey
                    }
                }
        val = json.dumps(data)
        print(url)
        print(val)

        try:
            res = requests.post(url, data=val, headers={'Authorization':'Bearer '+self.jwt})
            print(res.status_code, type(res.status_code))
            return (res.status_code == 200)
        except Exception as e:
            print(e)
            return False

    def run(self):
        wb = xlrd.open_workbook(self.filename)
        tb = wb.sheets()[0]
        rows = tb.nrows
        for i in range(1, rows):
            (name, desc, eui, appKey) = tb.row_values(i)
            eui = eui.replace(' ', '').replace('-', '')
            appKey = appKey.replace(' ', '').replace('-', '')
            ret_create = self.add_a_device(self.jwt, name, desc, eui, self.appID, self.dpfID)
            ret_set = self.set_device_key(self.jwt, eui, appKey)
            if ret_create and ret_set:
                self.addedDevName.emit(True, name)
            else:
                self.addedDevName.emit(False, name)
            time.sleep(0.5)

    def stop(self):
        self.is_running = False
        print('线程停止中...')
        self.terminate()

class MainDialog(QDialog, Ui_AddDeviceDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.chooseFileButton.clicked.connect(self.choose_file)
        self.startImportButton.clicked.connect(self.start_import)
        self.jwt = ''
        self.host = '127.0.0.2'
        self.port = '8080'
        self.filename = ''
        self.user = ''
        self.password = ''
        self.apps = []
        self.devprofiles = []
        self.read_host()
        if self.login() == False:
            self.info_log('登录服务器失败.\n请核实服务器IP和用户名密码.')
        else:
            self.info_log('登录服务器成功.')
            self.get_apps()
            self.get_dev_profiles()

    # 在textbrowser最后显示信息并移动光标到末尾
    def info_log(self, msg):
        self.infoText.append(msg)
        self.infoText.moveCursor(self.infoText.textCursor().End)
        filename = 'log/' + datetime.datetime.now().strftime('%Y%m%d') + '.txt'
        #with io.open(filename, 'a', encoding='utf-8') as f:
        with open(filename, 'a') as f:
            nowtime = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n'
            f.write(nowtime)
            f.write(msg + '\n')


    # 从文件server.txt中获取服务器ip并在UI上显示
    # 同时获取用户名和密码
    def read_host(self):
        with open('server.txt', 'r') as f:
            hstr = f.readline().strip()
            if len(hstr) > 0:
                self.host = hstr
                print('self.host=', self.host)
            self.user = f.readline().strip()
            self.password = f.readline().strip()
            print('user:%s, password:%s' % (self.user, self.password))

        self.ServerIPText.setText(self.host)

    # 用指定用户名和密码登录服务器，获取jwt
    # 若无法登录（服务器故障或者用户名密码错误）则弹出对话框提示并退出
    def login(self):
        baseurl = 'http://' + self.host + ':' + self.port
        url = baseurl + '/api/internal/login'
        data = {"username":self.user, "password":self.password}
        val = json.dumps(data)
        print(url)
        print(val)

        try:
            res = requests.post(url, data=val)
            print(res.text)
            self.jwt = json.loads(res.text)['jwt']
            return True
        except Exception as e:
            print(e)
            return False

    # 获取应用列表并更新控件内容
    def get_apps(self):
        baseurl = 'http://' + self.host + ':' + self.port
        url = baseurl + '/api/applications'
        data = {"limit":"20", "offset":"0"}

        res = requests.get(url, params=data, headers={'Authorization':'Bearer '+self.jwt, 'Accept':'application/json'})
        ret = json.loads(res.text)
        
        print(ret)
        self.apps = ret['result']
        # 更新下拉框
        for app in self.apps:
            self.appsComboBox.addItem(app['name'])
        self.appsComboBox.setCurrentIndex(0)

    # 获取设备配置列表并更新控件内容
    def get_dev_profiles(self):
        baseurl = 'http://' + self.host + ':' + self.port
        url = baseurl + '/api/device-profiles'
        data = {"limit":"20", "offset":"0"}

        res = requests.get(url, params=data, headers={'Authorization':'Bearer '+self.jwt, 'Accept':'application/json'})
        ret = json.loads(res.text)
        
        print(ret)
        self.devprofiles = ret['result']
        # 更新下拉框
        for devpf in self.devprofiles:
            self.devprofileComboBox.addItem(devpf['name'])
        self.devprofileComboBox.setCurrentIndex(1)


    # 打开设备数据文件
    # xls表格，列分别为：devEUI, 名称, 描述, appkey
    def choose_file(self, event):
        fname, ftype = QFileDialog.getOpenFileName(self, '选取文件', os.getcwd(),
                "ExcelFile(*.xls *.xlsx);;AllFiles(*.*)")
        print('fname=%s, ftype=%s' % (fname, ftype))
        self.filename = fname
        self.filePathText.setText(self.filename)

    # 开始导入设备
    # 先获取选定的应用和设备配置信息，然后创建线程开始上传
    def start_import(self, event):
        if self.filename == '':
            self.info_log('请先选择待添加的设备表格文件.')
            return

        appIndex = self.appsComboBox.currentIndex()
        dpfIndex = self.devprofileComboBox.currentIndex()
        self.info_log('选择应用：'+self.apps[appIndex]['name'])
        self.info_log('选择设备配置文件：'+self.devprofiles[dpfIndex]['name'])
        self.import_thread = RunThread(self.host, self.port, self.jwt, 
                self.filename, self.apps[appIndex]['id'], 
                self.devprofiles[dpfIndex]['id'])
        self.import_thread.addedDevName.connect(self.display_progress)
        self.filename = ''
        self.filePathText.setText(self.filename)

    # 线程中每添加一个设备后发射信号对应的槽函数
    def display_progress(self, result, devName):
        if result == True:
            tips = '设备 ' + devName + ' 添加成功.'
            self.info_log(tips)
        else:
            tips = '设备 ' + devName + ' 添加失败.'
            self.info_log(tips)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    dlg = MainDialog()
    dlg.exec_()
