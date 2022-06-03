#!/usr/bin/python3
#coding=gbk

import json
import requests
import hashlib
import pymysql
from configparser import ConfigParser
from datetime import datetime

# ����configparser����
config = ConfigParser()

# ��configparser�����ȡ�����ļ�
config.read('config.ini', encoding='gbk')

# �������ļ���ȡ���ݿ�������Ϣ
host   = config.get('database', 'dbhost')
port   = config.get('database', 'dbport')
user   = config.get('database', 'dbuser')
pswd   = config.get('database', 'dbpswd')
dbname = config.get('database', 'dbname')
table  = config.get('database', 'table')

# �������ļ���ȡ�ο����ݲɼ��ӿ�API��Ϣ
req_url  = config.get('jgb_api', 'url')
SIGNKEY  = config.get('jgb_api', 'key')
jgb_sjly = config.get('jgb_api', 'sjly')
jgb_gszc = config.get('jgb_api', 'gszc')
print('req_url=%s' % req_url)
print('SIGKEY=%s' % SIGNKEY)

# �������ݿ����ӣ����ӳɹ�����True�����򷵻�False
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

# ��api��ȡ���Ĳ�ѯ���д�����ݿ�
# api��ȡ���Ľ�����б��б�Ԫ��Ϊ�ֵ䣬ÿ���ֵ���һ����Ʊ��¼����
# [{'ordercode': '20220525999777006', 'phone': '13452305349', 'idcard': None, 'stdt': '2022-05-25', 'name': '��Ӧ��', 'xdsj': '2022-05-25 05:05:21'}, {...}]
# ���ز���ļ�¼����������ʧ�ܷ���-1
def save_to_db(rcds):
    try:
        conn = pymysql.connect(host=host, user=user, password=pswd, database=dbname)
        cur = conn.cursor()
        for rc in rcds:
            idcard = ' ' if (not rc['idcard']) else rc['idcard']
            xdsj = datetime.strptime(rc['xdsj'], '%Y-%m-%d %H:%M:%S').strftime('%Y%m%d%H%M%S')
            # ���ɲ����¼��SQL���
            sql = "insert into %s (XM, ZJHM, LXDH, GPSJ, DDBH, XXLRSJ, XJ_ID, SJLY, GSZCH) \
                   values ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')" % (table,  
                   rc['name'], idcard, rc['phone'], xdsj, rc['ordercode'], xdsj, '500109',
                   jgb_sjly, jgb_gszc)
            print('sql=', sql)
            # �����¼
            cur.execute(sql)
        # �ύ���񲢹ر�����
        conn.commit()
        conn.close()
        print('�ɹ�����%d����¼.' % len(rcds))
        return len(rcds)
    except Exception as msg:
        print(repr(msg))
        return -1

# �����ַ�����MD5
def MD5(ss):
    return hashlib.md5(ss.encode('ascii')).hexdigest()

# ���Բɼ�API��Ч��
def check_api():
    starttime = '2022-05-25 11:00:00'
    endtime = '2022-05-25 12:00:00'
    qtype = 'H'
    timetype = 'X'
    ret = get_data(SIGNKEY, starttime, endtime, qtype, timetype)

    return ret.status_code == 200

# ��ȡһ������
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

    # ��params���ε�get����
    #return requests.get(req_url, params=data)
    # ��body���ε�get����
    result = requests.get(url=req_url, data=data, headers=headers)
    # �ֽ�����ʽ�ķ�������
    #print(result.content)
    # unicode����ʽ�ķ�������
    #print(result.text)
    return result

if __name__ == '__main__':
    # ����API���ݻ�ȡ
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

    # �������ݿ�
    #print(check_db())
    #ret = save_to_db(result['data'][:2])
    #print('ret=', ret)
