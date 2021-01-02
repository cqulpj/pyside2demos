#!/usr/bin/python
#coding=utf-8

import requests
import json

# 登录
# 传入用户名、密码
# 返回[True, jwt] 或者 [False, None]
def login(username, password):
    url = 'http://localhost:8080/api/internal/login'
    val = {"username":username, "password":password}
    val = json.dumps(val)

    try:
        res = requests.post(url, data=val)
        print(res.text)
        jwt = json.loads(res.text)['jwt']
        return [True, jwt]
    except:
        return [False, None]

# 获取Applications
def list_apps(jwt):
    url = 'http://localhost:8080/api/applications'
    data = {"limit":"10", "offset":"0"}

    res = requests.get(url, params=data, headers={'Authorization':'Bearer '+jwt, 'Accept':'application/json'})
    ret = json.loads(res.text)
    
    print(ret)

# 获取设备配置文件
def list_device_profiles(jwt):
    url = 'http://localhost:8080/api/device-profiles'
    data = {"limit":"10", "offset":"0"}

    res = requests.get(url, params=data, headers={'Authorization':'Bearer '+jwt, 'Accept':'application/json'})
    ret = json.loads(res.text)
    
    print(ret)

# 添加网络服务器
# 传入服务器名及token
# 返回生成的网络服务器ID
def create_ns(nsname, jwt):
    url = 'http://localhost:8080/api/network-servers'
    val = {
              "networkServer": 
              {
                  "id": "1",
                  "name": nsname,
                  "server": "chirpstack-network-server:8000",
                  "gatewayDiscoveryEnabled": True,
                  "gatewayDiscoveryInterval": 1,
                  "gatewayDiscoveryTXFrequency": 0,
                  "gatewayDiscoveryDR": 0,
                  "caCert": "",
                  "tlsCert": "",
                  "tlsKey": "",
                  "routingProfileCACert": "",
                  "routingProfileTLSCert": "",
                  "routingProfileTLSKey": ""
              }
          }
    val = json.dumps(val)

    res = requests.post(url, data=val, headers={'Authorization':'Bearer '+jwt})
    nsID = json.loads(res.text)['id']
    print(res.text)

    return nsID

# 添加服务配置
# 传入服务配置名、服务器ID和jwt
def create_sf(sfname, nID, jwt):
    url = 'http://localhost:8080/api/service-profiles'
    val = {
              "serviceProfile": 
              {
                  "name": sfname,
                  "organizationID": "1",
                  "networkServerID": nID,
                  "addGWMetaData": True,
                  "devStatusReqFreq": 0,
                  "drMin": 0,
                  "drMax": 5,
                  "id": "1"
              }
          }
    val = json.dumps(val)

    res = requests.post(url, data=val, headers={'Authorization':'Bearer '+jwt})
    print(res.text)

# 添加网关配置
# 传入网关配置名、服务器ID和jwt
def create_gf(gfname, nID, jwt):
    url = 'http://localhost:8080/api/service-profiles'
    val = {
              "gateway": 
              {
                  "name": gfname,
                  "networkServerID": nID,
                  "organizationID": "1",
                  "discoveryEnabled": true,
                  #"gatewayProfileID": "string",
                  "id": "1"
              }
          }
    val = json.dumps(val)

    res = requests.post(url, data=val, headers={'Authorization':'Bearer '+jwt})
    print(res.text)

# 取消设备激活状态
# 传入DevEUI、jwt
def deactive_dev(deui, jwt):
    url = 'http://localhost:8080/api/devices/' + deui.strip() + '/activation'
    ret = requests.delete(url, headers={'Authorization':'Bearer '+jwt})
    print(ret.text)


# 主函数
if __name__ == '__main__':

    while True:
        print('----------------------------------')
        print('1、登录服务器，得到jwt.')
        print('2、列出应用列表.')
        print('3、列出设备配置文件列表.')
        print('7、退出.')
        print('----------------------------------')
        sw = int(input('请选择操作:'))
        if sw == 1:
            # 登录服务器
            [ret, jwt] = login('admin', 'admin')
            if not ret:
                print('登录服务器出错，程序退出.')
                break

        elif sw == 2:
            # 显示应用程序列表
            list_apps(jwt)

        elif sw == 3:
            #显示设备配置文件列表
            list_device_profiles(jwt)
        
        elif sw == 7:
            # 退出
            break

        else:
            print('不支持的操作.')

    
