#-*-coding:utf-8-*-
__author__ = 'zhonglingling'
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

fh = logging.FileHandler('rmlog.log',mode='w')
fh.setLevel(logging.INFO)

formatter = logging.Formatter("%(asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s")
fh.setFormatter(formatter)

logger.addHandler(fh)



