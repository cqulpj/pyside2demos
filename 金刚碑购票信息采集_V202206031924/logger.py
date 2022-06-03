#!/usr/bin/python3
#encoding=utf-8

import os
import sys
import logging
from logging import handlers
import time

LOG_PATH = 'logs'

def get_logger(name):
    # 创建logger实例
    logger = logging.getLogger(name)
    # 检查路径，没有则创建
    if not os.path.exists(LOG_PATH):
        os.mkdir(LOG_PATH)
    # 设置日志级别
    logger.setLevel(logging.DEBUG)
    # 设置格式
    formatter = '%(asctime)s [%(module)s] %(levelname)s %(message)s'
    log_formatter = logging.Formatter(formatter)
    # 控制台日志
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(log_formatter)
    # 文件日志
    # "S"：Second 秒
    # "M"：Minutes 分钟
    # "H"：Hour 小时
    # "D"：Days 天
    # "W"：Week day（0 = Monday）
    # "midnight"：Roll over at midnight
    file_handler = logging.handlers.TimedRotatingFileHandler(
            filename=LOG_PATH + '/file',
            when='midnight',
            backupCount=30,
            encoding='utf-8')
    file_handler.suffix = "%Y-%m-%d-%H%M.log"
    file_handler.setFormatter(log_formatter)
    file_handler.setLevel(logging.DEBUG)
    # 添加日志处理器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

if __name__ == '__main__':
    log = get_logger(__name__)
    t = 0
    while t < 60:
        time.sleep(5)
        log.info('测试日志输出，t=%d' % t)
        t += 1


