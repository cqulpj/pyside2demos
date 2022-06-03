#!/usr/bin/python3
#coding=gbk

import json
import requests
import hashlib
import pymysql
from configparser import ConfigParser
from datetime import datetime

# 生成configparser对象
config = ConfigParser()

# 用configparser对象读取配置文件
config.read('config.ini', encoding='gbk')

# 从配置文件获取数据库连接信息
host   = config.get('database', 'dbhost')
port   = config.get('database', 'dbport')
user   = config.get('database', 'dbuser')
pswd   = config.get('database', 'dbpswd')
dbname = config.get('database', 'dbname')
table  = config.get('database', 'table')

# 从配置文件获取游客数据采集接口API信息
req_url  = config.get('jgb_api', 'url')
SIGNKEY  = config.get('jgb_api', 'key')
jgb_sjly = config.get('jgb_api', 'sjly')
jgb_gszc = config.get('jgb_api', 'gszc')
print('req_url=%s' % req_url)
print('SIGKEY=%s' % SIGNKEY)

# 测试数据库连接，连接成功返回True，否则返回False
def check_db():
    try:
        conn = pymysql.connect(host=host, user=user, password=pswd, database=dbname)
        cur = conn.cursor()
        cur.execute('select * from %s' % table)
        conn.close()
        return [True, 'OK']
    except Exception as msg:
        print(repr(msg))
        return [False, repr(msg)]

# 将api获取到的查询结果写入数据库
# api获取到的结果是列表，列表元素为字典，每个字典是一条购票记录，如
# [{'ordercode': '20220525999777006', 'phone': '13452305349', 'idcard': None, 'stdt': '2022-05-25', 'name': '王应明', 'xdsj': '2022-05-25 05:05:21'}, {...}]
# 返回插入的记录条数，插入失败返回-1
def save_to_db(rcds):
    try:
        conn = pymysql.connect(host=host, user=user, password=pswd, database=dbname)
        cur = conn.cursor()
        for rc in rcds:
            idcard = ' ' if (not rc['idcard']) else rc['idcard']
            xdsj = datetime.strptime(rc['xdsj'], '%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
            # 生成插入记录的SQL语句
            sql = "insert into %s (XM, ZJHM, LXDH, GPSJ, DDBH, XXLRSJ, XJ_ID, SJLY, GSZCH) \
                   values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (table,  
                   rc['name'], idcard, rc['phone'], xdsj, rc['ordercode'], xdsj, '500109',
                   jgb_sjly, jgb_gszc)
            print('sql=', sql)
            # 插入记录
            cur.execute(sql)
        # 提交事务并关闭连接
        conn.commit()
        conn.close()
        print('成功插入%d条记录.' % len(rcds))
        return len(rcds)
    except Exception as msg:
        print(repr(msg))
        return -1

# 计算字符串的MD5
def MD5(ss):
    return hashlib.md5(ss.encode('ascii')).hexdigest()

# 测试采集API有效性
def check_api():
    starttime = '2022-05-25 11:00:00'
    endtime = '2022-05-25 12:00:00'
    qtype = 'H'
    timetype = 'X'
    ret = get_data(SIGNKEY, starttime, endtime, qtype, timetype)

    return ret.status_code == 200

# 获取一次数据
def get_data(signkey, stime, etime, qtype='D', ttype='X'):
    src = signkey + stime + etime + qtype + ttype
    #print('srcstr=', src)
    sign = MD5(src)
    #print('sign=', sign)

    headers = { "Content-Type":"application/json" }
    data = {'sign':sign,
            'starttime':stime,
            'endtime':etime,
            'qtype':qtype,
            'timetype':ttype}
    data = json.dumps(data)

    # 以params传参的get请求
    #return requests.get(req_url, params=data)
    # 以body传参的get请求
    result = requests.get(url=req_url, data=data, headers=headers)
    # 字节码形式的返回内容
    #print(result.content)
    # unicode码形式的返回内容
    #print(result.text)
    return result

if __name__ == '__main__':
    # 测试API数据获取
    starttime = '2022-05-25 11:00:00'
    endtime = '2022-05-25 12:00:00'
    qtype = 'H'
    timetype = 'X'
    print(MD5(SIGNKEY + starttime + endtime + qtype + timetype))

    ret = get_data(SIGNKEY, starttime, endtime, qtype, timetype)
    print(ret)
    print(ret.Status)
    result = json.loads(ret.content)
    print(result)
    print(len(result['data']))

    # 测试数据库
    #print(check_db())
    #ret = save_to_db(result['data'][:2])
    #print('ret=', ret)
