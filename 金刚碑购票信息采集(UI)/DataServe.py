#!/usr/bin/python3
#coding=gbk

import json
import requests
import hashlib

SIGNKEY = '123456'
req_url = 'http://47.108.234.170:18081/order/trealnames/'

# 计算字符串的MD5
def MD5(ss):
    return hashlib.md5(ss.encode('ascii')).hexdigest()

# 获取一次数据
def get_data(signkey, stime, etime, qtype='D', ttype='X'):
    src = signkey + stime + etime + qtype + ttype
    print('srcstr=', src)
    sign = MD5(src)
    print('sign=', sign)

    headers = { "Content-Type":"application/json" }
    data = {'sign':sign,
            'starttime':stime,
            'endtime':etime,
            'qtype':qtype,
            'timetype':ttype}
    print('data=', data)
    data = json.dumps(data)
    print('json(data)=', data)

    # 以params传参的get请求
    #return requests.get(req_url, params=data)
    # 以body传参的get请求
    result = requests.get(url=req_url, data=data, headers=headers)
    # 字节码形式的返回内容
    print(result.content)
    # unicode码形式的返回内容
    print(result.text)
    return result


if __name__ == '__main__':
    # 测试MD5
    starttime = '2022-01-01'
    endtime = '2022-03-31'
    qtype = 'D'
    timetype = 'X'
    print(MD5(SIGNKEY + starttime + endtime + qtype + timetype))

    ret = get_data(SIGNKEY, starttime, endtime, qtype, timetype)
    print(ret)


